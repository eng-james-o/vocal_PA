"""
Unit tests for RangeTracker class.
"""
import pytest
from datetime import datetime
from core.range_tracker import RangeTracker
from models.vocal_range import VocalRange


@pytest.fixture
def tracker():
    """Fixture providing a RangeTracker instance."""
    return RangeTracker()


class TestRangeTrackerInitialization:
    """Tests for RangeTracker initialization."""

    def test_default_initialization(self):
        """RangeTracker should initialize with default values."""
        tracker = RangeTracker()
        assert tracker.confidence_threshold == 0.8
        assert tracker.min_duration_ms == 200
        assert tracker.history == []
        assert tracker.min_freq == float('inf')
        assert tracker.max_freq == 0.0

    def test_custom_initialization(self):
        """RangeTracker should accept custom parameters."""
        tracker = RangeTracker(
            confidence_threshold=0.9,
            min_duration_ms=300
        )
        assert tracker.confidence_threshold == 0.9
        assert tracker.min_duration_ms == 300


class TestAddSample:
    """Tests for adding samples to RangeTracker."""

    def test_add_valid_sample(self, tracker):
        """RangeTracker should add valid samples."""
        tracker.add_sample(440.0, 0.95)
        
        assert len(tracker.history) == 1
        assert tracker.history[0]['freq'] == 440.0
        assert tracker.history[0]['conf'] == 0.95

    def test_add_multiple_samples(self, tracker):
        """RangeTracker should add multiple samples."""
        tracker.add_sample(440.0, 0.95)
        tracker.add_sample(550.0, 0.90)
        tracker.add_sample(660.0, 0.85)
        
        assert len(tracker.history) == 3

    def test_ignore_low_confidence(self, tracker):
        """RangeTracker should ignore samples below confidence threshold."""
        tracker.add_sample(440.0, 0.7)  # Below threshold of 0.8
        
        assert len(tracker.history) == 0

    def test_ignore_zero_frequency(self, tracker):
        """RangeTracker should ignore zero frequency."""
        tracker.add_sample(0.0, 0.95)
        
        assert len(tracker.history) == 0

    def test_ignore_negative_frequency(self, tracker):
        """RangeTracker should ignore negative frequency."""
        tracker.add_sample(-100.0, 0.95)
        
        assert len(tracker.history) == 0

    def test_ignore_none_frequency(self, tracker):
        """RangeTracker should ignore None frequency."""
        tracker.add_sample(None, 0.95)
        
        assert len(tracker.history) == 0

    def test_update_min_max(self, tracker):
        """RangeTracker should update min and max frequencies."""
        tracker.add_sample(440.0, 0.95)
        tracker.add_sample(550.0, 0.95)
        tracker.add_sample(330.0, 0.95)
        
        assert tracker.min_freq == 330.0
        assert tracker.max_freq == 550.0


class TestGetRange:
    """Tests for getting vocal range from RangeTracker."""

    def test_get_range_empty(self, tracker):
        """RangeTracker should return None for empty history."""
        result = tracker.get_range()
        
        assert result is None

    def test_get_range_single_sample(self, tracker):
        """RangeTracker should return range for single sample."""
        tracker.add_sample(440.0, 0.95)
        
        result = tracker.get_range()
        
        assert result is not None
        assert isinstance(result, VocalRange)
        assert result.min_freq == 440.0
        assert result.max_freq == 440.0

    def test_get_range_multiple_samples(self, tracker):
        """RangeTracker should return correct range for multiple samples."""
        tracker.add_sample(440.0, 0.95)
        tracker.add_sample(550.0, 0.95)
        tracker.add_sample(330.0, 0.95)
        
        result = tracker.get_range()
        
        assert result is not None
        assert result.min_freq == 330.0
        assert result.max_freq == 550.0

    def test_get_range_with_filtering(self, tracker):
        """RangeTracker should filter outliers when requested."""
        # Add many samples with some outliers
        for i in range(50):
            tracker.add_sample(440.0 + i, 0.95)
        # Add outliers
        tracker.add_sample(100.0, 0.95)  # Low outlier
        tracker.add_sample(1000.0, 0.95)  # High outlier
        
        result = tracker.get_range(filter_outliers=True)
        
        assert result is not None
        # With filtering, outliers should be excluded
        assert result.min_freq > 100.0
        assert result.max_freq < 1000.0

    def test_get_range_without_filtering(self, tracker):
        """RangeTracker should include all samples when filtering disabled."""
        tracker.add_sample(440.0, 0.95)
        tracker.add_sample(100.0, 0.95)  # Low outlier
        tracker.add_sample(1000.0, 0.95)  # High outlier
        
        result = tracker.get_range(filter_outliers=False)
        
        assert result is not None
        assert result.min_freq == 100.0
        assert result.max_freq == 1000.0


class TestReset:
    """Tests for resetting RangeTracker."""

    def test_reset_clears_history(self, tracker):
        """RangeTracker reset should clear history."""
        tracker.add_sample(440.0, 0.95)
        tracker.add_sample(550.0, 0.95)
        
        tracker.reset()
        
        assert len(tracker.history) == 0
        assert tracker.min_freq == float('inf')
        assert tracker.max_freq == 0.0

    def test_reset_allows_new_samples(self, tracker):
        """RangeTracker should allow new samples after reset."""
        tracker.add_sample(440.0, 0.95)
        tracker.reset()
        tracker.add_sample(550.0, 0.95)
        
        assert len(tracker.history) == 1
        assert tracker.history[0]['freq'] == 550.0


class TestEdgeCases:
    """Tests for edge cases in RangeTracker."""

    def test_very_large_history(self, tracker):
        """RangeTracker should handle large history."""
        for i in range(1000):
            tracker.add_sample(440.0 + i % 100, 0.95)
        
        result = tracker.get_range()
        
        assert result is not None
        assert len(tracker.history) == 1000

    def test_all_same_frequency(self, tracker):
        """RangeTracker should handle all samples at same frequency."""
        for i in range(10):
            tracker.add_sample(440.0, 0.95)
        
        result = tracker.get_range()
        
        assert result is not None
        assert result.min_freq == 440.0
        assert result.max_freq == 440.0

    def test_decreasing_frequencies(self, tracker):
        """RangeTracker should handle decreasing frequencies."""
        for freq in [550.0, 440.0, 330.0, 220.0]:
            tracker.add_sample(freq, 0.95)
        
        result = tracker.get_range()
        
        assert result is not None
        assert result.min_freq == 220.0
        assert result.max_freq == 550.0
