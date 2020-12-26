# /exercises/exercise3?seed=0b829d8d-8223-46c7-8e56-68a0b451331b
from selenium.webdriver.common.by import By


ex_03 = {
    "dropdown": (By.XPATH, "//select[@id='s13']"),
    "dropdown_pink_pong": (By.XPATH, "//option[contains(text(),'Pink Kong')]"),

    "solution": (By.XPATH, "//button[@id='solution']"),

    "trial": (By.XPATH, "//pre[@id='trail']"),
    "good_answer": (By.XPATH, "//code[contains(text(),'OK. Good answer')]"),
}

expected_result = {
    "good_answer_text": "OK. Good answer",
}

