from services.auth_service import Auth_Service
from services.comment_service import Comment_Service
from services.job_post_service import Job_Post_Service
from services.rating_service import Rating_Service
from services.request_service import Request_Service
from services.unban_request_service import Unban_Request_Service
from services.vote_service import Vote_Service

from registries.databases.db_registry import DB_Registry

"""
Factory for the services
"""
class Service_Factory:
    def __init__(self, registry : DB_Registry):
        self.db_registry = registry

    def auth(self):
        user_db = self.db_registry.get_db('user')
        auth_service = Auth_Service(user_db)
        return auth_service

    def comment(self):
        comment_db = self.db_registry.get_db("comment")
        vote_db = self.db_registry.get_db("vote")

        comment_service = Comment_Service(comment_db, vote_db)
        return comment_service

    def job_post(self):
        job_post_db = self.db_registry.get_db("job_post")

        job_post_service = Job_Post_Service(job_post_db)
        return job_post_service

    def rating(self):
        rating_db = self.db_registry.get_db("rating")
        job_post_db = self.db_registry.get_db("job_post")

        rating_service = Rating_Service(rating_db, job_post_db)
        return rating_service

    def request(self):
        request_db = self.db_registry.get_db("request")

        request_service = Request_Service(request_db)
        return request_service

    def unban_request(self):
        unban_request_db = self.db_registry.get_db("unban_request")

        unban_request_service = Unban_Request_Service(unban_request_db)
        return unban_request_service

    def vote(self):
        vote_db = self.db_registry.get_db("vote")
        comment_db = self.db_registry.get_db("comment")

        vote_service = Vote_Service(vote_db, comment_db)
        return vote_service