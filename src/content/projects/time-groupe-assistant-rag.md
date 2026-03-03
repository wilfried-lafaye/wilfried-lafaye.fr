---
title: "Time Groupe Assistant RAG"
description: ""
---

<section class="container">
<div class="glass" style="padding: 2rem; border-radius: var(--radius-lg); margin-bottom: 2rem;">
<h1 style="margin-bottom: 1rem;">Time Groupe Assistant RAG</h1>
<p style="color: var(--text-secondary); margin-bottom: 2rem;">
A virtual AI assistant exploration project leveraging <strong>Retrieval-Augmented Generation
(RAG)</strong> technology to provide context-aware responses based on a custom knowledge base.
</p>

<!-- Project Details / Overview -->
<div style="margin-bottom: 2rem;">
<h2 style="font-size: 1.5rem; margin-bottom: 0.5rem;">Overview & Discovery</h2>
<p style="color: var(--text-secondary); margin-bottom: 1rem;">
This repository serves as a practical discovery and implementation of modern
<strong>RAG</strong> architectures. It was built specifically to act as a virtual assistant for
<a href="https://timegroupe.ca" target="_blank"
style="color: var(--primary); text-decoration: underline;">Time Groupe</a>, an event
management company based in Montreal. By vectorizing their operational data, the assistant
answers highly specific questions accurately without hallucinating.
</p>
</div>

<!-- Core Technologies -->
<div style="margin-bottom: 2rem;">
<h2 style="font-size: 1.5rem; margin-bottom: 0.5rem;">Core Technologies</h2>
<ul
style="padding-left: 1.5rem; color: var(--text-secondary); list-style: disc; margin-bottom: 1rem;">
<li><strong>Backend API:</strong> Built with <code>FastAPI</code> and served via
<code>Uvicorn</code> for high-performance, asynchronous request handling.
</li>
<li><strong>AI Orchestration:</strong> Utilizing <code>LangChain</code> to manage the prompts,
LLM interactions, and data retrieval logic.</li>
<li><strong>Vector Database:</strong> <code>ChromaDB</code> acts as the local vector store,
caching the semantic embeddings of the knowledge base.</li>
<li><strong>Large Language Model:</strong> <code>OpenAI GPT-4o-mini</code> handles the
generative aspect of the responses based on retrieved context.</li>
</ul>
</div>

<!-- Architecture -->
<div style="margin-bottom: 2rem;">
<h2 style="font-size: 1.5rem; margin-bottom: 0.5rem;">System Architecture</h2>
<ul
style="padding-left: 1.5rem; color: var(--text-secondary); list-style: disc; margin-bottom: 1rem;">
<li><strong>Knowledge Base:</strong> A raw text data file (<code>time_groupe_info.txt</code>)
acts as the company's single source of truth.</li>
<li><strong>RAG Engine:</strong> The <code>rag_engine.py</code> module is responsible for
loading the text, chunking it into processable segments, storing it semantically in
ChromaDB, and executing the similarity search retrieval.</li>
<li><strong>API & Interface:</strong> The <code>main.py</code> exposes the orchestration via
REST endpoints, while a lightweight <code>static/index.html</code> serves as the user-facing
chat frontend.</li>
</ul>
</div>

<!-- Usage Context -->
<div style="margin-bottom: 2rem;">
<h2 style="font-size: 1.5rem; margin-bottom: 0.5rem;">API & Usage Context</h2>
<p style="color: var(--text-secondary); margin-bottom: 1rem;">
Once the local server is running, the core interaction happens via the default POST endpoint
(<code>/ask</code>). Users can submit natural language questions such as <em>"Quels types
d'événements organisez-vous ?"</em> (What types of events do you organize?) and the system
retrieves the top contexts from ChromaDB to synthesize an accurate response.
</p>
</div>

<!-- Link to Repo -->
<div style="text-align: center; margin-top: 2rem;">
<a href="https://github.com/wilfried-lafaye/time-groupe-assistant-rag" target="_blank"
class="btn-primary">View on GitHub</a>
</div>
</div>

<div class="glass" style="padding: 2rem; border-radius: var(--radius-lg);">
<h2>Technical Details</h2>
<ul style="margin-top: 1rem; padding-left: 1.5rem; list-style: disc; color: var(--text-secondary);">
<li><strong>Backend:</strong> Python, FastAPI, Uvicorn</li>
<li><strong>AI & DB:</strong> LangChain, ChromaDB, OpenAI</li>
</ul>
</div>
</section>