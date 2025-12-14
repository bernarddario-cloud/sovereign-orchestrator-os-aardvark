"""FastAPI entrypoint for Sovereign Orchestrator OS"""

from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from .models import Phase, EngineState, OrchestratorState
from .intent_engine import classify_intent, OS_NAME, OS_VERSION

app = FastAPI(
    title="Sovereign Orchestrator OS",
    description="6-phase agentic orchestration system for OpenAI Aardvark",
    version="1.5"
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

class IntentRequest(BaseModel):
    goal: str

@app.get("/health")
async def health():
    return {
        "status": "ok",
        "service": "aardvark-orchestrator",
        "version": "1.5"
    }

@app.get("/sovereign/status")
async def sovereign_status():
    """Main status endpoint - The heartbeat of Sovereign OS"""
    return {
        "os": OS_NAME,
        "version": OS_VERSION,
        "diamond_system": "active",
        "engines": {
            "intent_engine": "online",
            "memory_agent": "offline",
            "builder_api": "offline",
            "secure_review": "offline"
        },
        "current_mode": "BUILD",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

@app.post("/sovereign/intent")
async def process_intent(request: IntentRequest):
    """Process user intent and route to appropriate agent"""
    result = classify_intent(request.goal)
    return {
        "intent": result["intent"],
        "confidence": result["confidence"],
        "route_to": result["route_to"],
        "accepted": True,
        "goal": request.goal
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
