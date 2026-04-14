"""
Centralized constants and configuration for the Vocal Range Analyzer.
"""

# Audio Capture Settings
SAMPLE_RATE = 44100
BLOCK_SIZE = 2048
CHANNELS = 1

# Frequency Ranges for Pitch Detection (Librosa)
F_MIN = 65.41   # C2: Typical bottom of bass range
F_MAX = 1046.50 # C6: Typical top of soprano range

# Statistical Filtering Thresholds
MIN_NOTE_DURATION_MS = 200
CONFIDENCE_THRESHOLD = 0.8  # YIN confidence

# Musical Constants
REFERENCE_A4_FREQ = 440.0
SEMITONES_IN_OCTAVE = 12

# Solfa Map (Chromatic)
SOLFA_MAP = {
    0: 'Do', 1: 'Di/Ra', 2: 'Re', 3: 'Ri/Me', 
    4: 'Mi', 5: 'Fa', 6: 'Fi/Se', 7: 'Sol',
    8: 'Le/Si', 9: 'La', 10: 'Li/Te', 11: 'Ti'
}
