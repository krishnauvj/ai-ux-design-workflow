# AI-Powered Multi-Agent UX Design Workflow

An intelligent system that automates the entire UX design process using multiple specialized AI agents working together in a coordinated workflow.

**🎯 Transform Requirements into Production-Ready UX Designs**

## Overview

This project implements a **multi-agent architecture** where specialized AI agents collaborate through a well-defined workflow:

1. **Requirements Analyst** 📋 - Analyzes and structures user requirements
2. **UX Designer** 🎨 - Creates design systems and wireframes
3. **Prototyper** ⚡ - Builds interactive prototypes
4. **Evaluator** ✅ - Assesses quality and compliance
5. **Orchestrator** 🎼 - Coordinates the entire workflow

```
User Input
    ↓
Requirements Analysis
    ↓
Design Creation
    ↓
Prototype Development
    ↓
Quality Evaluation
    ↓
Production-Ready Output
```

## Features

✨ **Multi-Agent Architecture**
- Independent specialized agents with clear responsibilities
- Async/await support for efficient execution
- Modular and extensible design

🔄 **Complete Workflow**
- Requirements → Design → Prototype → Evaluation pipeline
- Seamless data flow between agents
- State management with full history tracking

📊 **Quality Assessment**
- Automatic evaluation against requirements
- Design quality metrics
- Usability assessment
- Accessibility audits
- Performance evaluation

🛠️ **Developer Friendly**
- Type-safe with Pydantic models
- Comprehensive error handling
- Detailed logging
- Well-documented API

📦 **Extensible**
- Easy to add new agents
- Pluggable LLM integration
- Configurable via environment variables
- Support for multiple design tools

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/krishnauvj/ai-ux-design-workflow.git
cd ai-ux-design-workflow

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

```python
import asyncio
from src.agents import OrchestratorAgent

async def main():
    # Initialize the orchestrator
    orchestrator = OrchestratorAgent()
    await orchestrator.initialize()
    
    try:
        # Run the workflow
        workflow = await orchestrator.run_workflow(
            "Build an e-commerce platform for artisan goods"
        )
        
        # Access results
        print(f"Status: {workflow.status}")
        print(f"Quality Score: {workflow.evaluation.get('overall_score')}")
        
        # Save results
        from src.utils import save_json
        save_json(workflow.model_dump(), "output/results.json")
    finally:
        await orchestrator.shutdown()

if __name__ == "__main__":
    asyncio.run(main())
```

### Run the Example

```bash
python -m src.main
```

## Project Structure

```
ai-ux-design-workflow/
├── src/
│   ├── agents/                      # Agent implementations
│   │   ├── base_agent.py           # Abstract base class
│   │   ├── requirements_analyst/   # Requirements analysis
│   │   ├── ux_designer/           # Design creation
│   │   ├── prototyper/            # Prototype development
│   │   ├── evaluator/             # Quality evaluation
│   │   └── orchestrator/          # Workflow orchestration
│   ├── types/                     # Type definitions
│   │   └── models.py             # Pydantic data models
│   ├── config/                    # Configuration
│   │   └── config.py             # App configuration
│   ├── utils/                     # Utilities
│   │   ├── logging_utils.py      # Logging setup
│   │   └── file_utils.py         # File operations
│   └── main.py                   # Entry point
├── tests/
│   ├── unit/                     # Unit tests
│   ├── integration/              # Integration tests
│   └── conftest.py              # Pytest configuration
├── docs/
│   ├── architecture.md          # Architecture guide
│   ├── api.md                   # API reference
│   └── usage.md                # Usage guide
├── pyproject.toml              # Project configuration
├── requirements.txt            # Python dependencies
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

## Workflow Phases

### Phase 1: Requirements Analysis
- Extracts and structures user requirements
- Identifies user stories and acceptance criteria
- Documents functional and non-functional requirements
- **Output**: Detailed requirements specification

### Phase 2: UX Design
- Creates wireframes and layouts
- Designs color palettes and typography
- Builds component library
- Defines accessibility features
- **Output**: Complete design specification

### Phase 3: Prototyping
- Creates interactive prototypes
- Defines user interactions and animations
- Tests responsive behavior
- **Output**: Interactive prototype specification

### Phase 4: Evaluation
- Validates against requirements
- Assesses design quality
- Evaluates usability
- Audits accessibility compliance
- **Output**: Comprehensive evaluation report with score

## Configuration

Create a `.env` file:

```env
# Application
APP_NAME=ai-ux-design-workflow
DEBUG=false
LOG_LEVEL=INFO

# Agents
MAX_AGENTS=10
AGENT_TIMEOUT=300

# LLM Configuration
LLM_PROVIDER=openai
LLM_MODEL=gpt-4
LLM_TEMPERATURE=0.7
LLM_MAX_TOKENS=2048

# Output
ENABLE_PERSISTENCE=true
OUTPUT_DIR=outputs
```

## Testing

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html

# Run specific test suite
pytest tests/unit/ -v
pytest tests/integration/ -v
```

## Documentation

- 📖 [Architecture Guide](docs/architecture.md) - System design and components
- 🔧 [API Reference](docs/api.md) - Complete API documentation
- 📚 [Usage Guide](docs/usage.md) - How to use the system

## Key Components

### BaseAgent
Abstract base class for all agents providing:
- Task execution framework
- Error handling
- Logging
- Status tracking

### WorkflowState
Maintains complete workflow state:
- Phase outputs from each agent
- Execution history
- Timestamps
- Status tracking

### OrchestratorAgent
Coordinates the entire workflow:
- Initializes agents
- Manages workflow phases
- Passes data between agents
- Tracks overall progress

## Advanced Usage

### Custom Workflow ID
```python
workflow = await orchestrator.run_workflow(
    user_input="requirements",
    workflow_id="my-custom-id"
)
```

### Access Workflow History
```python
for response in workflow.history:
    print(f"{response.agent_type}: {response.status}")
```

### Retrieve Workflow Results
```python
workflow_state = orchestrator.get_workflow_status(workflow_id)
all_workflows = orchestrator.get_all_workflows()
```

## Extending the System

### Add a New Agent

1. Create a new directory under `src/agents/`
2. Extend `BaseAgent`
3. Implement the `execute` method
4. Add to orchestrator

### Add a New Workflow Phase

1. Add phase to `WorkflowPhase` enum
2. Create corresponding agent
3. Add execution method to orchestrator
4. Call method in `run_workflow()`

## LLM Integration

Each agent can be enhanced with LLM capabilities:

```python
from src.config import get_config

class CustomAgent(BaseAgent):
    async def execute(self, task: Task) -> AgentResponse:
        config = get_config()
        # Use config.llm_provider, config.llm_model, etc.
        # Integrate with your preferred LLM API
```

## Roadmap

- [ ] Integration with popular LLM APIs (OpenAI, Anthropic, etc.)
- [ ] Export to design tools (Figma, Adobe XD, Sketch)
- [ ] Real-time collaboration features
- [ ] Advanced caching for similar projects
- [ ] Web UI for workflow visualization
- [ ] Mobile app support
- [ ] A/B testing integration

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch
3. Write tests for new features
4. Submit a pull request

## License

MIT License - see LICENSE file for details

## Support

For issues, questions, or suggestions:
- 📧 Open an issue on GitHub
- 💬 Create a discussion
- 📖 Check the documentation

## Author

Built with ❤️ by Krishna

---

**Ready to transform your UX design process?** Start by running the example:

```bash
python -m src.main
```
