# 🗺️ Project Navigation Guide

A complete guide to navigating and understanding the AI UX Design Workflow project structure.

## 📍 Start Here

### For Project Overview
👉 **[README.md](README.md)** - Main project description and quick start

### For Visual Summary
👉 **[BUILD_SUMMARY.md](BUILD_SUMMARY.md)** - Build completion summary with statistics

### For File Organization
👉 **[STRUCTURE.md](STRUCTURE.md)** - Detailed directory and file structure

## 📚 Documentation

### Understanding the System
1. **[Architecture.md](docs/architecture.md)** - System design and components
   - System architecture diagram
   - Workflow phases explanation
   - Component structure
   - Data flow
   - Design patterns
   - Extensibility guidelines

2. **[API Reference](docs/api.md)** - Complete API documentation
   - BaseAgent class
   - All agent classes (Requirements, Designer, Prototyper, Evaluator, Orchestrator)
   - Type definitions
   - Configuration options
   - Utility functions

3. **[Usage Guide](docs/usage.md)** - How to use the system
   - Quick start instructions
   - Advanced usage examples
   - Configuration setup
   - Logging configuration
   - Testing procedures
   - Troubleshooting

## 💻 Source Code Navigation

### Entry Point
**[src/main.py](src/main.py)**
- Example usage of the entire workflow
- Shows how to run a complete design workflow
- Demonstrates output handling

### Core Agents

#### Requirements Analysis
**[src/agents/requirements_analyst/agent.py](src/agents/requirements_analyst/agent.py)**
- Analyzes user requirements
- Extracts user stories and acceptance criteria
- Returns requirements specification

#### UX Design
**[src/agents/ux_designer/agent.py](src/agents/ux_designer/agent.py)**
- Creates design systems and wireframes
- Defines color palettes and typography
- Returns design specification

#### Prototyping
**[src/agents/prototyper/agent.py](src/agents/prototyper/agent.py)**
- Builds interactive prototypes
- Defines interactions and animations
- Returns prototype specification

#### Evaluation
**[src/agents/evaluator/agent.py](src/agents/evaluator/agent.py)**
- Evaluates designs against requirements
- Assesses quality and compliance
- Returns evaluation report with score

#### Workflow Orchestration
**[src/agents/orchestrator/agent.py](src/agents/orchestrator/agent.py)**
- Coordinates all agents
- Manages workflow phases
- Maintains workflow state
- **KEY FILE** - Shows how agents work together

#### Base Agent (Abstract)
**[src/agents/base_agent.py](src/agents/base_agent.py)**
- Abstract base class for all agents
- Provides common functionality
- Shows agent pattern

### Type Definitions

**[src/types/models.py](src/types/models.py)**
- WorkflowState - Complete workflow output
- Task - Agent task definition
- AgentResponse - Standard response format
- Enums: AgentType, WorkflowPhase, TaskStatus, Priority
- Other models: Message, WorkflowState

### Configuration

**[src/config/config.py](src/config/config.py)**
- WorkflowConfig class with all settings
- Configuration loading from environment and YAML
- LLM provider settings
- Application settings

### Utilities

**[src/utils/logging_utils.py](src/utils/logging_utils.py)**
- Logging setup
- Logger creation
- Support for loguru and standard logging

**[src/utils/file_utils.py](src/utils/file_utils.py)**
- JSON save/load operations
- Directory management
- Dictionary utilities

## 🧪 Testing

### Unit Tests
**[tests/unit/test_agents.py](tests/unit/test_agents.py)**
- Tests for each agent type
- Task execution tests
- Status retrieval tests
- 10+ test cases

### Integration Tests
**[tests/integration/test_workflow.py](tests/integration/test_workflow.py)**
- Complete workflow execution tests
- Workflow persistence tests
- Multiple workflow handling

### Test Configuration
**[tests/conftest.py](tests/conftest.py)**
- Pytest fixtures
- Event loop setup for async tests

## ⚙️ Configuration Files

### Application Configuration
**[pyproject.toml](pyproject.toml)**
- Project metadata
- Build system configuration
- Tool configurations (black, isort, mypy, pytest)
- Dependency specifications

### Dependencies
**[requirements.txt](requirements.txt)** - Production dependencies
**[requirements-dev.txt](requirements-dev.txt)** - Development dependencies

### Environment Setup
**[.env.example](.env.example)** - Template for environment variables
**[config/workflow.example.yaml](config/workflow.example.yaml)** - Example YAML configuration

### Git Configuration
**[.gitignore](.gitignore)** - Files to ignore in git
**[LICENSE](LICENSE)** - MIT License

## 📊 Quick Reference

### Workflow Execution Flow
```
User Input
  ↓
Orchestrator.run_workflow()
  ├─→ RequirementsAnalystAgent
  ├─→ UXDesignerAgent  
  ├─→ PrototyperAgent
  ├─→ EvaluatorAgent
  ↓
WorkflowState (complete output)
```

### Key Classes
- **BaseAgent** - Abstract base for all agents
- **RequirementsAnalystAgent** - Requirements analysis
- **UXDesignerAgent** - Design creation
- **PrototyperAgent** - Prototype development
- **EvaluatorAgent** - Quality evaluation
- **OrchestratorAgent** - Workflow coordination

### Key Models
- **WorkflowState** - Workflow output
- **Task** - Agent task
- **AgentResponse** - Agent response
- **WorkflowPhase** - Phase enumeration
- **TaskStatus** - Status enumeration

## 🔍 How to Read the Code

### For Understanding Agents
1. Read [BaseAgent](src/agents/base_agent.py) first
2. Then read any specific agent (e.g., [RequirementsAnalystAgent](src/agents/requirements_analyst/agent.py))
3. Notice how they extend BaseAgent and implement execute()

### For Understanding Workflow
1. Read [OrchestratorAgent](src/agents/orchestrator/agent.py)
2. Notice how it initializes all agents
3. See how run_workflow() calls each phase

### For Understanding Data Flow
1. Check [WorkflowState](src/types/models.py) model
2. See how it's passed between methods
3. Notice the history tracking

### For Understanding Configuration
1. Read [config.py](src/config/config.py)
2. See environment variable handling
3. Check how configuration is used in agents

## 🚀 Getting Started Guide

### Step 1: Explore Documentation
- Start with [README.md](README.md)
- Read [BUILD_SUMMARY.md](BUILD_SUMMARY.md)
- Review [Architecture.md](docs/architecture.md)

### Step 2: Understand the Code
- Look at [src/main.py](src/main.py) for example usage
- Read [OrchestratorAgent](src/agents/orchestrator/agent.py)
- Check one agent implementation

### Step 3: Run the System
```bash
# Install dependencies
pip install -r requirements.txt

# Run example
python -m src.main

# Run tests
pytest tests/ -v
```

### Step 4: Customize
- Modify agents for your use case
- Add new agents following the pattern
- Integrate with LLMs
- Export to design tools

## 📋 File Checklist

### Essential Files
- ✅ [README.md](README.md) - Project description
- ✅ [src/agents/orchestrator/agent.py](src/agents/orchestrator/agent.py) - Workflow coordinator
- ✅ [src/main.py](src/main.py) - Entry point
- ✅ [src/types/models.py](src/types/models.py) - Data models

### Documentation
- ✅ [docs/architecture.md](docs/architecture.md) - System design
- ✅ [docs/api.md](docs/api.md) - API reference
- ✅ [docs/usage.md](docs/usage.md) - Usage guide
- ✅ [BUILD_SUMMARY.md](BUILD_SUMMARY.md) - Build summary
- ✅ [STRUCTURE.md](STRUCTURE.md) - Detailed structure

### Configuration
- ✅ [pyproject.toml](pyproject.toml) - Project config
- ✅ [requirements.txt](requirements.txt) - Dependencies
- ✅ [.env.example](.env.example) - Environment template
- ✅ [LICENSE](LICENSE) - License file

### Testing
- ✅ [tests/unit/test_agents.py](tests/unit/test_agents.py) - Unit tests
- ✅ [tests/integration/test_workflow.py](tests/integration/test_workflow.py) - Integration tests

## 🎯 Common Tasks

### Run the Workflow
See [src/main.py](src/main.py) for example

### Add a New Agent
1. Create directory under [src/agents/](src/agents/)
2. Extend BaseAgent from [src/agents/base_agent.py](src/agents/base_agent.py)
3. Implement execute() method
4. Add to OrchestratorAgent in [src/agents/orchestrator/agent.py](src/agents/orchestrator/agent.py)

### Add a New Phase
1. Add phase to WorkflowPhase enum in [src/types/models.py](src/types/models.py)
2. Create agent for the phase
3. Add method to OrchestratorAgent
4. Call method in run_workflow()

### Configure the System
1. Copy [.env.example](.env.example) to .env
2. Set environment variables
3. Or use [config/workflow.example.yaml](config/workflow.example.yaml) for YAML config

### Run Tests
```bash
# All tests
pytest tests/ -v

# Specific test file
pytest tests/unit/test_agents.py -v

# With coverage
pytest tests/ --cov=src --cov-report=html
```

## 📞 Need Help?

1. **Understanding System**: Read [Architecture.md](docs/architecture.md)
2. **Using the System**: Read [Usage.md](docs/usage.md)
3. **API Questions**: Check [API.md](docs/api.md)
4. **Code Examples**: See [src/main.py](src/main.py) or test files
5. **Troubleshooting**: Read [Usage.md](docs/usage.md) troubleshooting section

---

**Happy coding!** 🚀

*Last Updated: November 24, 2026*
