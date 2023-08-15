from infra.configs.connection import DBConnectionHandler
from infra.entities.projects import Project

class ProjectsRepository:
  def select(self):
    with DBConnectionHandler() as db:
      data = db.session.query(Project).all()
      return data

  def select_by_id(self, id):
    with DBConnectionHandler() as db:
      data = db.session.query(Project).where(Project.id == id).one().users
      return data

  def select_data_by_id(self, id):
    with DBConnectionHandler() as db:
      data = db.session.query(Project).where(Project.id == id).one()
      return data

  def insert(self, **body):
    with DBConnectionHandler() as db:
      print(body)
      data_insert = Project(
          name = body["name"]
      )
      db.session.add(data_insert)
      db.session.commit()

      return data_insert.id

  def delete(self, id):
    with DBConnectionHandler() as db:
      data_delete = db.session.query(Project).filter(Project.id == id).first()
      data_delete.delete()
      db.session.commit()

  def update(self, id, **body):
    with DBConnectionHandler() as db:
      data_update = db.session.query(Project).filter(Project.id == id).first()
      for key, value in body.items():
        setattr(data_update, key, value)
      db.session.commit()
