import unittest
from unittest.mock import MagicMock
import dimensional as dim

class TestEntities(unittest.TestCase):

    def setUp(self):
        self.subject = "foo"

    @unittest.expectedFailure
    def test_entity_attributes(self):
        dataset = dim.Dataset()

        name = "Dataset"
        header = ['foo', 'bar']
        rows = [[1,2], [3,4]]

        dataset.name = name
        dataset.header = header
        dataset.rows = rows

        self.assertEqual(name, dataset.name)
        self.assertEqual(header, dataset.header)
        self.assertEqual(rows, dataset.rows)

    @unittest.skip
    def test_lazy_evaluation(self):
        """How do I test that this is lazy?
        I need to know that I actually can take a large
        dataset and define it, extract its metadata,
        package it, without having to run the ETL first.
        """
        pass

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestEntities)
  unittest.TextTestRunner(verbosity=2).run(suite)
