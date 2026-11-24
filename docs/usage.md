# Usage Guide

## Quick Start

### 1. Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Or using the development setup
pip install -e ".[dev]"
```

### 2. Basic Usage

```python
import asyncio
from src.agents import OrchestratorAgent

async def main():
    orchestrator = OrchestratorAgent()
    await orchestrator.initialize()
    
    try:
        workflow = await orchestrator.run_workflow(
            "Build a modern e-commerce platform"
        )
        print(f"Workflow completed: {workflow.status}")
        print(f"Quality score: {workflow.evaluation.get('overall_score')}")
    finally:
        await orchestrator.shutdown()

if __name__ == "__main__":
    asyncio.run(main())
```

### 3. Run the Example

```bash
python -m src.main
```

## Advanced Usage

### Custom Workflow ID

```python
workflow = await orchestrator.run_workflow(
    user_input="Your requirements here",
    workflow_id="custom-workflow-123"
)
```

### Save Results

```python
from src.utils import save_json

save_json(workflow.model_dump(), "output/workflow_results.json")
```

### Access Workflow History

```python
# Get all executed tasks
for response in workflow.history:
    print(f"{response.agent_type}: {response.status}")

# Get specific phase results
print(workflow.requirements)
print(workflow.design)
print(workflow.prototype)
print(workflow.evaluation)
```

### Custom Configuration

Create a `.env` file:

```env
APP_NAME=my-ux-workflow
DEBUG=false
LOG_LEVEL=INFO
LLM_PROVIDER=openai
LLM_MODEL=gpt-4
LLM_TEMPERATURE=0.7
```

Or use YAML config:

```python
from src.config import load_config

config = load_config("config/workflow.yaml")
```

## Workflow Results

### WorkflowState Structure

```python
WorkflowState(
    workflow_id: str              # Unique workflow identifier
    phase: WorkflowPhase          # Current phase
    status: TaskStatus            # Overall status
    requirements: dict            # Requirements specification
    design: dict                  # Design specification
    prototype: dict               # Prototype specification
    evaluation: dict              # Evaluation report
    created_at: datetime          # Creation timestamp
    updated_at: datetime          # Last update timestamp
    history: list[AgentResponse]  # Complete agent response history
)
```

### Evaluation Report Structure

```python
{
    "requirements_compliance": {
        "functional_requirements_met": 0.90,
        "non_functional_requirements_met": 0.85,
        "user_stories_covered": 0.95,
        "constraints_respected": 0.88
    },
    "design_quality": {
        "consistency": 0.92,
        "visual_hierarchy": 0.88,
        "component_reusability": 0.85,
        "design_system_adherence": 0.90
    },
    "usability_assessment": {
        "intuitiveness": 0.87,
        "learnability": 0.90,
        "efficiency": 0.85,
        "error_recovery": 0.80
    },
    "accessibility_audit": {
        "wcag_aa_compliance": True,
        "keyboard_navigation": True,
        "screen_reader_support": True,
        "color_contrast": True,
        "font_readability": True
    },
    "performance_metrics": {
        "page_load_time": 1.2,
        "first_contentful_paint": 0.8,
        "interaction_latency": 100,
        "memory_usage": "low"
    },
    "issues": [...],
    "recommendations": [...],
    "overall_score": 0.88
}
```

## Logging

### Configure Logging

```python
from src.utils import setup_logging

# Setup logging with file output
setup_logging(
    log_level="DEBUG",
    log_file="logs/workflow.log",
    use_loguru=True
)
```

### Log Levels

- `DEBUG`: Detailed debugging information
- `INFO`: General informational messages
- `WARNING`: Warning messages
- `ERROR`: Error messages
- `CRITICAL`: Critical errors

## Testing

### Run Unit Tests

```bash
pytest tests/unit/ -v
```

### Run Integration Tests

```bash
pytest tests/integration/ -v
```

### Run All Tests with Coverage

```bash
pytest tests/ --cov=src --cov-report=html
```

## Integration with LLMs

Each agent can be enhanced to use LLMs for intelligent processing:

```python
class RequirementsAnalystAgent(BaseAgent):
    async def execute(self, task: Task) -> AgentResponse:
        # Use LLM to analyze requirements
        llm_response = await call_llm(
            prompt=f"Analyze these requirements: {task.input_data['user_input']}",
            model=self.config.llm_model,
            temperature=self.config.llm_temperature
        )
        # Process LLM response...
```

## Best Practices

1. **Error Handling**: Always use try-finally to ensure agent cleanup
2. **Configuration**: Use environment variables for sensitive data
3. **Logging**: Enable debug logging during development
4. **Persistence**: Save workflow results for audit trails
5. **Testing**: Write tests for custom agent implementations
6. **Documentation**: Document any custom modifications

## Troubleshooting

### Workflow Fails at a Phase

Check the response status and error message:

```python
if workflow.status == TaskStatus.FAILED:
    for response in workflow.history:
        if response.status == TaskStatus.FAILED:
            print(f"Failed at {response.agent_type}: {response.error}")
```

### Low Quality Scores

Review recommendations in evaluation report:

```python
evaluation = workflow.evaluation
for recommendation in evaluation.get("recommendations", []):
    print(recommendation)
```

### Agent Timeout

Increase timeout in configuration:

```env
AGENT_TIMEOUT=600  # 10 minutes
```
