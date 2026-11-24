# API Reference

## Core Classes

### BaseAgent

Abstract base class for all agents.

#### Methods

- **`__init__(agent_id, agent_type, name)`**
  - Initialize an agent
  - Args: `agent_id` (optional), `agent_type`, `name` (optional)

- **`async initialize()`**
  - Initialize agent resources
  - Override in subclasses for custom initialization

- **`async shutdown()`**
  - Clean up agent resources
  - Override in subclasses for custom cleanup

- **`async execute(task: Task) -> AgentResponse`** (Abstract)
  - Execute a task (must be implemented by subclasses)
  - Args: `task` - Task to execute
  - Returns: `AgentResponse`

- **`async process_task(task: Task) -> AgentResponse`**
  - Process a task with error handling
  - Args: `task` - Task to process
  - Returns: `AgentResponse`

- **`get_task_history() -> list[Task]`**
  - Get completed tasks history
  - Returns: List of completed tasks

- **`get_status() -> dict`**
  - Get current agent status
  - Returns: Status dictionary

### RequirementsAnalystAgent

Analyzes user requirements and creates specifications.

```python
from src.agents import RequirementsAnalystAgent

agent = RequirementsAnalystAgent()
response = await agent.execute(task)
```

**Output**: `requirements_specification` with:
- `primary_goal`: Main objective
- `user_stories`: List of user stories
- `functional_requirements`: Required features
- `non_functional_requirements`: Quality attributes
- `constraints`: Limitations and constraints
- `acceptance_criteria`: Definition of done

### UXDesignerAgent

Creates UX designs and design systems.

```python
from src.agents import UXDesignerAgent

agent = UXDesignerAgent()
response = await agent.execute(task)
```

**Output**: `design_specification` with:
- `wireframes`: Layout sketches
- `user_flows`: Navigation flows
- `layout_grid`: Grid system
- `color_palette`: Color system
- `typography`: Font definitions
- `component_library`: Reusable components
- `accessibility_features`: A11y features
- `responsive_breakpoints`: Breakpoint definitions

### PrototyperAgent

Creates interactive prototypes.

```python
from src.agents import PrototyperAgent

agent = PrototyperAgent()
response = await agent.execute(task)
```

**Output**: `prototype_specification` with:
- `prototype_type`: Type of prototype
- `pages`: Interactive pages
- `interactions`: User interactions
- `animations`: Animation definitions
- `responsive_behavior`: Responsive design details
- `testing_scenarios`: Test cases

### EvaluatorAgent

Evaluates designs and prototypes.

```python
from src.agents import EvaluatorAgent

agent = EvaluatorAgent()
response = await agent.execute(task)
```

**Output**: `evaluation_report` with:
- `requirements_compliance`: Compliance metrics
- `design_quality`: Quality metrics
- `usability_assessment`: Usability scores
- `accessibility_audit`: A11y compliance
- `performance_metrics`: Performance data
- `issues`: Identified issues
- `recommendations`: Improvement suggestions
- `overall_score`: Overall quality score

### OrchestratorAgent

Coordinates the entire workflow.

```python
from src.agents import OrchestratorAgent

orchestrator = OrchestratorAgent()
await orchestrator.initialize()

workflow = await orchestrator.run_workflow("Your requirements")

await orchestrator.shutdown()
```

#### Methods

- **`async initialize()`**
  - Initialize orchestrator and all agents

- **`async shutdown()`**
  - Shutdown orchestrator and all agents

- **`async run_workflow(user_input: str, workflow_id: str = None) -> WorkflowState`**
  - Run complete workflow
  - Args: `user_input` - User requirements, `workflow_id` - Optional ID
  - Returns: `WorkflowState`

- **`get_workflow_status(workflow_id: str) -> WorkflowState`**
  - Get workflow status
  - Args: `workflow_id` - Workflow ID
  - Returns: `WorkflowState` or None

- **`get_all_workflows() -> dict`**
  - Get all workflows
  - Returns: Dictionary of workflows

## Type Definitions

### WorkflowState

```python
WorkflowState(
    workflow_id: str              # Unique identifier
    phase: WorkflowPhase          # Current phase
    status: TaskStatus            # Overall status
    requirements: dict            # Phase outputs
    design: dict
    prototype: dict
    evaluation: dict
    created_at: datetime
    updated_at: datetime
    history: list[AgentResponse]
)
```

### Task

```python
Task(
    task_id: str                  # Unique task ID
    agent_id: str                 # Assigned agent
    agent_type: AgentType         # Agent type
    phase: WorkflowPhase          # Workflow phase
    description: str              # Task description
    input_data: dict              # Input parameters
    priority: Priority            # Task priority
    status: TaskStatus            # Task status
    result: Optional[dict]        # Task result
    error: Optional[str]          # Error message
    created_at: datetime
    started_at: Optional[datetime]
    completed_at: Optional[datetime]
)
```

### AgentResponse

```python
AgentResponse(
    agent_id: str                 # Agent ID
    agent_type: AgentType         # Agent type
    status: TaskStatus            # Task status
    result: dict                  # Task result
    error: Optional[str]          # Error message
    timestamp: datetime           # Response time
)
```

## Enums

### WorkflowPhase
- `REQUIREMENTS` - Requirements analysis
- `DESIGN` - UX design
- `PROTOTYPING` - Prototyping
- `EVALUATION` - Evaluation
- `COMPLETE` - Workflow complete

### TaskStatus
- `PENDING` - Pending execution
- `IN_PROGRESS` - Currently executing
- `COMPLETED` - Successfully completed
- `FAILED` - Execution failed
- `CANCELLED` - Cancelled

### AgentType
- `REQUIREMENTS_ANALYST`
- `UX_DESIGNER`
- `PROTOTYPER`
- `EVALUATOR`
- `ORCHESTRATOR`

### Priority
- `LOW`
- `MEDIUM`
- `HIGH`
- `CRITICAL`

## Configuration

### WorkflowConfig

```python
from src.config import get_config

config = get_config()
```

**Properties**:
- `app_name`: Application name
- `debug`: Debug mode
- `log_level`: Logging level
- `max_agents`: Maximum agents
- `agent_timeout`: Agent timeout (seconds)
- `api_timeout`: API timeout (seconds)
- `max_retries`: Max retry attempts
- `enable_persistence`: Save results
- `output_dir`: Output directory
- `llm_provider`: LLM provider
- `llm_model`: LLM model
- `llm_temperature`: LLM temperature
- `llm_max_tokens`: Max LLM tokens

## Utilities

### logging_utils

```python
from src.utils import setup_logging, get_logger

setup_logging(log_level="INFO", log_file="app.log")
logger = get_logger(__name__)
```

### file_utils

```python
from src.utils import save_json, load_json, ensure_directory, merge_dicts

save_json(data, "output.json")
data = load_json("output.json")
path = ensure_directory("output/")
merged = merge_dicts(base, updates)
```

## Error Handling

All agents return `AgentResponse` with status and optional error:

```python
response = await agent.process_task(task)

if response.status == TaskStatus.FAILED:
    print(f"Error: {response.error}")
else:
    print(f"Result: {response.result}")
```

## Async/Await Usage

All async operations use asyncio:

```python
import asyncio

async def main():
    orchestrator = OrchestratorAgent()
    await orchestrator.initialize()
    workflow = await orchestrator.run_workflow("requirements")
    await orchestrator.shutdown()

# Run
asyncio.run(main())
```
