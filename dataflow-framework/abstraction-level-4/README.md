# Level 4: Stream Processing and Stateful Processors

## Task Description

In this level, you will move from simple `str -> str` functions to full stream-based processing. This opens the door to much more powerful behaviors, including:

- Returning multiple lines from one line (fan-out)
- Combining multiple lines into one output (fan-in)
- Stateful processing (e.g. counters, buffers, aggregators)
- More modular and lifecycle-aware processors

### Problem Context

The current `str -> str` processors are limited:

- They can’t drop lines easily.
- They can’t emit zero or multiple lines.
- They can’t maintain state across lines. 

To build a real-world pipeline, we need processors that operate on streams — meaning, they take an iterator of lines and yield processed output lines one by one.

You will:
- Redesign your processor interface to be `Iterator[str] -> Iterator[str]`
- Convert your simple processors using a decorator or wrapper so you can still reuse existing ones
- Build at least one processor that requires internal state (e.g., line counting)




## Project Structure
```
abstraction-level-4/
├── cli.py              # Typer CLI entrypoint
├── main.py             # Orchestration: read → process_stream → write
├── core.py             # Stream runner + decorator/wrapper
├── pipeline.py         # Static assembly of stream processors
├── processor_types.py  # Type aliases for SimpleFn and StreamProcessor
└── processors/         # Processor implementations
    ├── stateless.py    # Simple str→str functions
    ├── counter.py      # Stateful LineCounter
    ├── fan_in.py       # JoinEvery (fan-in)
    └── fan_out.py      # SplitOn (fan-out)
```

## ⚙️ Requirements

* **Python 3.7+**
* Install dependencies:

  ```bash
  uv pip install typer
  ```

## 🚀 Quick Start

1. **Prepare an input file** (`input.txt`):

    ```text
    this line will be beside second line
    i'm besides the first line
    i'm the third line my line partner is the fourth line
    i'm the fourth line the third is beside me
    i'm the fifth line i'll break-in two parts
    ```

2. **Run the CLI** from this folder:
   ```bash
   python main.py --input input.txt --output out.txt
   ```
3. **Inspect** `out.txt` or stdout:
   - You should see a mix of 
     - Fan-in, 
     - Fan-out, 
     - Line counts, and
     - Case Transformation.

---

## 📘 How It Works

* **`core.stream_processor`**: lifts `str→str` functions into stream processors.
* **Fan-out**: `processors.fan_out.SplitOn` splits lines on a delimiter, emitting multiple output lines.
* **Fan-in**: `processors.fan_in.JoinEvery` buffers N lines and emits them joined.
* **Stateful**: `processors.counter.LineCounter` prefixes each line with a running count.
* **Pipeline**: defined in `pipeline.py` as an ordered list of processors.

---

## 🔎 Usage 

With the sample input above and the default pipeline, you might see output like:

```text
LINE 1: THIS_LINE_WILL_BE_BESIDE_SECOND_LINE || I'M_BESIDES_THE_FIRST_LINE
LINE 2: I'M_THE_THIRD_LINE_MY_LINE_PARTNER_IS_THE_FOURTH_LINE || I'M_THE_FOURTH_LINE_THE_THIRD_IS_BESIDE_ME
LINE 3: I'M_THE_FIFTH_LINE_I'LL_BREAK
IN_TWO_PARTS
```

(This output order may vary depending on processor sequence.)

[![asciicast](https://asciinema.org/a/qFJZfwbrWkeP6Tzy9QsMEpOab.svg)](https://asciinema.org/a/qFJZfwbrWkeP6Tzy9QsMEpOab)

---

## 🔎 Challenge Questions

Q] How can you reuse existing str -> str processors in a streaming system?
- **Reusing `str→str` processors**: Wrap them with `stream_processor` (or a decorator) to lift them into the `Iterator[str]→Iterator[str]` interface.

Q] How should a processor be initialized if it needs a parameter like `min_length=5`?
- **Parameterized processors**: Use class-based processors initialized via constructor arguments (e.g., `MinLengthFilter(min_length=5)`) so configuration is separated from logic.

Q] If you split one line into many, how will downstream processors handle the multiple outputs?
- **Handling fan‑out outputs**: Downstream processors simply operate on the flattened stream; multiple yielded lines are processed sequentially without special handling.

Q] What’s the best way to test a stateful processor?
- **Testing stateful processors**: Feed a known iterator of lines and assert the sequence of outputs and internal state after execution, using small, isolated test cases.

Q] Can you identify which processors are stateless vs. stateful?
- **Stateless vs. stateful**:
  - Stateless: `to_uppercase`, `to_snakecase` (wrapped via stream_processor).
  - Stateful: `LineCounter`, `JoinEvery` (buffers state), `SplitOn` (manages local split state).

## ✅ Checklist

* [x] All processors implement `Iterator[str] → Iterator[str]`.
* [x] `stream_processor` reuses old `str→str` functions.
* [x] Fan-out, fan-in, and stateful processors included.
* [x] Configuration passed via constructor parameters in `pipeline.py`.
* [x] CLI remains a thin wrapper over `main.run()`.
* [x] Processors are testable in isolation.

---