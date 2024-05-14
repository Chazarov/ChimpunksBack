from django.db import models

class Task(models.Model):
    id = models.CharField("ID задачи", max_length=50, primary_key = True)
    title = models.CharField("Описание", max_length=50)
    name = models.CharField("Имя макета", max_length=50)

    def __str__(self):
        return self.id
    

class Test(models.Model):
    task_id = models.CharField("Id задачи", max_length=50)
    def __str__(self):
        return self.task_id

    
class Resolve(models.Model):
    task_id = models.CharField("ID задачи", max_length=50)
    def __str__(self):
        return self.task_id