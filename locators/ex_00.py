# /

from selenium.webdriver.common.by import By


base = {
    "exercise_1": (By.XPATH, "//a[contains(text(),'1 - Three buttons')]"),
    "exercise_2": (By.XPATH, "//a[contains(text(),'2 - Editbox')]"),
    "exercise_3": (By.XPATH, "//a[contains(text(),'3 - Dropdown list')]"),
    "exercise_4": (By.XPATH, "//a[contains(text(),'4 - Radio buttons')]"),
}
