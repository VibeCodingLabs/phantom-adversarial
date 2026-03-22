"""Unit tests for evaluation pipeline."""
import pytest
from src.evaluator.metrics import (
    compute_asr,
    compute_self_bleu,
    compute_diversity_score,
)


class TestMetrics:
    """Test evaluation metrics."""

    def test_asr_all_success(self):
        results = [{"success": True}] * 10
        asr = compute_asr(results)
        assert asr == 1.0

    def test_asr_none_success(self):
        results = [{"success": False}] * 10
        asr = compute_asr(results)
        assert asr == 0.0

    def test_asr_mixed(self):
        results = [{"success": True}] * 3 + [{"success": False}] * 7
        asr = compute_asr(results)
        assert abs(asr - 0.3) < 0.01

    def test_asr_empty(self):
        asr = compute_asr([])
        assert asr == 0.0

    def test_diversity_score_identical(self):
        prompts = ["same prompt"] * 5
        score = compute_diversity_score(prompts)
        assert score < 0.2  # Low diversity for identical prompts

    def test_diversity_score_diverse(self):
        prompts = [
            "The quick brown fox jumps over the lazy dog",
            "A completely different sentence about AI safety",
            "Security testing requires rigorous methodology",
            "Adversarial prompts exploit model weaknesses",
            "Machine learning models need robust evaluation",
        ]
        score = compute_diversity_score(prompts)
        assert score > 0.5  # High diversity for different prompts
