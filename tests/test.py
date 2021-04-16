import os
import sys
from unittest import TestCase
from unittest.mock import Mock

sys.path.append(os.getcwd())
from logger import Logger, settings, logger

settings.DATBASE_PATH = os.getcwd() + '/test.db'
settings.WRITE_TO_STDOUT = True
settings.WRITE_TO_DB = True
settings.EXCEPTION_LOGGING = True

mock_data = {
        'error': '',
        'logs': [
            {
                'created_at': '9999-12-31T23:59:59',
                'user_id': '2147483647',
                'first_name': 'Sat',
                'second_name': 'Luci',
                'message': 'And now we end everything.',
            },
            {
                'created_at': '0001-01-01T00:00:00',
                'user_id': '1',
                'first_name': 'Jess',
                'second_name': 'Christopher',
                'message': 'Everything begins here.',
            },
        ]
}

mock_data_error = {'error': 'Error message from mock_data_error.'}

class MockResponse():
    def __init__(self, data):
        self.data = data
    
    def json(self):
        return self.data

obj = Logger()

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
        logger.requests.get = Mock(return_value=MockResponse(mock_data))
        self.assertIsInstance(obj.get_data("20210414"), list)
        self.assertIsInstance(obj.logs[0], dict)
        self.assertEqual(obj.last_log.message,
                         f"Logger.get_data() executed succesfully. "
                         f"Received {len(obj.logs)} records.")
        #logger.requests.get = Mock(return_value=MockResponse(mock_data_error))
        #self.assertRaisesRegex(Exception, 'got error from*', obj.get_data('20120414'))

    def test_sort_data(self):
        obj.sort_data()
        self.assertEqual(obj.logs[0]['user_id'], '1')
        obj.sort_data('message')
        self.assertEqual(obj.logs[0]['user_id'], '2147483647')
        obj.sort_data('user_id')
        self.assertEqual(obj.logs[0]['user_id'], '1')

    def test_save_to_db(self):
        pass

    @classmethod
    def tearDownClass(cls):
        os.remove(settings.DATABASE_PATH)
