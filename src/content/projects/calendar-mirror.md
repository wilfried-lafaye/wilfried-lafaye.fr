---
title: "Calendar Mirror"
description: "An application for mirroring calendar events, built for iOS/macOS using Swift."
---

<section class="container">
<div class="glass" style="padding: 2rem; border-radius: var(--radius-lg); margin-bottom: 2rem;">
<h1 style="margin-bottom: 1rem;">Calendar Mirror (MirrorCal)</h1>
<p style="color: var(--text-secondary); margin-bottom: 2rem;">
A native Apple application (macOS menu bar and iOS app) that seamlessly synchronizes and mirrors
events from multiple source calendars into a single unified destination calendar.
</p>

<!-- Project Images -->
<div
style="display: flex; flex-direction: row; gap: 1.5rem; align-items: flex-start; justify-content: center; margin-bottom: 2rem;">
<!-- macOS App Mockup -->
<div style="flex: 2; text-align: center;">
<div
style="border-radius: var(--radius-md); overflow: hidden; border: 1px solid var(--glass-border); box-shadow: 0 4px 6px rgba(0,0,0,0.3); margin-bottom: 0.5rem;">
<img src="../img/calendar-mirror.png" alt="MirrorCal macOS App Mockup"
style="width: 100%; height: auto; display: block;">
</div>
<p style="color: var(--text-secondary); font-size: 0.9rem; margin: 0;">Application macOS</p>
</div>
<!-- iOS App Mockup -->
<div style="flex: 1; max-width: 300px; text-align: center;">
<div
style="border-radius: var(--radius-md); overflow: hidden; border: 1px solid var(--glass-border); box-shadow: 0 4px 6px rgba(0,0,0,0.3); margin-bottom: 0.5rem;">
<img src="../img/calendar-mirror-ios.png" alt="MirrorCal iOS App Mockup"
style="width: 100%; height: auto; display: block;">
</div>
<p style="color: var(--text-secondary); font-size: 0.9rem; margin: 0;">Application iOS</p>
</div>
</div>

<!-- Project Details / Introduction -->
<div style="margin-bottom: 2rem;">
<h2 style="font-size: 1.5rem; margin-bottom: 0.5rem;">Introduction</h2>
<p style="color: var(--text-secondary); margin-bottom: 1rem;">
MirrorCal is specifically designed to solve the problem of fragmented schedules. It perfectly
combines professional, personal, and family calendars into one unified overview without
accidentally mixing or merging the underlying accounts.
</p>
</div>

<!-- Features -->
<div style="margin-bottom: 2rem;">
<h2 style="font-size: 1.5rem; margin-bottom: 0.5rem;">Key Features</h2>
<ul
style="padding-left: 1.5rem; color: var(--text-secondary); list-style: disc; margin-bottom: 1rem;">
<li><strong>Multi-Source Synchronization:</strong> Select and consolidate events from multiple
platforms simultaneously (iCloud, Google, Exchange, Outlook, Local calendars).</li>
<li><strong>Unified Destination:</strong> Choose a dedicated local destination calendar where
all copied events will reside cleanly.</li>
<li><strong>Automatic Sync (macOS):</strong> Listens to calendar changes and mirrors them
within seconds, with a catch-up sync at launch. No date range to pick: the window is a rolling
one (90 days back to 3 years ahead), and <em>Launch at Login</em> keeps the app running.</li>
<li><strong>Smart Incremental Sync (macOS):</strong> Each mirrored event is tracked in a local
mapping and compared with a SHA256 hash. Only created, modified or deleted events are written;
a sync with no change writes nothing.</li>
<li><strong>Recurrence & Deletions:</strong> Gracefully supports recurring events and implements
safeties algorithms for sweeping orphaned/deleted events.</li>
<li><strong>100% Local & Private:</strong> Operates entirely on-device using the native Apple
EventKit framework. There are no external servers, no network calls, and absolutely no data
collection.</li>
<li><strong>Shortcuts &amp; Siri:</strong> A "refresh calendars" action (App Intents) on macOS
and iOS, usable from the Shortcuts app, Siri and Automations.</li>
<li><strong>Cross-Platform:</strong> Available as a lightweight, unobtrusive macOS menu bar
utility and an iOS application.</li>
</ul>
</div>

<!-- How it works -->
<div style="margin-bottom: 2rem;">
<h2 style="font-size: 1.5rem; margin-bottom: 0.5rem;">How it Works</h2>
<p style="color: var(--text-secondary); margin-bottom: 1rem;">
The user experience is built around a simple, transparent workflow running natively on the
device:
</p>
<ol
style="padding-left: 1.5rem; color: var(--text-secondary); list-style: decimal; margin-bottom: 1rem;">
<li>Grant Calendar access to the application gracefully via EventKit.</li>
<li>Select one or more <strong>Source Calendars</strong> to pull event data from.</li>
<li>Designate a <strong>Destination Calendar</strong> (creating an empty local calendar is
standard practice).</li>
<li><strong>macOS:</strong> nothing else to do. The app syncs at launch and whenever a source
calendar changes, and <strong>Sync Now</strong> (⌘R) is available in the menu bar.</li>
<li><strong>iOS:</strong> set the <strong>Synchronization Period</strong> (from/to dates, the
current week by default), then tap <strong>Sync Now</strong>. The app also re-syncs on calendar
changes while it is open.</li>
</ol>
</div>

<!-- AI Assistance -->
<div style="margin-bottom: 2rem;">
<h2 style="font-size: 1.5rem; margin-bottom: 0.5rem;">AI Assistance</h2>
<p style="color: var(--text-secondary); margin-bottom: 1rem;">
This project was developed with the help of an AI coding assistant, <strong>Claude</strong>
(Anthropic), notably for the macOS automatic synchronization engine and the Shortcuts / App
Intents support. This is also visible in the repository's commit history.
</p>
</div>

<!-- Link to Repo -->
<div style="text-align: center; margin-top: 2rem;">
<a href="https://github.com/wilfried-lafaye/calendar-mirror" target="_blank"
class="btn-primary">View on GitHub</a>
</div>
</div>

<div class="glass" style="padding: 2rem; border-radius: var(--radius-lg);">
<h2>Technical Details</h2>
<ul style="margin-top: 1rem; padding-left: 1.5rem; list-style: disc; color: var(--text-secondary);">
<li><strong>Technologies:</strong> Swift, iOS, macOS, EventKit</li>
<li><strong>Development:</strong> Built with the help of Claude (AI coding assistant)</li>
</ul>
</div>
</section>