# -*- coding: utf-8 -*-

import unittest
from lastuserapp import app, db, init_for
from lastuser_core.models import *
from .fixtures import make_fixtures

class BasicTestFixture(unittest.TestCase):
    def setUp(self, users=1, clients=1, orgs=1, user_clients=0, org_clients=0):
        init_for('testing')
        app.config['TESTING'] = True
        db.app = app
        db.drop_all()
        db.create_all()
        self.db = db
        self.bootstrap_users(users)
        # make_fixtures()

    def bootstrap_users(self, n=2):
        if hasattr(self, 'users') is False:
            self.users = []
        if n - len(self.users) >= 0:
            for i in range(n - len(self.users)):
                self.users.append(
                    User(
                        username=u"user" + unicode(i),
                        fullname=u"User " + unicode(i)
                        )
                    )


    def tearDown(self):
        self.db.drop_all()
