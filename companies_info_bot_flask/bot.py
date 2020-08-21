import config
import logging
import sqlalchemy
from aiogram import Bot, Dispatcher, executor, types
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import mapper, sessionmaker

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.API_TOKEN)

dp = Dispatcher(bot)

engine = sqlalchemy.create_engine(config.SQLALCHEMY_DATABASE_URL, echo=False)
metadata = MetaData()

class Car(object):
    def __init__(self, reg_year=None, reg_month=None, vehicle_year=None, vehicle_age_category=None, mark=None,
                 model=None, vehicle_category_wide=None, vehicle_category=None, empty_weight=None, plated_weight=None,
                 engine_volume=None, owner_type=None, region=None, area_kato=None, area=None, vehicle_count=None,
                 seating_count=None, vehicle_color=None, engine_power_kwt=None, add_information=None,
                 first_registration_date=None, chassis_number=None, VIN=None, manufacturer=None, origin_country=None,
                 car_number=None, name_company=None, BIN=None, kato=None):
        self.reg_year = reg_year
        self.reg_month = reg_month
        self.vehicle_year = vehicle_year
        self.vehicle_age_category = vehicle_age_category
        self.mark = mark
        self.model = model
        self.vehicle_category_wide = vehicle_category_wide
        self.vehicle_category = vehicle_category
        self.empty_weight = empty_weight
        self.plated_weight = plated_weight
        self.engine_volume = engine_volume
        self.owner_type = owner_type
        self.region = region
        self.area_kato = area_kato
        self.area = area
        self.vehicle_count = vehicle_count
        self.seating_count = seating_count
        self.vehicle_color = vehicle_color
        self.engine_power_kwt = engine_power_kwt
        self.add_information = add_information
        self.first_registration_date = first_registration_date
        self.chassis_number = chassis_number
        self.VIN = VIN
        self.manufacturer = manufacturer
        self.origin_country = origin_country
        self.car_number = car_number
        self.name_company = name_company
        self.BIN = BIN
        self.kato = kato

    def __repr__(self):
        return f"Car info: \n \
                   reg_year: {self.reg_year} \n \
                   reg_month: {self.reg_month} \n \
                   vehicle_year: {self.vehicle_year} \n \
                   vehicle_age_category: {self.vehicle_age_category} \n \
                   mark: {self.mark} \n \
                   model: {self.model} \n \
                   vehicle_category_wide: {self.vehicle_category_wide} \n \
                   vehicle_category: {self.vehicle_category} \n \
                   empty_weight: {self.empty_weight} \n \
                   plated_weight: {self.plated_weight} \n \
                   engine_volume: {self.engine_volume} \n \
                   owner_type: {self.owner_type} \n \
                   region: {self.region} \n \
                   area_kato: {self.area_kato} \n \
                   area: {self.area} \n \
                   vehicle_count: {self.vehicle_count} \n \
                   seating_count: {self.seating_count} \n \
                   vehicle_color: {self.vehicle_color} \n \
                   engine_power_kwt: {self.engine_power_kwt} \n \
                   add_information: {self.add_information} \n \
                   first_registration_date: {self.first_registration_date} \n \
                   chassis_number: {self.chassis_number} \n \
                   VIN: {self.VIN} \n \
                   manufacturer: {self.manufacturer} \n \
                   origin_country: {self.origin_country} \n \
                   car_number: {self.car_number} \n \
                   name_company: {self.name_company} \n \
                   BIN: {self.BIN} \n \
                   kato: {self.kato} \n \
                "

    def __str__(self):
        return f"Car info:\n \
                   reg_year: {self.reg_year} \n \
                   reg_month: {self.reg_month} \n \
                   vehicle_year: {self.vehicle_year} \n \
                   vehicle_age_category: {self.vehicle_age_category} \n \
                   mark: {self.mark} \n \
                   model: {self.model} \n \
                   vehicle_category_wide: {self.vehicle_category_wide} \n \
                   vehicle_category: {self.vehicle_category} \n \
                   empty_weight: {self.empty_weight} \n \
                   plated_weight: {self.plated_weight} \n \
                   engine_volume: {self.engine_volume} \n \
                   owner_type: {self.owner_type} \n \
                   region: {self.region} \n \
                   area_kato: {self.area_kato} \n \
                   area: {self.area} \n \
                   vehicle_count: {self.vehicle_count} \n \
                   seating_count: {self.seating_count} \n \
                   vehicle_color: {self.vehicle_color} \n \
                   engine_power_kwt: {self.engine_power_kwt} \n \
                   add_information: {self.add_information} \n \
                   first_registration_date: {self.first_registration_date} \n \
                   chassis_number: {self.chassis_number} \n \
                   VIN: {self.VIN} \n \
                   manufacturer: {self.manufacturer} \n \
                   origin_country: {self.origin_country} \n \
                   car_number: {self.car_number} \n \
                   name_company: {self.name_company} \n \
                   BIN: {self.BIN} \n \
                   kato: {self.kato} \n \
                "


cars_table = Table('cars', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('reg_year', String, nullable=True),
                   Column('reg_month', String, nullable=True),
                   Column('vehicle_year', String, nullable=True),
                   Column('vehicle_age_category', String, nullable=True),
                   Column('mark', String, nullable=True),
                   Column('model', String, nullable=True),
                   Column('vehicle_category_wide', String, nullable=True),
                   Column('vehicle_category', String, nullable=True),
                   Column('empty_weight', String, nullable=True),
                   Column('plated_weight', String, nullable=True),
                   Column('engine_volume', String, nullable=True),
                   Column('owner_type', String, nullable=True),
                   Column('region', String, nullable=True),
                   Column('area_kato', String, nullable=True),
                   Column('area', String, nullable=True),
                   Column('vehicle_count', String, nullable=True),
                   Column('seating_count', String, nullable=True),
                   Column('vehicle_color', String, nullable=True),
                   Column('engine_power_kwt', String, nullable=True),
                   Column('add_information', String, nullable=True),
                   Column('first_registration_date', String, nullable=True),
                   Column('chassis_number', String, nullable=True),
                   Column('VIN', String, nullable=True),
                   Column('manufacturer', String, nullable=True),
                   Column('origin_country', String, nullable=True),
                   Column('car_number', String, nullable=True),
                   Column('name_company', String, nullable=True),
                   Column('BIN', String, nullable=True),
                   Column('kato', String, nullable=True),
                   )
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
