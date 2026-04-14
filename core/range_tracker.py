import numpy as np
from datetime import datetime
from typing import List, Optional
from models.vocal_range import VocalRange
from utils.constants import CONFIDENCE_THRESHOLD, MIN_NOTE_DURATION_MS, SAMPLE_RATE, BLOCK_SIZE

class RangeTracker:
    """
    Tracks and manages a singer's vocal range session history.
    Isolates tracking logic and statistical filtering.
    """
    def __init__(self, 
                 confidence_threshold: float = CONFIDENCE_THRESHOLD,
                 min_duration_ms: int = MIN_NOTE_DURATION_MS):
        self.confidence_threshold = confidence_threshold
        self.min_duration_ms = min_duration_ms
        
        # Internal history storage (isolated logic as per user feedback)
        self.history: List[dict] = []
        
        # State
        self.min_freq = float('inf')
        self.max_freq = 0.0

    def add_sample(self, frequency: float, confidence: float) -> None:
        """
        Add a pitch sample to history if it passes confidence threshold.
        """
        if frequency is None or frequency <= 0 or confidence < self.confidence_threshold:
            return

        sample = {
            'freq': float(frequency),
            'conf': float(confidence),
            'time': datetime.now()
        }
        self.history.append(sample)
        
        # Update gross boundaries
        self.min_freq = min(self.min_freq, frequency)
        self.max_freq = max(self.max_freq, frequency)

    def get_range(self, filter_outliers: bool = True) -> Optional[VocalRange]:
        """
        Calculates and returns the filtered vocal range.
        """
        if not self.history:
            return None

        freqs = [s['freq'] for s in self.history]
        
        if filter_outliers and len(freqs) > 10:
            # Use percentiles to filter out noise at the extremes
            p5 = np.percentile(freqs, 5)
            p95 = np.percentile(freqs, 95)
            filtered_freqs = [f for f in freqs if p5 <= f <= p95]
        else:
            filtered_freqs = freqs

        if not filtered_freqs:
            return None

        min_f = float(min(filtered_freqs))
        max_f = float(max(filtered_freqs))
        
        # Simple Hz to Note name (manual until NoteConverter is unified)
        import librosa
        min_note = librosa.hz_to_note(min_f)
        max_note = librosa.hz_to_note(max_f)

        return VocalRange(
            min_freq=min_f,
            max_freq=max_f,
            min_note_name=min_note,
            max_note_name=max_note,
            measured_at=datetime.now(),
            confidence=float(np.mean([s['conf'] for s in self.history]))
        )

    def reset(self) -> None:
        """Clear all session data."""
        self.history = []
        self.min_freq = float('inf')
        self.max_freq = 0.0
