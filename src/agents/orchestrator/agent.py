"""Orchestrator Agent - coordinates the entire UX design workflow."""
import logging
import uuid
from datetime import datetime
from typing import Any, Dict, Optional

from src.agents.base_agent import BaseAgent
from src.agents.requirements_analyst import RequirementsAnalystAgent
from src.agents.ux_designer import UXDesignerAgent
from src.agents.prototyper import PrototyperAgent
from src.agents.evaluator import EvaluatorAgent
from src.types import (
    AgentType,
    WorkflowPhase,
    TaskStatus,
    Task,
    AgentResponse,
    WorkflowState,
)

logger = logging.getLogger(__name__)


class OrchestratorAgent(BaseAgent):
    """Agent responsible for orchestrating the entire UX design workflow."""
    
    def __init__(self, agent_id: str = None, name: str = "Workflow Orchestrator"):
        """Initialize the Orchestrator Agent."""
        super().__init__(agent_id, AgentType.ORCHESTRATOR, name)
        
        # Initialize specialized agents
        self.requirements_analyst = RequirementsAnalystAgent()
        self.ux_designer = UXDesignerAgent()
        self.prototyper = PrototyperAgent()
        self.evaluator = EvaluatorAgent()
        
        self.agents: Dict[AgentType, BaseAgent] = {
            AgentType.REQUIREMENTS_ANALYST: self.requirements_analyst,
            AgentType.UX_DESIGNER: self.ux_designer,
            AgentType.PROTOTYPER: self.prototyper,
            AgentType.EVALUATOR: self.evaluator,
        }
        
        self.workflows: Dict[str, WorkflowState] = {}
    
    async def initialize(self) -> None:
        """Initialize all agents."""
        logger.info("Initializing Orchestrator and all agents...")
        for agent in self.agents.values():
            await agent.initialize()
    
    async def shutdown(self) -> None:
        """Shutdown all agents."""
        logger.info("Shutting down all agents...")
        for agent in self.agents.values():
            await agent.shutdown()
        await super().shutdown()
    
    async def execute(self, task: Task) -> AgentResponse:
        """Execute a workflow task (not used directly, use run_workflow instead).
        
        Args:
            task: Task to execute
            
        Returns:
            AgentResponse
        """
        # This method is not typically called directly on the orchestrator
        return AgentResponse(
            agent_id=self.agent_id,
            agent_type=self.agent_type,
            status=TaskStatus.FAILED,
            error="Use run_workflow method instead",
        )
    
    async def run_workflow(self, user_input: str, workflow_id: Optional[str] = None) -> WorkflowState:
        """Run the complete UX design workflow.
        
        Args:
            user_input: User requirements or project description
            workflow_id: Optional workflow ID; generates one if not provided
            
        Returns:
            WorkflowState with results from all phases
        """
        workflow_id = workflow_id or str(uuid.uuid4())
        logger.info(f"Starting workflow {workflow_id}")
        
        # Initialize workflow state
        workflow_state = WorkflowState(workflow_id=workflow_id)
        self.workflows[workflow_id] = workflow_state
        
        try:
            # Phase 1: Requirements Analysis
            workflow_state = await self._run_requirements_phase(workflow_state, user_input)
            if workflow_state.status == TaskStatus.FAILED:
                return workflow_state
            
            # Phase 2: UX Design
            workflow_state = await self._run_design_phase(workflow_state)
            if workflow_state.status == TaskStatus.FAILED:
                return workflow_state
            
            # Phase 3: Prototyping
            workflow_state = await self._run_prototyping_phase(workflow_state)
            if workflow_state.status == TaskStatus.FAILED:
                return workflow_state
            
            # Phase 4: Evaluation
            workflow_state = await self._run_evaluation_phase(workflow_state)
            
            workflow_state.phase = WorkflowPhase.COMPLETE
            workflow_state.status = TaskStatus.COMPLETED
            workflow_state.updated_at = datetime.utcnow()
            
            logger.info(f"Workflow {workflow_id} completed successfully")
            
        except Exception as e:
            logger.error(f"Error in workflow execution: {str(e)}", exc_info=True)
            workflow_state.status = TaskStatus.FAILED
            workflow_state.updated_at = datetime.utcnow()
        
        self.workflows[workflow_id] = workflow_state
        return workflow_state
    
    async def _run_requirements_phase(self, workflow_state: WorkflowState, user_input: str) -> WorkflowState:
        """Run the requirements analysis phase."""
        logger.info(f"Running requirements phase for workflow {workflow_state.workflow_id}")
        
        workflow_state.phase = WorkflowPhase.REQUIREMENTS
        workflow_state.status = TaskStatus.IN_PROGRESS
        workflow_state.updated_at = datetime.utcnow()
        
        try:
            task = Task(
                task_id=str(uuid.uuid4()),
                agent_id=self.requirements_analyst.agent_id,
                agent_type=AgentType.REQUIREMENTS_ANALYST,
                phase=WorkflowPhase.REQUIREMENTS,
                description="Analyze user requirements",
                input_data={"user_input": user_input},
            )
            
            response = await self.requirements_analyst.process_task(task)
            workflow_state.history.append(response)
            
            if response.status == TaskStatus.COMPLETED:
                workflow_state.requirements = response.result.get("requirements_specification", {})
                workflow_state.status = TaskStatus.PENDING
            else:
                workflow_state.status = TaskStatus.FAILED
            
        except Exception as e:
            logger.error(f"Error in requirements phase: {str(e)}")
            workflow_state.status = TaskStatus.FAILED
        
        workflow_state.updated_at = datetime.utcnow()
        return workflow_state
    
    async def _run_design_phase(self, workflow_state: WorkflowState) -> WorkflowState:
        """Run the UX design phase."""
        logger.info(f"Running design phase for workflow {workflow_state.workflow_id}")
        
        workflow_state.phase = WorkflowPhase.DESIGN
        workflow_state.status = TaskStatus.IN_PROGRESS
        workflow_state.updated_at = datetime.utcnow()
        
        try:
            task = Task(
                task_id=str(uuid.uuid4()),
                agent_id=self.ux_designer.agent_id,
                agent_type=AgentType.UX_DESIGNER,
                phase=WorkflowPhase.DESIGN,
                description="Create UX design",
                input_data={
                    "requirements_specification": workflow_state.requirements,
                },
            )
            
            response = await self.ux_designer.process_task(task)
            workflow_state.history.append(response)
            
            if response.status == TaskStatus.COMPLETED:
                workflow_state.design = response.result.get("design_specification", {})
                workflow_state.status = TaskStatus.PENDING
            else:
                workflow_state.status = TaskStatus.FAILED
            
        except Exception as e:
            logger.error(f"Error in design phase: {str(e)}")
            workflow_state.status = TaskStatus.FAILED
        
        workflow_state.updated_at = datetime.utcnow()
        return workflow_state
    
    async def _run_prototyping_phase(self, workflow_state: WorkflowState) -> WorkflowState:
        """Run the prototyping phase."""
        logger.info(f"Running prototyping phase for workflow {workflow_state.workflow_id}")
        
        workflow_state.phase = WorkflowPhase.PROTOTYPING
        workflow_state.status = TaskStatus.IN_PROGRESS
        workflow_state.updated_at = datetime.utcnow()
        
        try:
            task = Task(
                task_id=str(uuid.uuid4()),
                agent_id=self.prototyper.agent_id,
                agent_type=AgentType.PROTOTYPER,
                phase=WorkflowPhase.PROTOTYPING,
                description="Create interactive prototype",
                input_data={
                    "design_specification": workflow_state.design,
                    "requirements_specification": workflow_state.requirements,
                },
            )
            
            response = await self.prototyper.process_task(task)
            workflow_state.history.append(response)
            
            if response.status == TaskStatus.COMPLETED:
                workflow_state.prototype = response.result.get("prototype_specification", {})
                workflow_state.status = TaskStatus.PENDING
            else:
                workflow_state.status = TaskStatus.FAILED
            
        except Exception as e:
            logger.error(f"Error in prototyping phase: {str(e)}")
            workflow_state.status = TaskStatus.FAILED
        
        workflow_state.updated_at = datetime.utcnow()
        return workflow_state
    
    async def _run_evaluation_phase(self, workflow_state: WorkflowState) -> WorkflowState:
        """Run the evaluation phase."""
        logger.info(f"Running evaluation phase for workflow {workflow_state.workflow_id}")
        
        workflow_state.phase = WorkflowPhase.EVALUATION
        workflow_state.status = TaskStatus.IN_PROGRESS
        workflow_state.updated_at = datetime.utcnow()
        
        try:
            task = Task(
                task_id=str(uuid.uuid4()),
                agent_id=self.evaluator.agent_id,
                agent_type=AgentType.EVALUATOR,
                phase=WorkflowPhase.EVALUATION,
                description="Evaluate prototype and design",
                input_data={
                    "requirements_specification": workflow_state.requirements,
                    "design_specification": workflow_state.design,
                    "prototype_specification": workflow_state.prototype,
                },
            )
            
            response = await self.evaluator.process_task(task)
            workflow_state.history.append(response)
            
            if response.status == TaskStatus.COMPLETED:
                workflow_state.evaluation = response.result.get("evaluation_report", {})
                workflow_state.status = TaskStatus.PENDING
            else:
                workflow_state.status = TaskStatus.FAILED
            
        except Exception as e:
            logger.error(f"Error in evaluation phase: {str(e)}")
            workflow_state.status = TaskStatus.FAILED
        
        workflow_state.updated_at = datetime.utcnow()
        return workflow_state
    
    def get_workflow_status(self, workflow_id: str) -> Optional[WorkflowState]:
        """Get the status of a workflow.
        
        Args:
            workflow_id: The workflow ID
            
        Returns:
            WorkflowState or None if not found
        """
        return self.workflows.get(workflow_id)
    
    def get_all_workflows(self) -> Dict[str, WorkflowState]:
        """Get all workflows.
        
        Returns:
            Dictionary of all workflows
        """
        return self.workflows.copy()
