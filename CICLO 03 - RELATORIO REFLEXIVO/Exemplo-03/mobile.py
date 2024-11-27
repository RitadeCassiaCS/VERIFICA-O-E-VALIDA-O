from appium import webdriver
from selenium.webdriver.common.by import By
import unittest

class TestTodoApp(unittest.TestCase):
    def setUp(self):
        caps = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "app": "/path/to/todo-app.apk"
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

    def test_adicionar_tarefa(self):
        self.driver.find_element(By.ID, "add_task_button").click()
        self.driver.find_element(By.ID, "task_input").send_keys("EstudarAppium")
        self.driver.find_element(By.ID, "save_task_button").click()
        self.assertIn("Estudar Appium", self.driver.page_source)

    def test_remover_tarefa(self):
        self.driver.find_element(By.XPATH, "//android.widget.TextView[@text='Estudar Appium']").click()
        self.driver.find_element(By.ID, "delete_task_button").click()
        self.assertNotIn("Estudar Appium", self.driver.page_source)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


