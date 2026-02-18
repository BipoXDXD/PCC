"""
Sample tests for Python Crash Course chapters.
Run with: pytest
"""
import sys
import os

# Add parent directory to path to import chapter modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_ch01_main_exists():
    """Test that ch01 main module exists and can be imported."""
    from ch01 import main
    assert hasattr(main, 'main')


def test_ch01_main_function():
    """Test that ch01 main function works correctly."""
    from ch01 import main
    # Test that main function can be called without error
    result = main.main()
    assert result is None  # main() prints but returns None


def test_sample_addition():
    """Sample test to verify pytest is working."""
    assert 1 + 1 == 2


def test_sample_string():
    """Sample test for string operations."""
    message = "Hello, Python Crash Course!"
    assert "Python" in message
    assert message.startswith("Hello")

