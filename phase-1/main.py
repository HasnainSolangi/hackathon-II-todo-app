"""Main entry point for the Todo application."""

from src.cli.todo_cli import TodoCLI


def main():
    """Run the Todo application."""
    cli = TodoCLI()
    cli.run()


if __name__ == "__main__":
    main()