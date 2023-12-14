from sqlalchemy import Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

engine = create_engine("postgresql://localhost/portfolio_db_test_1")


# declarative base class
class Base(DeclarativeBase):
    pass


class Collision(Base):
    __tablename__ = 'collision'

    id: Mapped[str] = mapped_column(primary_key=True)
    source: Mapped[str]
    collision_type: Mapped[str]
    severity: Mapped[str]
    vehicle_count: Mapped[int]
    pedestrian_count: Mapped[int]
    injuries: Mapped[int]
    pedestrian_cycle_count[int]
    report_number: Mapped[str]


    def __repr__(self):
        return f'Collision(id={self.id},source={self.source} collision_type={self.collision_type}, severity={self.severity}, vehicle_count={self.vehicle_count}, pedestrian_count={self.pedestrian_count}, injuries={self.injuries}, pedestrian_cycle_count={self.pedestrian_cycle_count}, report_number={self.report_number})'


class Vehicle(Base):
    __tablename__ = 'vehicle'

    vehicle_type: mapped[str]
    vehicle_condition: Mapped[str]
    vehicle_action: Mapped[str]
    report_number: Mapped[str]

    def __repr__(self):
        return f'Vehicle(id={self.id}, vehicle_type={self.vehicle_type}, vehicle_condition={self.vehicle_condition}, vehicle_action={self.vehicle_action}, report_number={self.report_number})'


class Location(Base):
    __tablename__ = 'location'

    lat: Mapped[float]
    lon: Mapped[float]
    location_type: Mapped[str]
    address: mapped[str]
    road_surface: Mapped[str]
    traffic_control: Mapped[str]
    posted_speed: mapped[float]
    report_number: Mapped[str]

    def __repr__(self):
        return f'Location(lat={self.lat}, lon={self.lon}, location_type={self.location_type}, address={self.address}, road_surface={self.road_surface}, traffic_control={self.traffic_control}, posted_speed={self.posted_speed}, report_number={self.report_number})'


class Date(Base):
    __tablename__ = 'date'

    incident_date: Mapped[str]
    modified_date: Mapped[str]
    report_number: Mapped[str]

    def __repr__(self):
        return f'Date(incident_date={self.incident_date}, modified_date={self.modified_date}, report_number={self.report_number})'


Base.metadata.create_all(engine)

