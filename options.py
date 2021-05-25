from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
from omegaconf import MISSING
from hydra.core.config_store import ConfigStore

def defaulter(mut):
    return field(default_factory=lambda: mut)

@dataclass
class ExperimentConfig:
    name: str = "test"
    data_root: str = "../../../datasets"
    
    trainer_args: Any = defaulter({'max_epochs': 30, 'profiler': None})
    dataset: Any = defaulter({})
    optimizer: str = 'Adam'
    optimizer_args: Any = defaulter({'lr': 0.001})
    scheduler: Optional[str] = 'ExponentialLR'
    scheduler_args: Any = defaulter({})

    system: str = "CandidateFreeTE"
    base_model: str = 'bert-base-uncased'
    type_embedding_max: int = 7
    max_tokens_lemma: int = 5
    top_k: int = 10

    model_type: str = 'kbert'  # kbertgat/kbert
    gat_n_heads: int = 4
    gat_hidden_size: int = 128
    bert_encoder: bool = True

@dataclass
class Config:
    defaults: List[Any] = defaulter([{'experiment': 'basic'}])
    experiment: ExperimentConfig = ExperimentConfig()

cs = ConfigStore.instance()
cs.store(name="config", node=Config)
cs.store(group="experiment", name="basic", node=ExperimentConfig)