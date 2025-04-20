"""Exercise for linked lists"""

__author__: str = "730671996"

class Node:
    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None ):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        if self.next is None:
            return f"{self.value} -> None"
        else:
            return f"{self.value} -> {self.next}"

def recursive_range(start:int, end:int) -> Node | None:
    if start < end:
        rest: Node | None = recursive_range(start= start + 1, end=end )
        return Node(start,rest)
    elif start == end:
        return None
    else:
        raise Exception ("start shouldn't be > end")

def value_at(head: Node | None, index: int) -> int:
    if index >= 1:
        rest: Node | None = recursive_range(start = head, end = index - 1 )
        return Node (head, rest)
    elif index = 0:
        return head
    else:
        raise IndexError("Index is out of bounds on the list.")
