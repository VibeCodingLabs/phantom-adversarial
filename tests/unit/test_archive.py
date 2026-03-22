"""Unit tests for QD archive."""
import pytest
from src.archive.qd_archive import QDArchive, PromptCandidate, BehavioralDescriptor


class TestBehavioralDescriptor:
    """Test behavioral descriptor computation."""

    def test_descriptor_creation(self):
        desc = BehavioralDescriptor(
            risk_category="jailbreak",
            style="narrative",
            technique="persona_injection",
            evasion="none",
            length_bucket="medium",
            model_family="general",
        )
        assert desc.risk_category == "jailbreak"
        assert desc.cell_key() is not None

    def test_cell_key_uniqueness(self):
        desc1 = BehavioralDescriptor(
            risk_category="jailbreak", style="narrative",
            technique="persona_injection", evasion="none",
            length_bucket="medium", model_family="general",
        )
        desc2 = BehavioralDescriptor(
            risk_category="extraction", style="direct",
            technique="persona_injection", evasion="base64",
            length_bucket="short", model_family="openai",
        )
        assert desc1.cell_key() != desc2.cell_key()


class TestQDArchive:
    """Test MAP-Elites QD archive operations."""

    def test_archive_creation(self):
        archive = QDArchive(k=5)
        assert archive is not None
        stats = archive.get_statistics()
        assert stats["total_prompts"] == 0

    def test_add_and_retrieve(self):
        archive = QDArchive(k=5)
        candidate = PromptCandidate(
            prompt="Test adversarial prompt",
            quality=0.85,
            descriptor=BehavioralDescriptor(
                risk_category="jailbreak", style="narrative",
                technique="persona_injection", evasion="none",
                length_bucket="medium", model_family="general",
            ),
            metadata={"intent": "jailbreak", "source": "test"},
        )
        archive.add(candidate)
        stats = archive.get_statistics()
        assert stats["total_prompts"] == 1

    def test_sample_returns_candidate(self):
        archive = QDArchive(k=5)
        candidate = PromptCandidate(
            prompt="Test prompt",
            quality=0.9,
            descriptor=BehavioralDescriptor(
                risk_category="jailbreak", style="narrative",
                technique="persona_injection", evasion="none",
                length_bucket="medium", model_family="general",
            ),
            metadata={},
        )
        archive.add(candidate)
        sampled = archive.sample(strategy="quality")
        assert sampled is not None
        assert sampled.prompt == "Test prompt"
