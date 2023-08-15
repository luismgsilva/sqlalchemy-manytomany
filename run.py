from infra.repository.users_repository import UsersRepository
from infra.repository.projects_repository import ProjectsRepository

users_repo = UsersRepository()
projects_repo = ProjectsRepository()

user1_id = users_repo.insert(name="bob")
user2_id = users_repo.insert(name="alice")

prj1_id = projects_repo.insert(name = "Project 1")
prj2_id = projects_repo.insert(name = "Project 2")

user1 = users_repo.select_data_by_id(user1_id)
user2 = users_repo.select_data_by_id(user2_id)

projects_repo.update(prj1_id, users=[user1, user2])
projects_repo.update(prj2_id, users=[user2])


print(users_repo.select_by_id(2))
print(projects_repo.select_by_id(1))



