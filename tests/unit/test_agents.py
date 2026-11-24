"""Unit tests for agents."""
import pytest
from unittest.mock import AsyncMock, MagicMock

from src.agents import (
    BaseAgent,
    RequirementsAnalystAgent,
    UXDesignerAgent,
    PrototyperAgent,
    EvaluatorAgent,
    OrchestratorAgent,
)
from src.types import AgentType, TaskStatus, WorkflowPhase, Task


@pytest.mark.asyncio
async def test_requirements_analyst_initialization():
    """Test RequirementsAnalystAgent initialization."""
    agent = RequirementsAnalystAgent()
    assert agent.agent_type == AgentType.REQUIREMENTS_ANALYST
    assert agent.is_active is True


@pytest.mark.asyncio
async def test_requirements_analyst_execute():
    """Test RequirementsAnalystAgent execute method."""
    agent = RequirementsAnalystAgent()
    
    task = Task(
        task_id="test-123",
        agent_id=agent.agent_id,
        agent_type=AgentType.REQUIREMENTS_ANALYST,
        phase=WorkflowPhase.REQUIREMENTS,
        description="Test requirement analysis",
        input_data={"user_input": "Build a user management system"},
    )
    
    response = await agent.execute(task)
    
    assert response.status == TaskStatus.COMPLETED
    assert response.agent_type == AgentType.REQUIREMENTS_ANALYST
    assert "requirements_specification" in response.result


@pytest.mark.asyncio
async def test_ux_designer_initialization():
    """Test UXDesignerAgent initialization."""
    agent = UXDesignerAgent()
    assert agent.agent_type == AgentType.UX_DESIGNER
    assert agent.is_active is True


@pytest.mark.asyncio
async def test_ux_designer_execute():
    """Test UXDesignerAgent execute method."""
    agent = UXDesignerAgent()
    
    task = Task(
        task_id="test-123",
        agent_id=agent.agent_id,
        agent_type=AgentType.UX_DESIGNER,
        phase=WorkflowPhase.DESIGN,
        description="Test design creation",
        input_data={"requirements_specification": {}},
    )
    
    response = await agent.execute(task)
    
    assert response.status == TaskStatus.COMPLETED
    assert response.agent_type == AgentType.UX_DESIGNER
    assert "design_specification" in response.result


@pytest.mark.asyncio
async def test_prototyper_initialization():
    """Test PrototyperAgent initialization."""
    agent = PrototyperAgent()
    assert agent.agent_type == AgentType.PROTOTYPER
    assert agent.is_active is True


@pytest.mark.asyncio
async def test_prototyper_execute():
    """Test PrototyperAgent execute method."""
    agent = PrototyperAgent()
    
    task = Task(
        task_id="test-123",
        agent_id=agent.agent_id,
        agent_type=AgentType.PROTOTYPER,
        phase=WorkflowPhase.PROTOTYPING,
        description="Test prototype creation",
        input_data={"design_specification": {}},
    )
    
    response = await agent.execute(task)
    
    assert response.status == TaskStatus.COMPLETED
    assert response.agent_type == AgentType.PROTOTYPER
    assert "prototype_specification" in response.result


@pytest.mark.asyncio
async def test_evaluator_initialization():
    """Test EvaluatorAgent initialization."""
    agent = EvaluatorAgent()
    assert agent.agent_type == AgentType.EVALUATOR
    assert agent.is_active is True


@pytest.mark.asyncio
async def test_evaluator_execute():
    """Test EvaluatorAgent execute method."""
    agent = EvaluatorAgent()
    
    task = Task(
        task_id="test-123",
        agent_id=agent.agent_id,
        agent_type=AgentType.EVALUATOR,
        phase=WorkflowPhase.EVALUATION,
        description="Test evaluation",
        input_data={
            "requirements_specification": {},
            "design_specification": {},
            "prototype_specification": {},
        },
    )
    
    response = await agent.execute(task)
    
    assert response.status == TaskStatus.COMPLETED
    assert response.agent_type == AgentType.EVALUATOR
    assert "evaluation_report" in response.result


@pytest.mark.asyncio
async def test_orchestrator_initialization():
    """Test OrchestratorAgent initialization."""
    orchestrator = OrchestratorAgent()
    assert orchestrator.agent_type == AgentType.ORCHESTRATOR
    assert len(orchestrator.agents) == 4


@pytest.mark.asyncio
async def test_orchestrator_workflow():
    """Test complete workflow execution."""
    orchestrator = OrchestratorAgent()
    await orchestrator.initialize()
    
    try:
        workflow_state = await orchestrator.run_workflow(
            "Build a simple task management app",
        )
        
        assert workflow_state.status == TaskStatus.COMPLETED
        assert workflow_state.phase == WorkflowPhase.COMPLETE
        assert len(workflow_state.history) == 4
        assert len(workflow_state.requirements) > 0
        assert len(workflow_state.design) > 0
        assert len(workflow_state.prototype) > 0
        assert len(workflow_state.evaluation) > 0
    finally:
        await orchestrator.shutdown()


@pytest.mark.asyncio
async def test_base_agent_process_task():
    """Test BaseAgent process_task method."""
    agent = RequirementsAnalystAgent()
    
    task = Task(
        task_id="test-123",
        agent_id=agent.agent_id,
        agent_type=AgentType.REQUIREMENTS_ANALYST,
        phase=WorkflowPhase.REQUIREMENTS,
        description="Test",
        input_data={"user_input": "Test input"},
    )
    
    response = await agent.process_task(task)
    
    assert response.status == TaskStatus.COMPLETED
    assert len(agent.task_history) == 1


@pytest.mark.asyncio
async def test_agent_status():
    """Test agent status retrieval."""
    agent = RequirementsAnalystAgent()
    status = agent.get_status()
    
    assert status["agent_type"] == AgentType.REQUIREMENTS_ANALYST
    assert status["is_active"] is True
    assert status["tasks_completed"] == 0
