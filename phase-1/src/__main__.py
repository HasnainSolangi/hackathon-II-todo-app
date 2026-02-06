"""Main module for the Todo application."""

from .cli.todo_cli import TodoCLI


def main():
    """Entry point for the application."""
    cli = TodoCLI()
    cli.run()


if __name__ == "__main__":
    main()