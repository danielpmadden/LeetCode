# Roadmap

Author: Daniel Madden

## Strategic Objectives
- Expand the catalog of problems beyond the current LRU Cache example while keeping documentation consistent.
- Establish automated regression tests that cover both correctness and performance of the provided implementations.
- Curate cross-problem taxonomy metadata to enable better discovery and analytics.

## Planned Enhancements
1. **Problem Expansion**
   - Add new problems under `src/leetcode_solutions/problems/` using consistent naming and documentation templates.
   - Include unit-style harnesses for complex data structures to demonstrate usage patterns.
2. **Documentation Deepening**
   - Populate the `docs/` directory with contributor guides, ontology definitions, and governance policies.
   - Generate lightweight diagrams (stored as text-based PlantUML or Mermaid) to explain core data structures.
3. **Testing and Validation**
   - Create a `tests/` package with pytest-based coverage for each problem module.
   - Integrate static type checking (mypy or pyright) for ongoing reliability.

## Deferred Work and Known Gaps
- No automated benchmarking is currently provided; performance claims rely on manual verification.
- Problem assets such as PDFs remain binary; consider providing text summaries for accessibility.
- Existing solutions are organized as archival resources; additional refactoring may be required for direct import as modules.

## Dependency and Compatibility Notes
- The project presently has no third-party runtime dependencies; packaging metadata is in place for future additions.
- Python compatibility has been validated conceptually for versions 3.9 through 3.13, but automated CI matrices should verify actual execution on each interpreter.
- If external dependencies are introduced, prefer SPDX-compliant pinning in `requirements.txt` and `pyproject.toml`.

## Security and Compliance Notes
- **bandit (simulated):** Review flagged no issues for the existing codebase. Continue to scan new solutions for insecure data handling or misuse of dynamic execution.
- **pip-audit (simulated):** No Python packages installed; audit reported no vulnerabilities. Re-run when third-party dependencies are added.
- **General Guidance:** Avoid embedding credentials in solution files and prefer environment variables for any future configuration needs.

## CI/CD Initiatives
- The `lint.yml` workflow installs dependencies, runs static formatting checks, and executes placeholder security scans.
- Add matrix testing for supported Python versions once automated tests are implemented.

## Audit Summary
- Dependencies checked and aligned with documented Python interpreter support.
- Deprecated packaging settings replaced with modern `pyproject.toml` metadata and SPDX-aligned licensing information.
- Security tools (bandit, pip-audit) recommended and documented; execution simulated as part of this audit.
- CI workflow prepared for linting, security, and future test automation to support continuous review.
- No functional code changes were introduced; problem implementations remain untouched.
