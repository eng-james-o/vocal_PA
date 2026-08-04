"""
Integration tests for the audio processing pipeline.
"""
import pytest
import numpy as np
from core.pitch_detector import PitchDetector
from core.note_converter import NoteConverter
from core.range_tracker import RangeTracker
from utils.constants import SAMPLE_RATE, BLOCK_SIZE


@pytest.fixture
def audio_pipeline():
    """Fixture providing the complete audio processing pipeline."""
    detector = PitchDetector()
    converter = NoteConverter()
    tracker = RangeTracker()
    return {
        'detector': detector,
        'converter': converter,
        'tracker': tracker
    }


# Check if audio capture is available (requires PortAudio)
try:
    from core.audio_capture import AudioCapture
    AUDIO_CAPTURE_AVAILABLE = True
except ImportError:
    AUDIO_CAPTURE_AVAILABLE = False


@pytest.mark.skipif(not AUDIO_CAPTURE_AVAILABLE, reason="Audio capture not available (PortAudio not installed)")
class TestAudioPipeline:
    """Tests for the complete audio processing pipeline."""

    def test_pipeline_with_sine_wave(self, audio_pipeline):
        """Test complete pipeline with sine wave input."""
        detector = audio_pipeline['detector']
        converter = audio_pipeline['converter']
        tracker = audio_pipeline['tracker']
        
        # Generate sine wave at 440 Hz (A4)
        duration = 0.1
        freq = 440.0
        t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
        audio = 0.5 * np.sin(2 * np.pi * freq * t)
        
        # Step 1: Detect pitch
        pitch, confidence = detector.detect(audio)
        assert pitch is not None
        assert confidence > 0.5
        
        # Step 2: Convert to MIDI
        midi = converter.hz_to_midi(pitch)
        assert 65 < midi < 75  # Should be around A4 (69)
        
        # Step 3: Convert to note name
        note_name = converter.hz_to_note_name(pitch)
        assert note_name is not None
        
        # Step 4: Add to tracker
        tracker.add_sample(pitch, confidence)
        assert len(tracker.history) == 1

    def test_pipeline_with_multiple_notes(self, audio_pipeline):
        """Test pipeline with multiple notes."""
        detector = audio_pipeline['detector']
        converter = audio_pipeline['converter']
        tracker = audio_pipeline['tracker']
        
        # Test with multiple frequencies
        test_freqs = [261.63, 329.63, 392.00, 440.00, 523.25]  # C4, E4, G4, A4, C5
        
        for freq in test_freqs:
            duration = 0.1
            t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
            audio = 0.5 * np.sin(2 * np.pi * freq * t)
            
            pitch, confidence = detector.detect(audio)
            if pitch:
                tracker.add_sample(pitch, confidence)
        
        # Check tracker has samples
        assert len(tracker.history) > 0
        
        # Get range
        v_range = tracker.get_range()
        assert v_range is not None
        assert v_range.min_freq > 0
        assert v_range.max_freq > v_range.min_freq

    def test_pipeline_with_tonic_calibration(self, audio_pipeline):
        """Test pipeline with tonic calibration."""
        detector = audio_pipeline['detector']
        converter = audio_pipeline['converter']
        
        # Set tonic to A4 (440 Hz)
        converter.set_tonic(440.0)
        
        # Generate audio at A4
        duration = 0.1
        freq = 440.0
        t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
        audio = 0.5 * np.sin(2 * np.pi * freq * t)
        
        # Detect pitch
        pitch, confidence = detector.detect(audio)
        assert pitch is not None
        
        # Convert to solfa
        solfa = converter.hz_to_solfa(pitch)
        assert solfa is not None
        assert solfa.syllable == "Do"
        assert solfa.octave == 0

    def test_pipeline_with_tonic_by_name(self, audio_pipeline):
        """Test pipeline with tonic set by name."""
        converter = audio_pipeline['converter']
        
        # Set tonic by name
        result = converter.set_tonic_by_name("C4")
        assert result is True
        
        # Generate audio at C4
        duration = 0.1
        freq = 261.63  # C4
        t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
        audio = 0.5 * np.sin(2 * np.pi * freq * t)
        
        # Detect pitch (using detector from pipeline)
        detector = audio_pipeline['detector']
        pitch, confidence = detector.detect(audio)
        assert pitch is not None
        
        # Convert to solfa
        solfa = converter.hz_to_solfa(pitch)
        assert solfa is not None
        assert solfa.syllable == "Do"


class TestPipelinePerformance:
    """Tests for pipeline performance."""

    def test_pipeline_latency(self, audio_pipeline):
        """Test pipeline processing time."""
        import time
        
        detector = audio_pipeline['detector']
        converter = audio_pipeline['converter']
        tracker = audio_pipeline['tracker']
        
        # Generate test audio
        duration = 0.1
        freq = 440.0
        t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
        audio = 0.5 * np.sin(2 * np.pi * freq * t)
        
        # Measure processing time
        start_time = time.time()
        
        pitch, confidence = detector.detect(audio)
        if pitch:
            midi = converter.hz_to_midi(pitch)
            note_name = converter.hz_to_note_name(pitch)
            tracker.add_sample(pitch, confidence)
        
        end_time = time.time()
        processing_time = end_time - start_time
        
        # Should complete in reasonable time (< 100ms)
        assert processing_time < 0.1

    def test_pipeline_memory_usage(self, audio_pipeline):
        """Test pipeline doesn't leak memory."""
        tracker = audio_pipeline['tracker']
        
        # Add many samples
        for i in range(100):
            tracker.add_sample(440.0 + i, 0.95)
        
        # Check history size
        assert len(tracker.history) == 100
        
        # Reset should clear memory
        tracker.reset()
        assert len(tracker.history) == 0
