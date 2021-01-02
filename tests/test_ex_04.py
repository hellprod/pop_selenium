import unittest
from selenium import webdriver

from common.connfig import *
from pages.ex_00 import Ex00Page
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
        self.url = url_base
        self.driver.get(self.url)
        self.main_ex_00 = Ex00Page(self.driver)
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
        self.main_ex_00.exercise_4_click()
        trial_text = self.main_ex_04.trial_set_to()
        return trial_text

    def test_ex04(self):
        text = self.trial_set_to_ex4()
        set_text = text.split('to: [')[1].split(']')[0].split(', ')

        gr = 0
        for i in set_text:
            print(i, type(i))
            self.main_ex_04.gr00_00_click(gr, i)
            gr = gr + 1

        self.driver.execute_script("window.scrollTo(0,1200)")
        self.main_ex_04.trial_text()
        self.main_ex_04.solution_click()

        assert_text = self.main_ex_04.good_answer_text()
        self.assertEqual(expected_result["good_answer_text"], assert_text)


    # def test_trail_set_to_ex4(self):
    #     self.trial_set_to_ex4()
    #
    #     trial_text = self.main_ex_04.trial_text()
    #     self.assertEqual(trial_text, expected_result["trial_text"])
    #
    # def test_ex04(self):
    #     self.trial_set_to_ex4()
    #
    #     self.driver.execute_script("window.scrollTo(0,1200)")
    #     self.main_ex_04.solution_click()
    #
    #     # assert_text = self.main_ex_03.good_answer_text()
    #     trial_text = self.main_ex_04.trial_text()
    #     self.assertEqual(trial_text, expected_result["good_answer_text"])


if __name__ == '__main__':
    unittest.main()
