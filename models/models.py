from uuid_v7.base import uuid7
from datetime import datetime
from sqlalchemy import ForeignKey, func
from sqlalchemy import Column, String, Text, DateTime, Integer, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base import Base

class Championship(Base):
    __tablename__ = "championship"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), default=uuid7(), unique=True, primary_key=True, nullable=False) # UUID as string
    chmName: Mapped[str] = mapped_column(unique=True, nullable=False)
    dateInit: Mapped[datetime] = mapped_column(default = func.now(), nullable=False)
    dateEnd: Mapped[datetime] = mapped_column(nullable=True)
    createdAt: Mapped[datetime] = mapped_column(default = func.now())
    updatedAt: Mapped[datetime] = mapped_column(default = func.now(), onupdate=func.now())

class Participant(Base):

    __tablename__ = "participant"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), default=uuid7(), unique=True, primary_key=True, nullable=False) # UUID as string
    prtName: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    alias: Mapped[str] = mapped_column(unique=True, nullable=True, default=None)
    createdAt: Mapped[datetime] = mapped_column(default = func.now())
    updatedAt: Mapped[datetime] = mapped_column(default = func.now(), onupdate=func.now())
    
class Classification(Base):
    __tablename__ = "classification"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), default=uuid7(), unique=True, primary_key=True, nullable=False) # UUID as string
    points: Mapped[int] = mapped_column(Integer, unique=False, index=True, nullable=False, default=0) # This field is subject to change
    prtId: Mapped[str] = mapped_column(ForeignKey("participant.id"))
    chmId: Mapped[str] = mapped_column(ForeignKey("championship.id"))
    createdAt: Mapped[datetime] = mapped_column(default = func.now())
    updatedAt: Mapped[datetime] = mapped_column(default = func.now(), onupdate=func.now())

class Result(Base):
    __tablename__ = "result"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), default=uuid7(), unique=True, primary_key=True, nullable=False) # UUID as string
    position: Mapped[int] = mapped_column(Integer, unique=False, index=True, nullable=False, default=0) # 0 means it is not set or counted
    prtId: Mapped[str] = mapped_column(ForeignKey("participant.id"))
    racId: Mapped[str] = mapped_column(ForeignKey("race.id"))
    createdAt: Mapped[datetime] = mapped_column(default = func.now())
    updatedAt: Mapped[datetime] = mapped_column(default = func.now(), onupdate=func.now())

class Race(Base):
    __tablename__ = "race"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), default=uuid7(), unique=True, primary_key=True, nullable=False) # UUID as string
    prtId: Mapped[str] = mapped_column(ForeignKey("combo.id"))
    chmId: Mapped[str] = mapped_column(ForeignKey("championship.id"))
    createdAt: Mapped[datetime] = mapped_column(default = func.now())
    updatedAt: Mapped[datetime] = mapped_column(default = func.now(), onupdate=func.now())

class Combo(Base):
    __tablename__ = "combo"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), default=uuid7(), unique=True, primary_key=True, nullable=False) # UUID as string
    cars: Mapped[str] = mapped_column(index=True, nullable=False)
    circuit: Mapped[str] = mapped_column(index=True, nullable=True)
    createdAt: Mapped[datetime] = mapped_column(default = func.now())
    updatedAt: Mapped[datetime] = mapped_column(default = func.now(), onupdate=func.now())
    
class PointsSystem(Base):
    __tablename__ = "points_system"

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), default=uuid7(), unique=True, primary_key=True, nullable=False) # UUID as string
    position: Mapped[int] = mapped_column(Integer, unique=True, index=True, nullable=False, default=0) 
    points: Mapped[int] = mapped_column(Integer, unique=False, index=True, nullable=False, default=0)
    chmId: Mapped[str] = mapped_column(ForeignKey("championship.id"))
    createdAt: Mapped[datetime] = mapped_column(default = func.now())
    updatedAt: Mapped[datetime] = mapped_column(default = func.now(), onupdate=func.now())
    
    __table_args__ = (
        CheckConstraint("position >= 1 AND position <= 30", name="check_position_range"), # Number is subject to change
    )