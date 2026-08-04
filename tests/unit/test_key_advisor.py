"""
Unit tests for KeyAdvisor class.
"""
import pytest
from datetime import datetime
from core.key_advisor import KeyAdvisor
from models.vocal_range import VocalRange
from models.key_recommendation import KeyRecommendation


@pytest.fixture
def vocal_range():
    """Fixture providing a sample VocalRange."""
    return VocalRange(
        min_freq=100.0,
        max_freq=1000.0,
        min_note_name="C3",
        max_note_name="C5",
        measured_at=datetime.now(),
        confidence=0.95
    )


@pytest.fixture
def advisor(vocal_range):
    """Fixture providing a KeyAdvisor instance."""
    return KeyAdvisor(vocal_range)


class TestKeyAdvisorInitialization:
    """Tests for KeyAdvisor initialization."""

    def test_initialization_with_vocal_range(self, vocal_range):
        """KeyAdvisor should initialize with vocal range."""
        advisor = KeyAdvisor(vocal_range)
        
        assert advisor.vocal_range == vocal_range
        assert advisor.v_low_midi is not None
        assert advisor.v_high_midi is not None
        assert advisor.comfort_low is not None
        assert advisor.comfort_high is not None

    def test_comfort_zone_calculation(self, advisor):
        """KeyAdvisor should calculate comfort zone correctly."""
        # Comfort zone is central 70% of range
        span = advisor.v_high_midi - advisor.v_low_midi
        expected_buffer = span * 0.15
        
        assert abs(advisor.comfort_low - (advisor.v_low_midi + expected_buffer)) < 0.01
        assert abs(advisor.comfort_high - (advisor.v_high_midi - expected_buffer)) < 0.01


class TestFindOptimalKey:
    """Tests for finding optimal key."""

    def test_find_optimal_key_empty_song(self, advisor):
        """KeyAdvisor should handle empty song note list."""
        result = advisor.find_optimal_key([])
        
        assert isinstance(result, KeyRecommendation)
        assert result.semitone_shift == 0
        assert result.confidence_score == 0

    def test_find_optimal_key_single_note(self, advisor):
        """KeyAdvisor should handle single note song."""
        song_notes = [60]  # C4
        result = advisor.find_optimal_key(song_notes)
        
        assert isinstance(result, KeyRecommendation)
        # The shift will depend on where C4 falls in the vocal range
        # Just check it returns a valid recommendation
        assert result.confidence_score >= 0

    def test_find_optimal_key_within_range(self, advisor):
        """KeyAdvisor should find optimal key for song within range."""
        # Song notes that fit within the vocal range
        song_notes = [60, 64, 67, 72]  # C4, E4, G4, C5
        result = advisor.find_optimal_key(song_notes)
        
        assert isinstance(result, KeyRecommendation)
        assert result.confidence_score > 0

    def test_find_optimal_key_comfort_strategy(self, advisor):
        """KeyAdvisor should use comfort strategy by default."""
        song_notes = [60, 64, 67, 72]
        result = advisor.find_optimal_key(song_notes, strategy="comfort")
        
        assert isinstance(result, KeyRecommendation)

    def test_find_optimal_key_high_strategy(self, advisor):
        """KeyAdvisor should support high strategy."""
        song_notes = [60, 64, 67, 72]
        result = advisor.find_optimal_key(song_notes, strategy="high")
        
        assert isinstance(result, KeyRecommendation)

    def test_find_optimal_key_low_strategy(self, advisor):
        """KeyAdvisor should support low strategy."""
        song_notes = [60, 64, 67, 72]
        result = advisor.find_optimal_key(song_notes, strategy="low")
        
        assert isinstance(result, KeyRecommendation)


class TestKeyRecommendationProperties:
    """Tests for KeyRecommendation properties."""

    def test_recommendation_has_all_fields(self, advisor):
        """KeyRecommendation should have all required fields."""
        song_notes = [60, 64, 67, 72]
        result = advisor.find_optimal_key(song_notes)
        
        assert hasattr(result, 'semitone_shift')
        assert hasattr(result, 'confidence_score')
        assert hasattr(result, 'comfort_low')
        assert hasattr(result, 'comfort_high')
        assert hasattr(result, 'warning')

    def test_confidence_score_range(self, advisor):
        """Confidence score should be between 0 and 100."""
        song_notes = [60, 64, 67, 72]
        result = advisor.find_optimal_key(song_notes)
        
        assert 0 <= result.confidence_score <= 100

    def test_comfort_scores_range(self, advisor):
        """Comfort scores should be between 0 and 10."""
        song_notes = [60, 64, 67, 72]
        result = advisor.find_optimal_key(song_notes)
        
        assert 0 <= result.comfort_low <= 10
        assert 0 <= result.comfort_high <= 10


class TestEdgeCases:
    """Tests for edge cases in KeyAdvisor."""

    def test_song_outside_range(self, advisor):
        """KeyAdvisor should handle song outside vocal range."""
        # Song notes way above vocal range
        song_notes = [100, 104, 107]  # Very high notes
        result = advisor.find_optimal_key(song_notes)
        
        assert isinstance(result, KeyRecommendation)
        # The advisor will try to shift it down, so check it returns something valid
        assert result.confidence_score >= 0

    def test_song_way_below_range(self, advisor):
        """KeyAdvisor should handle song way below vocal range."""
        # Song notes way below vocal range
        song_notes = [20, 24, 27]  # Very low notes
        result = advisor.find_optimal_key(song_notes)
        
        assert isinstance(result, KeyRecommendation)
        # The advisor will try to shift it up, so check it returns something valid
        assert result.confidence_score >= 0

    def test_very_wide_song_range(self, advisor):
        """KeyAdvisor should handle very wide song range."""
        # Song with very wide range (more than 2 octaves)
        song_notes = [48, 50, 52, 55, 57, 60, 64, 67, 72, 76, 79, 84]
        result = advisor.find_optimal_key(song_notes)
        
        assert isinstance(result, KeyRecommendation)

    def test_single_octave_song(self, advisor):
        """KeyAdvisor should handle single octave song."""
        # Song within single octave
        song_notes = [60, 62, 64, 65, 67, 69, 71]
        result = advisor.find_optimal_key(song_notes)
        
        assert isinstance(result, KeyRecommendation)
        assert result.confidence_score > 50
