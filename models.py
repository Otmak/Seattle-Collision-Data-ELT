print('Entering Models.py!!!')
from typing import List
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

print('Starting....')


class Base(DeclarativeBase):
    pass


print('Base class done.......')


class Collision(Base):
    __tablename__ = 'collision'

    report_number: Mapped[str] = mapped_column(primary_key=True)
    source: Mapped[str]
    collision_type: Mapped[str]
    severity: Mapped[str]
    vehicle_count: Mapped[int]
    pedestrian_count: Mapped[int]
    fatalities: Mapped[int]
    serious_injuries: Mapped[int]
    injuries: Mapped[int]
    pedestrian_cycle_count: Mapped[int]

    vehicle: Mapped[List["Vehicle"]] = relationship()
    location: Mapped[List["Location"]] = relationship()
    date: Mapped[List["Date"]] = relationship()

    def __repr__(self):
        return f'Collision(id={self.report_number},source={self.source} collision_type={self.collision_type}, severity={self.severity}, vehicle_count={self.vehicle_count}, pedestrian_count={self.pedestrian_count}, fatalities={self.fatalities}, serious_injuries={self.serious_injuries}, injuries={self.injuries}, pedestrian_cycle_count={self.pedestrian_cycle_count})'


class Vehicle(Base):
    __tablename__ = 'vehicle'

    id: Mapped[int] = mapped_column(primary_key=True)
    vehicle_type: Mapped[str]
    vehicle_condition: Mapped[str]
    vehicle_action: Mapped[str]
    collision_report_number: Mapped[str] = mapped_column(ForeignKey("collision.id"))

    def __repr__(self):
        return f'Vehicle(id={self.id}, vehicle_type={self.vehicle_type}, vehicle_condition={self.vehicle_condition}, vehicle_action={self.vehicle_action}, report_number={self.collision_report_number})'


class Location(Base):
    __tablename__ = 'location'

    id: Mapped[int] = mapped_column(primary_key=True)
    lat: Mapped[float]
    lon: Mapped[float]
    location_type: Mapped[str]
    address: Mapped[str]
    road_condition: Mapped[str]
    weather: Mapped[str]
    light_condition: Mapped[str]
    speed: Mapped[float]
    collision_report_number: Mapped[str] = mapped_column(ForeignKey("collision.id"))

    def __repr__(self):
        return f'Location(lat={self.lat}, lon={self.lon}, location_type={self.location_type}, address={self.address}, road_condition={self.road_condition}, weather={self.weather}, light_condition={self.light_condition} speed={self.speed}, report_number={self.collision_report_number})'


class Date(Base):
    __tablename__ = 'date'

    id: Mapped[int] = mapped_column(primary_key=True)
    incident_date: Mapped[str]
    modified_date: Mapped[str]
    added_date: Mapped[str]
    collision_report_number: Mapped[str] = mapped_column(ForeignKey("collision.id"))

    def __repr__(self):
        return f'Date( id={self.id}, incident_date={self.incident_date}, modified_date={self.modified_date}, added_date={self.added_date} report_number={self.collision_report_number})'



