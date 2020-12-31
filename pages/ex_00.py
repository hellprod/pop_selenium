# /
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.ex_00 import base as selectors


class Ex00Page:
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.selectors = selectors

    def exercise_1_click(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.selectors["exercise_1"])).click()
        print(f"exercise_1_click() - OK: ")

    def exercise_2_click(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.selectors["exercise_2"])).click()
        print(f"exercise_2_click() - OK: ")

    def exercise_3_click(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.selectors["exercise_3"])).click()
        print(f"exercise_3_click() - OK: ")

    def exercise_4_click(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.selectors["exercise_4"])).click()
        print(f"exercise_4_click() - OK: ")
