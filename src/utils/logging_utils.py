"""Logging utilities for the workflow."""
import sys
import logging
from pathlib import Path
from typing import Optional
from loguru import logger as loguru_logger


def setup_logging(
    log_level: str = "INFO",
    log_file: Optional[str] = None,
    use_loguru: bool = True,
) -> None:
    """Setup logging configuration.
    
    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Optional log file path
        use_loguru: Whether to use loguru or standard logging
    """
    if use_loguru:
        # Remove default handler
        loguru_logger.remove()
        
        # Add console handler
        loguru_logger.add(
            sys.stderr,
            format="<level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>",
            level=log_level,
        )
        
        # Add file handler if specified
        if log_file:
            Path(log_file).parent.mkdir(parents=True, exist_ok=True)
            loguru_logger.add(
                log_file,
                format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function} - {message}",
                level=log_level,
                rotation="500 MB",
                retention="7 days",
            )
    else:
        # Standard logging configuration
        logging.basicConfig(
            level=getattr(logging, log_level.upper(), logging.INFO),
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        )
        
        if log_file:
            Path(log_file).parent.mkdir(parents=True, exist_ok=True)
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(getattr(logging, log_level.upper(), logging.INFO))
            logging.getLogger().addHandler(file_handler)


def get_logger(name: str) -> logging.Logger:
    """Get a logger instance.
    
    Args:
        name: Logger name (usually __name__)
        
    Returns:
        Logger instance
    """
    return logging.getLogger(name)
