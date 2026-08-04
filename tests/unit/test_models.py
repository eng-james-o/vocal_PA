"""
Unit tests for data models.
"""
import pytest
from datetime import datetime
from models.vocal_range import VocalRange
from models.solfa_result import SolfaResult
from models.key_recommendation import KeyRecommendation


class TestSolfaResult:
    """Tests for SolfaResult dataclass."""

    def test_creation(self):
        """SolfaResult should be created with all fields."""
        result = SolfaResult(
            syllable="Do",
            octave=0,
            cents_deviation=0.0,
            chromatic_variant=None
        )
        
        assert result.syllable == "Do"
        assert result.octave == 0
        assert result.cents_deviation == 0.0
        assert result.chromatic_variant is None

    def test_creation_with_variant(self):
        """SolfaResult should be created with chromatic variant."""
        result = SolfaResult(
            syllable="Do",
            octave=1,
            cents_deviation=25.0,
            chromatic_variant="Di"
        )
        
        assert result.syllable == "Do"
        assert result.octave == 1
        assert result.cents_deviation == 25.0
        assert result.chromatic_variant == "Di"

    def test_equality(self):
        """Two SolfaResults with same values should be equal."""
        result1 = SolfaResult("Do", 0, 0.0, None)
        result2 = SolfaResult("Do", 0, 0.0, None)
        
        assert result1 == result2

    def test_inequality(self):
        """Two SolfaResults with different values should not be equal."""
        result1 = SolfaResult("Do", 0, 0.0, None)
        result2 = SolfaResult("Re", 0, 0.0, None)
        
        assert result1 != result2


class TestKeyRecommendation:
    """Tests for KeyRecommendation dataclass."""

    def test_creation(self):
        """KeyRecommendation should be created with all fields."""
        rec = KeyRecommendation(
            semitone_shift=2,
            confidence_score=95.0,
            comfort_low=8.0,
            comfort_high=9.0,
            warning=None
        )
        
        assert rec.semitone_shift == 2
        assert rec.confidence_score == 95.0
        assert rec.comfort_low == 8.0
        assert rec.comfort_high == 9.0
        assert rec.warning is None

    def test_creation_with_warning(self):
        """KeyRecommendation should be created with warning."""
        rec = KeyRecommendation(
            semitone_shift=-1,
            confidence_score=75.0,
            comfort_low=5.0,
            comfort_high=6.0,
            warning="Exceeds your high range"
        )
        
        assert rec.semitone_shift == -1
        assert rec.warning == "Exceeds your high range"

    def test_creation_minimal(self):
        """KeyRecommendation should be created with minimal fields."""
        rec = KeyRecommendation(
            semitone_shift=0,
            confidence_score=0.0,
            comfort_low=0.0,
            comfort_high=0.0
        )
        
        assert rec.semitone_shift == 0
        assert rec.confidence_score == 0.0
        assert rec.warning is None

    def test_equality(self):
        """Two KeyRecommendations with same values should be equal."""
        rec1 = KeyRecommendation(2, 95.0, 8.0, 9.0, None)
        rec2 = KeyRecommendation(2, 95.0, 8.0, 9.0, None)
        
        assert rec1 == rec2


class TestVocalRange:
    """Tests for VocalRange dataclass."""

    def test_creation(self):
        """VocalRange should be created with all fields."""
        now = datetime.now()
        v_range = VocalRange(
            min_freq=100.0,
            max_freq=1000.0,
            min_note_name="C3",
            max_note_name="C5",
            measured_at=now,
            confidence=0.95
        )
        
        assert v_range.min_freq == 100.0
        assert v_range.max_freq == 1000.0
        assert v_range.min_note_name == "C3"
        assert v_range.max_note_name == "C5"
        assert v_range.measured_at == now
        assert v_range.confidence == 0.95

    def test_span(self):
        """VocalRange span should be max_freq - min_freq."""
        v_range = VocalRange(
            min_freq=100.0,
            max_freq=1000.0,
            min_note_name="C3",
            max_note_name="C5",
            measured_at=datetime.now(),
            confidence=0.95
        )
        
        span = v_range.max_freq - v_range.min_freq
        assert span == 900.0

    def test_equality(self):
        """Two VocalRanges with same values should be equal."""
        now = datetime.now()
        v_range1 = VocalRange(100.0, 1000.0, "C3", "C5", now, 0.95)
        v_range2 = VocalRange(100.0, 1000.0, "C3", "C5", now, 0.95)
        
        assert v_range1 == v_range2

    def test_inequality(self):
        """Two VocalRanges with different values should not be equal."""
        now = datetime.now()
        v_range1 = VocalRange(100.0, 1000.0, "C3", "C5", now, 0.95)
        v_range2 = VocalRange(110.0, 1000.0, "C3", "C5", now, 0.95)
        
        assert v_range1 != v_range2

    def test_confidence_range(self):
        """Confidence should be between 0.0 and 1.0."""
        v_range = VocalRange(
            min_freq=100.0,
            max_freq=1000.0,
            min_note_name="C3",
            max_note_name="C5",
            measured_at=datetime.now(),
            confidence=0.95
        )
        
        assert 0.0 <= v_range.confidence <= 1.0

    def test_repr(self):
        """VocalRange should have a useful repr."""
        now = datetime.now()
        v_range = VocalRange(
            min_freq=100.0,
            max_freq=1000.0,
            min_note_name="C3",
            max_note_name="C5",
            measured_at=now,
            confidence=0.95
        )
        
        repr_str = repr(v_range)
        assert "VocalRange" in repr_str
        assert "min_freq" in repr_str
        assert "max_freq" in repr_str
