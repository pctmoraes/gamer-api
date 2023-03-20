from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Gamer(Base):
    __tablename__ = 'gamer'

    nickname = Column(String(20), primary_key=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    characters = relationship('Character', backref='gamer', lazy='subquery', cascade='all, delete')


class Character(Base):
    __tablename__ = 'character'

    name = Column(String(20), primary_key=True, nullable=False)
    gamer_nickname = Column(String, ForeignKey('gamer.nickname', ondelete='CASCADE'))