# Level 0: Basic Text Processing Script

## Task Description

Write a Python script that:

1. Reads the `stdin` line by line
2. Strips leading and trailing whitespace from each line
3. Converts the result to uppercase
4. Prints the processed lines to the stdout

5. Put everything in a single file named `process.py`.


## 📝 Overview

* **Goal**: Read text from standard input, strip whitespace, convert to uppercase, and print to standard output.
* **File**: `process.py`
* **Approach**: Sequential, top-to-bottom code without any functions or imports beyond the standard library.

## 📦 Files

* `process.py` — The Level 0 script.
* `input.txt` - input file.
* `README.md` — This document.

## ⚙️ Requirements

* Python 3.x (no external dependencies)
* Unix-like shell (or Windows PowerShell/CMD) for redirection

## 🚀 Usage

```bash
python process.py < input.txt
```

[![asciicast](https://asciinema.org/a/wgKmBTUlEkvYjPeCuuhJaMkGw.svg)](https://asciinema.org/a/wgKmBTUlEkvYjPeCuuhJaMkGw)

### Expected Behavior

* Lines are read one at a time from stdin.
* Leading and trailing whitespace is removed.
* The remaining text is converted to uppercase.
* Each processed line is printed to stdout.

## ✅ Checklist

* [x] Produces expected output:
  ```bash
  python process.py < input.txt
  
  // Output
  IT SHOULD PRINT IN UPPERCASE
  ```
* [x] Runs without errors when invoked from the command line.
* [x] Contains **no** functions or abstractions—just a linear script.
---