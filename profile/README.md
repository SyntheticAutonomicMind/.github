# Synthetic Autonomic Mind

**Free, open source AI tools that do things, not just chat.**

I built SAM for my wife. She wanted an AI assistant that could work with her documents, research purchases, generate images, and remember what they'd talked about. Nothing fit, so I built it.

I built CLIO for myself. I spend more time in terminal sessions than I do using GUIs, and I wanted a terminal-first AI development tool that worked the way I work. It didn't really exist, so I built it.

I built ALICE for fun. I wanted to generate images on my own hardware without paying per image or uploading prompts to someone else's server.

Together they became an ecosystem. SAM handles the desktop. CLIO handles the terminal. ALICE handles image and audio generation. They share providers, keep your data local, and adapt to how you work.

---

## SAM - Native macOS AI Assistant

A native SwiftUI app for people who aren't developers. Say "Hey SAM" to go hands-free. Upload a PDF and ask questions about it. Research a purchase across Amazon, Walmart, and eBay in one conversation. Generate images by connecting to ALICE. All without touching a command line.

**What you can do:**
- **Talk to your documents** - Upload PDFs, Word docs, Excel files. SAM indexes them locally and lets you ask questions about the content. Your documents stay on your Mac.
- **Research from real sources** - Google, Bing, Amazon, Yelp, TripAdvisor. SAM fetches live data and cites where it found the information.
- **Generate images and music** - Connect to an ALICE server on your network for image and audio generation.
- **Go hands-free** - "Hey SAM" wake word, speech recognition, text-to-speech. Works offline with local models.
- **Remember across conversations** - Create Shared Topics to connect related conversations. Search your history by meaning, not just keywords.
- **Run completely offline** - MLX and llama.cpp support. Your conversations never leave your Mac unless you choose a cloud provider.

**macOS 14.0+ (Apple Silicon).** [GitHub](https://github.com/SyntheticAutonomicMind/SAM)

---

## CLIO - Terminal AI Coding Assistant

A terminal-native AI tool that reads your code, edits files, runs commands, manages git, and works through tasks with you in the loop. Not a chat wrapper. Not an IDE plugin. A pair programmer that lives in your shell.

**What you can do:**
- **Give it a task, it does the work** - CLIO investigates your codebase, proposes a plan, you approve, it implements. Edits files, runs tests, commits changes.
- **Work from anywhere** - Local shells, SSH sessions, tmux, Docker, headless servers. Anywhere Perl runs.
- **Zero dependencies** - Pure Perl with standard core modules. No CPAN, no npm, no pip. Install and run.
- **Pick up where you left off** - Persistent sessions with full history. Long-term memory carries across projects.
- **Coordinate parallel agents** - Spawn sub-agents with file locks, git locks, and rate limiting.
- **Run across your fleet** - SSH into any machine, deploy CLIO, run a task, get results.
- **Stay private** - Secret redaction catches API keys and tokens before they reach the AI. Your code stays on your machine.

**macOS, Linux, Windows.** [GitHub](https://github.com/SyntheticAutonomicMind/CLIO)

---

## ALICE - Local Image & Audio Generation

SAM's media generation engine - and a standalone Stable Diffusion and audio generation server for anyone who wants private image and music generation on their own hardware. Text-to-image with SD 1.5, SDXL, and FLUX. Stable Audio Open 1.0 and MiniMax Music 3 for text-to-audio generation. Browse and download models from CivitAI and HuggingFace. Private gallery with optional sharing. Runs on NVIDIA, AMD (including Steam Deck), and Apple Silicon.

**Install:** [Getting Started](https://github.com/SyntheticAutonomicMind/ALICE#quick-start) | [GitHub](https://github.com/SyntheticAutonomicMind/ALICE)

---

## What They Share

- **Local-first** - SAM defaults to local models. CLIO sends only minimum context to AI providers. ALICE runs on your hardware. Your data stays on your machine.
- **Tool-powered** - They don't just generate text. They use real tools - files, git, terminal, web, memory - to accomplish tasks.
- **Free and open source** - GPL-3.0. No subscriptions, no tiers, no paywalls. Community-funded through [Patreon](https://www.patreon.com/fewtarius).
- **Multi-provider** - OpenAI, Anthropic, GitHub Copilot, Google Gemini, DeepSeek, MiniMax, OpenRouter, or local models. Switch whenever you want.

---

## Quick Start

| Tool | Install | Platforms |
|------|---------|-----------|
| **SAM** | `brew install --cask sam` | macOS 14.0+ (Apple Silicon) |
| **CLIO** | `brew install clio` | macOS, Linux, Windows |
| **ALICE** | [Setup Guide](https://github.com/SyntheticAutonomicMind/ALICE#quick-start) | macOS, Linux |

**All repositories:** [SAM](https://github.com/SyntheticAutonomicMind/SAM) · [CLIO](https://github.com/SyntheticAutonomicMind/CLIO) · [ALICE](https://github.com/SyntheticAutonomicMind/ALICE) · [SAM-Web](https://github.com/SyntheticAutonomicMind/SAM-web) · [CLIO-helper](https://github.com/SyntheticAutonomicMind/CLIO-helper)

**Website:** [syntheticautonomicmind.org](https://www.syntheticautonomicmind.org) · **Support development:** [Patreon](https://www.patreon.com/fewtarius)

---

*AI tools should respect your privacy, be transparent about what they do, and be accessible to everyone. GPL-3.0 for code, CC BY-NC 4.0 for docs.*