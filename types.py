from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class ProjectType(Base):
    __tablename__ = 'project'
    project_id = Column(Integer, primary_key=True)
    project_name = Column(String(250), nullable=False)
    project_description = Column(String(250), nullable=False)
    project_due_date = Column(Date, nullable=True)
    project_priority = Column(Integer, nullable=False)
    project_create_date = Column(Date, nullable=False)
    aud_project_create_date = Column(Date, nullable=False)
    aud_project_create_uid = Column(String(250), nullable=False)
    aud_project_update_date = Column(Date, nullable=True)
    aud_project_update_uid = Column(String(250), nullable=True)


class TaskType(Base):
    __tablename__ = 'task'
    task_id = Column(Integer, primary_key=True)
    task_name = Column(String(250), nullable=False)
    task_description = Column(String(250), nullable=False)
    task_priority = Column(Integer, nullable=False)
    task_due_date = Column(Date, nullable=True)
    task_create_date = Column(Date, nullable=False)
    task_project_id = Column(Integer, ForeignKey('project.project_id'))
    project = relationship(ProjectType)
    aud_task_create_date = Column(Date, nullable=False)
    aud_task_create_uid = Column(String(250), nullable=False)
    aud_task_update_date = Column(Date, nullable=True)
    aud_task_update_uid = Column(String(250), nullable=True)


class NoteType(Base):
    __tablename__ = 'note'
    note_id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey('task.task_id'), nullable=True)
    project_id = Column(Integer, ForeignKey('project.project_id'), nullable=True)
    note_text = Column(String(250), nullable=False)
    note_create_date = Column(Date, nullable=False)
    aud_note_create_date = Column(Date, nullable=False)
    aud_note_create_uid = Column(String(250), nullable=False)
    aud_note_update_date = Column(Date, nullable=True)
    aud_note_update_uid = Column(String(250), nullable=True)
    project = relationship(ProjectType)
    task = relationship(TaskType)
