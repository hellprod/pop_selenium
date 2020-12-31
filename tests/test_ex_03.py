import unittest
from selenium import webdriver

from common.connfig import *
from pages.ex_00 import Ex00Page
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
        self.url = url_base
        self.driver.get(self.url)
        self.main_ex_00 = Ex00Page(self.driver)
        self.main_ex_03 = Ex03Page(self.driver)

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

    def trial_set_to_ex3(self):
        self.main_ex_00.exercise_3_click()
        trial_text = self.main_ex_03.trial_set_to()
        return trial_text

    def test_ex03(self):
        text = self.trial_set_to_ex3()
        choose = text.split('s13:')[1]
        self.main_ex_03.dropdown_click()
        self.main_ex_03.dropdown_choose(choose)

        self.main_ex_03.solution_click()

        trial_text = self.main_ex_03.good_answer_text()
        self.assertEqual(expected_result["good_answer_text"], trial_text)


if __name__ == '__main__':
    unittest.main()
