"""
Unit tests for VocalRange dataclass.
"""
import pytest
from datetime import datetime
from models.vocal_range import VocalRange


class TestVocalRangeCreation:
    """Tests for VocalRange instantiation."""

    def test_basic_creation(self):
        """VocalRange should be created with required fields."""
        vr = VocalRange(
            min_freq=100.0,
            max_freq=1000.0,
            min_note_name="C3",
            max_note_name="C5",
            measured_at=datetime.now(),
            confidence=0.95
        )
        assert vr is not None
        assert vr.min_freq == 100.0
        assert vr.max_freq == 1000.0
        assert vr.min_note_name == "C3"
        assert vr.max_note_name == "C5"
        assert vr.confidence == 0.95

    def test_creation_with_datetime(self):
        """VocalRange should store the measured_at timestamp."""
        now = datetime.now()
        vr = VocalRange(
            min_freq=100.0,
            max_freq=1000.0,
            min_note_name="C3",
            max_note_name="C5",
            measured_at=now,
            confidence=0.95
        )
        assert vr.measured_at == now


class TestVocalRangeProperties:
    """Tests for VocalRange properties and behavior."""

    def test_range_span(self):
        """VocalRange span should be max_freq - min_freq."""
        vr = VocalRange(
            min_freq=100.0,
            max_freq=1000.0,
            min_note_name="C3",
            max_note_name="C5",
            measured_at=datetime.now(),
            confidence=0.95
        )
        span = vr.max_freq - vr.min_freq
        assert span == 900.0

    def test_confidence_range(self):
        """Confidence should be between 0.0 and 1.0."""
        vr = VocalRange(
            min_freq=100.0,
            max_freq=1000.0,
            min_note_name="C3",
            max_note_name="C5",
            measured_at=datetime.now(),
            confidence=0.95
        )
        assert 0.0 <= vr.confidence <= 1.0

    def test_note_names_format(self):
        """Note names should follow scientific pitch notation."""
        vr = VocalRange(
            min_freq=100.0,
            max_freq=1000.0,
            min_note_name="C3",
            max_note_name="C5",
            measured_at=datetime.now(),
            confidence=0.95
        )
        # Basic validation of note name format
        assert len(vr.min_note_name) >= 2  # e.g., "C3"
        assert len(vr.max_note_name) >= 2


class TestVocalRangeEquality:
    """Tests for VocalRange equality and comparison."""

    def test_equality(self):
        """Two VocalRanges with same values should be equal."""
        now = datetime.now()
        vr1 = VocalRange(
            min_freq=100.0,
            max_freq=1000.0,
            min_note_name="C3",
            max_note_name="C5",
            measured_at=now,
            confidence=0.95
        )
        vr2 = VocalRange(
            min_freq=100.0,
            max_freq=1000.0,
            min_note_name="C3",
            max_note_name="C5",
            measured_at=now,
            confidence=0.95
        )
        assert vr1 == vr2

    def test_inequality_different_freq(self):
        """VocalRanges with different frequencies should not be equal."""
        now = datetime.now()
        vr1 = VocalRange(
            min_freq=100.0,
            max_freq=1000.0,
            min_note_name="C3",
            max_note_name="C5",
            measured_at=now,
            confidence=0.95
        )
        vr2 = VocalRange(
            min_freq=110.0,  # Different
            max_freq=1000.0,
            min_note_name="C3",
            max_note_name="C5",
            measured_at=now,
            confidence=0.95
        )
        assert vr1 != vr2


class TestVocalRangeRepresentation:
    """Tests for VocalRange string representation."""

    def test_repr(self):
        """VocalRange should have a useful repr."""
        now = datetime.now()
        vr = VocalRange(
            min_freq=100.0,
            max_freq=1000.0,
            min_note_name="C3",
            max_note_name="C5",
            measured_at=now,
            confidence=0.95
        )
        repr_str = repr(vr)
        assert "VocalRange" in repr_str
        assert "min_freq" in repr_str
        assert "max_freq" in repr_str

    def test_str(self):
        """VocalRange should have a useful str."""
        now = datetime.now()
        vr = VocalRange(
            min_freq=100.0,
            max_freq=1000.0,
            min_note_name="C3",
            max_note_name="C5",
            measured_at=now,
            confidence=0.95
        )
        str_str = str(vr)
        assert "VocalRange" in str_str or "min_freq" in str_str


class TestVocalRangeEdgeCases:
    """Tests for edge cases in VocalRange."""

    def test_zero_confidence(self):
        """VocalRange with 0 confidence should be valid."""
        vr = VocalRange(
            min_freq=100.0,
            max_freq=1000.0,
            min_note_name="C3",
            max_note_name="C5",
            measured_at=datetime.now(),
            confidence=0.0
        )
        assert vr.confidence == 0.0

    def test_full_confidence(self):
        """VocalRange with 1.0 confidence should be valid."""
        vr = VocalRange(
            min_freq=100.0,
            max_freq=1000.0,
            min_note_name="C3",
            max_note_name="C5",
            measured_at=datetime.now(),
            confidence=1.0
        )
        assert vr.confidence == 1.0

    def test_same_min_max(self):
        """VocalRange with same min and max should be valid."""
        vr = VocalRange(
            min_freq=440.0,
            max_freq=440.0,
            min_note_name="A4",
            max_note_name="A4",
            measured_at=datetime.now(),
            confidence=0.95
        )
        assert vr.min_freq == vr.max_freq

    def test_very_wide_range(self):
        """VocalRange with very wide range should be valid."""
        vr = VocalRange(
            min_freq=20.0,
            max_freq=20000.0,
            min_note_name="C0",
            max_note_name="C8",
            measured_at=datetime.now(),
            confidence=0.95
        )
        assert vr.max_freq - vr.min_freq == 19980.0
