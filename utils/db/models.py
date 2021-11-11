from datetime import datetime

from sqlalchemy import Column, Integer, BigInteger, String, ForeignKey, Boolean, TIMESTAMP, CheckConstraint, MetaData
from sqlalchemy.orm import declarative_base
from sqlalchemy import update as sqlalchemy_update
from sqlalchemy.future import select
from sqlalchemy.orm import relationship

from utils.db.connect import async_db_session, Base

metadata = MetaData()


class ModelAdmin:
    @classmethod
    async def create(cls, **kwargs):
        async_db_session.add(cls(**kwargs))
        await async_db_session.commit()

    @classmethod
    async def update(cls, id, **kwargs):
        query = (
            sqlalchemy_update(cls)
                .where(cls.id == id)
                .values(**kwargs)
                .execution_options(synchronize_session="fetch")
        )

        await async_db_session.execute(query)
        await async_db_session.commit()

    @classmethod
    async def get(cls, id):
        query = select(cls).where(cls.id == id)
        results = await async_db_session.execute(query)
        (result,) = results.one()
        return result


class User(Base, ModelAdmin):
    __tablename__ = "user"
    id = Column(BigInteger, primary_key=True)
    first_name = Column(String(64))
    last_name = Column(String(64))
    username = Column(String(32))

    notification = Column(Boolean, nullable=False, default=True)
    active = Column(Boolean, nullable=False, default=True)
    created_at = Column(TIMESTAMP, default=datetime.now())
    lang = Column(String(2), CheckConstraint("lang in ('ru', 'uz')"), nullable=False)

    def __init__(self, **kw):
        super().__init__(**kw)
        self._views = list()

    @property
    def views(self):
        return self._views

    @views.setter
    def add_views(self, view):
        self._views.add(view)
