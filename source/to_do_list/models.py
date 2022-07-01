from django.db import models

STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class Tasks(models.Model):
    task = models.CharField(max_length=30, verbose_name="Задача")
    description = models.TextField(max_length=2500, null=False, blank=False, verbose_name="Описание")
    status_t = models.CharField(max_length=30, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0], verbose_name="Статус")
    date_of_completion = models.DateField(null=False, blank=False, verbose_name="Дата выполнения")

    def __str__(self):
        return f"{self.id}. {self.status_t}: {self.date_of_completion}"

    class Meta:
        db_table = "tasks"
        verbose_name = "задача"
        verbose_name_plural = "задачи"
