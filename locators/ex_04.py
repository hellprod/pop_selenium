# /exercises/exercise4?seed=0b829d8d-8223-46c7-8e56-68a0b451331b
from selenium.webdriver.common.by import By

# //*[@type='radio']
# //h5[contains(text(),'Group 0')]
# //*[contains(text(),'Pink Kong')]
# //*[@class='row u-full-width'][1]//*[@type='radio'][2]


ex_04 = {
    "gr0_5": (By.XPATH, "//*[@class='row u-full-width'][1]//*[@type='radio'][5]"),
    "gr1_8": (By.XPATH, "//*[@class='row u-full-width'][2]//*[@type='radio'][8]"),
    "gr2_5": (By.XPATH, "//*[@class='row u-full-width'][3]//*[@type='radio'][5]"),
    "gr3_3": (By.XPATH, "//*[@class='row u-full-width'][4]//*[@type='radio'][3]"),

    "solution": (By.XPATH, "//button[@id='solution']"),

    "trial": (By.XPATH, "//pre[@id='trail']"),
    "good_answer": (By.XPATH, "//code[contains(text(),'OK. Good answer')]"),
}

expected_result = {
    "good_answer_text": "OK. Good answer",
    "trial_text": "[5, 8, 5, 2]",
}

