import unittest
from selenium import webdriver

from common.connfig import *
from pages.ex_00 import Ex00Page
from pages.ex_01 import Ex01Page
from pages.ex_02 import Ex02Page
from pages.ex_03 import Ex03Page
from pages.ex_04 import Ex04Page
import locators.ex_01, locators.ex_02, locators.ex_03, locators.ex_04


class MyEx00Test(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        print('\nstart class tests')
        options = webdriver.ChromeOptions()
        for argument in chrome_options:
            options.add_argument(argument)
        self.driver = webdriver.Chrome(options=options, executable_path=chrome_path)
        self.url = url_base
        # self.driver.get(self.url)
        self.main_ex_00 = Ex00Page(self.driver)
        self.main_ex_01 = Ex01Page(self.driver)
        self.main_ex_02 = Ex02Page(self.driver)
        self.main_ex_03 = Ex03Page(self.driver)
        self.main_ex_04 = Ex04Page(self.driver)

    @classmethod
    def setUp(self) -> None:
        self.driver.get(self.url)
        self.driver.refresh()
        print('\nstart test')

    @classmethod
    def tearDown(self) -> None:
        print('\nend test')

    @classmethod
    def tearDownClass(self) -> None:
        self.driver.quit()
        print('\nend class tests')

    def test_exercise_1_h1_text(self):
        self.main_ex_00.exercise_1_click()
        h1_text = self.main_ex_01.h1_exercise()
        self.assertEqual(h1_text, locators.ex_01.expected_result["h1_text"])

    def test_exercise_2_h1_text(self):
        self.main_ex_00.exercise_2_click()
        h1_text = self.main_ex_02.h1_exercise()
        self.assertEqual(h1_text, locators.ex_02.expected_result["h1_text"])

    def test_exercise_3_h1_text(self):
        self.main_ex_00.exercise_3_click()
        h1_text = self.main_ex_03.h1_exercise()
        self.assertEqual(h1_text, locators.ex_03.expected_result["h1_text"])

    def test_exercise_4_h1_text(self):
        self.main_ex_00.exercise_4_click()
        h1_text = self.main_ex_04.h1_exercise()
        self.assertEqual(h1_text, locators.ex_04.expected_result["h1_text"])


if __name__ == '__main__':
    unittest.main()
