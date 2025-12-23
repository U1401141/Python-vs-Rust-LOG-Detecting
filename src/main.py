import sys
import time

def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <filename> <keyword>")
        return

    filename = sys.argv[1]
    keyword = sys.argv[2]

    start_time = time.time()

    total = 0
    try:
        # 'r' = read mode, 'utf-8' = standard text format
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                if keyword in line:
                    total += 1
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return

    end_time = time.time()
    total_second = end_time - start_time

    print(f"The amount of '{keyword}': {total}")
    print(f"{total_second:.6f} seconds to find all items")

if __name__ == "__main__":
    main()