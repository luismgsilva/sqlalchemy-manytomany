from infra.repository.users_repository import UsersRepository
from infra.repository.projects_repository import ProjectsRepository

users_repo = UsersRepository()
projects_repo = ProjectsRepository()

user1 = users_repo.insert(name="bob")
user2 = users_repo.insert(name="alice")

prj1 = projects_repo.insert(name = "Project 1")
prj2 = projects_repo.insert(name = "Project 2")

projects_repo.update(prj1, users=[user1, user2])
projects_repo.update(prj2, users=[user2])


print(users_repo.select_by_id(2))
print(projects_repo.select_by_id(1))



