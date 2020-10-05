from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

WAIT_TIME = 10

def start_chrome(url="https://www.wise-tt.com/wtt_um_feri/"):
    driver = webdriver.Chrome()
    driver.get(url)
    return driver

def navigate_to_right_program_year(driver, program="RAČUNALNIŠTVO IN INFORMACIJSKE TEHNOLOGIJE (BU20)", year="3"):
    WebDriverWait(driver, WAIT_TIME).until(
        EC.presence_of_element_located((By.XPATH, "//table[@class='noBorderTable']"))
    )

    # poisce ustrezen program
    try:
        WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "//li[contains(@class, 'ui-selectonemenu-item ui-selectonemenu-list-item') and @data-label='"+ program + "']"))
        )
        driver.find_element(By.XPATH, "//div[@id='form:j_idt171']").click()
        driver.find_element(By.XPATH, "//li[contains(@class, 'ui-selectonemenu-item ui-selectonemenu-list-item') and @data-label='"+ program + "']").click()
    except TimeoutException:
        print("Preveri ustreznost vnosa PROGRAM studija")
        return -1


    temp_year = str(year)

    # pocaka dokler se ne nalozi stevilke za letnik
    try:
        WebDriverWait(driver, WAIT_TIME).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//ul[@id='form:j_idt175_items']//li[contains(@class, 'ui-selectonemenu-item ui-selectonemenu-list-item') and @data-label='" + temp_year + "']"))
        )
        driver.find_element(By.XPATH, "//div[@id='form:j_idt175']").click()
        driver.find_element(By.XPATH, "//ul[@id='form:j_idt175_items']//li[contains(@class, 'ui-selectonemenu-item ui-selectonemenu-list-item') and @data-label='"+ temp_year + "']").click()
    except TimeoutException:
        print("Preveri ustreznost vnosa za LETNIK studija")
        return -2


    print("Uspesno nalozen urnik t(-.-t)")
    return 0


if __name__=="__main__":
    driver = start_chrome()
    navigate_to_right_program_year(driver)

