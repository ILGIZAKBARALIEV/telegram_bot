
from aiogram import Bot, Dispatcher, Router,F
from aiogram.filters import Command
from aiogram import types
from  aiogram.fsm.context import FSMContext
from  aiogram.fsm.state import  State,StatesGroup
from bot_config import  database

dish_router = Router()
dish_router.message.filter(
    F.from_user.id ==  7107548042
)
class Dish(StatesGroup):
    name = State()
    price = State()
    description = State()
    category= State()
    portion = State()


@dish_router.message(Command("dish_add"))
async def start_review(message,state:FSMContext):
    await message.answer("what's dish name?")
    await state.set_state(Dish.name)



@dish_router.message (Dish.name)
async  def process_name (m:types.Message,state:FSMContext):
    await  state.update_data(name=m.text)
    await m.answer("what's your price?")
    await  state.set_state(Dish.price)

@dish_router.message (Dish.price)
async  def process_name (m:types.Message,state:FSMContext):
    await  state.update_data(price=m.text)
    await m.answer("what's your discription?")
    await  state.set_state(Dish.description)

@dish_router.message (Dish.description)
async  def process_name (m:types.Message,state:FSMContext):
    await state.update_data(desc=m.text)
    await m.answer("what's the category")
    await  state.set_state(Dish.category)

@dish_router.message (Dish.category)
async  def process_name (m:types.Message,state:FSMContext):
    await state.update_data(cat=m.text)
    await m.answer("what's your portion?")
    await  state.set_state(Dish.portion)

@dish_router.message(Dish.portion)
async  def process_portion_data(m:types.Message,state:FSMContext):
    await state.update_data(portion=m.text)
    data = await state.get_data()
    await m.answer(f"name:{data['name']}\n, price:{data['price']}\n, desc:{data['desc']}\n, portion:{data['portion']}\n")
    database.save_dish(data)
    await state.clear()



