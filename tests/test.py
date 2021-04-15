import os
import sys
from unittest import TestCase
from unittest.mock import patch, Mock

sys.path.append(os.getcwd())
from logger import Logger, settings

settings.DATBASE_PATH = os.getcwd() + '/test.db'
settings.WRITE_TO_STDOUT = True
settings.WRITE_TO_DB = True
settings.EXCEPTION_LOGGING = True

mock_data = {
        'error': '',
        'logs': [
            {
                'created_at': '0001-01-01T00:00:00',
                'user_id': '1',
                'first_name': 'Jess',
                'second_name': 'Christopher',
                'message': 'Everything begins here.',
            },
            {
                'created_at': '9999-12-31T23:59:59',
                'user_id': '2147483647',
                'first_name': 'Sat',
                'second_name': 'Luci',
                'message': 'Now we end everything.',
            },
        ]
}

mock_data_error = {'error': 'Error message from mock_data_error.'}

logger = Logger()

class TestLogger(TestCase):

    def test_logg(self):
        msg = 'Some message to log.'
        settings.WRITE_TO_DB = False
        obj.logg(msg)
        self.assertEqual(obj.last_log.message, msg)
        self.assertFalse(obj.last_log in obj.last_log.get_all_logs())
        settings.WRITE_TO_DB = True
        obj.logg(msg)
        self.assertTrue(obj.last_log in obj.last_log.get_all_logs())

    def test_get_data(self):
        pass

    def test_sort_data(self):
        pass

    def test_save_to_db(self):
        pass

    #@classmethod
    #def tearDownClass(cls):
    #    os.remove(settings.DATABASE_PATH)
