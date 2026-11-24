"""Integration tests for the workflow."""
import pytest

from src.agents import OrchestratorAgent
from src.types import TaskStatus, WorkflowPhase


@pytest.mark.asyncio
async def test_complete_workflow():
    """Test the complete UX design workflow."""
    orchestrator = OrchestratorAgent()
    await orchestrator.initialize()
    
    try:
        user_input = "Create a modern e-commerce platform for artisan goods"
        
        workflow_state = await orchestrator.run_workflow(user_input)
        
        # Assertions
        assert workflow_state.workflow_id is not None
        assert workflow_state.status == TaskStatus.COMPLETED
        assert workflow_state.phase == WorkflowPhase.COMPLETE
        
        # Verify all phases were executed
        assert len(workflow_state.history) == 4
        
        # Verify requirements phase
        assert len(workflow_state.requirements) > 0
        assert "primary_goal" in workflow_state.requirements
        assert "user_stories" in workflow_state.requirements
        
        # Verify design phase
        assert len(workflow_state.design) > 0
        assert "wireframes" in workflow_state.design
        assert "color_palette" in workflow_state.design
        
        # Verify prototyping phase
        assert len(workflow_state.prototype) > 0
        assert "pages" in workflow_state.prototype
        assert "interactions" in workflow_state.prototype
        
        # Verify evaluation phase
        assert len(workflow_state.evaluation) > 0
        assert "overall_score" in workflow_state.evaluation
        
    finally:
        await orchestrator.shutdown()


@pytest.mark.asyncio
async def test_workflow_persistence():
    """Test that workflows can be retrieved after creation."""
    orchestrator = OrchestratorAgent()
    await orchestrator.initialize()
    
    try:
        workflow_state = await orchestrator.run_workflow("Test input")
        workflow_id = workflow_state.workflow_id
        
        # Retrieve workflow
        retrieved = orchestrator.get_workflow_status(workflow_id)
        
        assert retrieved is not None
        assert retrieved.workflow_id == workflow_id
        assert retrieved.status == TaskStatus.COMPLETED
        
    finally:
        await orchestrator.shutdown()


@pytest.mark.asyncio
async def test_multiple_workflows():
    """Test running multiple workflows."""
    orchestrator = OrchestratorAgent()
    await orchestrator.initialize()
    
    try:
        inputs = [
            "Build a social media platform",
            "Create a fitness tracking app",
            "Design a project management tool",
        ]
        
        workflow_ids = []
        for user_input in inputs:
            workflow_state = await orchestrator.run_workflow(user_input)
            workflow_ids.append(workflow_state.workflow_id)
        
        # Verify all workflows were created
        assert len(workflow_ids) == 3
        
        all_workflows = orchestrator.get_all_workflows()
        assert len(all_workflows) == 3
        
        # Verify each workflow
        for workflow_id in workflow_ids:
            workflow = orchestrator.get_workflow_status(workflow_id)
            assert workflow is not None
            assert workflow.status == TaskStatus.COMPLETED
        
    finally:
        await orchestrator.shutdown()
