"""Pytest configuration and fixtures."""

import os
import sys
from pathlib import Path

import pytest

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Load .env file BEFORE any other imports
from dotenv import load_dotenv

load_dotenv(dotenv_path=project_root / ".env")

# Set default log level for tests
os.environ.setdefault("LOG_LEVEL", "DEBUG")


@pytest.fixture
def api_token():
    """Get API token from environment for integration tests."""
    token = os.environ.get("ACEDATACLOUD_API_TOKEN", "")
    if not token:
        pytest.skip("ACEDATACLOUD_API_TOKEN not configured for integration tests")
    return token


@pytest.fixture
def mock_image_response():
    """Mock successful image generation response."""
    return {
        "success": True,
        "task_id": "test-task-123",
        "trace_id": "test-trace-456",
        "data": [
            {
                "prompt": "a cute cat running across a meadow",
                "image_url": "https://platform.cdn.acedata.cloud/seedream/test-image.jpg",
                "size": "1024x1024",
            }
        ],
    }


@pytest.fixture
def mock_edit_response():
    """Mock successful image edit response."""
    return {
        "success": True,
        "task_id": "test-edit-789",
        "trace_id": "test-trace-012",
        "data": [
            {
                "prompt": "Change the background to a sunset beach",
                "image_url": "https://platform.cdn.acedata.cloud/seedream/test-edited.jpg",
                "size": "1024x1024",
            }
        ],
    }


@pytest.fixture
def mock_task_response():
    """Mock task query response."""
    return {
        "id": "task-123",
        "created_at": 1705788000.0,
        "type": "images",
        "request": {
            "prompt": "A test image",
            "model": "doubao-seedream-4-0-250828",
        },
        "response": {
            "success": True,
            "task_id": "task-123",
            "data": [
                {
                    "prompt": "A test image",
                    "image_url": "https://platform.cdn.acedata.cloud/seedream/test.jpg",
                }
            ],
        },
    }


@pytest.fixture
def mock_batch_task_response():
    """Mock batch task query response."""
    return {
        "count": 2,
        "items": [
            {
                "id": "task-001",
                "created_at": 1705788000.0,
                "response": {
                    "success": True,
                    "data": [
                        {
                            "image_url": "https://platform.cdn.acedata.cloud/seedream/img1.jpg",
                        }
                    ],
                },
            },
            {
                "id": "task-002",
                "created_at": 1705788100.0,
                "response": {
                    "success": True,
                    "data": [
                        {
                            "image_url": "https://platform.cdn.acedata.cloud/seedream/img2.jpg",
                        }
                    ],
                },
            },
        ],
    }


@pytest.fixture
def mock_error_response():
    """Mock error response."""
    return {
        "success": False,
        "error": {
            "code": "invalid_request",
            "message": "Invalid parameters provided",
        },
    }
