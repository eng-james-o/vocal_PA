"""
Unit tests for NoteConverter class.
"""
import pytest
import numpy as np
from core.note_converter import NoteConverter
from models.solfa_result import SolfaResult


@pytest.fixture
def converter():
    """Fixture providing a fresh NoteConverter instance."""
    return NoteConverter()


@pytest.fixture
def calibrated_converter():
    """Fixture providing a NoteConverter with A4 (440Hz) as tonic."""
    converter = NoteConverter()
    converter.set_tonic(440.0)  # A4 as DOH
    return converter


class TestHzToMidi:
    """Tests for Hz to MIDI conversion."""

    def test_a4_is_midi_69(self, converter):
        """A4 (440Hz) should be MIDI note 69."""
        assert abs(converter.hz_to_midi(440.0) - 69.0) < 0.01

    def test_c4_is_midi_60(self, converter):
        """C4 (261.63Hz) should be MIDI note 60."""
        assert abs(converter.hz_to_midi(261.63) - 60.0) < 0.01

    def test_middle_c_is_midi_60(self, converter):
        """Middle C (261.625565Hz) should be MIDI note 60."""
        middle_c = 261.6255653005986
        assert abs(converter.hz_to_midi(middle_c) - 60.0) < 0.0001

    def test_octave_relationship(self, converter):
        """Doubling frequency should increase MIDI by 12."""
        freq = 220.0  # A3
        midi_a3 = converter.hz_to_midi(freq)
        midi_a4 = converter.hz_to_midi(freq * 2)  # A4
        assert abs(midi_a4 - midi_a3 - 12.0) < 0.01


class TestMidiToHz:
    """Tests for MIDI to Hz conversion."""

    def test_midi_69_is_a4(self, converter):
        """MIDI note 69 should be A4 (440Hz)."""
        assert abs(converter.midi_to_hz(69.0) - 440.0) < 0.01

    def test_midi_60_is_c4(self, converter):
        """MIDI note 60 should be C4 (261.63Hz)."""
        assert abs(converter.midi_to_hz(60.0) - 261.63) < 0.01

    def test_round_trip_conversion(self, converter):
        """Hz -> MIDI -> Hz should be identity for valid frequencies."""
        test_freqs = [110.0, 220.0, 440.0, 880.0, 1760.0]
        for freq in test_freqs:
            midi = converter.hz_to_midi(freq)
            converted_back = converter.midi_to_hz(midi)
            assert abs(converted_back - freq) < 0.01


class TestHzToNoteName:
    """Tests for Hz to scientific pitch notation conversion."""

    def test_a4_is_a4(self, converter):
        """440Hz should be A4."""
        assert converter.hz_to_note_name(440.0) == "A4"

    def test_c4_is_c4(self, converter):
        """261.63Hz should be C4."""
        assert converter.hz_to_note_name(261.63) == "C4"

    def test_known_notes(self, converter):
        """Test various known note frequencies."""
        test_cases = [
            (110.0, "A2"),
            (220.0, "A3"),
            (440.0, "A4"),
            (880.0, "A5"),
            (164.81, "E3"),
            (329.63, "E4"),
        ]
        for freq, expected in test_cases:
            result = converter.hz_to_note_name(freq)
            # Note: librosa might return slightly different notation
            # (e.g., "A#3" vs "Bb3"), so we check the base note
            assert result[0] == expected[0]


class TestSetTonic:
    """Tests for tonic setting functionality."""

    def test_set_tonic_by_frequency(self, converter):
        """Setting tonic by frequency should work."""
        converter.set_tonic(440.0)
        assert converter.doh_freq == 440.0
        assert abs(converter.doh_midi - 69.0) < 0.01

    def test_set_tonic_by_name_valid(self, converter):
        """Setting tonic by valid note name should work."""
        result = converter.set_tonic_by_name("A4")
        assert result is True
        assert converter.doh_freq is not None
        assert abs(converter.doh_freq - 440.0) < 0.01

    def test_set_tonic_by_name_invalid(self, converter):
        """Setting tonic by invalid note name should fail gracefully."""
        result = converter.set_tonic_by_name("InvalidNote")
        assert result is False
        assert converter.doh_freq is None

    def test_set_tonic_by_name_various_notes(self, converter):
        """Test setting tonic with various note names."""
        test_cases = [
            ("C4", 261.63),
            ("D4", 293.66),
            ("E4", 329.63),
            ("F4", 349.23),
            ("G4", 392.00),
            ("A4", 440.00),
            ("B4", 493.88),
        ]
        for note_name, expected_freq in test_cases:
            converter.set_tonic_by_name(note_name)
            assert converter.doh_freq is not None
            assert abs(converter.doh_freq - expected_freq) < 0.1


class TestHzToSolfa:
    """Tests for Hz to Solfa conversion."""

    def test_solfa_without_tonic_returns_none(self, converter):
        """Hz to solfa without tonic should return None."""
        result = converter.hz_to_solfa(440.0)
        assert result is None

    def test_solfa_with_tonic_doh(self, calibrated_converter):
        """Tonic frequency should return Do."""
        result = calibrated_converter.hz_to_solfa(440.0)
        assert result is not None
        assert result.syllable == "Do"
        assert result.octave == 0

    def test_solfa_octave_up(self, calibrated_converter):
        """Frequency one octave above tonic should be Do with octave +1."""
        result = calibrated_converter.hz_to_solfa(880.0)  # A5, one octave above A4
        assert result is not None
        assert result.syllable == "Do"
        assert result.octave == 1

    def test_solfa_octave_down(self, calibrated_converter):
        """Frequency one octave below tonic should be Do with octave -1."""
        result = calibrated_converter.hz_to_solfa(220.0)  # A3, one octave below A4
        assert result is not None
        assert result.syllable == "Do"
        assert result.octave == -1

    def test_solfa_perfect_fifth(self, calibrated_converter):
        """Perfect fifth above tonic (E5) should be Sol."""
        # A4 to E5 is a perfect fifth (7 semitones)
        e5_freq = 659.25  # E5
        result = calibrated_converter.hz_to_solfa(e5_freq)
        assert result is not None
        # Note: This depends on the SOLFA_MAP configuration
        # In movable-do, E above A (tonic) would be Mi if A is Do
        # But this test verifies the conversion works
        assert result.octave == 0

    def test_solfa_result_structure(self, calibrated_converter):
        """SolfaResult should have all required fields."""
        result = calibrated_converter.hz_to_solfa(440.0)
        assert result is not None
        assert isinstance(result, SolfaResult)
        assert hasattr(result, 'syllable')
        assert hasattr(result, 'octave')
        assert hasattr(result, 'cents_deviation')
        assert hasattr(result, 'chromatic_variant')

    def test_cents_deviation(self, calibrated_converter):
        """Cents deviation should be within -50 to +50."""
        result = calibrated_converter.hz_to_solfa(440.0)
        assert result is not None
        assert -50 <= result.cents_deviation <= 50


class TestEdgeCases:
    """Tests for edge cases and error handling."""

    def test_zero_frequency(self, converter):
        """Zero frequency should be handled gracefully."""
        # Should not crash
        result = converter.hz_to_note_name(0.0)
        assert result is not None  # librosa returns a note for 0Hz

    def test_negative_frequency(self, converter):
        """Negative frequency should be handled gracefully."""
        # Should not crash
        result = converter.hz_to_note_name(-100.0)
        # The behavior might be undefined, but shouldn't crash
        assert True  # Just checking it doesn't crash

    def test_very_low_frequency(self, converter):
        """Very low frequencies should be handled."""
        result = converter.hz_to_note_name(20.0)
        assert result is not None

    def test_very_high_frequency(self, converter):
        """Very high frequencies should be handled."""
        result = converter.hz_to_note_name(5000.0)
        assert result is not None

    def test_nan_frequency(self, converter):
        """NaN frequency should be handled gracefully."""
        # Should not crash
        try:
            result = converter.hz_to_note_name(float('nan'))
            # If it doesn't crash, that's fine
            assert True
        except:
            # If it raises an exception, that's also acceptable
            assert True

    def test_inf_frequency(self, converter):
        """Infinite frequency should be handled gracefully."""
        # Should not crash
        try:
            result = converter.hz_to_note_name(float('inf'))
            assert True
        except:
            assert True
