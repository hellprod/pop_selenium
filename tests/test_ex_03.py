import unittest
from selenium import webdriver

from common.connfig import *
from pages.ex_03 import Ex03Page
from locators.ex_03 import expected_result


class MyEx03Test(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        print('\nstart class tests')
        options = webdriver.ChromeOptions()
        for argument in chrome_options:
            options.add_argument(argument)
        self.driver = webdriver.Chrome(options=options, executable_path=chrome_path)
        self.url = url_base + url_ex_03
        self.driver.get(self.url)
        self.main_ex_03 = Ex03Page(self.driver)

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

    def test_ex02(self):
        self.main_ex_03.dropdown_click()
        self.main_ex_03.dropdown_pink_pong()

        self.main_ex_03.solution_click()

        # assert_text = self.main_ex_03.good_answer_text()
        trial_text = self.main_ex_03.trial_text()
        self.assertEqual(trial_text, expected_result["good_answer_text"])


if __name__ == '__main__':
    unittest.main()
