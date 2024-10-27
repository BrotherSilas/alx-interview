#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics"""

import sys
import re
from typing import Dict, Match


def print_statistics(total_size: int, status_codes: Dict[int, int]) -> None:
    """Print the accumulated statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def parse_line(line: str) -> Match:
    """Parse a log line and return the match object if valid."""
    pattern = (
        r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - '
        r'\[(.*?)\] '
        r'"GET /projects/260 HTTP/1.1" '
        r'(\d{3}) (\d+)$'
    )
    return re.match(pattern, line)


def main():
    """Main function to process the log file."""
    total_size = 0
    line_count = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }

    try:
        for line in sys.stdin:
            line = line.strip()
            match = parse_line(line)

            if match:
                status_code = int(match.group(3))
                file_size = int(match.group(4))

                if status_code in status_codes:
                    status_codes[status_code] += 1
                total_size += file_size

                line_count += 1
                if line_count % 10 == 0:
                    print_statistics(total_size, status_codes)

    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)
        raise


if __name__ == "__main__":
    main()
