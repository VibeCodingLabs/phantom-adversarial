"""Unit tests for the narrative engine generator."""
import pytest


class TestGeneratorConfig:
    """Test generator configuration."""

    def test_import(self):
        from src.narrative_engine.generator import NarrativeEngine
        assert NarrativeEngine is not None
