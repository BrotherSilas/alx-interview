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
        # Strip and split the line to ensure consistent format
        line = line.strip().split()
        if len(line) < 7:
            continue  # Skip lines that don't match the expected format

        # Extract file size and status code
        try:
            file_size = int(line[-1])
            status_code = int(line[-2])
            total_size += file_size  # Add to total file size
            if status_code in status_codes:
                # Increment count for the status code
                status_codes[status_code] += 1
        except ValueError:
            continue  # Skip lines with invalid integers

        # Increment line count and print stats every 10 lines
        line_count += 1
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    pass
finally:
    # Print final stats on exit or interrupt
    print_stats()
