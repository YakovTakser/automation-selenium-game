from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def game():
    """Func - automatic game playing"""
    try:
        # Opens a webdriver
        driver = webdriver.Chrome(
            executable_path=r"C:\Users\Yakov Takser\Desktop\fabriik test\chromeDriver\chromedriver.exe")

        # Opens website with a game
        driver.get("https://www.playbuzz.com/jessicafavish10/can-you-pass-this-tricky-eye-test")
        time.sleep(3)
        driver.maximize_window()
        time.sleep(2)

        # Finds the 'start button of the game'
        start_game_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button/div[2]/div/div[2]")))

        # Scroll into screen of 'start button of the game'
        driver.execute_script("arguments[0].scrollIntoView();", start_game_button)

        # Click on start button of the game
        driver.execute_script("arguments[0].click();", start_game_button)
        time.sleep(3)

        list_of_right_answers = [3, 2, 3, 1, 1, 2, 3, 2, 1]
        # Loop that goes through all questions and answering the right answers for the questions
        for i in range(9):
            right_answer = list_of_right_answers[i]
            right_answer_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//div[2]/div/div/div/div[{right_answer}]/div/button/div/div[1]/div[2]")))
            # Click on right answer
            time.sleep(4)
            right_answer_button.click()
            # Wait until next question appears
            time.sleep(4)
        # Take a screenshot with the result and sva it
        time.sleep(8)
        driver.save_screenshot("result.png")
        time.sleep(10)
        driver.close()

        return True

    except:
        return False


def test_game():
    """Test that tests the game, if there is an error in the func-game then the test will fall"""
    assert game() == True
