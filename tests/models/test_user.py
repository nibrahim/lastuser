import unittest
from sqlalchemy.exc import IntegrityError
from lastuser_core.models import User
from ..test_db import db, BasicTestFixture

class TestUserModel(BasicTestFixture):
    def setUp(self):
        super(TestUserModel, self).setUp(dict(users=1))
        # self.user = User.query.filter_by()
        print self.users


    def test_noop(self):
        pass

    def tearDown(setUp):
        pass