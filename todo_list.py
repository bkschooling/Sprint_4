tasks = []

def add_task(task, priority="Medium", due_date=None, completed=False):
    """Adds a new task to the list with a priority, optional due date, and completion status."""
    tasks.append({"task": task, "priority": priority, "due_date": due_date, "completed": completed})
    return f"Task '{task}' added with priority '{priority}', due date '{due_date}', and status {'completed' if completed else 'incomplete'}."

def view_tasks():
    """Returns all tasks in the list."""
    if not tasks:
        return "No tasks available."
    result = []
    for i, task in enumerate(tasks):
        due_date = task["due_date"] if task["due_date"] else "None"
        status = "Completed" if task["completed"] else "Incomplete"
        result.append(f"{i + 1}. {task['task']} (Priority: {task['priority']}, Due: {due_date}, Status: {status})")
    return "\n".join(result)

def update_task(index, new_task=None, new_priority=None, new_due_date=None, new_status=None):
    """Updates the task at the given index."""
    try:
        if new_task:
            tasks[index]["task"] = new_task
        if new_priority:
            tasks[index]["priority"] = new_priority
        if new_due_date:
            tasks[index]["due_date"] = new_due_date
        if new_status is not None:
            tasks[index]["completed"] = new_status
        return f"Task {index + 1} updated successfully."
    except IndexError:
        return "Error: Task index out of range."

def delete_task(index):
    """Deletes the task at the given index."""
    try:
        task = tasks.pop(index)
        return f"Task '{task['task']}' deleted."
    except IndexError:
        return "Error: Task index out of range."

def mark_as_complete(index):
    """Marks the task at the given index as complete."""
    try:
        tasks[index]["completed"] = True
        return f"Task {index + 1} marked as complete."
    except IndexError:
        return "Error: Task index out of range."

def mark_as_incomplete(index):
    """Marks the task at the given index as incomplete."""
    try:
        tasks[index]["completed"] = False
        return f"Task {index + 1} marked as incomplete."
    except IndexError:
        return "Error: Task index out of range."

def sort_tasks(by="priority"):
    """Sorts tasks by the specified attribute ('priority' or 'due_date')."""
    try:
        if by == "priority":
            tasks.sort(key=lambda x: x["priority"])
        elif by == "due_date":
            tasks.sort(key=lambda x: (x["due_date"] is None, x["due_date"]))
        return f"Tasks sorted by {by}."
    except Exception as e:
        return f"Error: {str(e)}"

def export_tasks(file_name="tasks.txt"):
    """Exports tasks to a file."""
    try:
        with open(file_name, "w") as file:
            for task in tasks:
                due_date = task["due_date"] if task["due_date"] else "None"
                status = "Completed" if task["completed"] else "Incomplete"
                file.write(f"{task['task']},{task['priority']},{due_date},{status}\n")
        return f"Tasks exported successfully to {file_name}."
    except Exception as e:
        return f"Error exporting tasks: {str(e)}"
