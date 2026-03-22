"""Evaluator — multi-tier jailbreak evaluation pipeline."""

from src.evaluator.embedding_eval import EmbeddingEvaluator, JailbreakMLP
from src.evaluator.judge import JudgeEvaluator
from src.evaluator.metrics import (
    attack_success_rate,
    asr_at_k,
    cell_coverage,
    composite_reward,
    efficiency_ratio,
    embedding_diversity,
    iterations_to_success,
    novelty_score,
    self_bleu,
    self_bleu_diversity,
    shannon_evenness,
    simpsons_diversity,
)

__all__ = [
    "EmbeddingEvaluator",
    "JailbreakMLP",
    "JudgeEvaluator",
    "attack_success_rate",
    "asr_at_k",
    "cell_coverage",
    "composite_reward",
    "efficiency_ratio",
    "embedding_diversity",
    "iterations_to_success",
    "novelty_score",
    "self_bleu",
    "self_bleu_diversity",
    "shannon_evenness",
    "simpsons_diversity",
]
