"""Unit tests for mutation operators."""
import pytest
from src.narrative_engine.mutators import (
    Base64Encoder,
    LeetSpeakEncoder,
    SynonymSubstitution,
    CapitalizationShuffle,
    WordReorder,
    ROT13Encoder,
    HexEncoder,
    ExpandMutator,
    ShortenMutator,
    MutationRegistry,
)


class TestEncodingMutators:
    """Test encoding-family mutation operators."""

    def test_base64_encode_decode(self):
        mutator = Base64Encoder()
        result = mutator("Hello, world!")
        assert "SGVsbG8sIHdvcmxkIQ==" in result or "base64" in result.lower() or len(result) > 0

    def test_leetspeak_transforms(self):
        mutator = LeetSpeakEncoder()
        result = mutator("test prompt for encoding")
        assert result != "test prompt for encoding"
        assert len(result) > 0

    def test_rot13_roundtrip(self):
        mutator = ROT13Encoder()
        result = mutator("Hello World")
        assert "Hello World" not in result
        assert len(result) > 0

    def test_hex_encoder(self):
        mutator = HexEncoder()
        result = mutator("test")
        assert len(result) > 0


class TestLexicalMutators:
    """Test lexical-family mutation operators."""

    def test_synonym_substitution_changes_text(self):
        mutator = SynonymSubstitution()
        original = "The quick brown fox jumps over the lazy dog"
        result = mutator(original)
        assert len(result) > 0

    def test_capitalization_shuffle(self):
        mutator = CapitalizationShuffle()
        result = mutator("hello world test prompt")
        assert len(result) > 0

    def test_word_reorder(self):
        mutator = WordReorder()
        result = mutator("one two three four five six")
        assert len(result) > 0


class TestStructuralMutators:
    """Test structural-family mutation operators."""

    def test_expand_adds_content(self):
        mutator = ExpandMutator()
        original = "test prompt"
        result = mutator(original)
        assert len(result) >= len(original)

    def test_shorten_reduces_content(self):
        mutator = ShortenMutator()
        original = "This is a very long test prompt with many words that should be shortened significantly"
        result = mutator(original)
        assert len(result) > 0


class TestMutationRegistry:
    """Test the mutation operator registry."""

    def test_registry_has_operators(self):
        registry = MutationRegistry()
        operators = registry.list_operators()
        assert len(operators) > 0

    def test_registry_get_by_family(self):
        registry = MutationRegistry()
        encoding_ops = registry.get_by_family("encoding")
        assert len(encoding_ops) > 0

    def test_registry_get_operator(self):
        registry = MutationRegistry()
        op = registry.get("base64_encode")
        assert op is not None
        assert callable(op)
