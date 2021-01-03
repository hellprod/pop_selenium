# /exercises/exercise4
from selenium.webdriver.common.by import By

ex_04 = {
    "gr0_0": (By.XPATH, "//*[@value='v00']"),
    "gr0_1": (By.XPATH, "//*[@value='v10']"),
    "gr0_2": (By.XPATH, "//*[@value='v20']"),
    "gr0_4": (By.XPATH, "//*[@value='v40']"),
    "gr0_5": (By.XPATH, "//*[@value='v50']"),
    "gr0_6": (By.XPATH, "//*[@value='v60']"),
    "gr0_7": (By.XPATH, "//*[@value='v70']"),
    "gr0_8": (By.XPATH, "//*[@value='v80']"),

    "gr1_0": (By.XPATH, "//*[@value='v01']"),
    "gr1_1": (By.XPATH, "//*[@value='v11']"),
    "gr1_2": (By.XPATH, "//*[@value='v21']"),
    "gr1_4": (By.XPATH, "//*[@value='v41']"),
    "gr1_5": (By.XPATH, "//*[@value='v51']"),
    "gr1_6": (By.XPATH, "//*[@value='v61']"),
    "gr1_7": (By.XPATH, "//*[@value='v71']"),
    "gr1_8": (By.XPATH, "//*[@value='v81']"),

    "gr2_0": (By.XPATH, "//*[@value='v02']"),
    "gr2_1": (By.XPATH, "//*[@value='v12']"),
    "gr2_2": (By.XPATH, "//*[@value='v22']"),
    "gr2_4": (By.XPATH, "//*[@value='v42']"),
    "gr2_5": (By.XPATH, "//*[@value='v52']"),
    "gr2_6": (By.XPATH, "//*[@value='v62']"),
    "gr2_7": (By.XPATH, "//*[@value='v72']"),
    "gr2_8": (By.XPATH, "//*[@value='v82']"),

    "gr3_0": (By.XPATH, "//*[@value='v03']"),
    "gr3_1": (By.XPATH, "//*[@value='v13']"),
    "gr3_2": (By.XPATH, "//*[@value='v23']"),
    "gr3_4": (By.XPATH, "//*[@value='v43']"),
    "gr3_5": (By.XPATH, "//*[@value='v53']"),
    "gr3_6": (By.XPATH, "//*[@value='v63']"),
    "gr3_7": (By.XPATH, "//*[@value='v73']"),
    "gr3_8": (By.XPATH, "//*[@value='v83']"),


    "solution": (By.XPATH, "//button[@id='solution']"),

    "trial": (By.XPATH, "//pre[@id='trail']"),
    "trial_set_to": (By.XPATH, "//*[contains(text(),'Trail set to')]"),
    "good_answer": (By.XPATH, "//code[contains(text(),'OK. Good answer')]"),
    "h1_exercise": (By.XPATH, "//h1[contains(text(),'Exercise 4 - Radio buttons')]"),
}

expected_result = {
    "good_answer_text": "OK. Good answer",
    "h1_text": "Exercise 4 - Radio buttons"
}
