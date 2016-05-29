from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = relationship("Address", back_populates="person")
    def __repr__(self):
        return "<Class Person id=%s name=%s>" % (self.id, self.name)
class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship("Person", back_populates="address")
    def __repr__(self):
        return "<Class Address id=%s email=%s person_id=%s>" % (self.id, self.email, self.person_id)

Base.metadata.create_all(engine)
#create fake persons
p1 = Person(id=1, name="p1")
p2 = Person(id=2, name="p2")
addr1=Address(id=1, email="p1@example.com", person_id=1)
addr2=Address(id=2, email="p2@example.com", person_id=2)
p1.address.append(addr1)
p2.address.append(addr2)
session = Session()
session.add(p1)
session.add(p2)
session.commit()
