import unittest
from models import Airflow


def tearDown_item() -> None:
    Airflow.todolist_list.todolist_item = []


class TestModels(unittest.TestCase):
    def setUp(self) -> None:
        self.new_todolist = Airflow("Grocery Shopping")

    def test_init(self):
        self.assertEqual(self.new_todolist.todolist_name, "Grocery Shopping")

    def test_save_todolist(self):
        self.new_todolist.save_todolist_list_item()
        self.assertEqual(len(Airflow.todolist_list), 1)

    def tearDown(self) -> None:
        Airflow.todolist_list = []

    def test_save_multiple_todolist(self):
        self.new_todolist.save_todolist_list_item()
        test_todolist = Airflow("Finish HomePod project")
        test_todolist.save_todolist_list_item()
        self.assertEqual(len(Airflow.todolist_list), 2)

    def test_delete_todolist(self):
        self.new_todolist.save_todolist_list_item()
        test_todolist = Airflow("Finish HomePod project")
        test_todolist.save_todolist_list_item()

        self.new_todolist.delete_todolist_list()
        self.assertEqual(len(Airflow.todolist_list), 1)

    def test_display_todolist(self):
        self.assertEqual(Airflow.display_todolist_list(), Airflow.todolist_list)


if __name__ == '__main__':
    unittest.main()
