def add_task(tasks, title):
    task = {"title": title, "completed": False}
    tasks.append(task)
    return tasks

def mark_completed(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
    return tasks

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return tasks
