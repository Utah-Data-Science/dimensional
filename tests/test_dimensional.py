import unittest
from unittest.mock import MagicMock

class Bar(object):

  def thud(self):
    return "thunk"

  def baz(self):
    return self.thud()

class TestDimensional(unittest.TestCase):

  def setUp(self):
    self.subject = "foo"

  @unittest.skip("using skip")
  def test_true(self):
    self.assertTrue(True)

  @unittest.expectedFailure
  def test_weird(self):
    self.assertTrue(False)

  def test_foo(self):
    self.assertTrue(True)
    self.assertEqual("foo", self.subject)

  def test_bar(self):
    thing = Bar()
    thing.thud = MagicMock(return_value="foo")
    result = thing.baz()
    self.assertEqual("foo", thing.baz())

  def tearDown(self):
    self.subject = None
    # Just for example, no reason to tear down I should think (in this case)

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestDimensional)
  unittest.TextTestRunner(verbosity=2).run(suite)
  # Simple:
  # unittest.main()

