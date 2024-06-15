import enum
from aiogram.fsm.state import State, StatesGroup
from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InputMediaPhoto

from app.callbacks_factory.base import CommunityCallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from app.callbacks_factory.base import UserCallbackData

from magic_filter import F


def get_quiz_buttons() -> InlineKeyboardButton:
    inline_kb_full = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Да",
                    callback_data=CommunityCallbackData(action="anonymous_yes").pack(),
                ),
                InlineKeyboardButton(
                    text="Нет",
                    callback_data=CommunityCallbackData(action="anonymous_no").pack(),
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Назад", callback_data=UserCallbackData(action="start").pack()
                )
            ],
        ],
    )
    return inline_kb_full


class QuizEnum(int, enum.Enum):
    adj = 0
    int = 1
    geo = 2
    pro = 3
    non = 4
    background = 5


router = Router()


class QuizOrder(StatesGroup):
    upload_media = State()
    choosing_defect = State()
    escape_quiz = State()


@router.callback_query(CommunityCallbackData.filter(F.action == "quiz"))
async def community_ask_anonymous(callback: CallbackQuery, state: FSMContext):
    # async with Transaction():
    #     variance = await Quiz.get_quiz()
    # var = random.choices(variance)

    await callback.message.edit_media(
        media=InputMediaPhoto(
            media="http://81.200.149.209:9201/api/v1/download-shared-object/http:%2F%2Flocalhost:9000%2Fatomic-bucket%2Fquiz%2F6%2520%252863%2529.jpg%3FX-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=0O9MG175QY49SX9Z6FJ7%252F20240615%252Fus-east-1%252Fs3%252Faws4_request&X-Amz-Date=20240615T204606Z&X-Amz-Expires=43200&X-Amz-Security-Token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NLZXkiOiIwTzlNRzE3NVFZNDlTWDlaNkZKNyIsImV4cCI6MTcxODUwMjA4MSwicGFyZW50IjoiYXRvbSJ9.c4zZh_uaUskPpuTSzfpsD5BCz6_UW3ohL0r_M59nzpgsobZE8j8dR4aLzG_SFfrwuEYmzIkSEhvVJ-r69szS-A&X-Amz-SignedHeaders=host&versionId=null&X-Amz-Signature=de1262d0e36b84f81b35099809791f9b20a24db3785c24c704299e9899fcad70",
            caption="Выберите дефект",
        )
    )
    await callback.message.edit_text(
        text="Выберите тип дефекта", reply_markup=get_quiz_buttons()
    )


# @router.message(Command(commands=["quiz"]))
# async def start_quiz(message: Message):
#     try:
#         await S3Service.get_s3_client()
#         async with Transaction():
#             variance = await Quiz.get_quiz()

#             random.choices(variance)

#         await message.answer (random.choices(variance))
#     finally:
#         await S3Service.close_s3_session()
