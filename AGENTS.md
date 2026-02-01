# AGENTS.md

This file provides project context for AI coding assistants (CLIO, Cursor, Aider, GitHub Copilot, etc.).

## Project Overview

**SAM-profile** is the organizational profile repository for **Synthetic Autonomic Mind** - a collection of privacy-first, open-source AI tools.

- **Purpose:** Main profile/README for the SyntheticAutonomicMind organization on GitHub
- **Content Type:** Documentation and organization marketing
- **Audience:** Users discovering SAM, CLIO, and ALICE projects
- **Repository:** https://github.com/SyntheticAutonomicMind/SAM-profile

## What This Project Contains

### Primary Content
- **`profile/README.md`** - Main organizational profile describing SAM, CLIO, and ALICE
- **`.github/`** - GitHub organization files (FUNDING.yml)
- **`.clio/`** - CLIO AI assistant configuration
- **`.gitignore`** - Standard ignores for CLIO projects

### Related Projects (for reference)
- **SAM** (macOS AI Assistant) - https://github.com/SyntheticAutonomicMind/SAM
- **CLIO** (Terminal AI Assistant) - https://github.com/SyntheticAutonomicMind/CLIO
- **ALICE** (Image Generation Backend) - https://github.com/SyntheticAutonomicMind/ALICE
- **SAM-website** (Documentation site) - https://www.syntheticautonomicmind.org

## Project Philosophy

All Synthetic Autonomic Mind projects are built on these principles:

- **Respect your privacy** - Your data stays where you control it
- **Be transparent** - You understand what's happening and why
- **Work your way** - Adapt to your workflow, not the reverse
- **Empower, not replace** - AI should help you accomplish more, not take over
- **Be accessible** - Powerful tools should work for everyone, not just developers

**100% free & open source** under:
- Code: GPL v3.0
- Documentation: CC BY-NC 4.0

## Code Style & Standards

### Markdown Standards

**File Naming:**
- Use lowercase with hyphens: `feature-description.md`
- Main profile file: `profile/README.md`

**Formatting:**
- Use clear header hierarchy (H1 for title, H2 for sections)
- Link text should be descriptive, not "here" or "click here"
- Use bold for **important terms** and *italic* for emphasis
- Code blocks for commands, config, and examples
- Bullet lists for features, links for repos

**Content Guidelines:**
- Clear, direct language - no jargon without explanation
- Organize by user audience (beginners first)
- Provide links to detailed documentation
- Keep line length reasonable for readability

### Link Standards

**Repository Links:**
- Format: `https://github.com/SyntheticAutonomicMind/PROJECT`
- Always use full URLs, not shortened links
- Test links before committing

**Documentation Links:**
- Main website: https://www.syntheticautonomicmind.org
- GitHub READMEs: Link to specific sections when possible
- External resources: Provide full URLs with context

### GitHub Markdown Features

- Use GitHub's built-in features (tables, lists, links)
- Test rendering on GitHub (not just locally)
- Keep files readable in raw GitHub view

## Documentation Principles

### Accuracy First
- Feature descriptions must match actual product capabilities
- Test all claims against current project state
- Update documentation when features change
- Reference the actual implementation when in doubt

### User-Focused Organization
- Lead with benefits, not technical details
- Organize by what users want to accomplish
- Use real-world examples
- Provide clear next steps (download, docs, issues)

### Completeness
- Include all major features
- Document tradeoffs and limitations
- Link to related documentation
- Provide multiple paths to more information

## Common Workflows

### Updating the Profile

When making changes to `profile/README.md`:

1. **Check All Links**
   - Verify repository links are current
   - Test GitHub download links work
   - Confirm documentation site is accessible

2. **Review for Accuracy**
   - Features should match current implementation
   - Version info should be current
   - Screenshots should be from current release

3. **Test Rendering**
   - View in GitHub's markdown renderer
   - Check on mobile devices
   - Verify all formatting is correct

4. **Commit Message Format**
   ```
   docs(profile): [action] [component] for [reason]
   
   Examples:
   - docs(profile): update SAM features for new image generation
   - docs(profile): add SAM-Web documentation link
   - docs(profile): clarify CLIO positioning for terminal users
   ```

### Adding New Projects

If a new Synthetic Autonomic Mind project launches:

1. Create new section in format matching SAM, CLIO, ALICE
2. Include: Repository link, documentation link, description, features, target audience
3. Add to "All Repositories" list at bottom
4. Link from Website if appropriate
5. Update Quick Links if relevant

### Sync with Related Projects

When SAM, CLIO, or ALICE have major updates:

1. Review their current README files
2. Verify features listed in profile match their capabilities
3. Update download/documentation links if changed
4. Check if positioning or audience description needs adjustment

## Testing

### Pre-Commit Checklist

Before committing changes to `profile/README.md`:

- [ ] All links are valid and work when clicked
- [ ] Repository URLs point to correct projects
- [ ] Feature descriptions match actual products
- [ ] Screenshots are from current versions
- [ ] Markdown renders correctly on GitHub
- [ ] No formatting issues (proper indentation, link syntax)
- [ ] Spelling and grammar are correct
- [ ] Tone is consistent with existing content
- [ ] Commit message follows format guidelines

### Link Validation

Key links to verify:
- Repository links (github.com/SyntheticAutonomicMind/...)
- Download links (GitHub releases)
- Website (syntheticautonomicmind.org)
- Support links (Patreon, Reddit, GitHub Issues)
- Documentation links

## Build & Deployment

This is a documentation-only repository. **No build process needed.**

- Repository is static content
- GitHub renders markdown automatically
- Changes are live immediately when committed to main branch
- No tests, no build steps, no deployment pipeline required

## Contributing Standards

### For Contributors

When updating `profile/README.md`:

1. Read and understand the project philosophy
2. Check existing documentation standards
3. Review recent commits to see current style
4. Make focused changes (one feature/section at a time)
5. Test all links before committing
6. Use clear, descriptive commit messages
7. Be willing to revise based on feedback

### For Code Reviewers

When reviewing changes:

1. Verify all links are valid
2. Check features match actual product capabilities
3. Ensure tone is consistent with existing content
4. Confirm formatting and markdown syntax are correct
5. Check for spelling and grammar
6. Validate positioning and audience alignment

## Repository Structure

```
SAM-profile/
├── profile/                    # Main content
│   ├── README.md              # Organizational profile
│   └── .images/               # Images for README
├── .github/                    # GitHub organization files
│   └── FUNDING.yml            # Donation links
├── .clio/                      # CLIO AI assistant config
│   ├── instructions.md        # CLIO methodology
│   └── ...                    # Session logs, memory
├── .gitignore                 # Standard CLIO ignores
├── AGENTS.md                  # This file
└── LICENSE                    # Project licenses
```

## Key Files & Decisions

- **`profile/README.md`** - Main deliverable, primary focus for updates
- **`AGENTS.md`** - This context file (read-only reference)
- **`.clio/instructions.md`** - CLIO-specific methodology (use for CLIO sessions)

## Quick Reference Commands

**Check git status:**
```bash
git status
```

**View recent changes:**
```bash
git log --oneline -5
```

**Review a specific change:**
```bash
git diff HEAD~1
```

**Commit changes:**
```bash
git add profile/README.md AGENTS.md
git commit -m "docs(profile): [your message]"
git push
```

## Support & Resources

- **Main Website:** https://www.syntheticautonomicmind.org
- **GitHub Issues:** https://github.com/SyntheticAutonomicMind/SAM/issues
- **Community:** https://reddit.com/r/PopularAI
- **Support:** https://patreon.com/fewtarius

## License

- **Code:** GPL v3.0
- **Documentation:** CC BY-NC 4.0

This document and all SAM-profile content are subject to these licenses.
