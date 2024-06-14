from typing import Any, Mapping, Optional


class CommonException(Exception):
    def __init__(self, code: int, error: str) -> None:
        super().__init__()
        self.error = error
        self.code = code


class InternalServerError(Exception):
    status_code: int = 500
    message = "Something went wrong!"

    def __init__(self, message: Optional[str] = None, debug: Any = None) -> None:
        self.message = message or self.message
        self.debug = debug

    @classmethod
    def code(cls):
        return cls.__name__

    def to_json(self) -> Mapping:
        return {
            "code": self.status_code,
            "message": self.message,
            "debug": self.debug,
        }


class NotFoundException(CommonException):
    def __init__(self, error: str) -> None:
        super().__init__(404, error)


class BadRequest(CommonException):
    def __init__(self, error: str) -> None:
        super().__init__(400, error)


class ForbiddenException(CommonException):
    def __init__(self, error: str) -> None:
        super().__init__(403, error)


class UserNotFoundException(CommonException):
    def __init__(self, error: str) -> None:
        super().__init__(404, error)


class UserUnCorrectException(CommonException):
    def __init__(self, error: str) -> None:
        super().__init__(400, error)
