"""Requirements Analyst Agent - analyzes user requirements and creates specifications."""
import logging
from typing import Any, Dict

from src.agents.base_agent import BaseAgent
from src.types import AgentType, Task, AgentResponse, TaskStatus

logger = logging.getLogger(__name__)


class RequirementsAnalystAgent(BaseAgent):
    """Agent responsible for analyzing requirements and creating specifications."""
    
    def __init__(self, agent_id: str = None, name: str = "Requirements Analyst"):
        """Initialize the Requirements Analyst Agent."""
        super().__init__(agent_id, AgentType.REQUIREMENTS_ANALYST, name)
    
    async def execute(self, task: Task) -> AgentResponse:
        """Analyze requirements and produce specifications.
        
        Args:
            task: Task containing user requirements
            
        Returns:
            AgentResponse with analyzed requirements
        """
        try:
            # Extract input data
            user_input = task.input_data.get("user_input", "")
            context = task.input_data.get("context", {})
            
            logger.info(f"Analyzing requirements: {user_input[:100]}...")
            
            # Simulate requirement analysis
            requirements_spec = {
                "primary_goal": self._extract_primary_goal(user_input),
                "user_stories": self._extract_user_stories(user_input),
                "functional_requirements": self._extract_functional_requirements(user_input),
                "non_functional_requirements": self._extract_non_functional_requirements(user_input),
                "constraints": self._extract_constraints(user_input),
                "acceptance_criteria": self._generate_acceptance_criteria(user_input),
                "context": context,
            }
            
            return AgentResponse(
                agent_id=self.agent_id,
                agent_type=self.agent_type,
                status=TaskStatus.COMPLETED,
                result={
                    "requirements_specification": requirements_spec,
                    "analysis_confidence": 0.85,
                },
            )
        except Exception as e:
            logger.error(f"Error in requirements analysis: {str(e)}")
            return AgentResponse(
                agent_id=self.agent_id,
                agent_type=self.agent_type,
                status=TaskStatus.FAILED,
                error=str(e),
            )
    
    def _extract_primary_goal(self, user_input: str) -> str:
        """Extract the primary goal from user input."""
        # This would be replaced with LLM-based extraction
        return "Build an intuitive user interface for the application"
    
    def _extract_user_stories(self, user_input: str) -> list[str]:
        """Extract user stories from requirements."""
        # This would be replaced with LLM-based extraction
        return [
            "As a user, I want to easily navigate the interface",
            "As a user, I want quick access to frequently used features",
            "As a user, I want clear feedback for my actions",
        ]
    
    def _extract_functional_requirements(self, user_input: str) -> Dict[str, Any]:
        """Extract functional requirements."""
        return {
            "authentication": "User login/logout capability",
            "data_management": "Create, read, update, delete operations",
            "search": "Full-text search functionality",
            "notifications": "Real-time user notifications",
        }
    
    def _extract_non_functional_requirements(self, user_input: str) -> Dict[str, Any]:
        """Extract non-functional requirements."""
        return {
            "performance": "Response time < 2 seconds",
            "accessibility": "WCAG 2.1 AA compliance",
            "compatibility": "Support for modern browsers",
            "security": "End-to-end encryption for sensitive data",
        }
    
    def _extract_constraints(self, user_input: str) -> list[str]:
        """Extract constraints and limitations."""
        return [
            "Mobile-first design",
            "Support for offline mode",
            "Responsive design for all screen sizes",
        ]
    
    def _generate_acceptance_criteria(self, user_input: str) -> list[str]:
        """Generate acceptance criteria for the requirements."""
        return [
            "All user stories are testable",
            "Requirements are prioritized",
            "Security requirements are addressed",
            "Performance targets are achievable",
        ]
