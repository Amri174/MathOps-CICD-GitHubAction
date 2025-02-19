## Overview
This demonstration is based on implementation of Continuous Integration (CI) and Continuous Deployment (CD) using GitHub Actions. The project includes a Python-based application with automated workflows for building, testing, and maintaining the codebase. GitHub Actions is utilized for ensuring code quality and streamline deployment processes.

## Features
- Automated testing using pytest for mathematical operations.
- CI/CD pipeline configured with GitHub Actions.
- Modular Python functions for addition, subtraction, multiplication, division, and modulus operations.
- Floating-point precision handling with pytest.approx.
- Error handling done for edge cases like division by zero or modulus by zero.

## Project Structure
```
MathOps-CICD-GitHubAction/
│
├── src/
│   ├── math_operations.py       # Python module with mathematical functions
│
├── tests/
│   ├── test_operations.py       # Pytest test cases for mathematical operations
│
├── .github/
│   ├── workflows/
│       ├── ci.yml               # GitHub Actions workflow file for CI/CD
│
├── README.md                    # Summary
├── requirements.txt             # Python dependencies used
```

## Installation
Clone the repository:

```
git clone https://github.com/Amri174/MathOps-CICD-GitHubAction.git
cd MathOps-CICD-GitHubAction
```
Create and activate a virtual environment:

```
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
Install dependencies:

```
pip install -r requirements.txt
```
Run tests locally:

```
pytest tests/test_operations.py
```
## Issues Faced:
1. Modulus operation % in Python will return result that has same sign as the divisor.

- Example: modulus(-9, 4) returns 3, not -1.

2. Floating-point precision caused small errors in Test results (handled using pytest.approx).
