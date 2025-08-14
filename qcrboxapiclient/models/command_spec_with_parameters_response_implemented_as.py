from enum import Enum


class CommandSpecWithParametersResponseImplementedAs(str, Enum):
    CLI_COMMAND = "cli_command"
    INTERACTIVE_SESSION = "interactive_session"
    PYTHON_CALLABLE = "python_callable"

    def __str__(self) -> str:
        return str(self.value)
