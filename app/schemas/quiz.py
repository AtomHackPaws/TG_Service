from enum import Enum


class QuizEnum(int, Enum):
    adj = 0
    int = 1
    geo = 2
    pro = 3
    non = 4
    background = 5

    def get_enum_name_by_value(value):
        try:
            return QuizEnum(value).name
        except ValueError:
            return None


deffects_name = {
    "adj": "Прилегающие деффекты",
    "int": "Деффект целостности",
    "geo": "Деффект геометри",
    "pro": "Деффект постобработки",
    "non": "Деффект невыполнения",
    "background": "Нет деффектов",
}
