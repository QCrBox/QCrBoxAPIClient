from enum import Enum


class CalculationStatusDetailsStatus(str, Enum):
    CANCELLED = "cancelled"
    FAILED = "failed"
    RUNNING = "running"
    SUBMITTED = "submitted"
    SUCCESSFUL = "successful"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
