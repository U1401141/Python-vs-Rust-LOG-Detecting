import random

NUM_LINES = 100_000_000
filename = "test.log"

messages = [
    "INFO: User logged in",
    "INFO: Page rendered successfully",
    "WARN: Response time slow",
    "ERROR: Database connection failed",
    "ERROR: NullPointerException",
]

print(f"Generating {NUM_LINES} lines...")

with open(filename, "w", encoding="utf-8") as f:
    for i in range(NUM_LINES):
        msg = random.choice(messages)
        line = f"20XX-XX-XX XX:XX:XX {msg}\n"
        f.write(line)

print("Done!")