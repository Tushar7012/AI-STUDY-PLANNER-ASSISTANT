# exception/custom_exceptions.py

import sys
from logger.logg import error_message_detail

class PlannerException(Exception):
    """Base class for all Planner-related exceptions."""
    def __init__(self, message: str):
        super().__init__(message)
        # Log detailed error
        error_message_detail(self)

class SubjectNotFoundError(PlannerException):
    """Raised when a requested subject does not exist."""
    def __init__(self, subject: str):
        message = f"Subject not found: '{subject}'"
        super().__init__(message)
        self.subject = subject

class AvailabilityNotSetError(PlannerException):
    """Raised when availability has not been set but is required."""
    def __init__(self):
        message = "Availability is not set. Please run set_availability first."
        super().__init__(message)

class PlanNotGeneratedError(PlannerException):
    """Raised when attempting to access a study plan that hasn't been generated."""
    def __init__(self):
        message = "No study plan found. Please run generate_study_plan first."
        super().__init__(message)
