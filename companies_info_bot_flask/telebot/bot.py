import config
import logging
import sqlalchemy
from aiogram import Bot, Dispatcher, executor, types
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import mapper, sessionmaker
from schema.schema import cars_table, Car, metadata
logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.API_TOKEN)

dp = Dispatcher(bot)

engine = sqlalchemy.create_engine(config.SQLALCHEMY_DATABASE_URL, echo=False)
# metadata = MetaData()
metadata.create_all(engine)
mapper(Car, cars_table)
Session = sessionmaker(bind=engine)
session = Session()

@dp.message_handler()
async def echo(message: types.Message):
    text = message.text
    if session.query(Car).filter_by(BIN=text).count() > 0:
        await message.answer("Find car by BIN")
        await(message.answer(session.query(Car).filter_by(BIN=text).first()))
    else:
        await message.answer("Not found car by BIN")
    if session.query(Car).filter_by(VIN=text).count() > 0:
        await message.answer("Find car by VIN")
        await(message.answer(session.query(Car).filter_by(VIN=text).first()))
    else:
        await message.answer("Not found car by VIN")
    if session.query(Car).filter_by(car_number=text).count() > 0:
        await message.answer("Find car by car_number")
        await(message.answer(session.query(Car).filter_by(car_number=text).first()))
    else:
        await message.answer("Not found car by car_number")


if __name__ == '__main__':
    print("Версия SQLAlchemy:", sqlalchemy.__version__)
    executor.start_polling(dp, skip_updates=True)
