"""Main entry point for the AI UX Design Workflow."""
import asyncio
import logging
from typing import Optional

from src.agents import OrchestratorAgent
from src.config import get_config
from src.utils import setup_logging, save_json, ensure_directory
from src.types import WorkflowState


async def run_design_workflow(
    user_input: str,
    workflow_id: Optional[str] = None,
    output_dir: str = "outputs",
) -> WorkflowState:
    """Run the complete UX design workflow.
    
    Args:
        user_input: User requirements or project description
        workflow_id: Optional workflow ID
        output_dir: Directory to save outputs
        
    Returns:
        WorkflowState with all results
    """
    # Setup logging
    setup_logging(log_level="INFO")
    logger = logging.getLogger(__name__)
    
    # Ensure output directory exists
    ensure_directory(output_dir)
    
    logger.info("Starting AI UX Design Workflow")
    logger.info(f"Input: {user_input[:100]}...")
    
    # Initialize orchestrator
    orchestrator = OrchestratorAgent()
    await orchestrator.initialize()
    
    try:
        # Run the workflow
        workflow_state = await orchestrator.run_workflow(user_input, workflow_id)
        
        # Save results to file
        output_file = f"{output_dir}/workflow_{workflow_state.workflow_id}.json"
        save_json(workflow_state.model_dump(), output_file)
        logger.info(f"Workflow results saved to {output_file}")
        
        return workflow_state
    finally:
        # Cleanup
        await orchestrator.shutdown()


async def main():
    """Main function demonstrating workflow usage."""
    sample_input = """
    We need to build an e-commerce platform for selling handmade crafts.
    The platform should allow users to:
    - Browse and search for products
    - View detailed product information
    - Add items to a shopping cart
    - Checkout with payment integration
    - Track their orders
    - Leave reviews and ratings
    
    The design should be mobile-first, modern, and user-friendly.
    """
    
    workflow_state = await run_design_workflow(sample_input)
    
    # Print summary
    print("\n" + "="*60)
    print("WORKFLOW EXECUTION SUMMARY")
    print("="*60)
    print(f"Workflow ID: {workflow_state.workflow_id}")
    print(f"Status: {workflow_state.status}")
    print(f"Phase: {workflow_state.phase}")
    print(f"Phases Completed: {len(workflow_state.history)}")
    
    if workflow_state.evaluation:
        print(f"\nEvaluation Score: {workflow_state.evaluation.get('overall_score', 'N/A')}")
        print(f"Ready for Production: {workflow_state.evaluation.get('overall_score', 0) >= 0.75}")


if __name__ == "__main__":
    asyncio.run(main())
