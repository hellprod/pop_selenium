# /exercises/exercise4?seed=0b829d8d-8223-46c7-8e56-68a0b451331b
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from locators.ex_04 import ex_04 as selectors


class Ex04Page:
	def __init__(self, driver):
		super().__init__()
		self.driver = driver
		self.selectors = selectors
		self.waiting_time = 2

	def gr0_5_click(self):
		WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.selectors["gr0_5"])).click()
		time.sleep(self.waiting_time)
		print(f"gr0_5_click() - OK: ")

	def gr1_8_click(self):
		WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.selectors["gr1_8"])).click()
		time.sleep(self.waiting_time)
		print(f"gr1_8_click() - OK: ")

	def gr2_5_click(self):
		WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.selectors["gr2_5"])).click()
		time.sleep(self.waiting_time)
		print(f"gr2_5_click() - OK: ")

	def gr3_3_click(self):
		WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.selectors["gr3_3"])).click()
		time.sleep(self.waiting_time)
		print(f"gr3_3_click() - OK: ")

	def solution_click(self):
		WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.selectors["solution"])).click()
		time.sleep(self.waiting_time)
		print(f"solution_click() - OK: ")

	def good_answer_text(self):
		answer = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.selectors["good_answer"]))
		time.sleep(self.waiting_time)
		answer_text = answer.text
		print(f"good_answer_text({answer_text}) - OK: ")
		return answer_text

	def trial_text(self):
		answer = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.selectors["trial"]))
		time.sleep(self.waiting_time)
		answer_text = answer.text
		print(f"trial_text({answer_text}) - OK: ")
		return answer_text
