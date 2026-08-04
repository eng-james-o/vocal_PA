# Contributing to Vocal Range Analyzer

*First off, thank you for considering contributing to Vocal Range Analyzer! It's people like you that make the open source community such an amazing place to learn, inspire, and create.*

---

## 🌟 Welcome to Our Community

We're excited to have you here! Whether you're a developer, designer, tester, or just someone passionate about vocal music, there's a place for you in our project.

---

## 📋 Table of Contents

1. [Code of Conduct](#-code-of-conduct)
2. [Getting Started](#-getting-started)
3. [Development Setup](#-development-setup)
4. [Project Structure](#-project-structure)
5. [Coding Standards](#-coding-standards)
6. [Testing](#-testing)
7. [Pull Request Process](#-pull-request-process)
8. [Reporting Issues](#-reporting-issues)
9. [Community Guidelines](#-community-guidelines)
10. [Recognition](#-recognition)

---

## 🤝 Code of Conduct

We are committed to providing a friendly, safe, and welcoming environment for all, regardless of gender, sexual orientation, disability, ethnicity, religion, or similar personal characteristic.

Please read and follow our **[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)** in all your interactions with the project.

---

## 🚀 Getting Started

### For First-Time Contributors

If you're new to open source, here's a step-by-step guide:

1. **Find an Issue**: Look for issues labeled `good first issue` or `help wanted`
2. **Ask Questions**: Comment on the issue to clarify requirements
3. **Fork the Repo**: Create your own copy to work on
4. **Create a Branch**: Use a descriptive name like `fix/typo-in-readme`
5. **Make Changes**: Implement your fix or feature
6. **Test**: Ensure everything works
7. **Commit**: Write clear, descriptive commit messages
8. **Push**: Upload your changes to your fork
9. **Open PR**: Submit a pull request to the main repo

### For Experienced Developers

1. **Check the Roadmap**: See [TODO.md](TODO.md) for priorities
2. **Review Open Issues**: Find something that interests you
3. **Discuss**: Open a discussion or comment on an issue
4. **Implement**: Follow our coding standards
5. **Test**: Write comprehensive tests
6. **Document**: Update relevant documentation
7. **Submit PR**: Follow our PR process

---

## 💻 Development Setup

### Prerequisites

| Requirement | Version | Notes |
|-------------|---------|-------|
| **Python** | 3.9+ | Required for type hints and modern features |
| **Git** | Latest | For version control |
| **pip** | Latest | Python package manager |
| **Virtual Environment** | Any | venv, conda, poetry, etc. |

### Recommended Setup

#### Option 1: Using venv (Recommended)

```bash
# Clone the repository
git clone https://github.com/eng-james-o/vocal_PA.git
cd vocal_PA

# Create virtual environment
python -m venv venv

# Activate environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt  # If exists
```

#### Option 2: Using conda

```bash
# Create conda environment
conda create -n vocal_pa python=3.11
conda activate vocal_pa

# Clone and install
git clone https://github.com/eng-james-o/vocal_PA.git
cd vocal_PA
pip install -r requirements.txt
```

#### Option 3: Using poetry (Alternative)

```bash
# Install poetry
pip install poetry

# Clone and install
git clone https://github.com/eng-james-o/vocal_PA.git
cd vocal_PA
poetry install
```

### Verify Installation

```bash
# Run the application
python main.py

# Run tests (if available)
pytest tests/ -v

# Check code quality
flake8 core/
mypy core/ --strict
black core/ --check
```

---

## 🗂️ Project Structure

```
vocal_PA/
├── core/                      # Core processing logic
│   ├── __init__.py
│   ├── audio_capture.py       # Audio input streaming
│   ├── bridge.py             # Qt/Python to QML bridge
│   ├── key_advisor.py        # Key recommendation engine
│   ├── note_converter.py     # Frequency to notation conversion
│   ├── pitch_detector.py     # YIN pitch detection
│   └── range_tracker.py      # Vocal range tracking
│
├── models/                    # Data models
│   ├── __init__.py
│   ├── key_recommendation.py  # Key recommendation data
│   ├── solfa_result.py        # Solfa notation result
│   └── vocal_range.py         # Vocal range data
│
├── ui/                        # User interface (QML)
│   ├── components/           # Reusable UI components
│   │   ├── GainMeter.qml
│   │   ├── PitchDisplay.qml
│   │   ├── RangeDisplay.qml
│   │   ├── TonicControls.qml
│   │   └── qmldir
│   ├── pages/                 # UI pages
│   │   ├── AnalyzerPage.qml
│   │   └── qmldir
│   ├── Style.qml              # Design system
│   ├── main.qml               # Main application window
│   └── qmldir
│
├── utils/                     # Utility modules
│   ├── __init__.py
│   └── constants.py           # Centralized configuration
│
├── docs/                      # Documentation
│   ├── api.md                # API documentation (planned)
│   ├── data-models.md         # Data structures and relationships
│   ├── prd.md                 # Product requirements document
│   ├── REVIEW_AND_OPTIMIZATIONS.md  # Code review and optimizations
│   └── user-workflow.md       # User guides and workflows
│
├── tests/                     # Tests (to be created)
│   ├── unit/                  # Unit tests
│   ├── integration/           # Integration tests
│   └── conftest.py            # Test fixtures
│
├── .github/                   # GitHub configuration
│   └── workflows/             # CI/CD pipelines
│
├── .gitignore                 # Git ignore patterns
├── CHANGELOG.md               # Release history
├── CONTRIBUTING.md            # This file
├── LICENSE                    # MIT License
├── main.py                    # Application entry point
├── README.md                  # Project overview
└── requirements.txt            # Python dependencies
```

---

## 📜 Coding Standards

### General Principles

1. **Readability First**: Code should be easy to read and understand
2. **Consistency**: Follow existing patterns in the codebase
3. **Simplicity**: Keep it simple, stupid (KISS principle)
4. **Maintainability**: Write code that's easy to maintain and extend

### Python Standards

#### Style

- **PEP 8**: Follow [PEP 8](https://peps.python.org/pep-0008/) style guide
- **Line Length**: 88 characters maximum
- **Indentation**: 4 spaces (no tabs)
- **Encoding**: UTF-8 always

#### Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Variables | snake_case | `sample_rate`, `audio_buffer` |
| Functions | snake_case | `detect_pitch()`, `hz_to_midi()` |
| Classes | PascalCase | `PitchDetector`, `VocalRange` |
| Constants | UPPER_SNAKE_CASE | `SAMPLE_RATE`, `F_MIN` |
| Private | _prefix | `_internal_state`, `_callback()` |
| Protected | _prefix | `_protected_method()` |

#### Type Hints

- **Required**: All public functions and methods must have type hints
- **Complete**: Include return types for all functions
- **Optional**: Use `Optional[T]` for parameters that can be None
- **Union Types**: Use `Union[T1, T2]` or `T1 | T2` (Python 3.10+)

```python
# Good
def detect_pitch(audio_buffer: np.ndarray) -> Tuple[Optional[float], float]:
    pass

# Bad (missing type hints)
def detect_pitch(audio_buffer):
    pass
```

#### Docstrings

- **Style**: Google Style docstrings
- **Required**: All public classes, methods, and functions
- **Complete**: Include parameter descriptions, return values, and examples

```python
"""
Detects fundamental frequency from audio buffers using the YIN algorithm.

Args:
    audio_buffer: numpy.ndarray - Input audio samples (monophonic)
    
Returns:
    Tuple[Optional[float], float] - (frequency_hz, confidence)
    
Example:
    >>> detector = PitchDetector()
    >>> audio = np.random.randn(2048)
    >>> freq, conf = detector.detect(audio)
"""
```

#### Imports

- **Order**: Standard library, third-party, local imports
- **Grouping**: Separate groups with blank lines
- **Wildcard**: Avoid wildcard imports (`from module import *`)

```python
# Good
import os
import sys
from typing import Optional, Tuple

import numpy as np
import librosa

from utils.constants import SAMPLE_RATE
from models.vocal_range import VocalRange

# Bad
from core.* import *
```

### Qt/QML Standards

#### Signal/Slot Connections

- **Naming**: Use descriptive signal names
- **Thread Safety**: Ensure thread-safe signal emissions
- **Disconnect**: Always disconnect signals when cleaning up

```python
# Good
class CoreBridge(QObject):
    pitchChanged = Signal()  # Clear signal name
    
    def __init__(self):
        super().__init__()
        self._worker.pitch_detected.connect(self._on_pitch_detected)
    
    def cleanup(self):
        self._worker.pitch_detected.disconnect()
```

#### Property Naming

- **PascalCase**: For QML properties
- **Descriptive**: Clear what the property represents
- **Notify**: Always include notify signal

```qml
// Good
property string currentNote: "---"
property real currentGain: 0.0

// Bad
property string note
property real gain
```

---

## 🧪 Testing

### Testing Philosophy

We believe in **test-driven development (TDD)** and **comprehensive test coverage**. Every new feature should come with tests, and every bug fix should include a regression test.

### Test Structure

```
tests/
├── unit/                      # Unit tests (isolated components)
│   ├── test_pitch_detector.py
│   ├── test_note_converter.py
│   ├── test_range_tracker.py
│   ├── test_key_advisor.py
│   └── test_models.py
│
├── integration/               # Integration tests (component interactions)
│   ├── test_audio_pipeline.py
│   ├── test_ui_integration.py
│   └── test_bridge.py
│
└── conftest.py                # Shared test fixtures
```

### Writing Tests

#### Unit Tests

- **Focus**: Individual functions or classes
- **Isolation**: Mock dependencies
- **Speed**: Should run quickly (< 100ms each)

```python
# tests/unit/test_note_converter.py
import pytest
import numpy as np
from core.note_converter import NoteConverter

@pytest.fixture
def converter():
    return NoteConverter()

def test_hz_to_midi(converter):
    # A4 = 440 Hz = MIDI 69
    assert abs(converter.hz_to_midi(440.0) - 69.0) < 0.01

def test_set_tonic(converter):
    converter.set_tonic(440.0)  # A4 as DOH
    result = converter.hz_to_solfa(440.0)
    assert result.syllable == "Do"
    assert result.octave == 0
```

#### Integration Tests

- **Focus**: Component interactions
- **Real Dependencies**: Use real implementations where possible
- **End-to-End**: Test complete workflows

```python
# tests/integration/test_audio_pipeline.py
import numpy as np
from core.audio_capture import AudioCapture
from core.pitch_detector import PitchDetector

def test_pitch_detection_pipeline():
    # Generate test sine wave
    sr = 44100
    duration = 0.1
    freq = 440.0
    t = np.linspace(0, duration, int(sr * duration), False)
    audio = 0.5 * np.sin(2 * np.pi * freq * t)
    
    detector = PitchDetector()
    pitch, confidence = detector.detect(audio)
    
    assert pitch is not None
    assert abs(pitch - freq) < 1.0  # Within 1 Hz
    assert confidence > 0.5
```

### Running Tests

```bash
# Run all tests
pytest tests/

# Run with verbose output
pytest tests/ -v

# Run with coverage
pytest --cov=core --cov-report=term-missing tests/

# Run specific test file
pytest tests/unit/test_note_converter.py

# Run specific test function
pytest tests/unit/test_note_converter.py::test_hz_to_midi
```

### Test Coverage Goals

| Component | Target Coverage |
|-----------|-----------------|
| core/ | 95% |
| models/ | 100% |
| utils/ | 100% |
| **Total** | **90%+** |

---

## 🔄 Pull Request Process

### Before Submitting

1. **Check for Open PRs**: Make sure no one else is working on the same thing
2. **Update Your Branch**: Rebase on the latest main branch
3. **Run Tests**: Ensure all tests pass
4. **Check Code Quality**: Run linting and type checking
5. **Test Manually**: Verify your changes work as expected

### PR Requirements

1. **Descriptive Title**: Clear and concise
2. **Detailed Description**: Explain what and why
3. **Linked Issues**: Reference any related issues
4. **Tests**: Include new tests for your changes
5. **Documentation**: Update relevant docs
6. **Screenshots**: For UI changes

### PR Template

```markdown
## Summary

[Brief description of the change]

## Related Issues

- Closes #[issue-number]
- Related to #[issue-number]

## Changes Made

- [ ] Added new feature
- [ ] Fixed bug
- [ ] Improved performance
- [ ] Updated documentation
- [ ] Added tests

## Testing

- [ ] All existing tests pass
- [ ] New tests added
- [ ] Manual testing completed

## Screenshots (if applicable)

[Add screenshots for UI changes]

## Notes

[Any additional context or information]
```

### PR Review Process

1. **Initial Review**: Maintainer reviews within 48 hours
2. **Feedback**: Requested changes or approval
3. **Iteration**: Address feedback and update PR
4. **Final Review**: Second maintainer approval
5. **Merge**: PR is merged to main branch

### PR Checklist

- [ ] Code follows style guidelines
- [ ] All tests pass
- [ ] New tests added for new functionality
- [ ] Documentation updated
- [ ] No breaking changes (or documented)
- [ ] Signed commits (if required)

---

## 🐛 Reporting Issues

### Before Reporting

1. **Check Existing Issues**: Search for similar reports
2. **Update Software**: Ensure you're on the latest version
3. **Gather Information**: Collect relevant details

### Issue Template

```markdown
## Description

[Clear and concise description of the issue]

## Steps to Reproduce

1. [First step]
2. [Second step]
3. [Third step]

## Expected Behavior

[What you expected to happen]

## Actual Behavior

[What actually happened]

## Environment

- OS: [Windows/macOS/Linux]
- Python Version: [3.x.x]
- Vocal Range Analyzer Version: [x.x.x]
- Dependencies: [list versions]

## Additional Context

[Any other relevant information, logs, screenshots, etc.]
```

### Issue Labels

| Label | Description |
|-------|-------------|
| `bug` | Confirmed bug |
| `enhancement` | Feature request |
| `documentation` | Documentation improvement |
| `good first issue` | Good for new contributors |
| `help wanted` | Needs community help |
| `priority: critical` | Must be fixed immediately |
| `priority: high` | Important, should be fixed soon |
| `priority: medium` | Nice to have |
| `priority: low` | Future enhancement |

---

## 👥 Community Guidelines

### Communication

- **Be Respectful**: Treat everyone with kindness and respect
- **Be Inclusive**: Welcome all contributors regardless of background
- **Be Patient**: Everyone learns at different speeds
- **Be Helpful**: Share your knowledge and experience

### Collaboration

- **Ask Questions**: Don't hesitate to ask for clarification
- **Provide Feedback**: Constructive feedback helps everyone improve
- **Share Ideas**: All ideas are welcome, no matter how big or small
- **Celebrate Success**: Acknowledge good work and milestones

### Conflict Resolution

1. **Stay Calm**: Take a breath and approach with empathy
2. **Listen**: Understand all perspectives
3. **Discuss**: Find common ground
4. **Escalate**: Involve maintainers if needed

---

## 🏆 Recognition

### Contributor Levels

| Level | Requirements | Benefits |
|-------|--------------|----------|
| **New Contributor** | 1+ PR merged | Name in CONTRIBUTORS.md |
| **Regular Contributor** | 5+ PRs merged | Early access to features |
| **Active Contributor** | 10+ PRs merged | Review privileges |
| **Maintainer** | Consistent contributions | Full access |

### Contributor Spotlight

Each release, we highlight outstanding contributors in:
- Release notes
- README.md
- Social media (when applicable)

### Hall of Fame

Top contributors will be recognized in a dedicated **CONTRIBUTORS.md** file.

---

## 📚 Additional Resources

### Learning Materials

- [Python Documentation](https://docs.python.org/3/)
- [PySide6 Documentation](https://doc.qt.io/qtforpython-6/)
- [QML Documentation](https://doc.qt.io/qt-6/qmlapplications.html)
- [librosa Documentation](https://librosa.org/doc/latest/index.html)
- [GitHub Guides](https://guides.github.com/)

### Related Projects

- [librosa](https://github.com/librosa/librosa): Audio analysis library
- [sounddevice](https://github.com/spatialaudio/python-sounddevice): Audio I/O
- [music21](https://github.com/cuthbertLab/music21): Music theory toolkit
- [PySide6](https://github.com/qt/qtforpython): Qt for Python

### Community

- **GitHub Discussions**: [Join the discussion](https://github.com/eng-james-o/vocal_PA/discussions)
- **Issues**: [Report bugs](https://github.com/eng-james-o/vocal_PA/issues)
- **Pull Requests**: [Submit changes](https://github.com/eng-james-o/vocal_PA/pulls)

---

## 📝 Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

---

## 🙏 Thank You

Thank you for taking the time to contribute to Vocal Range Analyzer! Your contributions, no matter how small, make a real difference to the project and the community.

*"Alone we can do so little; together we can do so much."* - Helen Keller

---

*Last updated: 2026-04-10*
*Maintained by: Vocal Range Analyzer Team*
