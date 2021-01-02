import unittest
from selenium import webdriver

from common.connfig import *
from pages.ex_00 import Ex00Page
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
        self.url = url_base
        self.driver.get(self.url)
        self.main_ex_00 = Ex00Page(self.driver)
        self.main_ex_01 = Ex01Page(self.driver)

    @classmethod
    def setUp(self) -> None:
        self.driver.refresh()
        print('\nstart test')

    @classmethod
    def tearDown(self) -> None:
        print('\nend test')

    @classmethod
    def tearDownClass(self) -> None:
        self.driver.quit()
        print('\nend class tests')

    def trial_set_to_ex1(self):
        self.main_ex_00.exercise_1_click()
        trial_text = self.main_ex_01.trial_set_to()
        return trial_text

    def test_ex01(self):
        text = self.trial_set_to_ex1()
        # todo
        for i in text.split('b'):
            if i == '1':
                self.main_ex_01.button1_click()
            elif i == "2":
                self.main_ex_01.button2_click()

        self.main_ex_01.trial_text()
        self.main_ex_01.solution_click()

        answer_text = self.main_ex_01.good_answer_text()
        self.assertEqual(expected_result["good_answer_text"], answer_text)


if __name__ == '__main__':
    unittest.main()
