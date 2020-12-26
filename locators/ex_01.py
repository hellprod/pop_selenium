# /exercises/exercise1?seed=0b829d8d-8223-46c7-8e56-68a0b451331b

from selenium.webdriver.common.by import By


ex_01 = {
    "button1": (By.XPATH, "//button[@id='btnButton1']"),
    "button2": (By.XPATH, "//button[@id='btnButton2']"),
    "solution": (By.XPATH, "//button[@id='solution']"),
    "trial": (By.XPATH, "//pre[@id='trail']"),
    "good_answer": (By.XPATH, "//code[contains(text(),'OK. Good answer')]"),
}

expected_result = {
    "good_answer_text": "OK. Good answer",
}