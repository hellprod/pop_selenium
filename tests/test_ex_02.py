import unittest
from selenium import webdriver

from common.connfig import *
from pages.ex_00 import Ex00Page
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
        self.url = url_base
        self.driver.get(self.url)
        self.main_ex_00 = Ex00Page(self.driver)
        self.main_ex_02 = Ex02Page(self.driver)

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

    def trial_set_to_ex2(self):
        self.main_ex_00.exercise_2_click()
        self.main_ex_02.input_t14_clear()
        trial_text = self.main_ex_02.trial_set_to()
        return trial_text

    def test_ex02(self):
        text = self.trial_set_to_ex2()
        t14_text = text.split("t14:")[1].split("b1")[0]
        self.main_ex_02.input_t14(t14_text)
        self.main_ex_02.button1_click()

        self.main_ex_02.solution_click()

        answer_text = self.main_ex_02.good_answer_text()
        self.assertEqual(expected_result["good_answer_text"], answer_text)


if __name__ == '__main__':
    unittest.main()
