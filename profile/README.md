# Synthetic Autonomic Mind

**Where intelligent tools meet your workflow**

---

## Welcome to SAM

The Synthetic Autonomic Mind organization builds AI tools designed for real people doing real work. Whether you're an everyday user looking for a powerful macOS assistant, a developer needing specialized tools, or a power user living in the terminal — we have something for you.

**Start here:** [**SAM** - your intelligent macOS assistant](https://github.com/SyntheticAutonomicMind/SAM)  
The entry point for most users. Privacy-first, powerful, and designed for non-technical macOS users.

---

## Our Products

### 🔗 **SAM** - The Core Experience

**A native macOS AI assistant that remembers, creates, and gets work done.**

For everyday macOS users who want powerful AI without complexity.

- **🔗 Repository:** [github.com/SyntheticAutonomicMind/SAM](https://github.com/SyntheticAutonomicMind/SAM)
- **📄 Full Documentation:** [syntheticautonomicmind.org](https://www.syntheticautonomicmind.org)
- **⬇️ Download:** [Latest Release](https://github.com/SyntheticAutonomicMind/SAM/releases)

**What you can do with SAM:**
-  **Chat naturally** with AI (voice or text) — Say "Hey SAM" to go hands-free
-  **Work with documents** — Upload PDFs, Word docs, Excel files and ask questions
-  **Generate images locally** — Create images with Stable Diffusion (no internet needed)
- 🧠 **Smart memory** — SAM remembers your conversations and finds them semantically
-  **Multiple AI providers** — Use OpenAI, Claude, local models (MLX, llama.cpp), or DeepSeek
- 🚀 **Access from anywhere** — Chat with SAM from your iPad or iPhone via SAM-Web
- ⚙️️ **Automate tasks** — Run commands, manage files, research the web

**Why SAM?**
- Your data stays on your Mac (always)
- No subscriptions, no ads, no hidden costs
- 100% free & open source
- Built for non-technical users first

---

### 🔗 **ALICE** - Image Generation Backend

**A professional Stable Diffusion service for developers and organizations.**

For engineers building image generation into their applications, or deploying GPU workloads at scale.

- **🔗 Repository:** [github.com/SyntheticAutonomicMind/ALICE](https://github.com/SyntheticAutonomicMind/ALICE)
- **📄 Documentation:** [README](https://github.com/SyntheticAutonomicMind/ALICE#readme)

**What ALICE provides:**
-  **OpenAI-compatible REST API** for Stable Diffusion image generation
- 🚀 **Multi-GPU support** — NVIDIA (CUDA), AMD (ROCm), Apple Silicon, CPU
- ️ **Production deployment** — Systemd daemon for Linux, launchd for macOS
-  **Privacy controls** — Image ownership tracking, expiring public galleries
- ✅ **Model management** — Download from CivitAI and HuggingFace automatically
- 🔗 **Works with SAM** — Optional provider for offloading image generation

**Who uses ALICE?**
- Developers building AI image features
- Organizations deploying GPU workloads
- SAM users who want to offload image generation to dedicated hardware

---

### 🔗 **CLIO** - Terminal AI Assistant

**An AI code assistant that lives in your terminal. Privacy-first, portable, tool-powered.**

For developers, sysadmins, and power users who prefer the command line.

- **🔗 Repository:** [github.com/SyntheticAutonomicMind/CLIO](https://github.com/SyntheticAutonomicMind/CLIO)
- **📄 User Guide:** [Documentation](https://github.com/SyntheticAutonomicMind/CLIO#readme)
- **⬇️ Install:** See repository for setup

**What CLIO does:**
- ️ **Terminal-native** — Professional markdown rendering, color themes, streaming responses
-  **File operations** — Read, write, search, edit files seamlessly
-  **Full Git integration** — Commit, diff, branch, merge from chat
-  **Run commands** — Execute shell scripts and see results in real-time
- 🧠 **Persistent memory** — Save and recall context across sessions
- ️ **Todo lists** — Manage tasks without leaving your workflow
- 🎯 **Custom instructions** — Per-project `.clio/instructions.md` for your standards
- 🚀 **Multiple AI backends** — GitHub Copilot, OpenAI, DeepSeek, SAM, and more

**Who uses CLIO?**
- Terminal-first developers
- Sysadmins and DevOps engineers
- Anyone who prefers command line over GUI

---

## The SAM Ecosystem

These projects work together:

```
┌──────────────────────────────────┐
│   SAM (macOS Desktop)            │
│  - Chat, images, documents       │
├──────────────────────────────────┤
│   Uses ALICE for image generation│
│   Connects to SAM-Web for mobile │
└──────────────────────────────────┘

CLIO (Terminal)                ALICE (Backend)
- Standalone AI assistant      - Stable Diffusion service
- For developers               - Powers image features
```

---

## Quick Links

**Getting Started:**
-  **Website:** [www.syntheticautonomicmind.org](https://www.syntheticautonomicmind.org)
- **SAM Download:** [github.com/SyntheticAutonomicMind/SAM/releases](https://github.com/SyntheticAutonomicMind/SAM/releases)
- **CLIO Install:** [github.com/SyntheticAutonomicMind/CLIO#installation](https://github.com/SyntheticAutonomicMind/CLIO#installation)

**Support & Community:**
- 🐛 **Report Issues:** [github.com/SyntheticAutonomicMind/SAM/issues](https://github.com/SyntheticAutonomicMind/SAM/issues)
-  **Discussions:** Each repository has its own discussions
- ️ **Support Us:** [Patreon (patreon.com/fewtarius)](https://www.patreon.com/fewtarius)

**All Repositories:**
- [SAM](https://github.com/SyntheticAutonomicMind/SAM) - Main macOS application
- [SAM-Web](https://github.com/SyntheticAutonomicMind/SAM-web) - Web interface for iPad/iPhone/browser
- [ALICE](https://github.com/SyntheticAutonomicMind/ALICE) - Image generation backend
- [CLIO](https://github.com/SyntheticAutonomicMind/CLIO) - Terminal AI assistant
- [Website](https://github.com/SyntheticAutonomicMind/website) - Documentation and guides

---

## Our Philosophy

We believe AI should:

- **Respect your privacy** — Your data stays where you control it
- **Be transparent** — You understand what's happening and why
- **Work your way** — Adapt to your workflow, not the reverse
- **Empower, not replace** — AI should help you accomplish more, not take over
- **Be accessible** — Powerful tools should work for everyone, not just developers

All our projects are **100% free & open source** under GPL v3.0 (code) and CC BY-NC 4.0 (documentation).

---

## Support the Project

Your support helps us:
-  Fund software licenses and developer accounts
- 🚀 Build new features and improve existing ones
-  Maintain infrastructure and deployment systems
- 📄 Create documentation and tutorials

**[Become a Patron](https://www.patreon.com/fewtarius)**  
Help us build the next generation of transparent, user-first AI tools. Let's create something special together.

---

## License

- **Code:** [GPL v3.0](https://www.gnu.org/licenses/gpl-3.0)
- **Documentation:** [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)

---

**Built by [fewtarius](https://github.com/fewtarius) and contributors**
