# Task Description 

Enhance the application with the following:

1. Install the following modules in your environment from pypi: `rich`
2. Enhance your code to use `rich` to print rich message.
---

## 📚 Development Info

This package was created as part of a Python Bootcamp (Day 0 - Basics Tasks). It demonstrates:

- Python CLI app structure
- Virtual environment with `uv`
- Also, this uses `rich` package for Rich-colored terminal output
- Published to [TestPyPI](https://test.pypi.org)

---

## Folder Structure

```
bootcamp/
└── day0/
    └── ex-basics-1/
    └── ex-basics-2/
        └── src/                         # Your Python package
            └──ex_basics_2
               └── __init__.py
               └── main.py               # Main Code
        ├── pyproject.toml               # Project config (name, version, deps, scripts)
        ├── README.md                    # Markdown README 

```

---

## 📦 Installation (from TestPyPI)

```bash
uv pip install rich
```

```bash
uv pip install -i https://test.pypi.org/simple/ ex-basics-2
```

---

## 🚀 Usage

Once installed, run the following in your terminal:

```bash
ex-basics-2 -h
```

Output:
```bash
usage: ex-basics-2 [-h] [-n NAME]

Prints a friendly, rich-formatted greeting

options:
  -h, --help       show this help message and exit
  -n, --name NAME  Who to say hello to (default: world)
```

### Example 1 


```bash
ex-basics-2
```


Output (_In magenta & Green color_):
```
Hello, world!
```


### Example 2 


You can also greet someone by name:


```bash
ex-basics-2 -n Shreyas
```


Output (_In magenta & Green color_):

```
Hello, Shreyas
```

---

## 🔗 TestPyPI Package Link

https://test.pypi.org/project/ex-basics-2/

---

