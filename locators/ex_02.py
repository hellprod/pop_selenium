# /exercises/exercise2?seed=0b829d8d-8223-46c7-8e56-68a0b451331b
from selenium.webdriver.common.by import By


ex_02 = {
    "button1": (By.XPATH, "//button[@id='btnButton1']"),
    "input_t14": (By.XPATH, "//input[@id='t14']"),

    "solution": (By.XPATH, "//button[@id='solution']"),

    "trial": (By.XPATH, "//pre[@id='trail']"),
    "good_answer": (By.XPATH, "//code[contains(text(),'OK. Good answer')]"),
}

expected_result = {
    "good_answer_text": "OK. Good answer",
}

enter_your_text = {
    "T14": "Manage effect.",
}
