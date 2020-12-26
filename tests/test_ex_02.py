import unittest
from selenium import webdriver

from common.connfig import *
from pages.ex_02 import Ex02Page
from locators.ex_02 import expected_result


class MyEx02Test(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        print('\nstart class tests')
        options = webdriver.ChromeOptions()
        for argument in chrome_options:
            options.add_argument(argument)
        self.driver = webdriver.Chrome(options=options, executable_path=chrome_path)
        self.url = url_base + url_ex_02
        self.driver.get(self.url)
        self.main_ex_02 = Ex02Page(self.driver)

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
        self.main_ex_02.input_t14_clear()
        self.main_ex_02.input_t14()
        self.main_ex_02.button1_click()

        self.main_ex_02.solution_click()

        # assert_text = self.main_ex_02.good_answer_text()
        trial_text = self.main_ex_02.trial_text()
        self.assertEqual(trial_text, expected_result["good_answer_text"])


if __name__ == '__main__':
    unittest.main()
