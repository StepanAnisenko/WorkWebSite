from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import settings

engine = create_engine('sqlite:///%s' % settings.SQL_ALCHEMY_URI)

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    nickname = Column(String(50))
    password = Column(String(30))
    email = Column(String(120), unique=True)
    role_id = Column(Integer, ForeignKey('roles.id'))

    def __init__(self, first_name, last_name, nickname, password, email, role_id):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.nickname = nickname
        self.role_id = role_id

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def __init__(self, name):
        self.name = name

class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    name = Column(String(150))

class Stage(Base):
    __tablename__ = 'stages'
    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    start_date = Column(DateTime)
    finish_date = Column(DateTime)
    project_id = Column(Integer, ForeignKey('projects.id'))

class ProjectUser(Base):
    __tablename__ = 'projects_users'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    project_id = Column(Integer, ForeignKey('projects.id'))


if __name__ == "__main__":

    Base.metadata.create_all(bind=engine)
    print(settings.SQL_ALCHEMY_URI)
    db_session.query(Role).delete()
    db_session.commit()
    r1 = Role(name="admin")
    r2 = Role(name="manager")
    r3 = Role(name="worker")
    db_session.add(r1)
    db_session.add(r2)
    db_session.add(r3)
    db_session.commit()
