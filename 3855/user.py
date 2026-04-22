#!/usr/bin/env python3
"""Module defining a simple User class with type annotations."""


class User:
    """Represent a user with a name and an age."""

    def __init__(self, name: str, age: int) -> None:
        """Initialize a User instance.

        Args:
            name: The user's name.
            age: The user's age.
        """
        self.name: str = name
        self.age: int = age
      
