"""Base agent class for all agents in the workflow."""
import uuid
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any, Dict, Optional
import logging

from src.types import AgentType, TaskStatus, Task, AgentResponse, WorkflowPhase
from src.config import get_config

logger = logging.getLogger(__name__)


class BaseAgent(ABC):
    """Abstract base class for all agents."""
    
    def __init__(
        self,
        agent_id: Optional[str] = None,
        agent_type: Optional[AgentType] = None,
        name: Optional[str] = None,
    ):
        """Initialize the agent.
        
        Args:
            agent_id: Unique identifier for the agent
            agent_type: Type of the agent
            name: Human-readable name for the agent
        """
        self.agent_id = agent_id or str(uuid.uuid4())
        self.agent_type = agent_type
        self.name = name or self.__class__.__name__
        self.config = get_config()
        self.task_history: list[Task] = []
        self.is_active = True
        
    async def initialize(self) -> None:
        """Initialize agent resources. Can be overridden by subclasses."""
        logger.info(f"Initializing agent {self.name} ({self.agent_id})")
    
    async def shutdown(self) -> None:
        """Clean up agent resources. Can be overridden by subclasses."""
        logger.info(f"Shutting down agent {self.name} ({self.agent_id})")
        self.is_active = False
    
    @abstractmethod
    async def execute(self, task: Task) -> AgentResponse:
        """Execute a task. Must be implemented by subclasses.
        
        Args:
            task: The task to execute
            
        Returns:
            AgentResponse with the results of the task
        """
        pass
    
    async def process_task(self, task: Task) -> AgentResponse:
        """Process a task with error handling and logging.
        
        Args:
            task: The task to process
            
        Returns:
            AgentResponse with the results
        """
        try:
            task.status = TaskStatus.IN_PROGRESS
            task.started_at = datetime.utcnow()
            
            logger.info(f"Agent {self.name} processing task {task.task_id}")
            response = await self.execute(task)
            
            task.completed_at = datetime.utcnow()
            self.task_history.append(task)
            
            return response
        except Exception as e:
            logger.error(f"Error processing task {task.task_id}: {str(e)}", exc_info=True)
            return AgentResponse(
                agent_id=self.agent_id,
                agent_type=self.agent_type,
                status=TaskStatus.FAILED,
                error=str(e),
            )
    
    def get_task_history(self) -> list[Task]:
        """Get the task history for this agent.
        
        Returns:
            List of completed tasks
        """
        return self.task_history.copy()
    
    def get_status(self) -> Dict[str, Any]:
        """Get the current status of the agent.
        
        Returns:
            Status dictionary with agent information
        """
        return {
            "agent_id": self.agent_id,
            "agent_type": self.agent_type,
            "name": self.name,
            "is_active": self.is_active,
            "tasks_completed": len(self.task_history),
        }
