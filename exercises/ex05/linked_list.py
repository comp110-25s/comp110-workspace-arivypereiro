"""Exercise for linked lists."""

from __future__ import annotations

__author__: str = "730671996"


class Node:
    """Creating a Node Class."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Initializing Node Class."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Magic Method."""
        if self.next is None:
            return f"{self.value} -> None"
        else:
            return f"{self.value} -> {self.next}"


def value_at(head: Node | None, index: int) -> int:
    """Return value of the Node stored at the given index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    elif index == 0:
        return head.value
    else:
        return value_at(head=head.next, index=index - 1)


def max(head: Node | None) -> int:
    """Return maximum value in linked list."""
    if head is None:
        raise ValueError("Cannot call max with None")
    elif head.next is None:
        return head.value
    else:
        if head.value > max(head=head.next):
            return head.value
        else:
            return max(head=head.next)


def linkify(items: list[int]) -> Node | None:
    """Turn input list into list of Node."""
    if len(items) == 0:
        return None
    elif len(items) == 1:
        return Node(value=items[0], next=None)
    else:
        return Node(value=items[0], next=linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Scale values."""
    if head is None:
        return None
    elif head.next is None:
        return Node(value=head.value * factor, next=None)
    else:
        return Node(
            value=head.value * factor, next=scale(head=head.next, factor=factor)
        )
