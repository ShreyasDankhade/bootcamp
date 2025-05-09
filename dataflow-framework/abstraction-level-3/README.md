# Level 3: Dynamic Config-Driven Pipeline

## Task Description

- Create a pipeline.yaml file that defines the processing steps using import paths:

- pipeline:
    - type: processors.snake.to_snakecase
    - type: processors.upper.to_uppercase
- Write a function that:

  - Parses the config file
  - Loads each function dynamically from its import path
  - Returns a list of `ProcessorFn` functions

- Replace your static pipeline from Level 2 with this dynamic list. 
- Update your CLI to accept `--config pipeline.yaml` instead of `--mode`.


## Project Structure
```
abstraction-level-3/
├── main.py
├── cli.py
├── core.py
├── pipeline.py         # now loads pipeline from YAML
├── types.py
├── processors/
│   ├── upper.py
│   └── snake.py
└── pipeline.yaml
```
## 📦 Dependencies

* Python 3.7+
* `typer` — for CLI interface
* `PyYAML` — for parsing YAML configs

Install with:

```bash
pip install typer pyyaml
```

## 🚀 Quick Start


1. **Configure** `pipeline.yaml` with dotted import paths:

   ```yaml
   pipeline:
     - type: processors.snake.to_snakecase
     - type: processors.upper.to_uppercase
   ```

2. **Run the CLI** from this folder:

   ```bash
   # Default: print to stdout
   python main.py --input input.txt --config pipeline.yaml

   # Write to a file
   python main.py --input input.txt --config pipeline.yaml --output out.txt
   ```
   
[![asciicast](https://asciinema.org/a/NIj7wvrNeHCxqzPpJdFn7yAJc.svg)](https://asciinema.org/a/NIj7wvrNeHCxqzPpJdFn7yAJc)



## ✅ Checklist

* [x] CLI updated to accept `--config` instead of `--mode`.
* [x] Program dynamically imports and composes processors from YAML.
* [x] All processors conform to `str -> str` signature.
* [x] Import and type errors are handled with clear messages.
* [x] `pipeline.yaml` specifies functions via full dotted paths.

---
