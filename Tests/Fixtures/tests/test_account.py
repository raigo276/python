"""
Test Cases TestAccountModel
"""
from cmath import acos
import json
from random import randrange
from unittest import TestCase
from models import db
from models.account import Account, DataValidationError

ACCOUNT_DATA = {}

class TestAccountModel(TestCase):
    """Test Account Model"""

    @classmethod
    def setUpClass(cls):
        """ Connect and load data needed by tests """
        db.create_all()
        global ACCOUNT_DATA
        with open('tests/fixtures/account_data.json') as json_data:
            ACCOUNT_DATA = json.load(json_data)

    @classmethod
    def tearDownClass(cls):
        """Disconnect from database"""
        db.session.close()
        
    def setUp(self):
        """Truncate the tables"""
        self.rand = randrange(0, len(ACCOUNT_DATA))
        db.session.query(Account).delete()
        db.session.commit()

    def tearDown(self):
        """Remove the session"""
        db.session.remove()

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################
    def test_create_an_account(self):
        """ Test account creation"""
        data = ACCOUNT_DATA[self.rand]
        account = Account(**data)
        account.create()
        self.assertEqual(len(account.all()), 1)

    def test_create_all_accounts(self):
        """ Test create all accounts"""
        for data in ACCOUNT_DATA:
            account = Account(**data)
            account.create()
        self.assertEqual(len(account.all()), len(ACCOUNT_DATA))

    def test_account_as_string(self):
        """ Test account representation """
        account = Account()
        account.name = "Foo"
        self.assertEqual(str(account), "<Account 'Foo'>")

    def test_account_to_dict(self):
        """ Test account to dictionary"""
        data = ACCOUNT_DATA[self.rand]
        account = Account(**data)
        result = account.to_dict()
        self.assertEqual(result["name"], account.name)
        self.assertEqual(result["email"], account.email)
        self.assertEqual(result["phone_number"], account.phone_number)
        self.assertEqual(result["disabled"], account.disabled)

    def test_account_from_dict(self):
        """ Test account creation from dictionary """
        data = ACCOUNT_DATA[self.rand]
        account = Account()
        account.from_dict(data)
        self.assertEqual(data["name"], account.name)
        self.assertEqual(data["email"], account.email)
        self.assertEqual(data["phone_number"], account.phone_number)
        self.assertEqual(data["disabled"], account.disabled)

    def test_account_update(self):
        """ Test account update """
        data = ACCOUNT_DATA[self.rand]
        account = Account(**data)
        account.create()
        self.assertIsNotNone(account.id)
        account.name = "Foo"
        account.update()
        self.assertEqual(account.find(account.id).name, "Foo")

    def test_account_update_when_id_is_none(self):
        """ Test account update when Id is None"""
        data = ACCOUNT_DATA[self.rand]
        account = Account(**data)
        account.id = None
        self.assertRaises(DataValidationError, account.update)

    def test_delete_an_account(self):
        """ Test account creation"""
        data = ACCOUNT_DATA[self.rand]
        account = Account(**data)
        account.create()
        self.assertEqual(len(account.all()), 1)
        account.delete()
        self.assertEqual(len(account.all()), 0)