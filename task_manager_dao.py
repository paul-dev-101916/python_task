import sqlite3


class TaskManagerDAO:
    sqlite_file = './task_mngr_db.db'

    def get_connection(self):
        conn = sqlite3.connect(self.sqlite_file)
        return conn

    def insert_project(self, project):
        next_id = self.get_next_project_id()
        conn = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            values = {"id": next_id, "name": project.get_project_name(), "desc": project.get_project_description()}
            cursor.execute("INSERT INTO project (project_id, project_name, project_description) values (:id,"
                           + " :name, :desc)", values)
            conn.commit()
        except sqlite3.OperationalError as e:
            print('ERROR: Error occurred while trying to insert project' + e)
        conn.close()
        return next_id

    def get_next_project_id(self):
        max_id = None
        # try:
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(project_id) from project")
        max_id = cursor.fetchone()[0]
        conn.close()
        # except sqlite3.Error:
        # print('ERROR: Error occurred while trying to insert project')
        return max_id + 1
