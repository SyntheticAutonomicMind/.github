# CLIO Project Instructions

**Project:** Synthetic Autonomic Mind (SAM) - GitHub Profile Repository  
**Purpose:** GitHub organization profile page showcasing SAM AI assistant  
**Architecture:** Documentation repository with profile README and screenshots  


## CRITICAL: READ FIRST BEFORE ANY WORK

### Project Overview

This is the GitHub profile repository for **Synthetic Autonomic Mind** organization. It contains:
- `profile/README.md` - The organization's public-facing profile page
- `profile/.images/` - Screenshots and images showcasing SAM features
- `.github/FUNDING.yml` - Patreon funding configuration

**What SAM Is:**
SAM is a native macOS AI assistant built for non-developers. Key features:
- Privacy-first (local AI by default)
- Voice control ("Hey SAM" wake word)
- Local image generation (Stable Diffusion)
- Custom model training (LoRA fine-tuning)
- Remote access (SAM-Web for iPad/iPhone/browser)
- Document intelligence (PDF, Word, Excel)
- Project workspaces in `~/SAM/` folders
- Multi-AI provider support (OpenAI, Anthropic, GitHub Copilot, DeepSeek, MLX, llama.cpp)

**Target Audience:** Non-technical macOS users who want powerful AI assistance without complexity

**Key Repositories:**
- [SAM](https://github.com/SyntheticAutonomicMind/SAM) - Main macOS application
- [SAM-Web](https://github.com/SyntheticAutonomicMind/SAM-web) - Remote web interface
- [ALICE](https://github.com/SyntheticAutonomicMind/ALICE) - Image generation engine
- [website](https://github.com/SyntheticAutonomicMind/website) - Documentation site


## Core Principles for This Repository

### 1. User-First Communication
**This profile page speaks to everyday users, not developers.**

- Use welcoming, approachable language
- Avoid technical jargon unless explaining features
- Focus on benefits and use cases, not implementation details
- Use emojis strategically for visual scanning (but don't overuse)
- Short paragraphs and clear structure

**[CORRECT]:** "SAM remembers what matters across conversations."  
**[WRONG]:** "SAM implements a semantic memory system with vector embeddings."

### 2. Privacy & Trust
**Privacy is SAM's core value proposition.**

- Always emphasize local-first operation
- Clearly state when cloud providers are optional
- Highlight data staying on user's Mac
- Transparent about what goes where

### 3. Accessibility Over Power
**SAM is for everyone, not just tech enthusiasts.**

- Lead with use cases ("For documents & research")
- Show practical value ("Create images in seconds")
- Minimize technical requirements
- Focus on what users can *accomplish*, not what features exist


## Content Standards

### README Structure
The profile README follows this proven structure:
1. **Hero section** - What SAM is, quick links
2. **Introduction** - SAM's story and purpose  
3. **Why you'll love SAM** - Key benefits with emojis
4. **What you can do** - Use cases organized by category
5. **Features at a glance** - Comprehensive feature list
6. **Get started** - Clear next steps
7. **Repositories** - Links to all SAM projects
8. **License** - GPL v3.0 + CC BY-NC 4.0 for docs

**DO NOT restructure without reason.** This layout has been refined over time.

### Writing Style
- **Conversational but professional** - "You'll love" not "Users will appreciate"
- **Active voice** - "SAM helps you finish things" not "Things can be finished with SAM"
- **Benefit-focused** - Lead with outcome, then feature
- **Inclusive pronouns** - "Your data" not "The user's data"
- **Emotional connection** - SAM was built *for* someone, dedicated *to* someone

### Emoji Usage
Emojis serve as visual anchors for scanning:
- 🔗 **[LINK]** - External links
- 📖 **[DOC]** - Documentation
- 🐛 **[BUG]** - Issue tracking
- ❤️ - Support/Patreon
- 🎤 - Voice features
- 🧠 **[BRAIN]** - Intelligence/memory
- 🎨 - Creative/image features
- 📝 **[NOTE]** - Writing/documents
- 🗂️ - Organization
- 💡 **[IDEA]** - Learning/exploration
- ⬇️ - Downloads
- 💻 - Code/technical

**Use consistently but don't force it.** Each section should have 1-2 emojis max.

### Links & URLs
- **Website:** https://www.syntheticautonomicmind.org
- **Main repo:** https://github.com/SyntheticAutonomicMind/SAM
- **Patreon:** https://www.patreon.com/fewtarius
- **Email:** fewtarius@steamfork.org
- **Author:** fewtarius

Always use full URLs in README (not relative paths).


## Image & Screenshot Management

### Naming Convention
Images should follow this standardized format:
- `sam-image-{N}.png` - Generic screenshots/images
- `sam-feature-{name}.png` - Feature-specific screenshots
- `sam-demo-{name}.png` - Demo/tutorial images

**Numbers are sequential starting from 1.**

### Image Guidelines
- Screenshots should show SAM's clean, native macOS interface
- Capture both dark and light mode examples when relevant
- Highlight key features visually
- Use high-quality retina screenshots (2x resolution)
- Keep file sizes reasonable (<5MB per image when possible)
- Avoid showing sensitive/personal information

### Screenshots Section
When adding screenshots to README:
- Group by feature category
- Provide descriptive alt text
- Use consistent image sizing
- Link to full-resolution versions if needed


## Workflow Standards

### Before Making Changes
1. **Read the current content** - Understand context and voice
2. **Check git history** - See what changed recently and why
3. **Preview changes** - Ensure formatting renders correctly
4. **Verify all links** - Test external URLs

### Commit Message Format
```
type(scope): brief description

Problem: What was unclear/broken/missing
Solution: How you improved it
Impact: What users will notice/benefit
```

**Types:** 
- `docs` - Documentation changes (most common here)
- `feat` - New content/sections
- `fix` - Corrections/broken links
- `style` - Formatting/emoji/structure

**Examples:**
```
docs(readme): add screenshots section showcasing SAM features

Problem: Profile lacked visual demonstration of SAM's interface
Solution: Added 7 screenshots organized by feature category
Impact: Visitors can see SAM's UI before downloading

fix(links): correct broken ALICE repository URL

Problem: ALICE repo link pointed to old URL
Solution: Updated to current repository location
Impact: Users can find ALICE project correctly
```

### Testing Changes
```bash
# Check that markdown is valid
# (GitHub will render profile/README.md automatically)

# Verify image paths
ls -lh profile/.images/

# Check file sizes
du -sh profile/.images/*

# Preview locally (if you have a markdown viewer)
# Or push to a test branch and check GitHub rendering
```


## Common Tasks

### Adding New Screenshots
```bash
# 1. Add images to profile/.images/ with standardized names
# 2. Update profile/README.md with new screenshots section
# 3. Test that images display correctly on GitHub
# 4. Commit with descriptive message
```

### Updating Feature Descriptions
```bash
# 1. Read current description in profile/README.md
# 2. Maintain consistent tone and structure
# 3. Update relevant section (don't restructure unnecessarily)
# 4. Keep user-benefit focus, not technical details
# 5. Commit with clear explanation of change
```

### Adding New Repositories
```bash
# 1. Add to "Repositories" section near bottom
# 2. Follow existing format: [Name](URL) - Description
# 3. Keep descriptions brief (one line)
# 4. Maintain alphabetical or logical order
```


## Quality Checklist

### Before Committing Profile Changes
- [ ] Language is welcoming and non-technical
- [ ] Emojis are used consistently and strategically
- [ ] All external links tested and working
- [ ] Privacy/local-first messaging is clear
- [ ] User benefits emphasized over technical features
- [ ] Markdown formatting renders correctly on GitHub
- [ ] No typos or grammatical errors
- [ ] Images display correctly (if changed)
- [ ] Consistent voice throughout
- [ ] Call-to-action links are prominent


## Anti-Patterns: NEVER DO THESE

| Anti-Pattern | Why | What To Do Instead |
|--------------|-----|-------------------|
| Use technical jargon | Alienates target users | Plain language focused on benefits |
| Lead with features | Users don't care about specs | Lead with use cases and outcomes |
| Bury important links | Reduces conversion | Quick Links at top, CTAs throughout |
| Inconsistent tone | Confuses messaging | Maintain friendly, approachable voice |
| Generic screenshots | Low engagement | Show specific, compelling features |
| Skip image alt text | Accessibility issues | Descriptive alt text for all images |
| Overpromise | Damages trust | Be accurate about current capabilities |
| Ignore privacy messaging | Misses key differentiator | Emphasize local-first consistently |


## Project Context

### SAM's Origin Story
Built in July 2025 for the developer's wife - someone who wanted AI to adapt to her workflow, not the other way around. This personal origin story humanizes the project and explains SAM's user-first design philosophy.

**This context matters.** SAM isn't just another AI tool - it was purpose-built for real people.

### License Information
- **Code:** GPL v3.0 (all repositories)
- **Documentation:** CC BY-NC 4.0 (website content)

### Funding Model
SAM is funded through Patreon (https://www.patreon.com/fewtarius). Support covers:
- Software licenses
- Developer accounts (Apple, etc.)
- Infrastructure costs
- Development time

**Funding messaging:** Frame as partnership ("Let's create... together") not charity.


## Key Messages to Maintain

1. **"The AI That Works *With* You, Not Just *For* You"** - Core positioning
2. **"Built for macOS. Built for privacy. Built for you."** - Platform + values
3. **"Your data stays on your Mac. Always."** - Privacy guarantee
4. **"No technical skills needed"** - Accessibility promise
5. **"100% free & open source"** - Transparency + no lock-in


## Files to Never Change

- `.github/FUNDING.yml` - Patreon configuration (only update if Patreon username changes)


## Getting Help

- **Issues:** https://github.com/SyntheticAutonomicMind/SAM/issues
- **Discussions:** Check main SAM repository
- **Contact:** fewtarius@steamfork.org
- **Patreon:** https://www.patreon.com/fewtarius


## Remember

This repository is SAM's first impression. Every word should:
- Welcome new users
- Build trust through transparency
- Show practical value
- Make next steps obvious
- Reflect SAM's user-first philosophy

**You're not writing documentation - you're inviting people into a community built around better AI assistance.**
