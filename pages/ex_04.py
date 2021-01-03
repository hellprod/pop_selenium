# /exercises/exercise4
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from locators.ex_04 import ex_04 as selectors


class Ex04Page:
	def __init__(self, driver):
		super().__init__()
		self.driver = driver
		self.selectors = selectors
		self.waiting_time = 0

	def gr00_00_click(self, group, group_index):
		choose = f"gr{group}_{group_index}"
		WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.selectors[choose])).click()
		print(f"gr00_00_click(gr_{group}_{group_index}) - OK: ")

	def solution_click(self):
		WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.selectors["solution"])).click()
		print(f"solution_click() - OK: ")

	def good_answer_text(self):
		answer = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.selectors["good_answer"]))
		answer_text = answer.text
		print(f"good_answer_text({answer_text}) - OK: ")
		return answer_text

	def trial_text(self):
		answer = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.selectors["trial"]))
		answer_text = answer.text
		print(f"trial_text({answer_text}) - OK: ")
		return answer_text

	def h1_exercise(self):
		answer = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.selectors["h1_exercise"]))
		answer_text = answer.text
		print(f"h1_exercise({answer_text}) - OK: ")
		return answer_text

	def trial_set_to(self):
		answer = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.selectors["trial_set_to"]))
		answer_text = answer.text
		print(f"trial_set_to({answer_text}) - OK: ")
		return answer_text
