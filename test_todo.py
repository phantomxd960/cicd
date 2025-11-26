from todo import add_task, mark_completed, delete_task


def test_add_task():
    tasks = []
    add_task(tasks, "Buy milk")
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Buy milk"
    assert tasks[0]["completed"] is False


def test_mark_completed():
    tasks = [{"title": "Study", "completed": False}]
    mark_completed(tasks, 0)
    assert tasks[0]["completed"] is True


def test_delete_task():
    tasks = [
        {"title": "Task1", "completed": False},
        {"title": "Task2", "completed": False},
    ]
    delete_task(tasks, 0)
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Task2"
