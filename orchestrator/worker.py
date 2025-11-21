"""Worker module for task execution in Sovereign Orchestrator OS"""

from typing import Dict, Any


def run_task(task: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
    """Execute a task and return the result.
    
    Args:
        task: Task description or identifier
        context: Optional context data for task execution
        
    Returns:
        Dictionary containing task result and status
    """
    if context is None:
        context = {}
    
    # Minimal task execution logic
    return {
        "task": task,
        "status": "executed",
        "result": f"Task '{task}' completed successfully",
        "context": context
    }


def validate_task(task: str) -> bool:
    """Validate that a task is properly formatted."""
    return isinstance(task, str) and len(task) > 0
