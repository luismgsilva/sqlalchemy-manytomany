from infra.configs.base import Base
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship
from infra.entities.project_user import ProjectUser


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    projects = relationship('Project', secondary='project_users', back_populates='users')
