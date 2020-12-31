# /exercises/exercise1

from selenium.webdriver.common.by import By


ex_01 = {
    "button1": (By.XPATH, "//button[@id='btnButton1']"),
    "button2": (By.XPATH, "//button[@id='btnButton2']"),
    "solution": (By.XPATH, "//button[@id='solution']"),
    "trial": (By.XPATH, "//pre[@id='trail']"),
    "good_answer": (By.XPATH, "//code[contains(text(),'OK. Good answer')]"),
    "h1_exercise": (By.XPATH, "//h1[contains(text(),'Exercise 1 - Three buttons')]"),
}

expected_result = {
    "good_answer_text": "OK. Good answer",
    "trial_text": "b2b1b2",
    "h1_text": "Exercise 1 - Three buttons"
}