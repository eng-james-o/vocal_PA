# Contributing to Vocal Range Analyzer

First off, thank you for considering contributing to Vocal Range Analyzer! It's people like you that make the open source community such an amazing place to learn, inspire, and create.

## 1. Development Setup

### Prerequisites

- Python 3.9 or higher
- `venv` or `conda` for environment management
- Git

### Installation

1. **Clone the repo**:

```bash
    git clone https://github.com/yourusername/vocal-range-analyzer.git
    cd vocal-range-analyzer
```

2. **Create a Virtual Environment**:

```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    ```
3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    pip install -r requirements-dev.txt
    ```

## 2. Testing

We use `pytest` for our testing suite. Please ensure all tests pass before submitting a pull request.

```bash
# Run all tests
pytest tests/

# Run with coverage report
pytest --cov=core tests/
```

### Writing Tests

- **Unit Tests**: Place in `tests/unit/`. Focus on individual functions in `core/`.
- **Integration Tests**: Place in `tests/integration/`. Focus on the pipeline from audio buffer to solfa result.

## 3. Coding Standards

### Style

We follow **PEP 8** and use `black` for formatting.

- **Line Length**: 88 characters.
- **Docstrings**: Google Style.
- **Type Hints**: Required for all public class methods and standalone functions.

### Quality Checks

Before committing, please run the following:

```bash
# Linting
flake8 core/

# Type Checking
mypy core/ --strict

# Formatting
black core/ --check
```

## 4. Pull Request Process

1. **Direct Branching**: Use `feat/`, `fix/`, or `docs/` prefixes for branch names.

```bash
    Example: feat/real-time-smoothing
```

2. **Commit Messages**: Use imperative mood (e.g., "Add pitch detection" instead of "Added pitch detection").
3. **PR Description**: Use our template to explain *what* changed and *why*.
4. **Review**: At least one maintainer must approve the PR before merge.

## 5. Community

- **Code of Conduct**: Please adhere to the [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
- **Issues**: Report bugs or suggest features via the GitHub Issue Tracker.

---
Happy coding!
