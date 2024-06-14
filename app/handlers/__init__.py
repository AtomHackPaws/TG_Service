from app.handlers.start import start_router
from app.handlers.user import profile_router
from app.handlers.community import comunity_router
from app.handlers.model import model_router

list_of_routes = [
    start_router,
    profile_router,
    comunity_router,
    model_router,
]

__all__ = [
    "list_of_routes",
]
