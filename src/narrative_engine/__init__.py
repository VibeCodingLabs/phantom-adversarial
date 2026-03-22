"""Narrative Engine — adversarial prompt generation core."""

from src.narrative_engine.generator import NarrativeEngine, QLearningSelector
from src.narrative_engine.mutators import (
    MUTATION_PRIORITY,
    Q_PRIORS,
    BaseMutator,
    LLMMutator,
    build_mutator_registry,
)
from src.narrative_engine.strategies import PAIRRefinementLoop, StrategyLibrary

__all__ = [
    "NarrativeEngine",
    "QLearningSelector",
    "BaseMutator",
    "LLMMutator",
    "build_mutator_registry",
    "MUTATION_PRIORITY",
    "Q_PRIORS",
    "PAIRRefinementLoop",
    "StrategyLibrary",
]
