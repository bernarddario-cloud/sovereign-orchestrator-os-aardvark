"""FastAPI entrypoint for Sovereign Orchestrator OS"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from .models import Phase, EngineState, OrchestratorState

app = FastAPI(
    title="Sovereign Orchestrator OS",
    description="6-phase agentic orchestration system for OpenAI Aardvark",
    version="0.1.0"
)

# Global orchestrator state
orchestrator = OrchestratorState()


class OrchestrateRequest(BaseModel):
    engine_id: str
    phase: Phase
    data: dict = {}


class OrchestrateResponse(BaseModel):
    status: str
    message: str
    next_actions: List[str] = []
    diagnostics: dict = {}


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "service": "aardvark-orchestrator",
        "version": "0.1.0"
    }


@app.post("/orchestrate", response_model=OrchestrateResponse)
async def orchestrate(request: OrchestrateRequest):
    """Main orchestration endpoint"""
    # Create or update engine
    engine = orchestrator.get_engine(request.engine_id)
    if not engine:
        engine = EngineState(
            engine_id=request.engine_id,
            phase=request.phase,
            status="running",
            data=request.data
        )
        orchestrator.add_engine(engine)
    else:
        orchestrator.update_engine(
            request.engine_id,
            phase=request.phase,
            status="running",
            data=request.data
        )
    
    return OrchestrateResponse(
        status="success",
        message="Orchestration complete",
        next_actions=[],
        diagnostics={}
    )


@app.get("/engines")
async def list_engines():
    """List all active engines"""
    return {"engines": orchestrator.engines, "count": len(orchestrator.engines)}
