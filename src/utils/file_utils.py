"""Utility functions for the workflow."""
import json
from pathlib import Path
from typing import Any, Dict, Optional


def save_json(data: Any, file_path: str) -> None:
    """Save data to a JSON file.
    
    Args:
        data: Data to save
        file_path: Path to save file
    """
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2, default=str)


def load_json(file_path: str) -> Dict[str, Any]:
    """Load data from a JSON file.
    
    Args:
        file_path: Path to load file
        
    Returns:
        Loaded data
    """
    with open(file_path, "r") as f:
        return json.load(f)


def ensure_directory(directory: str) -> Path:
    """Ensure a directory exists.
    
    Args:
        directory: Directory path
        
    Returns:
        Path object
    """
    path = Path(directory)
    path.mkdir(parents=True, exist_ok=True)
    return path


def merge_dicts(base: Dict[str, Any], updates: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merge dictionaries.
    
    Args:
        base: Base dictionary
        updates: Updates to merge
        
    Returns:
        Merged dictionary
    """
    result = base.copy()
    for key, value in updates.items():
        if isinstance(value, dict) and key in result and isinstance(result[key], dict):
            result[key] = merge_dicts(result[key], value)
        else:
            result[key] = value
    return result
