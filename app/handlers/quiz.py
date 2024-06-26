from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from app.callbacks_factory.base import QuizCallbackData
from app.keyboards.quiz import (
    get_quiz_buttons,
    get_start_quiz_buttons,
    get_continue_quiz_buttons,
)
from magic_filter import F
from aiogram.types import URLInputFile
from app.config import settings
from app.db import Transaction
from app.models.quiz import Quiz
from app.states.quiz import QuizState
from app.schemas.quiz import deffects_name, QuizEnum

quiz_router = Router()


@quiz_router.callback_query(QuizCallbackData.filter(F.action == "quiz"))
async def community_ask_anonymous(callback: CallbackQuery, state: FSMContext):
    image = URLInputFile(
        settings.s3_url + "/test_image.png", filename="python-logo.png"
    )
    await callback.message.delete()
    await callback.message.answer_photo(
        photo=image,
        caption="Брось вызов своей точке зрения!",
        reply_markup=get_start_quiz_buttons(),
    )


@quiz_router.callback_query(QuizCallbackData.filter(F.action == "start"))
async def quiz_start(callback: CallbackQuery, state: FSMContext):
    async with Transaction():
        quiz = await Quiz.get_random_select()
    await state.set_state(QuizState.answer)
    await state.update_data(
        photo_base=quiz.id_photo, photo_mark=quiz.id_mark, label=quiz.label
    )
    image = URLInputFile(
        settings.s3_url + "/quiz/" + quiz.id_photo, filename="python-logo.jpg"
    )

    await callback.message.delete()
    await callback.message.answer_photo(
        photo=image, caption="Найди деффект!", reply_markup=get_quiz_buttons()
    )


@quiz_router.callback_query(QuizCallbackData.filter, QuizState.answer)
async def quiz_check_answer(callback: CallbackQuery, state: FSMContext):
    base_caption = "Правильный ответ:"
    data_quiz = await state.get_data()
    name = QuizEnum.get_enum_name_by_value(data_quiz["label"])
    normal_name = deffects_name[name]
    base_caption += f"\n {normal_name}"
    if name in callback.data:
        base_caption += "\n Ты прав!"
    else:
        base_caption += "\n Ты ошибся :( \n Присмотрись."
    await state.set_state(QuizState.start)
    image_mark = URLInputFile(
        settings.s3_url + "/quiz/" + data_quiz["photo_mark"], filename="python-logo.jpg"
    )
    await callback.message.delete()
    await callback.message.answer_photo(
        photo=image_mark, caption=base_caption, reply_markup=get_continue_quiz_buttons()
    )
