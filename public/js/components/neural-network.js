/**
 * Neural Network Canvas Animation
 * Creates an animated network of interconnected nodes resembling a neural network.
 * Responds to mouse movement with a soft parallax / attraction effect.
 */
(function () {
    const canvas = document.getElementById('neural-canvas');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    let width, height;
    let nodes = [];
    let mouse = { x: null, y: null };
    let animationId;

    // --- Configuration ---
    const CONFIG = {
        nodeCount: 60,
        connectionDistance: 140,
        mouseRadius: 200,
        nodeMinRadius: 1.5,
        nodeMaxRadius: 3.5,
        baseSpeed: 0.3,
        colors: {
            node: 'rgba(139, 92, 246, 0.8)',       // Violet accent
            nodeHighlight: 'rgba(59, 130, 246, 1)', // Blue accent
            line: 'rgba(139, 92, 246, 0.12)',
            lineHighlight: 'rgba(59, 130, 246, 0.35)',
        }
    };

    // --- Node Class ---
    class Node {
        constructor() {
            this.x = Math.random() * width;
            this.y = Math.random() * height;
            this.radius = CONFIG.nodeMinRadius + Math.random() * (CONFIG.nodeMaxRadius - CONFIG.nodeMinRadius);
            this.vx = (Math.random() - 0.5) * CONFIG.baseSpeed;
            this.vy = (Math.random() - 0.5) * CONFIG.baseSpeed;
            this.baseAlpha = 0.3 + Math.random() * 0.5;
            this.pulseOffset = Math.random() * Math.PI * 2;
        }

        update(time) {
            // Slow organic movement
            this.x += this.vx;
            this.y += this.vy;

            // Bounce off edges softly
            if (this.x < 0 || this.x > width) this.vx *= -1;
            if (this.y < 0 || this.y > height) this.vy *= -1;

            // Clamp within bounds
            this.x = Math.max(0, Math.min(width, this.x));
            this.y = Math.max(0, Math.min(height, this.y));

            // Mouse repulsion / attraction
            if (mouse.x !== null) {
                const dx = this.x - mouse.x;
                const dy = this.y - mouse.y;
                const dist = Math.sqrt(dx * dx + dy * dy);
                if (dist < CONFIG.mouseRadius) {
                    const force = (CONFIG.mouseRadius - dist) / CONFIG.mouseRadius * 0.015;
                    this.vx += dx * force;
                    this.vy += dy * force;
                }
            }

            // Dampen velocity
            this.vx *= 0.99;
            this.vy *= 0.99;

            // Pulsing alpha
            this.alpha = this.baseAlpha + Math.sin(time * 0.002 + this.pulseOffset) * 0.2;
        }

        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
            ctx.fillStyle = CONFIG.colors.node;
            ctx.globalAlpha = this.alpha;
            ctx.fill();
            ctx.globalAlpha = 1;
        }
    }

    // --- Initialization ---
    function init() {
        resize();
        nodes = [];
        for (let i = 0; i < CONFIG.nodeCount; i++) {
            nodes.push(new Node());
        }
    }

    function resize() {
        const rect = canvas.parentElement.getBoundingClientRect();
        const dpr = window.devicePixelRatio || 1;
        width = rect.width;
        height = rect.height;
        canvas.width = width * dpr;
        canvas.height = height * dpr;
        canvas.style.width = width + 'px';
        canvas.style.height = height + 'px';
        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }

    // --- Drawing ---
    function drawConnections(time) {
        for (let i = 0; i < nodes.length; i++) {
            for (let j = i + 1; j < nodes.length; j++) {
                const dx = nodes[i].x - nodes[j].x;
                const dy = nodes[i].y - nodes[j].y;
                const dist = Math.sqrt(dx * dx + dy * dy);

                if (dist < CONFIG.connectionDistance) {
                    const opacity = 1 - dist / CONFIG.connectionDistance;

                    // Check if near mouse for highlight
                    let isHighlighted = false;
                    if (mouse.x !== null) {
                        const midX = (nodes[i].x + nodes[j].x) / 2;
                        const midY = (nodes[i].y + nodes[j].y) / 2;
                        const mouseDist = Math.sqrt((midX - mouse.x) ** 2 + (midY - mouse.y) ** 2);
                        isHighlighted = mouseDist < CONFIG.mouseRadius * 0.8;
                    }

                    ctx.beginPath();
                    ctx.moveTo(nodes[i].x, nodes[i].y);
                    ctx.lineTo(nodes[j].x, nodes[j].y);
                    ctx.strokeStyle = isHighlighted ? CONFIG.colors.lineHighlight : CONFIG.colors.line;
                    ctx.globalAlpha = opacity * (isHighlighted ? 1 : 0.6);
                    ctx.lineWidth = isHighlighted ? 1.2 : 0.6;
                    ctx.stroke();
                    ctx.globalAlpha = 1;
                }
            }
        }
    }

    function drawHighlightedNodes() {
        if (mouse.x === null) return;

        for (const node of nodes) {
            const dx = node.x - mouse.x;
            const dy = node.y - mouse.y;
            const dist = Math.sqrt(dx * dx + dy * dy);

            if (dist < CONFIG.mouseRadius) {
                const intensity = 1 - dist / CONFIG.mouseRadius;
                // Outer glow
                ctx.beginPath();
                ctx.arc(node.x, node.y, node.radius + 4 * intensity, 0, Math.PI * 2);
                ctx.fillStyle = CONFIG.colors.nodeHighlight;
                ctx.globalAlpha = intensity * 0.3;
                ctx.fill();
                ctx.globalAlpha = 1;

                // Brighter core
                ctx.beginPath();
                ctx.arc(node.x, node.y, node.radius * 1.3, 0, Math.PI * 2);
                ctx.fillStyle = CONFIG.colors.nodeHighlight;
                ctx.globalAlpha = intensity * 0.9;
                ctx.fill();
                ctx.globalAlpha = 1;
            }
        }
    }

    // --- Animation Loop ---
    function animate(time) {
        ctx.clearRect(0, 0, width, height);

        for (const node of nodes) {
            node.update(time);
        }

        drawConnections(time);

        for (const node of nodes) {
            node.draw();
        }

        drawHighlightedNodes();

        animationId = requestAnimationFrame(animate);
    }

    // --- Event Listeners ---
    canvas.addEventListener('mousemove', (e) => {
        const rect = canvas.getBoundingClientRect();
        mouse.x = e.clientX - rect.left;
        mouse.y = e.clientY - rect.top;
    });

    canvas.addEventListener('mouseleave', () => {
        mouse.x = null;
        mouse.y = null;
    });

    // Touch support for mobile
    canvas.addEventListener('touchmove', (e) => {
        const rect = canvas.getBoundingClientRect();
        mouse.x = e.touches[0].clientX - rect.left;
        mouse.y = e.touches[0].clientY - rect.top;
    }, { passive: true });

    canvas.addEventListener('touchend', () => {
        mouse.x = null;
        mouse.y = null;
    });

    let resizeTimeout;
    window.addEventListener('resize', () => {
        clearTimeout(resizeTimeout);
        resizeTimeout = setTimeout(() => {
            resize();
            // Reposition nodes within new bounds
            for (const node of nodes) {
                node.x = Math.min(node.x, width);
                node.y = Math.min(node.y, height);
            }
        }, 200);
    });

    // --- Start ---
    init();
    animate(0);
})();
