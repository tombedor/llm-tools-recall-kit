from .tool import RecallKit, register_tools

# Create a standalone function that wraps the RecallKit.create_memory method
def create_memory(input: str) -> str:
    """
    Create a memory entry.

    This is a convenience function that wraps the RecallKit.create_memory method.
    """
    return RecallKit().create_memory(input)

__all__ = ["RecallKit", "register_tools", "create_memory"]
