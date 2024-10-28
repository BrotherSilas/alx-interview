#!/usr/bin/python3
import sys

# Initialize total file size and dictionary for status codes
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    """Print the current metrics."""
    print("File size:", total_size)
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 7:
            continue

        # Extract file size and status code
        try:
            file_size = int(parts[-1])
            status_code = int(parts[-2])
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1
        except ValueError:
            continue

        # Increment line count and check if we need to print
        line_count += 1
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    pass
finally:
    # Print final stats on program exit or interrupt
    print_stats()
