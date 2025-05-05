# Calculator CLI

----
## Task Description 
1. Install `typer`
2. Use `typer` to write a command line application in the module
3. Now, make the cli app as a part of the `pyproject.toml` so that it gets installed when we install the package.
4. Record and show the demo where you install the package and run the command and show it.

---
## 📚 Development Info

This package was created as part of a Python Bootcamp (Day 0 - Basics Tasks). It demonstrates:

- Python CLI app structure
- Virtual environment with `uv`
- Used [Typer](https://pypi.org/project/typer/) for command line operations. 
- Used [Rich](https://pypi.org/project/rich/) package for Rich-colored terminal output
- Published to TestPyPI

---

## Folder Structure

```
bootcamp/
└── day0/
    └── ex-basics-1/
    └── ex-basics-2/
    └── ex-basics-3/
        └── src/                         # Your Python package
            └──ex_basics_3
               └── __init__.py
               └── main.py               # Main Code
        ├── pyproject.toml               # Project config (name, version, deps, scripts)
        ├── README.md                    # Markdown README 

```

---

## ⚙️ Features

* **`add`**: Add two numbers
* **`sub`**: Subtract one number from another
* **`mul`**: Multiply two numbers
* **`div`**: Divide two numbers (with zero-division check)

---

## 📦 Installation (from TestPyPI)

```bash
uv pip install typer rich
```

```bash
uv pip install -i https://test.pypi.org/simple/ ex-basics-3
```
---

## 🚀 Usage

Once installed, the `calc` command is available:

```bash
# Show help and available commands
calc-cli --help

# Perform operations:
calc-cli add 2 3        # ➡️ 2 + 3 = 5
calc-cli sub 10 4       # ➡️ 10 - 4 = 6
calc-cli mul 6 7        # ➡️ 6 * 7 = 42
calc-cli div 9 3        # ➡️ 9 / 3 = 3
calc-cli div 5 0        # Error: Division by zero
```

*All results are printed with Rich styling.*

---

## Usage Recording

<a href="https://asciinema.org/a/2IHEwHKrpGhkoQ8n5r4G2DdSE" target="_blank"><img src="https://asciinema.org/a/2IHEwHKrpGhkoQ8n5r4G2DdSE.svg" /></a>

## 🔗 TestPyPI Package Link

https://test.pypi.org/project/ex-basics-3/

---
