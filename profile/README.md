# Synthetic Autonomic Mind

**Privacy-first AI tools. Free, open source, and built to work the way you do.**

---

## The Story

I built **SAM** for my wife - she wanted a powerful AI assistant that adapted to her workflow instead of forcing her to adapt. I built **CLIO** for myself - I live in the terminal and couldn't find an AI tool that felt native there. I built **ALICE** for fun - I wanted to generate images on my own hardware without cloud services taking a cut.

Together, they became an ecosystem. SAM handles the desktop. CLIO handles the terminal. ALICE handles image generation. They share providers, respect your privacy, and work the way you do.

Everything here is 100% free and open source. No telemetry. No accounts required. Your data stays on your machine.

---

## The Ecosystem

SAM, CLIO, and ALICE work together or independently - whatever fits your workflow.

| | **SAM** | **CLIO** | **ALICE** |
|---|---|---|---|
| **What** | Native macOS AI assistant | Terminal AI code assistant | Stable Diffusion image server |
| **For** | Everyday Mac users, developers, anyone | Developers, sysadmins, terminal users | Creators, developers, hobbyists |
| **Where** | macOS desktop + iPad/iPhone via SAM-Web | Any terminal (macOS, Linux, SSH, Docker) | macOS, Linux (NVIDIA, AMD, Apple Silicon) |
| **Standout** | Voice control, semantic memory, document analysis, LoRA training | 50 MB RAM, runs on a ClockworkPi, multi-agent coordination | Runs on a Steam Deck, OpenAI-compatible API, private gallery |

**How they connect:**
- SAM can offload image generation to ALICE on dedicated hardware
- CLIO can use SAM as an AI provider
- All three support the same cloud providers (OpenAI, Anthropic, GitHub Copilot, DeepSeek, and more)
- All three run local models for complete offline operation

---

## SAM - Built for My Wife

**A native macOS AI assistant that remembers, creates, and gets work done.**

In July 2025, I set out to build the AI assistant my wife actually wanted. One that adapted to her workflow, not the other way around. SAM grew from that into a full-featured macOS app that anyone can use.

Say "Hey SAM" to go hands-free. Import documents and ask questions about them. Generate images locally with Stable Diffusion. Train custom models on your own data with LoRA. Access SAM from your iPad or phone with SAM-Web. Choose from local models (MLX, llama.cpp) or cloud providers - your data never leaves your Mac unless you choose otherwise.

**Repository:** [github.com/SyntheticAutonomicMind/SAM](https://github.com/SyntheticAutonomicMind/SAM)
**Website:** [syntheticautonomicmind.org](https://www.syntheticautonomicmind.org)
**Download:** [Latest Release](https://github.com/SyntheticAutonomicMind/SAM/releases) or `brew install --cask sam`

---

## CLIO - Built for Myself

**An AI code assistant that lives in your terminal. Portable, privacy-first, and designed for real work.**

I work in the terminal. I wanted an AI assistant that felt native there - not a browser tab, not an IDE plugin, not something that needed Node.js and 500 MB of dependencies. CLIO is pure Perl, runs on standard Unix tools, and uses about 50 MB of RAM.

Since version 20260119.1, CLIO has been building itself. All development on SAM, CLIO, and ALICE is now done through pair programming with AI agents using CLIO. It reads, writes, tests, commits, and iterates - give it a task and it works through it end-to-end.

Real numbers from real sessions:

```
29h 43m uptime  |  10.7 MB RSS  |  502 tool calls
27h 27m uptime  |  10.8 MB RSS  |  58 tool calls
 3h 5m  uptime  |  50.6 MB RSS  |  507 tool calls
```

No memory leaks. No degradation. No restart needed.

Runs on everything from a ClockworkPi uConsole R01 to an M4 Mac. Works over SSH. Deploys via Docker. Supports multi-agent coordination, remote execution across your fleet, MCP integration, and long-term memory that persists across sessions.

**Repository:** [github.com/SyntheticAutonomicMind/CLIO](https://github.com/SyntheticAutonomicMind/CLIO)
**Install:** `brew install clio` or [see installation docs](https://github.com/SyntheticAutonomicMind/CLIO#quick-start)

---

## ALICE - Built for Fun

**A local Stable Diffusion service with a web interface, private gallery, and OpenAI-compatible API.**

I wanted to generate images on my own hardware without paying per-image or uploading prompts to someone else's server. ALICE started as a weekend project and turned into a full image generation platform.

Text-to-image with any Stable Diffusion model (SD 1.5, SDXL, FLUX). Browse and download models from CivitAI and HuggingFace. Private gallery with optional time-limited sharing. Real-time GPU dashboard. Admin panel with user management. Runs as a daemon on Linux or macOS.

Works on NVIDIA (CUDA), AMD (ROCm - including Steam Deck), and Apple Silicon. Integrates with SAM as an image provider, or use it standalone through the web interface or API.

**Repository:** [github.com/SyntheticAutonomicMind/ALICE](https://github.com/SyntheticAutonomicMind/ALICE)
**Install:** [Getting Started](https://github.com/SyntheticAutonomicMind/ALICE#quick-start)

---

## How These Tools Get Built

All three projects are developed using The Unbroken Method - a framework for human-AI pair programming that I developed alongside the tools themselves. The method prioritizes continuous context, complete ownership, investigation before action, and structured handoffs.

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
- **Contribute code:** All three projects welcome pull requests
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
