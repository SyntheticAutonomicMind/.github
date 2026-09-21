# Synthetic Autonomic Mind

**AI tools built for real work.**

An ecosystem of free, open-source tools that run on your hardware. SAM is a native macOS assistant for your desktop. CLIO is a terminal agent that reads your code, writes changes, and ships commits. ALICE is a local image-and-audio generator that runs on your GPU.

They share providers, keep your data local, and as a system build themselves.

Every line of CLIO, ALICE, and most of SAM has been written through pair-programming with CLIO itself, following a methodology called [the Unbroken Method](https://www.syntheticautonomicmind.org/docs/shared/the-unbroken-method.html): investigate before modifying, checkpoint before committing, carry context across sessions instead of resetting. The development tool and the tools it produces are part of the same reflexive loop. CLIO has been maintaining its own codebase since v20260119.1.

---

## What They Are

| | |
|---|---|
| **SAM** | A native macOS AI assistant. Voice-controlled ("Hey SAM"), document-aware (PDFs, Word, Excel), web-connected, and memory-enabled. [Repository](https://github.com/SyntheticAutonomicMind/SAM) |
| **CLIO** | Terminal-native AI coding agent. Reads your codebase, edits files, runs tests, manages git, coordinates parallel agents across your fleet - from a Raspberry Pi to an M4 Mac. Zero external dependencies. [Repository](https://github.com/SyntheticAutonomicMind/CLIO) |
| **ALICE** | Local Stable Diffusion and audio-generation server. Text-to-image, image-to-image, text-to-audio. Runs on NVIDIA, AMD (including Steam Deck), and Apple Silicon. [Repository](https://github.com/SyntheticAutonomicMind/ALICE) |

SAM is built in Swift and SwiftUI. CLIO is built in Perl. ALICE is built in Python with FastAPI.

---

## What They Share

- **Local-first** - Run offline with on-device models (MLX, llama.cpp). Only connect to cloud providers when you choose. Your data never leaves your machine unless you decide it should.
- **Tool-powered** - They execute real actions: file I/O, git operations, shell commands, web fetches, model downloads, GPU monitoring - not just text completion.
- **Multi-provider** - OpenAI, Anthropic, GitHub Copilot, Google Gemini, DeepSeek, MiniMax, OpenRouter, Z.AI, llama.cpp, LM Studio, SAM, or any OpenAI-compatible API. Switch providers mid-conversation.
- **Continuity** - SAM remembers conversations across sessions. CLIO retains long-term memory, learned patterns, and project context indefinitely.
- **Self-building** - CLIO has been modifying its own codebase under human direction since v20260119.1. It also built all of ALICE and maintains SAM.

---

## Supporting Tools

| | |
|---|---|
| **[CLIO-helper](https://github.com/SyntheticAutonomicMind/CLIO-helper)** | A GitHub monitoring daemon powered by CLIO. Reads your repos, triages issues, reviews pull requests, manages stale items, and generates release notes using CLIO's code-analysis tools. |

---

## Quick Start

| Tool | Install | Platforms |
|------|---------|-----------|
| **SAM** | `brew tap SyntheticAutonomicMind/homebrew-SAM && brew install --cask sam` | macOS 14.0+ (Apple Silicon) |
| **CLIO** | `brew tap SyntheticAutonomicMind/homebrew-SAM && brew install clio` | macOS, Linux, Windows |
| **ALICE** | [Setup Guide](https://github.com/SyntheticAutonomicMind/ALICE#quick-start) | macOS, Linux |

**Documentation:** [syntheticautonomicmind.org](https://www.syntheticautonomicmind.org) · **Support development:** [Patreon](https://www.patreon.com/fewtarius)

---

*AI tools should respect your privacy, be transparent about what they do, and be accessible to everyone. GPL-3.0 for code, CC BY-NC 4.0 for documentation.*
