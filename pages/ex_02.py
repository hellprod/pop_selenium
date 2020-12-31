# /exercises/exercise2?seed=0b829d8d-8223-46c7-8e56-68a0b451331b
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from locators.ex_02 import ex_02 as selectors
from locators.ex_02 import enter_your_text as your_text


class Ex02Page:
	def __init__(self, driver):
		super().__init__()
		self.driver = driver
		self.selectors = selectors
		self.waiting_time = 0.3

	def input_t14_clear(self):
		WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.selectors["input_t14"])).clear()
		time.sleep(self.waiting_time)
		print(f"input_t14_clean() - OK: ")

	def input_t14(self):
		WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.selectors["input_t14"])).send_keys(your_text["T14"])
		time.sleep(self.waiting_time)
		print(f"input_t14({your_text['T14']}) - OK: ")

	def button1_click(self):
		WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.selectors["button1"])).click()
		time.sleep(self.waiting_time)
		print(f"button1_click() - OK: ")

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

