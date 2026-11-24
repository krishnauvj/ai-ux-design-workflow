"""Configuration management for the workflow."""
from pathlib import Path
from typing import Optional, Dict, Any
import os
from dotenv import load_dotenv
import yaml
from pydantic_settings import BaseSettings


class WorkflowConfig(BaseSettings):
    """Configuration for the workflow system."""
    
    # Application settings
    app_name: str = "ai-ux-design-workflow"
    debug: bool = False
    log_level: str = "INFO"
    
    # Agent settings
    max_agents: int = 10
    agent_timeout: int = 300
    
    # API settings
    api_timeout: int = 30
    max_retries: int = 3
    
    # Workflow settings
    enable_persistence: bool = True
    output_dir: str = "outputs"
    
    # LLM settings (can be overridden for different LLM providers)
    llm_provider: str = "openai"
    llm_model: str = "gpt-4"
    llm_temperature: float = 0.7
    llm_max_tokens: int = 2048
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


def load_config(config_path: Optional[str] = None) -> WorkflowConfig:
    """Load configuration from environment and optional YAML file."""
    load_dotenv()
    
    config = WorkflowConfig()
    
    if config_path and Path(config_path).exists():
        with open(config_path, "r") as f:
            yaml_config = yaml.safe_load(f)
            if yaml_config:
                for key, value in yaml_config.items():
                    if hasattr(config, key):
                        setattr(config, key, value)
    
    return config


def get_config() -> WorkflowConfig:
    """Get the application configuration."""
    return load_config()
