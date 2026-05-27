import unittest
import os
from core.logic import add_task, list_tasks, complete_task
from core.exceptions import TaskNotFoundError

TEST_FILE = "test_tasks.json"

class TestTodoLogic(unittest.TestCase):
    def setUp(self):
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

    def tearDown(self):
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

    def test_add_task(self):
        task = add_task("Тестовая задача", TEST_FILE)
        self.assertEqual(task["text"], "Тестовая задача")
        self.assertFalse(task["done"])

    def test_list_tasks(self):
        add_task("Задача 1", TEST_FILE)
        self.assertEqual(len(list_tasks(TEST_FILE)), 1)

    def test_complete_task(self):
        task = add_task("Задача 2", TEST_FILE)
        self.assertTrue(complete_task(task["id"], TEST_FILE)["done"])

    def test_complete_not_found(self):
        with self.assertRaises(TaskNotFoundError):
            complete_task(999, TEST_FILE)

if __name__ == "__main__":
    unittest.main()
