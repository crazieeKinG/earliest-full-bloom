# Earliest Full Bloom

## Description
This project provides a solution to the LeetCode problem "Earliest Full Bloom Days." The solution calculates the earliest day on which all plants will be in full bloom, given their respective planting and growing times.

## Features
- Implements an efficient algorithm to solve the "Earliest Full Bloom Days" problem.
- Includes unit tests to ensure the correctness of the solution.
- Utilizes the `coverage` library to generate test coverage reports.

## Installation
Ensure you have Python 3.8+ installed on your system. Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/crazieeKinG/earliest-full-bloom.git
cd earliest-full-bloom
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage
To run the solution, execute the following command:

```bash
python earliest_full_bloom.py
```

## Testing
Unit tests are provided to verify the solution. To run the tests and generate a coverage report, use the following commands:

```bash
# Run tests
python -m unittest discover tests

# Generate coverage report
coverage run --source=. -m unittest discover tests
coverage report
```

The `.coveragerc` configuration file is used to omit test files from the coverage report.
