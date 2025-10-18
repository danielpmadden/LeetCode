# LeetCode Solutions Repository

## Overview
This repository captures a curated set of LeetCode exercises with accompanying explanations and supporting artifacts. The focus is on long-term maintainability, repeatability, and transparent reasoning so that each solution can be audited, tested, and evolved without guessing about original intent.

## Key Features
- Verified Python implementations for selected LeetCode problems
- Human-readable explanations documenting the underlying reasoning
- Source assets (such as accepted-submission PDFs) retained for traceability
- Modern Python packaging metadata for reproducible installation and reuse
- Continuous integration workflow prepared for linting and security auditing

## Repository Structure
```
LeetCode
├── src/                        → Installable Python package (`leetcode_solutions`)
│   └── leetcode_solutions/
│       ├── __init__.py         → Package metadata and helpers
│       └── problems/           → Problem archives and resources
│           └── 0146_LRU_Cache/ → Solution and supporting documents for problem 146
├── docs/                       → Reserved for project-wide documentation (future use)
├── tests/                      → Reserved for automated regression tests (future use)
├── .github/workflows/          → Continuous integration workflows
├── README.md                   → Project overview and getting started guide
├── ROADMAP.md                  → Planned enhancements and audit notes
├── CHANGELOG.md                → Release and update history
├── pyproject.toml              → Build metadata (Python 3.9–3.13 compatible)
├── requirements.txt            → Explicit dependency declaration
└── LICENSE                     → MIT License terms
```

## Dependency Overview
```
leetcode_solutions
├── __init__.py         → Exposes package root path
└── problems/
    └── 0146_LRU_Cache/
        ├── Solution.py → LRU Cache data structure implementation
        ├── README.md   → Problem summary and quick reference
        ├── Explanation.md → Detailed reasoning notes
        └── *.pdf       → Original problem statement and submission proof
```

## Installation
1. Create and activate a Python 3.9–3.13 virtual environment.
2. Install the project in editable mode:
   ```bash
   pip install -e .
   ```

The project currently depends only on the Python standard library. The package metadata is provided for consistency and future growth.

## Quick Start
```python
from leetcode_solutions import PACKAGE_ROOT

print("Solutions stored at:", PACKAGE_ROOT)
```
Individual problem solutions are designed for direct use in interview preparation or algorithm practice sessions. Each solution module can be run or imported independently within the `problems` directory structure.

## Example Usage
To experiment with the LRU Cache implementation interactively:
```python
from pathlib import Path
import runpy

solution_path = Path("src/leetcode_solutions/problems/0146_LRU_Cache/Solution.py")
runpy.run_path(solution_path)
```
This snippet loads the module so that the `LRUCache` class is available in the interpreter namespace. Refer to the accompanying `Explanation.md` for algorithm details and complexity analysis.

## Troubleshooting
- **Import Errors:** Ensure that the repository has been installed with `pip install -e .` so that the `leetcode_solutions` package is discoverable.
- **Python Version:** Confirm that you are using Python 3.9 or later. The project metadata is validated up to Python 3.13.
- **Missing PDFs:** The PDFs are included for provenance; if cloning with sparse-checkout, ensure binary files are fetched explicitly.

## Support and Contributions
Questions, corrections, and enhancements are welcome. Please open an issue or pull request describing the change along with relevant references or verification steps. When contributing new problems, include both code and documentation to maintain the repository's audit trail.

## License
This project is released under the MIT License. See [LICENSE](LICENSE) for full terms and conditions.
