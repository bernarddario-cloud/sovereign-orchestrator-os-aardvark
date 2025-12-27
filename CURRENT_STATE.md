# CURRENT_STATE.md

Sovereign Orchestrator OS - Current Architecture Snapshot
Generated: December 27, 2025

## 1. Project Overview

• **Purpose**: Multi-agent orchestration system for OpenAI Aardvark evaluation
• **Architecture**: FastAPI-based 6-phase agentic development system
• **Main Components**:
  - Orchestrator (main.py) - Core FastAPI application
  - Intent Engine (intent_engine.py) - Intent classification and routing
  - Engines (engines/) - Modular engine implementations
  - Worker (worker.py) - Background task processor
  - Models (models.py) - Data models and state management

## 2. Intent Engine v1

• **File Location**: `orchestrator/intent_engine.py`
• **Current Intent Labels**:
  - `BUILD` - Create, design, develop, construct (→ MindForgeArchitect)
  - `RESEARCH` - Analyze, investigate, study, explore (→ ResearchAgent)
  - `DOCUMENT` - Write, record, log, note (→ DocumentAgent)
  - `EXECUTE` - Run, perform, do, launch (→ ExecutionEngine)
  - `REVIEW` - Check, validate, verify, audit (→ GPTSecureReviewAgent)
  - `UNKNOWN` - Fallback for unclassified intents

• **Classification Method**: Keyword matching (v1 - naive implementation)
• **Confidence Scores**: 0.75-0.85 for recognized intents, 0.0 for unknown
• **How It's Called**: POST request to `/sovereign/intent` endpoint with `{"goal": "user instruction"}`

## 3. Endpoints

• `/health` - Health check endpoint
  - Returns: `{"status": "ok", "service": "aardvark-orchestrator", "version": "1.5"}`

• `/sovereign/status` - Main status endpoint (heartbeat)
  - Returns: OS name, version, diamond system status, engine states, current mode, timestamp
  - Engines tracked: intent_engine (online), memory_agent, builder_api, secure_review (offline)

• `/sovereign/intent` - Intent classification endpoint
  - Input: `{"goal": string}`
  - Output: `{"intent": string, "confidence": float, "route_to": string, "accepted": bool, "goal": string}`

• `/orchestrate` - Main orchestration endpoint
  - Input: `{"engine_id": string, "phase": Phase, "data": dict}`
  - Output: `{"status": string, "message": string, "next_actions": list, "diagnostics": dict}`

• `/engines` - List all active engines
  - Returns: Engine list and count

## 4. Testing & CI

• **Test Location**: `orchestrator/tests/` (implied from README)
• **Test Command**: `pytest orchestrator/tests/`
• **CI/CD**: No GitHub Actions configured yet (see suggested workflows)
• **Dependencies**: Managed via `requirements.txt`

## 5. Known Issues / Questions

• Intent Engine uses naive keyword matching - ready for optimization with Opik
• No automated testing currently running
• Memory Agent, Builder API, and Secure Review engines show as offline
• No observability/tracing infrastructure yet
• Configuration management needs centralization

## 6. Observability & Optimization Stack

**(To be added with Opik integration)**

• Opik SDK: (pending installation)
• Opik Optimizer: (pending installation)
• Tracing: (pending implementation)
• Datasets: (pending creation)
• Experiment tracking: (pending configuration)
