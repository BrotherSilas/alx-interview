# Log Parsing Project

## Overview
This project implements a log parsing system that processes web server logs from standard input and computes metrics in real-time. The script analyzes HTTP access logs, tracking file sizes and response status codes, providing periodic statistical summaries.

## Features
- Real-time log processing from stdin
- Tracks total file size of HTTP requests
- Monitors frequency of HTTP status codes
- Prints statistics every 10 lines
- Handles keyboard interruption (CTRL + C)
- Validates log entry format
- Sorts and displays status codes in ascending order

## Requirements
- Ubuntu 20.04 LTS
- Python 3.4.3
- Executable files
- PEP 8 style compliance

## Installation
Clone the repository:
```bash
git clone [repository-url]
cd 0x03-log_parsing
```

Make the script executable:
```bash
chmod +x 0-stats.py
```

## Usage
The script reads from standard input (stdin) and expects log entries in the following format:
```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

### Running the Script
1. Direct execution with input file:
```bash
cat logfile.txt | ./0-stats.py
```

2. Using the generator script (for testing):
```bash
./0-generator.py | ./0-stats.py
```

### Example Output
```
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
```

## Input Format
Each log entry must follow this specific format:
- IP Address: e.g., `123.12.12.12`
- Date: enclosed in square brackets
- Request: `"GET /projects/260 HTTP/1.1"`
- Status Code: Valid codes are 200, 301, 400, 401, 403, 404, 405, 500
- File Size: integer value

Example valid log entry:
```
128.230.61.246 - [2024-01-01] "GET /projects/260 HTTP/1.1" 200 1234
```

## Status Code Meanings
- 200: OK - Successful request
- 301: Moved Permanently - Resource relocated
- 400: Bad Request - Client error
- 401: Unauthorized - Authentication required
- 403: Forbidden - Server refuses to fulfill request
- 404: Not Found - Resource not found
- 405: Method Not Allowed - Invalid HTTP method
- 500: Internal Server Error - Generic server error

## Statistics Output
The script outputs statistics in two scenarios:
1. After every 10 valid log entries
2. When interrupted by CTRL + C (keyboard interrupt)

The statistics include:
- Total file size
- Count of each status code encountered

## Error Handling
- Invalid format lines are skipped
- Graceful handling of keyboard interrupts
- Status codes not in the valid list are ignored

## Project Structure
```
0x03-log_parsing/
│
├── 0-stats.py          # Main script
├── 0-generator.py      # Test data generator
└── README.md          # Documentation
```

## Implementation Details
The script uses:
- Regular expressions for log parsing
- Dictionary data structures for counting
- Signal handling for interrupts
- File I/O for stdin reading
- Exception handling for robustness

## Real-world Applications
This type of log parsing is commonly used in:
- Web server monitoring
- Traffic analysis
- Security auditing
- Performance monitoring
- Resource usage tracking
- Error detection and debugging

## Contributing
Contributions are welcome! Please ensure:
1. Code follows PEP 8 style guide
2. All files end with a new line
3. Scripts are executable
4. Comprehensive testing is performed

## License
[Specify your license here]

## Author
[Your name or organization]
