"""Reverse a list used as a stack with recursion only."""


def _remove_bottom[T](stack: list[T]) -> T:
    top = stack.pop()
    if not stack:
        return top
    bottom = _remove_bottom(stack)
    stack.append(top)
    return bottom


def reverse_stack[T](stack: list[T]) -> None:
    """Reverse ``stack`` in place without allocating another collection."""
    if not stack:
        return
    bottom = _remove_bottom(stack)
    reverse_stack(stack)
    stack.append(bottom)
