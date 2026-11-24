"""Type definitions for the UX design workflow."""
from enum import Enum
from typing import Any, Dict, List, Optional
from datetime import datetime
from pydantic import BaseModel, Field


class AgentType(str, Enum):
    """Enumeration of agent types in the workflow."""
    REQUIREMENTS_ANALYST = "requirements_analyst"
    UX_DESIGNER = "ux_designer"
    PROTOTYPER = "prototyper"
    EVALUATOR = "evaluator"
    ORCHESTRATOR = "orchestrator"


class WorkflowPhase(str, Enum):
    """Enumeration of workflow phases."""
    REQUIREMENTS = "requirements"
    DESIGN = "design"
    PROTOTYPING = "prototyping"
    EVALUATION = "evaluation"
    COMPLETE = "complete"


class TaskStatus(str, Enum):
    """Enumeration of task statuses."""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class Priority(str, Enum):
    """Enumeration of task priorities."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class Message(BaseModel):
    """Message model for inter-agent communication."""
    sender: str = Field(..., description="ID of the sending agent")
    recipient: str = Field(..., description="ID of the receiving agent")
    content: str = Field(..., description="Message content")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata")
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class AgentResponse(BaseModel):
    """Standard response model from agents."""
    agent_id: str = Field(..., description="ID of the agent")
    agent_type: AgentType = Field(..., description="Type of the agent")
    status: TaskStatus = Field(..., description="Status of the task")
    result: Dict[str, Any] = Field(default_factory=dict, description="Result data")
    error: Optional[str] = Field(None, description="Error message if task failed")
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class WorkflowState(BaseModel):
    """State of the entire workflow."""
    workflow_id: str = Field(..., description="Unique workflow identifier")
    phase: WorkflowPhase = Field(default=WorkflowPhase.REQUIREMENTS)
    status: TaskStatus = Field(default=TaskStatus.PENDING)
    requirements: Dict[str, Any] = Field(default_factory=dict)
    design: Dict[str, Any] = Field(default_factory=dict)
    prototype: Dict[str, Any] = Field(default_factory=dict)
    evaluation: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    history: List[AgentResponse] = Field(default_factory=list)


class Task(BaseModel):
    """Task model for agent assignments."""
    task_id: str = Field(..., description="Unique task identifier")
    agent_id: str = Field(..., description="Assigned agent ID")
    agent_type: AgentType = Field(..., description="Type of agent")
    phase: WorkflowPhase = Field(..., description="Workflow phase")
    description: str = Field(..., description="Task description")
    input_data: Dict[str, Any] = Field(default_factory=dict, description="Input data")
    priority: Priority = Field(default=Priority.MEDIUM)
    status: TaskStatus = Field(default=TaskStatus.PENDING)
    result: Optional[Dict[str, Any]] = Field(None)
    error: Optional[str] = Field(None)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    started_at: Optional[datetime] = Field(None)
    completed_at: Optional[datetime] = Field(None)
