from selenium import webdriver
from selenium.webdriver.common.by import By


def convert_currency(first_currency: str, second_currency: str, amount: int):

    LINK = 'https://finance.rambler.ru/calculators/converter/'

    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(LINK)

    browser.find_element(By.CSS_SELECTOR, "[data-finance_media-desktop = 'converter_first_select']").click()

    browser.find_element(By.CSS_SELECTOR, f"[data-finance_media-desktop = 'converter_first_select'] [data-char-code={first_currency}]").click()

    browser.find_element(By.CSS_SELECTOR, "[data-finance_media-desktop = 'converter_second_select']").click()

    browser.find_element(By.CSS_SELECTOR, f"[data-finance_media-desktop = 'converter_second_select'] [data-char-code={second_currency}]").click()

    browser.find_element(By.CSS_SELECTOR, "input[aria-label='Cумма']").send_keys(amount)

    browser.find_element(By.CSS_SELECTOR, "[aria-label='Перейти на страницу с результатами конвертирования']").click()

    text = browser.find_element(By.XPATH, '//div[@data-finance_media-desktop="converter_form"]/div[2]/div[1]/div[2]/span[2]').text

    print(f"{amount} {first_currency} равно {text} {second_currency}")

    print("\nquit browser..")
    browser.quit()

# Пример вызова функции с параметрами EUR -> AUD, 10 единиц.
convert_currency("EUR", "AUD", 10)