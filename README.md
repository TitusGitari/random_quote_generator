cat > README.md <<'EOF'
# Random Quote Generator (CLI + HTML)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](#license)
[![Last Commit](https://img.shields.io/github/last-commit/TitusGitari/random_quote_generator)](https://github.com/TitusGitari/random_quote_generator/commits/main)
[![Issues](https://img.shields.io/github/issues/TitusGitari/random_quote_generator)](https://github.com/TitusGitari/random_quote_generator/issues)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/TitusGitari/random_quote_generator/pulls)

A tiny, beginner‑friendly Python project that prints a **random quote** to the terminal and can **generate a minimal HTML page** showing the same quote.

---

## Features
- 🎲 Random quote from `quotes.json`
- 🖥️ CLI output: `python3 quotes.py`
- 🌐 HTML export: `python3 quotes.py --html` → creates `index.html`
- 🧩 Simple, readable code (great for learning)

---

## Quick Start
```bash
python3 quotes.py          # prints a quote in the terminal
python3 quotes.py --html   # writes index.html (open in your browser)
open index.html            # macOS quick open
