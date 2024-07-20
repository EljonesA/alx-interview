#!/usr/bin/python3
""" Log parsing algorithm """
import sys
import signal

# Dictionary to hold the count of each status code
status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
}

total_file_size = 0
line_count = 0


def print_stats():
    """Print the current statistics."""
    global total_file_size
    global status_codes

    print(f"File size: {total_file_size}")

    # Print status codes in ascending order
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

    print()


def signal_handler(sig, frame):
    """Handle keyboard interrupts."""
    print_stats()
    sys.exit(0)


def process_line(line):
    """Process each line to update metrics."""
    global total_file_size
    global status_codes
    global line_count

    try:
        parts = line.split()
        if len(parts) != 7:
            return

        file_size = int(parts[-1])
        status_code = int(parts[5].strip('"'))

        if status_code in status_codes:
            status_codes[status_code] += 1
            total_file_size += file_size
            line_count += 1

            if line_count % 10 == 0:
                print_stats()
    except ValueError:
        return


if __name__ == "__main__":
    # Setup signal handler for keyboard interrupt
    signal.signal(signal.SIGINT, signal_handler)

    # Read from stdin line by line
    for line in sys.stdin:
        process_line(line)
