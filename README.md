# SWYNEX Git Workflow and Project Baseline

Task 1 of my internship with **SWYNEX Technologies**. This repository demonstrates a clean Git workflow and a small, well-structured Python project.

## Features

- Command-line calculator (add, subtract, multiply, divide)
- Input validation and divide-by-zero handling
- Unit tests using Python's built-in `unittest`
- Documented branching strategy (see [BRANCHING.md](BRANCHING.md))

## Project Structure

```
SWYNEX-Git-Workflow-and-Project-Baseline/
├── src/
│   ├── __init__.py
│   └── calculator.py      # core logic
├── tests/
│   ├── __init__.py
│   └── test_calculator.py # unit tests
├── main.py                # CLI entry point
├── BRANCHING.md           # Git branching notes
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Git

### Installation

```bash
git clone https://github.com/<your-username>/SWYNEX-Git-Workflow-and-Project-Baseline.git
cd SWYNEX-Git-Workflow-and-Project-Baseline
```

### Run the app

```bash
python main.py
```

### Run the tests

```bash
python -m unittest discover tests
```

## Git Workflow

This project follows a simple branching model (`main` / `develop` / `feature/*`). Full details are in [BRANCHING.md](BRANCHING.md).

## What I Learned

- Initializing a repo and making meaningful commits
- Using `.gitignore` to keep unwanted files out of version control
- Creating and merging feature branches
- Writing a clear README and branching documentation

## Author

abhinav202404155 — SWYNEX Technologies Intern
