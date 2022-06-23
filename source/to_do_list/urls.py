from django.urls import path

from to_do_list.views import index_view, create_task, task_view

urlpatterns = [
    path('', index_view),
    path('task/', task_view),
    path('tasks/add/', create_task)
]