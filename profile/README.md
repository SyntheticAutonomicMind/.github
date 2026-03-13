# Synthetic Autonomic Mind

**Privacy-first AI tools for everyone. Free, open source, and built to work the way you do.**

---

## The Story

I built **SAM** for my wife - she wanted a powerful AI assistant that adapted to her workflow instead of forcing her to adapt. I built **CLIO** for myself - I live in the terminal and couldn't find an AI tool that felt native there. I built **ALICE** for fun - I wanted to generate images on my own hardware without cloud services taking a cut.

Together, they became an ecosystem. SAM handles the desktop. CLIO handles the terminal. ALICE handles image generation. They share providers, respect your privacy, and work the way you do.

Everything here is 100% free and open source. No telemetry. No accounts required. Your data stays on your machine.

---

## The Ecosystem

SAM, CLIO, and ALICE work together or independently - each one doing what it does best.

| | **SAM** | **CLIO** | **ALICE** |
|---|---|---|---|
| **What** | Native macOS AI assistant | Terminal AI code assistant | Stable Diffusion image server |
| **For** | Everyday Mac users, anyone | Developers, sysadmins, terminal users | Creators, developers, hobbyists |
| **Where** | macOS desktop + iPad/iPhone via SAM-Web | Any terminal (macOS, Linux, SSH, Docker) | macOS, Linux (NVIDIA, AMD, Apple Silicon) |
| **Standout** | Voice control, semantic memory, document analysis, image gen via ALICE | ~50 MB RAM, runs on a ClockworkPi, multi-agent coordination | SAM's image engine, OpenAI-compatible API, private gallery |

**How they connect:**
- SAM uses ALICE as its image engine - describe what you want, SAM asks ALICE, ALICE generates it locally
- CLIO can use SAM as an AI provider
- They support the same cloud providers (OpenAI, Anthropic, GitHub Copilot, DeepSeek, and more)
- They work with local models for complete offline operation

---

## SAM - Built for My Wife

**A native macOS AI assistant that remembers, gets work done, and keeps your data on your Mac.**

In July 2025, I set out to build the AI assistant my wife actually wanted. One that adapted to *her* workflow instead of forcing her to adapt. SAM grew from that into a native macOS assistant that anyone can use.

SAM is built for everyday use by real people, not just developers. Say "Hey SAM" to go hands-free. Import documents and ask questions about them. Generate images by connecting to an [ALICE](https://github.com/SyntheticAutonomicMind/ALICE) server - on your Mac, your network, or any machine you control. Run real math calculations without trusting AI to get the arithmetic right. Access SAM from your iPad or phone with SAM-Web. Choose from local models (MLX, llama.cpp) or cloud providers - your data never leaves your Mac unless you choose otherwise.

Image generation requires a running ALICE instance. The [ALICE quick install](https://github.com/SyntheticAutonomicMind/ALICE#quick-install) takes a few minutes and runs entirely on your machine.

**Repository:** [github.com/SyntheticAutonomicMind/SAM](https://github.com/SyntheticAutonomicMind/SAM)  
**Website:** [syntheticautonomicmind.org](https://www.syntheticautonomicmind.org)  
**Download:** [Latest Release](https://github.com/SyntheticAutonomicMind/SAM/releases) or `brew install --cask sam`

---

## CLIO - Built for Myself

**An AI code assistant that lives in your terminal. Portable, privacy-first, and built for real work.**

I work in the terminal. I wanted an AI assistant that felt native there - not a browser tab, not an IDE plugin, not something that needed Node.js and 500 MB of dependencies. CLIO is pure Perl, runs on standard Unix tools, and stays lightweight even through hours of heavy development work.

Since version 20260119.1, CLIO has been building itself. All development on SAM, CLIO, and ALICE is now done through pair programming with AI agents using CLIO. It reads, writes, tests, commits, and iterates - give it a task and it works through it end-to-end.

No memory leaks. No degradation. Runs for hours without restart needed.

Runs on everything from a ClockworkPi uConsole R01 to an M4 Mac. Works over SSH. Deploys via Docker. Supports multi-agent coordination, remote execution across your fleet, MCP integration, and long-term memory that persists across sessions.

**Repository:** [github.com/SyntheticAutonomicMind/CLIO](https://github.com/SyntheticAutonomicMind/CLIO)  
**Install:** `brew install clio` or [see installation docs](https://github.com/SyntheticAutonomicMind/CLIO#quick-start)

---

## ALICE - Built for Fun

**SAM's image engine - and a standalone local Stable Diffusion service for anyone who wants private, unlimited image generation.**

I wanted to generate images on my own hardware without paying per-image or uploading prompts to someone else's server. ALICE started as a weekend project and turned into a full image generation platform - and the dedicated image engine for SAM.

When SAM generates an image, ALICE does the work: SAM sends your description, ALICE generates it on your GPU, SAM displays the result. Everything stays on your hardware. No cloud uploads, no per-image cost, no subscription.

Text-to-image with any Stable Diffusion model (SD 1.5, SDXL, FLUX). Browse and download models from CivitAI and HuggingFace. Private gallery with optional time-limited sharing. Real-time GPU dashboard. Runs as a background service on macOS (LaunchAgent, no sudo required) or Linux (systemd).

Works on NVIDIA (CUDA), AMD (ROCm - including Steam Deck), and Apple Silicon. Integrates with SAM as an image provider, or use it standalone through the web interface or API.

**Repository:** [github.com/SyntheticAutonomicMind/ALICE](https://github.com/SyntheticAutonomicMind/ALICE)  
**Install:** [Getting Started](https://github.com/SyntheticAutonomicMind/ALICE#quick-start)

---

## How These Tools Get Built

These projects are developed using The Unbroken Method - a framework for human-AI pair programming that I developed alongside the tools themselves. The method prioritizes continuous context, complete ownership, investigation before action, and structured handoffs.

The practical result: CLIO builds CLIO. CLIO builds SAM. CLIO builds ALICE. One developer, working with AI agents, shipping production software across three languages (Swift, Perl, Python) and three platforms.

If you're interested in the methodology, there's a detailed write-up on the [website](https://www.syntheticautonomicmind.org/docs/shared/the-unbroken-method.html).

---

## Help This Project Grow

Synthetic Autonomic Mind is a small open source project with no marketing budget and no corporate backing. Word of mouth is how projects like this grow.

**If you find these tools useful, the most valuable thing you can do is tell someone.**

- Write a blog post or tweet about your experience
- Mention it to a colleague who might benefit
- Star the repos on GitHub - it helps with discoverability
- Share in communities where these tools would be relevant

**Other ways to help:**

- **Report bugs and request features:** [SAM Issues](https://github.com/SyntheticAutonomicMind/SAM/issues) · [CLIO Issues](https://github.com/SyntheticAutonomicMind/CLIO/issues) · [ALICE Issues](https://github.com/SyntheticAutonomicMind/ALICE/issues)
- **Join the conversation:** [GitHub Discussions](https://github.com/orgs/SyntheticAutonomicMind/discussions)
- **Contribute code:** All projects welcome pull requests
- **Support development:** [Patreon](https://www.patreon.com/fewtarius) - helps fund software licenses, developer accounts, and infrastructure

---

## Our Philosophy

We believe AI tools should respect your privacy, be transparent about what they do, adapt to your workflow, and be accessible to everyone - not just developers. These aren't aspirational goals. They're how the software is built today.

All projects are **100% free & open source** under GPL v3.0 (code) and CC BY-NC 4.0 (documentation).

---

## Quick Start

| Tool | Install | Platforms |
|------|---------|-----------|
| **SAM** | [Download](https://github.com/SyntheticAutonomicMind/SAM/releases) or `brew install --cask sam` | macOS 14.0+ |
| **CLIO** | `brew install clio` or [Docker](https://github.com/SyntheticAutonomicMind/CLIO#quick-start) | macOS, Linux |
| **ALICE** | [Setup Guide](https://github.com/SyntheticAutonomicMind/ALICE#quick-start) | macOS, Linux |

**All Repositories:**
- [SAM](https://github.com/SyntheticAutonomicMind/SAM) - Native macOS AI assistant
- [SAM-Web](https://github.com/SyntheticAutonomicMind/SAM-web) - Web interface for iPad/iPhone/browser
- [CLIO](https://github.com/SyntheticAutonomicMind/CLIO) - Terminal AI assistant
- [ALICE](https://github.com/SyntheticAutonomicMind/ALICE) - Image generation backend
- [Website](https://github.com/SyntheticAutonomicMind/website) - Documentation and guides

**Website:** [www.syntheticautonomicmind.org](https://www.syntheticautonomicmind.org)

---

## License

- **Code:** [GPL v3.0](https://www.gnu.org/licenses/gpl-3.0)
- **Documentation:** [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)
