from aiogram.fsm.state import State, StatesGroup


class UserActionState(StatesGroup):
    FIO = State() 
    Age = State()
    Email = State() 
    Phone = State()  
    message = State()
