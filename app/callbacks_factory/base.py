from aiogram.filters.callback_data import CallbackData


class UserCallbackData(CallbackData, prefix="my"):
    action: str


class CommunityCallbackData(CallbackData, prefix="community"):
    action: str


class ModelCallbackData(CallbackData, prefix="model"):
    action: str
