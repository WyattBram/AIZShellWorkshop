#!/usr/bin/env python3
"""ShellHacks support bot. Usage: python ask.py "<question>" """
import subprocess
import sys


def ask(question: str) -> str:
    result = subprocess.run(
        ["claude", "-p", question],
        capture_output=True,
        text=True,
        cwd=".",
    )
    return result.stdout.strip() or result.stderr.strip()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python ask.py "<question>"')
        sys.exit(1)
    print(ask(sys.argv[1]))
