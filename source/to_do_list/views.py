from django.shortcuts import render, redirect, get_object_or_404
from to_do_list.models import Tasks


def index_view(request):
    tasks = Tasks.objects.all()
    context = {"tasks": tasks}
    return render(request, "index.html", context)


def task_view(request, **kwargs):
    task_pk = kwargs.get("pk")
    task = get_object_or_404(Tasks, pk=task_pk)
    return render(request, 'task_view.html', {"task": task})


def create_task(request):
    if request.method == "GET":
        return render(request, "create.html")
    else:
        task = request.POST.get("task")
        date_of_completion = request.POST.get("date_of_completion")
        description = request.POST.get("description")
        new_task = Tasks.objects.create(task=task, description=description,  date_of_completion=date_of_completion)
        return redirect("task_view", pk=new_task.pk)

