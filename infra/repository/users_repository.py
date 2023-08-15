from infra.configs.connection import DBConnectionHandler
from infra.entities.users import Users
from infra.entities.projects import Project

class UsersRepository:
  def select(self):
    with DBConnectionHandler() as db:
      data = db.session.query(Users).all()
      return data


  def select_by_id(self, id):
    with DBConnectionHandler() as db:
      # data = db.session.query(Users).join(Project, Users.projects == Project.id).with_entities(Users.name, Project.name).all()
      data = db.session.query(Users).where(Users.id == id).one().projects
      return data

  def insert(self, **body):
    with DBConnectionHandler() as db:
      print(body)
      data_insert = Users(
          name = body["name"]
      )
      db.session.add(data_insert)
      db.session.commit()

      return data_insert

  def delete(self, id):
    with DBConnectionHandler() as db:
      data_delete = db.session.query(Users).filter(Users.id == id).first()
      data_delete.delete()
      db.session.commit()

  def update(self, id, **body):
    with DBConnectionHandler() as db:
      data_update = db.session.query(Users).filter(Users.id == id).first()
      for key, value in body.items():
        setattr(data_update, key, value)
      db.session.commit()
