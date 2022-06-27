from django.urls import path

from to_do_list.views import index_view, create_task, task_view

urlpatterns = [
    path('', index_view, name="index"),
    path('task/<int:pk>/', task_view, name="task_view"),
    path('tasks/add/', create_task, name="create_task"),
]
