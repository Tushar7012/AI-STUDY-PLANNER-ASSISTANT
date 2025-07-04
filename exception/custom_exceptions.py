# exception/custom_exceptions.py

from logger.logg import error_message_detail

class StudyPlannerException(Exception):
    """Base exception for the Study Planner application."""
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
        error_message_detail(self)

class SubjectNotFoundError(StudyPlannerException):
    """Raised when a subject is not found."""
    def __init__(self, subject: str):
        super().__init__(f"Subject not found: '{subject}'")
        self.subject = subject

class AvailabilityNotSetError(StudyPlannerException):
    """Raised when availability is requested but not set."""
    def __init__(self):
        super().__init__("Availability not set. Please use the availability tool first.")
