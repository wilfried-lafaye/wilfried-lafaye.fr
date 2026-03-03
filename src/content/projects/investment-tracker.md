---
title: "Investment Tracker"
description: ""
---

<section class="container">
<div class="glass" style="padding: 2rem; border-radius: var(--radius-lg); margin-bottom: 2rem;">
<h1 style="margin-bottom: 1rem;">Investment Tracker</h1>
<p style="color: var(--text-secondary); margin-bottom: 2rem;">
A premium, modern web application for tracking personal investments.
It allows you to manage your portfolio, track assets, and visualize financial performance with data
persisted locally on your device.
</p>

<!-- APP CONTAINER or IMAGE -->
<!-- APP CONTAINER -->
<div class="app-container"
style="width: 100%; aspect-ratio: 16/9; background: #000; border-radius: var(--radius-md); overflow: hidden; border: 1px solid var(--glass-border);">
<iframe src="../apps/investment-tracker/index.html"
style="width: 100%; height: 100%; border: none;"></iframe>
</div>

<div style="margin-top: 1rem; text-align: center;">
<p style="font-size: 0.8rem; color: var(--text-secondary);">
* Running locally in your browser (Static App). Data is saved to your device.
</p>
</div>
</div>

<div class="glass" style="padding: 2rem; border-radius: var(--radius-lg);">
<h2>Technical Details</h2>
<ul style="margin-top: 1rem; padding-left: 1.5rem; list-style: disc; color: var(--text-secondary);">
<li><strong>Frontend:</strong> React, Vite</li>
<li><strong>Styling:</strong> Tailwind CSS</li>
<li><strong>State Management:</strong> Context API</li>
<li><strong>Database:</strong> IndexedDB (Local persistence)</li>
<li><strong>Charts:</strong> Recharts</li>
<li><strong>Source Code:</strong> <a href="https://github.com/wilfried-lafaye/track-my-invest-app"
target="_blank" style="color: var(--primary);">GitHub Repository</a></li>
</ul>
</div>
</section>