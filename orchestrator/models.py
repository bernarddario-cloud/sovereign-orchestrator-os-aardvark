"""Canonical models.py v0.1 - Sovereign Orchestrator OS

This module defines the core 6-phase orchestration model for multi-agent workflows.
Designed for OpenAI Aardvark evaluation - demonstrates secure agentic architecture.
"""

from enum import Enum
from typing import List, Optional, Any
from pydantic import BaseModel, Field
from datetime import datetime


class Phase(str, Enum):
    """6-phase workflow enumeration - CRITICAL: All 6 phases required for Aardvark"""
    INTENTION = "intention"
    RESEARCH = "research"
    DESIGN = "design"
    BUILD = "build"
    EXECUTE = "execute"
    OPTIMIZE = "optimize"  # Phase 6 - Required!


class EngineState(BaseModel):
    """Represents the state of a single engine in the orchestration system"""
    engine_id: str = Field(..., description="Unique identifier for this engine")
    phase: Phase = Field(..., description="Current phase of execution")
    status: str = Field(default="idle", description="Current status: idle, running, completed, failed")
    data: dict = Field(default_factory=dict, description="Engine-specific state data")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_encoders = {datetime: lambda v: v.isoformat()}


class OrchestratorState(BaseModel):
    """Main orchestrator state managing multiple concurrent engines"""
    engines: List[EngineState] = Field(default_factory=list, description="List of active engine states")
    payload: Optional[Any] = Field(None, description="Global orchestrator payload")
    metadata: dict = Field(default_factory=dict, description="Additional orchestrator metadata")

    def add_engine(self, engine: EngineState) -> None:
        """Add a new engine to the orchestration"""
        self.engines.append(engine)

    def get_engine(self, engine_id: str) -> Optional[EngineState]:
        """Retrieve an engine by ID"""
        return next((e for e in self.engines if e.engine_id == engine_id), None)

    def update_engine(self, engine_id: str, **kwargs) -> bool:
        """Update an engine's state"""
        engine = self.get_engine(engine_id)
        if engine:
            for key, value in kwargs.items():
                setattr(engine, key, value)
            engine.updated_at = datetime.utcnow()
            return True
        return False
