#connect to the database (sql_alchemy)
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# connect to database
engine = create_engine("sqlite:///persons.db", echo=True)
#create object and assign database
Base = declarative_base()

class Person(Base):
    __tablename__ = "People" #table name

    #column table

    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self, ssn, first, last, gender, age):
        self.ssn = ssn
        self.firstname = first
        self.lastname = last
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"({self.ssn} {self.firstname} {self.lastname} {self.gender})"

class Thing(Base):
    __tablename__ = "things"
    tid = Column("tid", Integer, primary_key=True)
    description = Column("description", String)
    owner = Column(Integer, ForeignKey("people.ssn"))

    def __init__(self, tid, description, owner):
        self.tid = tid
        self.description = description
        self.owner = owner
    
    def __repr__(self):
        return f"({self.tid} {self.description} {self.owner})"
#connect to database 
engine = create_engine("sqlite:///mydb.db", echo=True)
#create table in database and add session
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

#creating data
person = Person(12312, "Collins", "Leky", "m", 35)
session.add(person)
#commiting changes
session.commit()

p1 = Person(31222, "joe", "Lema", "m", 34)
p2 = Person(34312, "Giidy", "Lemi", "m", 32)
p3 = Person(35444, "Anne", "Shiru", "f", 40)

session.add(p1)
session.add(p2)
session.add(p3)
session.commit()

# Quering database
# Select everything from person
results = session.query(Person).all()
results = session.query(Person).filter(Person.lastname =="Blue")
print(results)