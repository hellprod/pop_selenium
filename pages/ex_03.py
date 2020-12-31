# /exercises/exercise3?seed=0b829d8d-8223-46c7-8e56-68a0b451331b
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from locators.ex_03 import ex_03 as selectors


class Ex03Page:
	def __init__(self, driver):
		super().__init__()
		self.driver = driver
		self.selectors = selectors
		self.waiting_time = 0.3

	def dropdown_click(self):
		WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.selectors["dropdown"])).click()
		time.sleep(self.waiting_time)
		print(f"dropdown_click() - OK: ")

	def dropdown_pink_pong(self):
		WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.selectors["dropdown_pink_pong"])).click()
		time.sleep(self.waiting_time)
		print(f"dropdown_pink_pong() - OK: ")

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

	def h1_exercise(self):
		answer = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.selectors["h1_exercise"]))
		time.sleep(self.waiting_time)
		answer_text = answer.text
		print(f"h1_exercise({answer_text}) - OK: ")
		return answer_text

