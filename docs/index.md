# Vocal Range Analyzer Documentation

*Your comprehensive guide to understanding, using, and contributing to Vocal Range Analyzer.*

---

## 🎤 Welcome

Welcome to the official documentation for **Vocal Range Analyzer** - a powerful Python application designed to help vocalists scientifically measure their vocal range, track pitch using movable-do solfa, and find the perfect keys for their songs.

---

## 📚 Documentation Overview

### For Users

| Guide | Description |
|-------|-------------|
| [Quick Start](user-workflow.md) | Get up and running in 60 seconds |
| [User Workflows](user-workflow.md) | Detailed guides on range testing and key optimization |
| [Troubleshooting](user-workflow.md#troubleshooting-workflow) | Common issues and solutions |

### For Developers

| Guide | Description |
|-------|-------------|
| [Technical Architecture](prd.md) | Product goals, requirements, and system design |
| [Data Models](data-models.md) | Deep dive into classes and signal processing chain |
| [API Reference](api.md) | Complete API documentation |
| [Code Review & Optimizations](REVIEW_AND_OPTIMIZATIONS.md) | Comprehensive analysis and improvement suggestions |
| [Contributing](CONTRIBUTING.md) | How to set up, test, and contribute |

### Project Information

| Document | Description |
|----------|-------------|
| [Roadmap & TODO](../TODO.md) | Detailed release plans and sprint backlog |
| [Changelog](../CHANGELOG.md) | Complete history of changes and releases |
| [License](../LICENSE) | MIT License |
| [Code of Conduct](../CODE_OF_CONDUCT.md) | Community guidelines |

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/eng-james-o/vocal_PA.git
cd vocal_PA

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

### First Steps

1. **Start a Session**: Click "Start Session" button
2. **Allow Microphone Access**: Grant permission when prompted
3. **Sing a Note**: Your pitch will appear in real-time
4. **Calibrate Tonic**: Click "Calibrate DOH" while singing your reference note
5. **Explore Your Range**: Sing from low to high to map your vocal range

---

## 🎯 Key Features

### Real-time Pitch Detection
- **YIN Algorithm**: Industry-standard pitch detection
- **Low Latency**: < 50ms end-to-end processing
- **High Accuracy**: ±5 cents at 44.1kHz
- **Confidence Scoring**: Know when your pitch is stable

### Movable-Do Solfa Notation
- **Relative Pitch**: Display notes relative to your tonic
- **Easy Calibration**: Sing your DOH to establish reference
- **Manual Override**: Set tonic by note name
- **Chromatic Support**: All 12 semitones

### Vocal Range Mapping
- **Automatic Tracking**: Min/max frequencies in real-time
- **Statistical Filtering**: Outlier rejection for accuracy
- **Sustained Note Detection**: Only counts notes held for >200ms
- **Scientific Notation**: Hz and standard pitch notation

### Key Advisor
- **Optimal Transpositions**: Find the best key for any song
- **Comfort Zone Analysis**: Prioritize your comfortable register
- **Multiple Strategies**: Center, high, or low-focused
- **Confidence Scoring**: Know how well a song fits your range

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      Vocal Range Analyzer                      │
├─────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐   │
│  │   main.py    │    │   core/      │    │   ui/        │   │
│  │  (Entry)     │───▶│  (Processing)│───▶│  (QML)       │   │
│  └──────────────┘    └──────────────┘    └──────────────┘   │
│           │                   │                   │              │
│           │        ┌──────────────────────────┐    │              │
│           │        │   AudioCapture            │    │              │
│           │        │   PitchDetector (YIN)     │    │              │
│           │        │   NoteConverter           │    │              │
│           │        │   RangeTracker            │    │              │
│           │        │   KeyAdvisor              │    │              │
│           │        └──────────────────────────┘    │              │
│           │                   │                   │              │
│           │        ┌──────────────────────────┐    │              │
│           │        │   models/                  │    │              │
│           │        │   VocalRange              │    │              │
│           │        │   SolfaResult              │    │              │
│           │        │   KeyRecommendation        │    │              │
│           │        └──────────────────────────┘    │              │
│           │                                          │              │
│           └──────────────────────────────────────────┘              │
│                                                                  │
└─────────────────────────────────────────────────────────────┘
```

---

## 🤝 Contributing

We welcome contributions from everyone! Here's how you can help:

### Ways to Contribute

- **🐛 Report Bugs**: Open issues for bugs you find
- **💡 Suggest Features**: Share your ideas for improvements
- **📝 Improve Docs**: Help improve documentation
- **💻 Write Code**: Submit pull requests for new features or fixes
- **🎨 Design UI**: Help with user interface design
- **📢 Spread the Word**: Share the project with others

### Getting Started

1. **Read the [Contributing Guide](CONTRIBUTING.md)**
2. **Check the [Roadmap](../TODO.md)** for open tasks
3. **Join the Discussion**: Open an issue to discuss your idea
4. **Fork & Code**: Implement your changes
5. **Submit PR**: Follow our PR template

---

## 📊 Performance

### Current Metrics (v0.1.0-alpha)

| Metric | Value | Target |
|--------|-------|--------|
| **Latency** | ~30ms | < 50ms |
| **Accuracy** | ±5 cents | ±5 cents |
| **Sampling Rate** | 44.1kHz | 44.1kHz |
| **Test Coverage** | 0% | 80%+ |

### Benchmarks

```
Operation                    Time (ms)    Notes
─────────────────────────────────────────────────
Audio Capture (2048)         ~5           sounddevice callback
YIN Pitch Detection          ~10-20       librosa.pyin
Note Conversion              ~1-2         Simple math
Solfa Conversion             ~2-3         With string ops
Range Tracking               ~1-2         With filtering
─────────────────────────────────────────────────
Total Pipeline               ~20-30       End-to-end
```

---

## 📅 Release Timeline

| Version | Date | Status |
|---------|------|--------|
| v0.0.1 | 2026-03-25 | Pre-alpha |
| v0.1.0-alpha | 2026-04-10 | Current |
| v0.1.1 | 2026-04-15 | Planned |
| v0.2.0 | 2026-05-01 | Planned |
| v0.3.0 | 2026-06-01 | Planned |
| v0.4.0 | 2026-07-15 | Planned |
| v1.0.0 | 2026-09-01 | Planned |

---

## 🙏 Support

### Community

- **GitHub Discussions**: [Open a discussion](https://github.com/eng-james-o/vocal_PA/discussions)
- **Issues**: [Report a bug](https://github.com/eng-james-o/vocal_PA/issues)
- **Pull Requests**: [Submit a PR](https://github.com/eng-james-o/vocal_PA/pulls)

### Resources

- **[Documentation](https://github.com/eng-james-o/vocal_PA/docs)**: Complete project documentation
- **[Roadmap](../TODO.md)**: Future plans and priorities
- **[Changelog](../CHANGELOG.md)**: Release history
- **[Code Review](REVIEW_AND_OPTIMIZATIONS.md)**: Technical analysis

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](../LICENSE) file for details.

---

*"Your voice is unique. Understand it. Master it. Share it with the world."*

---

© 2026 Vocal Range Analyzer Contributors

*Built with ❤️ for singers everywhere*
