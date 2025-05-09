# Level 5: DAG Routing and Conditional Flows

## Task Description 

In this level, you will build a general-purpose DAG-based processing engine where each line can take a different path through the system based on its content or tags. 

This is a major abstraction step — you’re no longer just transforming lines, you're building a flexible routing system.

### 📋 Motivating Example: Log Routing

Imagine you're building a log processing tool.

Each line might be:
- An error that needs to be logged separately
- A warning to be counted
- A regular message to just pass through

#### Different kinds of lines need different processors.

### Desired Flow
1. All lines go through a trim processor.
2. Each line is tagged by tag_error or tag_warn (adds routing info).
3. A generic splitter sends lines to different branches:
   - **`errors`** → _count_ and _archive_ 
   - **`warnings`** → _tally_
   - **`general`** → _format_ and _print_
   
Now you need a system where:
1. Processors can tag their output
2. The engine routes based on tags
3. You define all routing behavior in a config file

### 🧠 What You’re Building
A general DAG-based processing engine where:
- Each processor is a **node**
- Processors yield **tagged lines** (e.g., (`"errors", line`))
- The engine uses **routing rules** to send lines to the right downstream node(s)
- You can define **multiple paths** in one config



---
## 📂 Structure
```
abstraction-level-5/
├── cli.py              # CLI: parses args, calls run()
├── main.py             # read_raw → run_engine → write_grouped
├── engine.py           # load_pipeline_config, run_engine, RoutingError
├── processor_types.py  # TaggedLine = (route, text), StreamProcessor type
├── pipeline.yaml       # Defines nodes, processors, and routing graph
└── processors/         # Individual processor modules
    ├── trimming.py     # trim: strip & normalize whitespace
    ├── tagging.py      # tag_error_warn: assign error/warning/default tag
    ├── archive_error.py# archive_error: pass-through sink for errors
    ├── tally_warning.py# WarningTally: count & list warnings
    ├── error_tally.py  # ErrorTally: count & list errors
    └── format_general.py # format_general: prefix INFO messages
```

---

## ⚙️ Installation

```bash
uv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
uv pip install -r requirement.txt
```

---

## 🔧 Configuration (`pipeline.yaml`)
- In `pipeline.yaml`, list each processing step (node) by name, point to its processor function (e.g., `processors.trimming.trim`), and map output tags to the next node. 


- Use `end` to mark terminal stages. All routing behavior lives here—no code changes needed for new branches.


---

## 🚦 Flow Overview

```plaintext
input.txt
  ↓ read_raw (tags='default')
┌─> trim (normalize whitespace)
│    ↓ yields 'default', clean_line
└─> tag_error_warn (tag by content)
       ├─ 'error' ─> archive_error
       │              ↓ yields ('error', line)
       │           ErrorTally ──> yields ('error', summary)
       │              ↓ terminate
       ├─ 'warning' ─> WarningTally ──> yields ('warning', summary)
       │              ↓ terminate
       └─ 'default' ─> format_general ──> yields ('default', '[INFO] '+line)
                      ↓ terminate
  ↓ write_grouped (collect & print INFO, warnings, errors)
```

---

## 🚀 Usage

1. To know the usage, use:
```bash
python main.py --help
```


2. Place your logs in `input.txt`, then:
```bash
python main.py --input input.txt --config pipeline.yaml --output output.txt
```
- Omit `--output` to print to stdout.


---

## 🧪 Example

**`input.txt`**
```
                 2025-05-09 10:00:00 INFO Application started
2025-05-09 10:01:00 WARN Disk space low
2025-05-09 10:02:00                          ERROR Failed to connect to DB
2025-05-09 10:03:00 INFO                  Received request
2025-05-09 10:04:00 WARN High                                  memory usage
                            2025-05-09 10:05:00 ERROR Timeout                                           occurred
```

**`out.txt`**
```
[INFO] 2025-05-09 10:00:00 INFO Application started
[INFO] 2025-05-09 10:03:00 INFO Received request

Warnings (2):
 • 2025-05-09 10:01:00 WARN Disk space low
 • 2025-05-09 10:04:00 WARN High memory usage

Errors (2):
 • 2025-05-09 10:02:00 ERROR Failed to connect to DB
 • 2025-05-09 10:05:00 ERROR Timeout occurred
```

[![asciicast](https://asciinema.org/a/Yj6PvIOZcGCKK6xqQEZiPrOW6.svg)](https://asciinema.org/a/Yj6PvIOZcGCKK6xqQEZiPrOW6)


---

## 🔑 Highlights

- **Whitespace normalization**: `trim` now collapses all multi-space runs.
- **Dynamic routing**: no code changes needed—adjust `pipeline.yaml` to rewire the DAG.
- **Stateful processors**: `WarningTally`/`ErrorTally` aggregate messages, emitting grouped summaries.
- **Single-pass engine**: `run_engine` manages a queue, terminates on `end`, and yields tagged lines.

---

## ✅ Checklist

- [x] Whitespace is trimmed and normalized.
- [x] Lines tagged correctly by content.
- [x] Errors archive and then count messages.
- [x] Warnings count messages.
- [x] INFO lines are formatted and grouped.
- [x] Output groups: INFO → Warnings → Errors.
- [x] Configuration drives all routing.

---

