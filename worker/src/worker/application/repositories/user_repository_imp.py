from worker.domain.entities.user_mo import User
from worker.domain.repositories.user_repository import UserRepository


class UserRepositoryImp(UserRepository):
    def get_users_by_topic(self, topic):
        return list(User.objects(topics__in=[topic]))
