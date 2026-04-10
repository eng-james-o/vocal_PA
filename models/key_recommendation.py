from dataclasses import dataclass
from typing import Optional

@dataclass
class KeyRecommendation:
    """
    Output from the KeyAdvisor when analyzing a song.
    """
    semitone_shift: int       # Transposition value
    confidence_score: float   # How well the song fits the range (0-100)
    comfort_low: float        # Low-end comfort rating (0-10)
    comfort_high: float       # High-end comfort rating (0-10)
    warning: Optional[str] = None
