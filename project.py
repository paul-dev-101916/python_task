class ProjectType1:
    project_id = None
    project_name = None
    project_description = None
    project_due_date = None
    project_priority = None

    def set_project_id(self, id):
        self.project_id = id

    def get_project_id(self):
        return self.project_id

    def set_project_description(self, description):
        self.project_description = description

    def get_project_description(self):
        return self.project_description

    def set_project_name(self, name):
        self.project_name = name

    def get_project_name(self):
        return self.project_name

    def set_project_due_date(self, date):
        self.project_due_date = date

    def get_project_due_date(self):
        return self.project_due_date

    def set_project_priority(self, priority):
        self.project_priority = priority

    def get_project_priority(self):
        return self.project_priority
