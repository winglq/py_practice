'''
Example address: http://docs.sqlalchemy.org/en/rel_1_0/orm/tutorial.html
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)
    addresses = relationship("Address", order_by=Address.id,
		             back_populates="user")

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
            self.name, self.fullname, self.password)



if __name__ == "__main__":
    #User.addresses = relationship("Address", order_by=Address.id,
    #		                  back_populates="user")
    Base.metadata.create_all(engine)
    ed_user = User(name='ed', fullname='Ed Jonse', password='123')
    print ed_user.name
    session = Session()
    session.add(ed_user)
    session.flush()
    our_user = session.query(User).filter_by(name='ed').first()
    print our_user
    session.add_all([
        User(name='wendy', fullname='Wendy Williams', password='foobar'),
        User(name='mary', fullname='Mary Contrary', password='xxg527'),
        User(name='fred', fullname='Fred Flinstone', password='blah')])
    ed_user.password = 'f8s7ccs'
    print session.dirty
    print session.new
    session.commit()
    for instance in session.query(User).order_by(User.id):
        print(instance.name, instance.fullname)
