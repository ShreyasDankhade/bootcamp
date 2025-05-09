import sys

# Level 0: Basic script, no functions, sequential code
for line in sys.stdin:
    # Strip leading/trailing whitespace and convert to uppercase
    processed = line.strip().upper()
    # Output the processed line
    print(processed)
