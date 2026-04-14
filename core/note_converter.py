import librosa
import numpy as np
from typing import Optional
from models.solfa_result import SolfaResult
from utils.constants import REFERENCE_A4_FREQ, SOLFA_MAP

class NoteConverter:
    """
    Handles conversion between frequency (Hz), MIDI, and Solfa notation.
    """
    def __init__(self, reference_pitch: float = REFERENCE_A4_FREQ):
        self.reference_pitch = reference_pitch
        self.doh_freq: Optional[float] = None
        self.doh_midi: Optional[float] = None

    def set_tonic(self, frequency: float) -> None:
        """
        Sets the reference frequency for movable-do solfa (DOH).
        """
        self.doh_freq = frequency
        self.doh_midi = librosa.hz_to_midi(frequency)

    def hz_to_midi(self, frequency: float) -> float:
        """Convert Hz to MIDI note number."""
        return float(librosa.hz_to_midi(frequency))

    def midi_to_hz(self, midi_note: float) -> float:
        """Convert MIDI note number to Hz."""
        return float(librosa.midi_to_hz(midi_note))

    def hz_to_note_name(self, frequency: float) -> str:
        """Convert Hz to scientific pitch notation (e.g. 'C4')."""
        return str(librosa.hz_to_note(frequency))

    def hz_to_solfa(self, frequency: float) -> Optional[SolfaResult]:
        """
        Converts frequency to movable-do solfa relative to the set tonic.
        """
        if self.doh_freq is None or self.doh_freq <= 0:
            return None

        # Calculate semitones from DOH
        # semitones = 12 * log2(f / f_doh)
        semitones_float = 12 * np.log2(frequency / self.doh_freq)
        semitones_rounded = int(round(semitones_float))
        
        # Calculate octave displacement and scale degree
        octave = semitones_rounded // 12
        degree = semitones_rounded % 12
        cents_deviation = (semitones_float - semitones_rounded) * 100

        syllable = SOLFA_MAP.get(degree, "Unknown")
        
        # Determine chromatic variant (basic logic)
        variant = None
        if "/" in syllable:
            # Simplified: just split the syllable for now
            # In a real app, we'd choose based on ascending/descending
            parts = syllable.split("/")
            syllable = parts[0]
            variant = parts[1] if len(parts) > 1 else None

        return SolfaResult(
            syllable=syllable,
            octave=octave,
            cents_deviation=float(cents_deviation),
            chromatic_variant=variant
        )
