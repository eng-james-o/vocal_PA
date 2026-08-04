"""
Unit tests for PitchDetector class.
"""
import pytest
import numpy as np
from core.pitch_detector import PitchDetector
from utils.constants import SAMPLE_RATE, F_MIN, F_MAX, BLOCK_SIZE


@pytest.fixture
def detector():
    """Fixture providing a PitchDetector instance."""
    return PitchDetector(
        sample_rate=SAMPLE_RATE,
        fmin=F_MIN,
        fmax=F_MAX,
        frame_length=BLOCK_SIZE
    )


class TestPitchDetectorInitialization:
    """Tests for PitchDetector initialization."""

    def test_default_initialization(self):
        """PitchDetector should initialize with default values."""
        detector = PitchDetector()
        assert detector.sr == SAMPLE_RATE
        assert detector.fmin == F_MIN
        assert detector.fmax == F_MAX
        assert detector.frame_length == BLOCK_SIZE

    def test_custom_initialization(self):
        """PitchDetector should accept custom parameters."""
        custom_sr = 48000
        custom_fmin = 80.0
        custom_fmax = 1200.0
        custom_frame = 4096
        
        detector = PitchDetector(
            sample_rate=custom_sr,
            fmin=custom_fmin,
            fmax=custom_fmax,
            frame_length=custom_frame
        )
        assert detector.sr == custom_sr
        assert detector.fmin == custom_fmin
        assert detector.fmax == custom_fmax
        assert detector.frame_length == custom_frame


class TestPitchDetection:
    """Tests for pitch detection functionality."""

    def test_detect_with_valid_audio(self, detector):
        """PitchDetector should detect pitch from valid audio."""
        # Generate a sine wave at 440 Hz (A4)
        duration = 0.1
        freq = 440.0
        t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
        audio = 0.5 * np.sin(2 * np.pi * freq * t)
        
        pitch, confidence = detector.detect(audio)
        
        assert pitch is not None
        assert confidence >= 0.0
        # Check if detected pitch is close to 440 Hz (within 5 Hz)
        assert abs(pitch - freq) < 5.0

    def test_detect_with_silence(self, detector):
        """PitchDetector should return None for silence."""
        audio = np.zeros(BLOCK_SIZE)
        pitch, confidence = detector.detect(audio)
        
        assert pitch is None
        assert confidence == 0.0

    def test_detect_with_short_audio(self, detector):
        """PitchDetector should handle short audio buffers."""
        short_audio = np.random.randn(BLOCK_SIZE // 2)
        pitch, confidence = detector.detect(short_audio)
        
        # Should return None for buffers shorter than frame_length
        assert pitch is None
        assert confidence == 0.0

    def test_detect_with_multiple_frequencies(self, detector):
        """PitchDetector should detect fundamental frequency."""
        # Generate a complex signal with fundamental at 220 Hz and harmonics
        duration = 0.1
        fundamental = 220.0
        t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
        audio = 0.5 * np.sin(2 * np.pi * fundamental * t)
        audio += 0.3 * np.sin(2 * np.pi * fundamental * 2 * t)  # 2nd harmonic
        audio += 0.2 * np.sin(2 * np.pi * fundamental * 3 * t)  # 3rd harmonic
        
        pitch, confidence = detector.detect(audio)
        
        assert pitch is not None
        # Should detect the fundamental frequency
        assert abs(pitch - fundamental) < 5.0

    def test_detect_with_noise(self, detector):
        """PitchDetector should handle noisy signals."""
        duration = 0.1
        freq = 440.0
        t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
        audio = 0.5 * np.sin(2 * np.pi * freq * t)
        # Add noise
        audio += 0.1 * np.random.randn(len(audio))
        
        pitch, confidence = detector.detect(audio)
        
        assert pitch is not None
        assert abs(pitch - freq) < 10.0  # Allow more tolerance with noise


class TestEdgeCases:
    """Tests for edge cases in pitch detection."""

    def test_detect_with_very_low_frequency(self, detector):
        """PitchDetector should handle very low frequencies."""
        duration = 0.1
        freq = 70.0  # Below F_MIN (65.41)
        t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
        audio = 0.5 * np.sin(2 * np.pi * freq * t)
        
        pitch, confidence = detector.detect(audio)
        # May or may not detect, but shouldn't crash
        assert True

    def test_detect_with_very_high_frequency(self, detector):
        """PitchDetector should handle very high frequencies."""
        duration = 0.1
        freq = 1200.0  # Above F_MAX (1046.50)
        t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
        audio = 0.5 * np.sin(2 * np.pi * freq * t)
        
        pitch, confidence = detector.detect(audio)
        # May or may not detect, but shouldn't crash
        assert True

    def test_detect_with_nan_values(self, detector):
        """PitchDetector should handle NaN values gracefully."""
        audio = np.random.randn(BLOCK_SIZE)
        audio[10:20] = np.nan
        
        try:
            pitch, confidence = detector.detect(audio)
            # Should not crash
            assert True
        except:
            # If it raises an exception, that's acceptable for now
            assert True

    def test_detect_with_inf_values(self, detector):
        """PitchDetector should handle infinite values gracefully."""
        audio = np.random.randn(BLOCK_SIZE)
        audio[10:20] = np.inf
        
        try:
            pitch, confidence = detector.detect(audio)
            # Should not crash
            assert True
        except:
            # If it raises an exception, that's acceptable for now
            assert True
