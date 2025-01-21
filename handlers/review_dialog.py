
from aiogram import Bot, Dispatcher, Router,F
from aiogram.filters import Command
from aiogram import types
from  aiogram.fsm.context import FSMContext
from  aiogram.fsm.state import  State,StatesGroup

review_router = Router()

class RestaurantReview(StatesGroup):
    name = State()
    instagram_username = State()
    rate = State()
    extra_comments = State()


@review_router.callback_query(F.data=='review')
async  def start_review(call:types.CallbackQuery,state:FSMContext):
    await call.message.answer("What's your name")
    await state.set_state(RestaurantReview.name)

@review_router.message(Command("stop"))
@review_router.message(F.text =="Стоп")
async def stop_review(call:types.CallbackQuery,state:FSMContext):
    await call.answer('enter your review stop bot by "/Stop" or "/Стоп" ')
    await call.message.answer("your review was saved")
    await state.clear()

@review_router.message (RestaurantReview.name)
async  def process_name (m:types.Message,state:FSMContext):
    instagram_username = m.text
    await  state.update_data(name=m.text)
    await state.update_data(name=m.text)
    await m.answer("what's your instagram?")
    await  state.set_state(RestaurantReview.instagram_username)

@review_router.message (RestaurantReview.instagram_username)
async  def process_name (m:types.Message,state:FSMContext):
    rate = m.text
    await  state.update_data(rate=m.text)
    await state.update_data(instagram_username=m.text)
    await m.answer("How would you rate our cafe?")
    await  state.set_state(RestaurantReview.rate)

@review_router.message (RestaurantReview.rate)
async  def process_name (m:types.Message,state:FSMContext):
    if m.text.isdigit():
        if 1>=int(m.text) <=5:
            await state.update_data(rate=m.text)
            await m.answer('your extra  comments?')
            await  state.set_state(RestaurantReview.extra_comments)
        else:
         await  m.answer("write only between 1 and 5!!:")
    else:
        await  m.answer("write only digits !!!")


@review_router.message (RestaurantReview.extra_comments)
async  def process_name (m:types.Message,state:FSMContext):
    review_text = m.text
    await  state.update_data(extra_comments=m.text)
    await state.get_data()
    data = await  state.get_data()
    await m.answer(f'name:{data["name"]}\n instagram: {data["instagram_username"]}\n rate:{data["rate"]}\n extra_comments: {data["extra_comments"]}')
    # all data_base saved here
    await  m.answer("thank you ")
    print(data)
    await  state.clear()