class TaskType:
    task_id = None
    task_name = None
    task_description = None
    task_priority = None
    task_due_date = None
    task_project_id = None
    task_project_id = None

    def set_task_id(self, id):
        self.task_id = id

    def set_task_name(self, name):
        self.task_name = name

    def set_task_description(self, description):
        self.task_description = description

    def set_task_due_date(self, due_date):
        self.task_due_date = due_date

    def set_task_project_id(self, project_id):
        self.task_project_id = project_id

    def get_task_id(self):
        return self.task_id

    def get_task_name(self):
        return self.task_name

    def get_task_description(self):
        return self.task_description

    def get_task_due_date(self):
        return self.task_due_date

    def get_task_project_id(self):
        return self.task_project_id

    def set_task_priority(self, priority):
        self.task_priority = priority

    def get_task_priority(self):
        return self.task_priority
