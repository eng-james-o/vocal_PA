from dataclasses import dataclass
from typing import Optional

@dataclass
class SolfaResult:
    """
    Represents a pitch relative to a user-defined tonic (DOH).
    """
    syllable: str             # "Do", "Re", "Mi", etc.
    octave: int               # Octave relative to the tonic
    cents_deviation: float    # Pitch error in cents (-50 to +50)
    chromatic_variant: Optional[str] = None  # e.g., "Di" for sharped Do
