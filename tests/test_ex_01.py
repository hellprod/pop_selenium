import unittest
from selenium import webdriver

from common.connfig import *
from pages.ex_01 import Ex01Page
from locators.ex_01 import expected_result


class MyEx01Test(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        print('\nstart class tests')
        options = webdriver.ChromeOptions()
        for argument in chrome_options:
            options.add_argument(argument)
        self.driver = webdriver.Chrome(options=options, executable_path=chrome_path)
        self.url = url_base + url_ex_01
        self.driver.get(self.url)
        self.main_ex_01 = Ex01Page(self.driver)

    @classmethod
    def setUp(self) -> None:
        print('\nstart test')

    @classmethod
    def tearDown(self) -> None:
        print('\nend test')

    @classmethod
    def tearDownClass(self) -> None:
        self.driver.quit()
        print('\nend class tests')

    def test_ex01(self):
        self.driver.get(self.url)
        self.main_ex_01.button2_click()
        self.main_ex_01.button1_click()
        self.main_ex_01.button2_click()


        self.main_ex_01.solution_click()

        # assert_text = self.main_ex_01.good_answer_text()
        trial_text = self.main_ex_01.trial_text()
        self.assertEqual(trial_text, expected_result["good_answer_text"])



if __name__ == '__main__':
    unittest.main()
