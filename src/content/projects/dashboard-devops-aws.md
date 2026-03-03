---
title: "Dashboard DevOps AWS"
description: "Monorepo combining a Flask dashboard for visualizing air quality in France and DevOps documentation built with Quartz, featuring automated deployment to AWS (EKS) and Cloudflare Pages."
---

<section class="container">
<div class="glass" style="padding: 2rem; border-radius: var(--radius-lg); margin-bottom: 2rem;">
<h1 style="margin-bottom: 1rem;">Dashboard DevOps AWS</h1>
<p style="color: var(--text-secondary); margin-bottom: 2rem;">
Monorepo combining a Flask dashboard for visualizing air quality in France and DevOps documentation
built with Quartz, featuring automated deployment to AWS (EKS) and Cloudflare Pages.
</p>

<!-- Project Details / Overview -->
<div style="margin-bottom: 2rem;">
<h2 style="font-size: 1.5rem; margin-bottom: 0.5rem;">Overview</h2>
<p style="color: var(--text-secondary); margin-bottom: 1rem;">
This project serves as a comprehensive monorepo managing both an application and its underlying
DevOps documentation. The primary components are:
</p>
<ul
style="padding-left: 1.5rem; color: var(--text-secondary); list-style: disc; margin-bottom: 1rem;">
<li><strong>Air Quality Dashboard:</strong> A Python/Flask application providing data
visualization for air pollution statistics across France.</li>
<li><strong>Labs Docs:</strong> An internal documentation site built using Quartz to record and
detail DevOps practices and labs.</li>
<li><strong>Infrastructure:</strong> Shared Kubernetes (K8s) manifests to orchestrate
deployments and define the infrastructure as code.</li>
</ul>
</div>

<!-- Architecture & Deployment -->
<div style="margin-bottom: 2rem;">
<h2 style="font-size: 1.5rem; margin-bottom: 0.5rem;">Architecture & Deployment</h2>
<p style="color: var(--text-secondary); margin-bottom: 1rem;">
The monorepo architecture streamlines continuous integration and deployment using GitHub
Actions:
</p>
<ul
style="padding-left: 1.5rem; color: var(--text-secondary); list-style: disc; margin-bottom: 1rem;">
<li>The <strong>Air Quality Dashboard</strong> is containerized natively and deployed to a
managed <strong>AWS Elastic Kubernetes Service (EKS)</strong> cluster.</li>
<li>The <strong>Labs Documentation</strong> leverages standard static site generation and is
pushed directly to <strong>Cloudflare Pages</strong> for rapid global edge delivery.</li>
</ul>
</div>

<!-- Link to Repo -->
<div style="text-align: center; margin-top: 2rem;">
<a href="https://github.com/wilfried-lafaye/dashboard-devops-aws" target="_blank"
class="btn-primary">View on GitHub</a>
<a href="https://dashboard-devops-aws.pages.dev" target="_blank" class="btn-secondary"
style="margin-left: 1rem;">View Labs Documentation</a>
</div>
</div>

<div class="glass" style="padding: 2rem; border-radius: var(--radius-lg);">
<h2>Technical Details</h2>
<ul style="margin-top: 1rem; padding-left: 1.5rem; list-style: disc; color: var(--text-secondary);">
<li><strong>Technologies:</strong> Flask, AWS EKS, Cloudflare Pages, TypeScript, Docker</li>
</ul>
</div>
</section>