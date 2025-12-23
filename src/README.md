# Log Analysis Benchmark: Rust vs. Python

A performance comparison tool that parses a 5GB log file (100 million lines) to count keyword occurrences. This project explores the systems-level differences between an interpreted language (Python) and a compiled language (Rust).

- Benchmark Results
  Test Environment: Local machine, 100 Million Line Log File (~5GB).

| Metric      | Rust (Release) | Python | Result                 |
| :---------- | :------------- | :----- | :--------------------- |
| Fastest Run | 17.76s         | 26.89s | Rust is ~1.5x faster   |
| Average Run | 20.71s         | 27.24s | Rust wins consistently |
| Stability   | High           | High   | Both reliable          |

> System Observation: Rust's first run was slower (31s) due to the OS loading the file into RAM (File System Cache). Subsequent runs settled at ~17.8s, whereas Python remained constant at ~27s.

- Why is Rust Faster?

1.  Compilation vs. Interpretation: Rust compiles directly to machine code (binary), eliminating the runtime translation overhead that Python incurs for every line.
2.  Zero-Cost Abstractions: Rust's `BufReader` manages memory efficiently without the overhead of Python's Garbage Collector (GC), which pauses execution to clean up unused objects.
3.  Memory Ownership: Rust manages memory at compile-time. It knows exactly when to free memory, avoiding runtime checks.

- Implementation Details

### The Challenger: Python

Approach: Uses a standard `with open(...)` context manager and lazy iteration (`for line in f`).
Key Libraries: `sys` (CLI args), `time` (benchmarking).
Pros: Extremely concise and readable code.

### The Champion: Rust

Approach: Uses `std::io::BufReader` to minimize expensive system calls by reading data in chunks (buffers) rather than byte-by-byte.
Key Libraries: `std::env` (CLI args), `std::fs::File`, `std::io::BufRead`.
Safety: Uses the `?` operator for robust error handling without crashing.

- How to Run

1. Generate Data (Warning: Creates a 5GB file)
   python generate_log.py
2. Run Python Version
   python main.py test.log ERROR
3. Run Rust Version Note: The --release flag is critical for compiler optimizations.
   cargo run --release -- test.log ERROR
