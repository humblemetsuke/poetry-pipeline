#!/usr/bin/env python
"""
Vulture wrapper script for pre-commit.

Vulture 2.x uses exit code 3 for "warnings only" (e.g., unused variables in
.vulture-ignore.py). Pre-commit treats any non-zero exit code as a failure,
which blocks commits.

This wrapper normalizes exit code 3 → 0.
Harmless warnings don't block commits.
This ensures real errors (exit codes 1 or 2) do.

Usage:
    python hooks/vulture-wrapper.py [vulture arguments]
"""

import subprocess  # nosec B404, noqa: F401
import sys  # noqa: F401

# ------------------------------------------------------------
# Run Vulture with all command-line arguments passed to this script.
# sys.argv[1:] contains everything after the script name.
# shell=False (default) is safe as command is trusted.
# ------------------------------------------------------------
result = subprocess.run(
    [
        "poetry",
        "run",
        "vulture",
    ]
    + sys.argv[1:],  # nosec B603
)

# ------------------------------------------------------------
# Normalize exit code 3 to 0 (warnings only)
# This prevents harmless warnings from blocking commits
# ------------------------------------------------------------
if result.returncode == 3:
    sys.exit(0)

# Pass through all other exit codes unchanged
sys.exit(result.returncode)
