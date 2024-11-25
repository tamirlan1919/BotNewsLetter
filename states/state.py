from aiogram.fsm.state import State, StatesGroup

class Letter(StatesGroup):
    text = State()