import unittest
from todo_list import add_task, view_tasks, update_task, delete_task, mark_as_complete, mark_as_incomplete, sort_tasks, export_tasks, tasks

class TestTodoList(unittest.TestCase):

    def setUp(self):
        tasks.clear()

    def test_add_task_with_completion(self):
        result = add_task("Buy groceries", "Low", None, completed=True)
        self.assertIn({"task": "Buy groceries", "priority": "Low", "due_date": None, "completed": True}, tasks)

    def test_mark_task_as_complete(self):
        add_task("Study Python", "High", "2024-12-05", completed=False)
        result = mark_as_complete(0)
        self.assertEqual(result, "Task 1 marked as complete.")
        self.assertTrue(tasks[0]["completed"])

    def test_mark_task_as_incomplete(self):
        add_task("Study Python", "High", "2024-12-05", completed=True)
        result = mark_as_incomplete(0)
        self.assertEqual(result, "Task 1 marked as incomplete.")
        self.assertFalse(tasks[0]["completed"])

    def test_sort_tasks_by_priority(self):
        add_task("Task A", "Medium")
        add_task("Task B", "High")
        add_task("Task C", "Low")
        sort_tasks("priority")
        self.assertEqual(tasks[0]["priority"], "High")
        self.assertEqual(tasks[-1]["priority"], "Low")

    def test_sort_tasks_by_due_date(self):
        add_task("Task A", "Medium", "2024-12-10")
        add_task("Task B", "High", None)
        add_task("Task C", "Low", "2024-12-01")
        sort_tasks("due_date")
        self.assertEqual(tasks[0]["due_date"], "2024-12-01")
        self.assertEqual(tasks[-1]["due_date"], None)

    def test_export_tasks(self):
        add_task("Task A", "Medium", "2024-12-10", completed=False)
        add_task("Task B", "High", None, completed=True)
        file_name = "test_tasks.txt"
        result = export_tasks(file_name)
        self.assertEqual(result, f"Tasks exported successfully to {file_name}")

if __name__ == '__main__':
    unittest.main()
