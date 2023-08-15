from infra.configs.base import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from infra.entities.project_user import ProjectUser



class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    users = relationship('Users', secondary='project_users', back_populates='projects')
