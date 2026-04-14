import numpy as np
import librosa
from typing import List, Tuple, Optional
from models.vocal_range import VocalRange
from models.key_recommendation import KeyRecommendation

class KeyAdvisor:
    """
    Recommends optimal song transpositions based on a singer's vocal range.
    Defaults to prioritizing the 'Comfort Zone' (central 70% of range).
    """
    def __init__(self, vocal_range: VocalRange):
        self.vocal_range = vocal_range
        self.v_low_midi = librosa.hz_to_midi(vocal_range.min_freq)
        self.v_high_midi = librosa.hz_to_midi(vocal_range.max_freq)
        
        # Calculate Comfort Zone (central 70% as per default strategy)
        span = self.v_high_midi - self.v_low_midi
        buffer = span * 0.15 # 15% on each side
        self.comfort_low = self.v_low_midi + buffer
        self.comfort_high = self.v_high_midi - buffer

    def find_optimal_key(self, 
                          song_midi_notes: List[int], 
                          strategy: str = "comfort") -> KeyRecommendation:
        """
        Finds the best transposition (in semitones) for a list of MIDI notes.
        """
        if not song_midi_notes:
            return KeyRecommendation(0, 0, 0, 0, "No notes provided")

        song_low = min(song_midi_notes)
        song_high = max(song_midi_notes)
        song_center = (song_low + song_high) / 2
        
        target_center = (self.comfort_low + self.comfort_high) / 2 if strategy == "comfort" \
                        else (self.v_low_midi + self.v_high_midi) / 2
        
        # Calculate ideal shift to center song in range
        ideal_shift = int(round(target_center - song_center))
        
        # Bound the shift to reasonable musical limits (+/- 12 semitones)
        # and verify it fits in the absolute vocal range
        best_shift = ideal_shift
        confidence = 100.0
        warning = None

        new_low = song_low + best_shift
        new_high = song_high + best_shift

        # Check if it fits absolute range
        if new_low < self.v_low_midi:
            warning = "Strongly low for your range"
            confidence -= 20
        if new_high > self.v_high_midi:
            warning = "Exceeds your high range"
            confidence -= 30

        # Calculate comfort scores (0-10)
        # 10 means inside comfort zone, decreasing as it approaches limits
        low_score = 10.0 if new_low >= self.comfort_low else \
                    max(0, 10 * (new_low - self.v_low_midi) / (self.comfort_low - self.v_low_midi))
        
        high_score = 10.0 if new_high <= self.comfort_high else \
                     max(0, 10 * (self.v_high_midi - new_high) / (self.v_high_midi - self.comfort_high))

        return KeyRecommendation(
            semitone_shift=best_shift,
            confidence_score=max(0, confidence),
            comfort_low=float(low_score),
            comfort_high=float(high_score),
            warning=warning
        )
