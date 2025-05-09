# Level 2: Modular Text Processing Tool

## Task Description 

- Split your code into the following modules:

```
abstraction-level-2/
├── main.py         # Reads input, writes output
├── cli.py          # Handles CLI via typer
├── core.py         # Applies a list of processors to each line
├── pipeline.py     # Assembles the processor list based on mode
└── types.py        # Defines ProcessorFn types
```
- Define a common function signature for processor
  - Implement these processors in core.py:
  - to_uppercase(line: str) -> str
  - to_snakecase(line: str) -> str
- Create a list of processors in pipeline.py. Pay attention to the mode. This is a static pipeline.
- Apply all processors in sequence to each line of input.
- CLI should stay the same as Level 1, with --input, --output, and --mode.

## ⚙️ Requirements

* **Python 3.7+**
* Install dependencies:

  ```bash
  pip install typer python-dotenv
  ```

## 🚀 Usage

Run the CLI from the `abstraction-level-2/` directory:

```bash
# Default (MODE from .env or uppercase), prints on console:
python cli.py --input input.txt

# Prints in snakecase on console
python cli.py --input input.txt --mode snakecase

# Prints in uppercase on console
python cli.py --input input.txt --mode uppercase

# Write to a file:
python cli.py --input input.txt --mode snakecase --output output.txt

# Write to a file:
python cli.py --input input.txt --mode uppercase --output output.txt
```

[![asciicast](https://asciinema.org/a/V8rqAz7iCtTdC93OY8tZxSw7D.svg)](https://asciinema.org/a/V8rqAz7iCtTdC93OY8tZxSw7D)


## ✅ Checklist

* [x] Five modules (`cli.py`, `main.py`, `core.py`, `pipeline.py`, `types.py`) exist.
* [x] `ProcessorFn` alias used for processor functions.
* [x] New processors can be added to `core.py` and `pipeline.py` without touching I/O logic.
* [x] CLI behavior matches Level 1.
* [x] No circular imports; types centralized in `types.py`.

---