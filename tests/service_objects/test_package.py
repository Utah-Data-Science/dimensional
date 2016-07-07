import unittest
try:
    from unittest.mock import MagicMock
except:
    from mock import MagicMock

import dimensional as dim
import petl as etl

class TestPackage(unittest.TestCase):
    pass

    # def test_export(self):
    #     exporter = lambda table, *args, **kwargs: table
    #     self.assertEqual('table', dim.export(exporter, 'table'))
    #
    # def test_export_csv(self):
    #     etl.tocsv = MagicMock(return_value=True)
    #     self.assertTrue(dim.export_csv('table', 'foo', 'bar'))
    #     etl.tocsv.assert_called_with('table', 'foo', 'bar')
    #
    # def test_append_csv(self):
    #     etl.appendcsv = MagicMock(return_value=True)
    #     self.assertTrue(dim.append_csv('table', 'foo', 'bar'))
    #     etl.appendcsv.assert_called_with('table', 'foo', 'bar')
    #
    # def test_export_db(self):
    #     etl.todb = MagicMock(return_value=True)
    #     self.assertTrue(dim.export_db('table', 'connection', 'tablename', 'foo', 'bar'))
    #     etl.todb.assert_called_with('table', 'connection', 'tablename', 'foo', 'bar')
    #
    # def test_append_db(self):
    #     etl.appenddb = MagicMock(return_value=True)
    #     self.assertTrue(dim.append_db('table', 'connection', 'tablename', 'foo', 'bar'))
    #     etl.appenddb.assert_called_with('table', 'connection', 'tablename', 'foo', 'bar')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPackage)
    unittest.TextTestRunner(verbosity=2).run(suite)

