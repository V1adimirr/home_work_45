from django.db import models


STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]

class Tasks(models.Model):
    task = models.TextField(max_length=3000, verbose_name="Задача")
    status_t = models.CharField(max_length=30, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0], verbose_name="Статус")
    date_of_completion = models.DateField(verbose_name="Дата выполнения")

    def __str__(self):
        return f"{self.id}. {self.status_t}: {self.date_of_completion}"
