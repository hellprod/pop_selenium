import unittest
from selenium import webdriver

from common.connfig import *
from pages.ex_04 import Ex04Page
from locators.ex_04 import expected_result


class MyEx04Test(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        print('\nstart class tests')
        options = webdriver.ChromeOptions()
        for argument in chrome_options:
            options.add_argument(argument)
        self.driver = webdriver.Chrome(options=options, executable_path=chrome_path)
        self.url = url_base + url_ex_04
        self.driver.get(self.url)
        self.main_ex_04 = Ex04Page(self.driver)

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

    def trial_set_to_ex4(self):
        self.main_ex_04.gr0_5_click()
        self.main_ex_04.gr1_8_click()
        self.driver.execute_script("window.scrollTo(0,1000)")
        self.main_ex_04.gr2_5_click()
        self.main_ex_04.gr3_3_click()

    def test_trail_set_to_ex4(self):
        self.trial_set_to_ex4()

        trial_text = self.main_ex_04.trial_text()
        self.assertEqual(trial_text, expected_result["trial_text"])

    def test_ex04(self):
        self.trial_set_to_ex4()

        self.driver.execute_script("window.scrollTo(0,1200)")
        self.main_ex_04.solution_click()

        # assert_text = self.main_ex_03.good_answer_text()
        trial_text = self.main_ex_04.trial_text()
        self.assertEqual(trial_text, expected_result["good_answer_text"])


if __name__ == '__main__':
    unittest.main()
