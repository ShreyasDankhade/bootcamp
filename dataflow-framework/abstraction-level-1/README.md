# Level 1: Parameterized CLI Tool

## Task Description

- Use typer to define a command-line interface

- Accept:

  - --input: input file path (required)
  - --output: output file path (optional)
   - --mode: processing mode (optional, defaults via .env)
- Load default values (in this case mode) from a .env file using python-dotenv
- Implement different processing behaviors based on the mode

## 📝 Overview

* **Goal**: Read text from a file, transform each line according to a selected *mode*, and write results to stdout or a file.
* **Files**:

  * `process.py` — The Level 1 script using Typer and dotenv.
  * `.env` — (Not included) Example file for setting default `MODE`.
  * `input.txt` - Input text file.
  * `README.md` — This document.

## ⚙️ Requirements

* Python 3.x
* Dependencies (install via `uv pip install typer python-dotenv`):

  * **typer** — for CLI definitions
  * **python-dotenv** — for loading defaults from `.env`

## 🔧 CLI Interface

`process.py` exposes a single command with options:

| Option          | Description                                        | Default                              |
| --------------- | -------------------------------------------------- | ------------------------------------ |
| `--input PATH`  | Path to the input file (required)                  | N/A                                  |
| `--output PATH` | Path to write output; if omitted, prints to stdout | stdout                               |
| `--mode [mode]` | Transformation mode: `uppercase` or `snakecase`    | from `MODE` in `.env` or `uppercase` |

### Example Usage

```bash
# Default (MODE from .env or uppercase), prints on console:
python process.py --input input.txt

# Prints in snakecase on console
python process.py --input input.txt --mode snakecase

# Prints in uppercase on console
python process.py --input input.txt --mode uppercase

# Write to a file:
python process.py --input input.txt --mode snakecase --output output.txt

# Write to a file:
python process.py --input input.txt --mode uppercase --output output.txt
```
[![asciicast](https://asciinema.org/a/R1XUiL4zyhjEoeBxmDlbMtjpH.svg)](https://asciinema.org/a/R1XUiL4zyhjEoeBxmDlbMtjpH)

## 🛠️ Checklist

* [x] **Input flexibility**: Can process any file via `--input`.
* [x] **Default mode**: Reads `MODE` from `.env`, falls back to `uppercase`.
* [x] **Alternate mode**: `--mode snakecase` applies underscore and lowercase.
* [x] **Output**: Prints to stdout or writes to file via `--output`.
* [x] **Typer CLI**: Uses Typer for clean option parsing and help messages.
* [x] **Functional decomposition**: Logic split into `read_lines()`, `transform_line()`, and `write_output()`.

---

*Level 1 completed: monolithic but configurable tool with CLI and modes. Level 2 will modularize and abstract further.*
