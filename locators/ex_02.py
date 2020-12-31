# /exercises/exercise2?seed=0b829d8d-8223-46c7-8e56-68a0b451331b
from selenium.webdriver.common.by import By


ex_02 = {
    "button1": (By.XPATH, "//button[@id='btnButton1']"),
    "input_t14": (By.XPATH, "//input[@id='t14']"),

    "solution": (By.XPATH, "//button[@id='solution']"),
    "trial_set_to": (By.XPATH, "//*[contains(text(),'Trail set to')]"),
    "trial": (By.XPATH, "//pre[@id='trail']"),
    "good_answer": (By.XPATH, "//code[contains(text(),'OK. Good answer')]"),
    "h1_exercise": (By.XPATH, "//h1[contains(text(),'Exercise 2 - Editbox')]"),
}

expected_result = {
    "good_answer_text": "OK. Good answer",
    "h1_text": "Exercise 2 - Editbox"
}

enter_your_text = {
    "T14": "Manage effect.",

}
