# Task Description 

1. Initialize an application for use with uv (uv init)
2. Create a virtual environment uv venv and source it.
3. Start your IDE in this environment
4. Setup your IDE to use the virtual environment you setup.
5. Create a module called <yourname>-hello in that folder.
6. Write the code that says hello to the argument passed or world, by default.
7. Publish the module in TestPyPI for Package Testing.

---

## 📚 Development Info

This package was created as part of a Python Bootcamp (Day 0 - Basics Tasks). It demonstrates:

- Python CLI app structure
- Virtual environment with `uv`
- Publishing to [TestPyPI](https://test.pypi.org)

---

## Folder Structure

```
bootcamp/
└── day0/
    └── ex-basics-1/
        ├── shreyas_hello/               # Your Python package
        │   ├── __init__.py
        │   └── main.py                  # Source Code
        ├── pyproject.toml               # Project config (name, version, deps, scripts)
        ├── README.md                    # Markdown README 

```



---

## 📦 Installation (from TestPyPI)

```bash
 uv pip install -i https://test.pypi.org/simple/ shreyas-hello
```

---

## 🚀 Usage

Once installed, run the following in your terminal:

```bash
shreyas-hello -h
```

Output:
```bash
usage: shreyas-hello [-h] [-n NAME]

Prints a friendly greeting

options:
  -h, --help       show this help message and exit
  -n, --name NAME  Who to say hello to (default: world)
```

### Example 1 

```bash
shreyas-hello
```

You’ll see:

```
Hello, world!
```

### Example 2 

You can also greet someone by name:

```bash
shreyas-hello Shreyas
```

Output:

```
Hello, Shreyas!
```

---

## 🔗 TestPyPI Package Link

[https://test.pypi.org/project/shreyas-hello](https://test.pypi.org/project/shreyas-hello)

---

