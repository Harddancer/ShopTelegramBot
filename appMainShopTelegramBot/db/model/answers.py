from sqlalchemy import Column, DateTime, Integer, ForeignKey,String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from product import Products

Base = declarative_base()

class Answers(Base):
    """
    Класс для создания таблицы "Отзывы",
    основан на декларативном стиле SQLAlchemy
    """
    __tablename__ = "answers"
    
    id = Column(Integer, primary_key=True)
    text = Column(String)
    data = Column(DateTime)
    product_id = Column(Integer, ForeignKey('products.id'))
    name_product = Column(String)
    user_id = Column(Integer)

    answers = relationship(
        Products,
        backref=backref('answers',
                        uselist=True,
                        cascade='delete,all')
    )

    def __str__(self):
        return f"{self.name_product}{self.text}{self.user_id}"
    