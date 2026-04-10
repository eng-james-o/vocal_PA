import librosa
import numpy as np
from typing import Optional, Tuple
from utils.constants import F_MIN, F_MAX, SAMPLE_RATE, BLOCK_SIZE

class PitchDetector:
    """
    Detects fundamental frequency from audio buffers using the YIN algorithm.
    """
    def __init__(self, 
                 sample_rate: int = SAMPLE_RATE,
                 fmin: float = F_MIN,
                 fmax: float = F_MAX,
                 frame_length: int = BLOCK_SIZE):
        self.sr = sample_rate
        self.fmin = fmin
        self.fmax = fmax
        self.frame_length = frame_length

    def detect(self, audio_buffer: np.ndarray) -> Tuple[Optional[float], float]:
        """
        Detect pitch in a monophonic audio buffer.
        
        Returns:
            Tuple of (frequency_hz, confidence)
        """
        if len(audio_buffer) < self.frame_length:
            return None, 0.0

        # YIN algorithm via librosa
        # f0: pitch estimates, voiced_flag: boolean array, voiced_probs: confidence
        f0, voiced_flag, voiced_probs = librosa.pyin(
            audio_buffer,
            fmin=self.fmin,
            fmax=self.fmax,
            sr=self.sr,
            frame_length=self.frame_length
        )

        # We take the median of detected pitches in this window for stability
        valid_pitches = f0[voiced_flag]
        valid_probs = voiced_probs[voiced_flag]

        if len(valid_pitches) > 0:
            pitch = float(np.median(valid_pitches))
            confidence = float(np.mean(valid_probs))
            return pitch, confidence
            
        return None, 0.0
