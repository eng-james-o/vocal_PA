# Vocal Range Analyzer 🎤

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> A powerful Python application for vocalists to scientifically measure their vocal range, track pitch using movable-do solfa, and find the perfect keys for their songs.

![Application Screenshot](https://via.placeholder.com/800x400.png?text=Vocal+Range+Analyzer+Screenshot)

## 🌟 Key Features

- **Real-time Pitch Detection**: Optimized YIN algorithm for human voice.
- **Movable-Do Solfa**: Relative pitch notation based on *your* tonic.
- **Vocal Range Mapping**: Track min/max notes with statistical outlier rejection.
- **Key Advisor**: Find optimal transpositions for songs and full setlists.

## 📖 Documentation

We have organized our documentation into specialized guides for easier navigation:

- **[Quick Start Guide](docs/user-workflow.md)**: Get up and running in 60 seconds.
- **[User Workflows](docs/user-workflow.md)**: Detailed guides on range testing and key optimization.
- **[Technical Architecture](docs/prd.md)**: Product goals, requirements, and system design.
- **[Data Models](docs/data-models.md)**: Deep dive into the classes and signal processing chain.
- **[Development Guide](CONTRIBUTING.md)**: How to set up, test, and contribute to the project.

## ⚡ Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/vocal-range-analyzer.git
cd vocal-range-analyzer

# Install dependencies
pip install -r requirements.txt

# Run the app
python main.py
```

## 🗺️ Project Status & Roadmap

See our **[TODO.md](TODO.md)** for a detailed list of current tasks and future vision.
Check the **[CHANGELOG.md](CHANGELOG.md)** for recent updates.

## 🤝 Contributing

We love contributions! Please read our **[Contributing Guide](CONTRIBUTING.md)** before submitting a pull request.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
© 2026 Vocal Range Analyzer Contributors
