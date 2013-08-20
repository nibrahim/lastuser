import unittest
from sqlalchemy.exc import IntegrityError
from lastuser_core.models import User
from ..test_db import db, BasicTestFixture

class TestUserModel(BasicTestFixture):
    def setUp(self):
        super(TestUserModel, self).setUp(dict(users=2))
        # self.user = User.query.filter_by()


    def test_noop(self):
        pass

    def tearDown(setUp):
        pass