# /exercises/exercise3
from selenium.webdriver.common.by import By


ex_03 = {
    "dropdown": (By.XPATH, "//select[@id='s13']"),
    "dropdown_pink_pong": (By.XPATH, "//option[contains(text(),'Pink Kong')]"),

    "solution": (By.XPATH, "//button[@id='solution']"),
    "trial_set_to": (By.XPATH, "//*[contains(text(),'Trail set to')]"),
    "trial": (By.XPATH, "//pre[@id='trail']"),
    "good_answer": (By.XPATH, "//code[contains(text(),'OK. Good answer')]"),
    "h1_exercise": (By.XPATH, "//h1[contains(text(),'Exercise 3 - Dropdown list')]"),
    'v0': (By.XPATH, "//option[contains(text(),'Beluga Brown')]"),
    'v1': (By.XPATH, "//option[contains(text(),'Mango Orange')]"),
    'v2': (By.XPATH, "//option[contains(text(),'Verdoro Green')]"),
    'v4': (By.XPATH, "//option[contains(text(),'Freudian Gilt')]"),
    'v5': (By.XPATH, "//option[contains(text(),'Pink Kong')]"),
    'v6': (By.XPATH, "//option[contains(text(),'Duck Egg Blue')]"),
    'v7': (By.XPATH, "//option[contains(text(),'Anti - Establishment Mint')]"),
    'v8': (By.XPATH, "//option[contains(text(),'Amberlite Firemist')]")
}

expected_result = {
    "good_answer_text": "OK. Good answer",
    # "trial_text": "s13:v5",
    "h1_text": "Exercise 3 - Dropdown list",
    'v0': 'Beluga Brown',
    'v1': 'Mango Orange',
    'v2': 'Verdoro Green',
    'v4': 'Freudian Gilt',
    'v5': 'Pink Kong',
    'v6': 'Duck Egg Blue',
    'v7': 'Anti - Establishment Mint',
    'v8': 'Amberlite Firemist'
}

