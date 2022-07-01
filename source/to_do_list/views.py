from django.shortcuts import render, redirect, get_object_or_404

from to_do_list.forms import TasksForm
from to_do_list.models import Tasks, STATUS_CHOICES


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
        form = TasksForm()
        return render(request, "create.html", {"form": form})
    else:
        form = TasksForm(data=request.POST)
        if form.is_valid():
            task = form.cleaned_data.get("task")
            description = form.cleaned_data.get("description")
            status_t = form.cleaned_data.get("status")
            date_of_completion = form.cleaned_data.get("date_of_completion")
            new_task = Tasks.objects.create(task=task, description=description, date_of_completion=date_of_completion,
                                            status_t=status_t)
            return redirect("task_view", pk=new_task.pk)
        return render(request, "create.html", {"form": form})


def update_task(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    if request.method == "GET":
        form = TasksForm(initial={
            "task": task.task,
            "description": task.description,
        })
        return render(request, "update.html", {"form": form})
    else:
        form = TasksForm(data=request.POST)
        if form.is_valid():
            task.task = form.cleaned_data.get("task")
            task.description = form.cleaned_data.get("description")
            task.status_t = form.cleaned_data.get("status")
            task.date_of_completion = form.cleaned_data.get("date_of_completion")
            task.save()
            return redirect("task_view", pk=task.pk)
        return render(request, "update.html", {"form": form})


def delete_task(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    if request.method == "GET":
        return render(request, "delete.html", {"task": task})
    else:
        task.delete()
        return redirect("index")
