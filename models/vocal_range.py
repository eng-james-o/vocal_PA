from dataclasses import dataclass
from datetime import datetime

@dataclass
class VocalRange:
    """
    Tracks the statistical boundaries of a singer's voice.
    """
    min_freq: float           # Hz
    max_freq: float           # Hz
    min_note_name: str        # e.g., "C3"
    max_note_name: str        # e.g., "G4"
    measured_at: datetime
    confidence: float         # 0.0 - 1.0 based on sample quality
