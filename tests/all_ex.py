import unittest

from tests.test_ex_00 import MyEx00Test
from tests.test_ex_01 import MyEx01Test
from tests.test_ex_02 import MyEx02Test
from tests.test_ex_03 import MyEx03Test
from tests.test_ex_04 import MyEx04Test


def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(unittest.makeSuite(MyEx00Test))
   test_suite.addTest(unittest.makeSuite(MyEx01Test))
   test_suite.addTest(unittest.makeSuite(MyEx02Test))
   test_suite.addTest(unittest.makeSuite(MyEx03Test))
   test_suite.addTest(unittest.makeSuite(MyEx04Test))

   return test_suite


if __name__ == 'main':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())
