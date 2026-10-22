# Copilot instructions

## Repository structure and architecture

- This repository is a sequence of CPSC 223P Python coursework exercises, organized into directories named for their class dates. Filenames identify the module, assignment, lecture, worksheet, or exam.
- Each `.py` file is generally a small, standalone script, not part of a packaged application. Scripts commonly execute their example or prompt for input at the top level and print results.
- Some exercises define reusable functions in one file and import them from another script in the same dated directory. For example, `10-8-2026/runner.py` exercises functions from `10-8-2026/M6A5.py`. Keep such imports local to the relevant exercise directory.
- The exercises progress through introductory Python topics, including variables and input/output, conditionals, loops, collections, functions, and classes. Use nearby exercises in the same directory or module as the best guide to the expected scope and style.

## Build, run, and checks

- There is no configured build system, automated test suite, or linter in the repository.
- Run one exercise with Python 3: `python3 <date-directory>/<script>.py`. For example: `python3 10-8-2026/runner.py`. Enter any requested input in the terminal.
- Check the syntax of one file with `python3 -m py_compile <date-directory>/<script>.py`.
- For exercises with functions demonstrated by a companion runner, run that runner as the manual behavior check. Otherwise, run the exercise script itself and compare its output or interaction with the assignment requirements.

## Conventions

- Keep each exercise self-contained in its existing dated directory; avoid introducing project-wide frameworks or dependencies for an individual assignment.
- Preserve the existing filename and assignment/module numbering when editing coursework, and follow the nearby comment-header format for assignment metadata.
- Match the learning objective and level of the exercise. Many files intentionally demonstrate a specific language construct using direct, readable code and `print`/`input`; avoid replacing that demonstration with unrelated abstractions.
- Follow local naming and formatting patterns. Some exercises use descriptive names with type-oriented suffixes such as `_list`, `_int`, and `_dict`; consistency within the exercise takes precedence over imposing a repository-wide renaming scheme.
