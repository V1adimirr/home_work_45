from django.shortcuts import render

from to_do_list.models import Tasks


def index_view(request):
    tasks = Tasks.objects.all()
    context = {"tasks": tasks}
    return render(request, "index.html", context)


def task_view(request):
    task_id = request.GET.get('pk')
    task = Tasks.objects.get(pk=task_id)
    context = {'task': task}
    return render(request, 'task_view.html', context)

def create_task(request):
    if request.method == "GET":
        return render(request, "create.html")
    else:
        task = request.POST.get("task")
        date_of_completion = request.POST.get("date_of_completion")
        new_task = Tasks.objects.create(task=task, date_of_completion=date_of_completion)
        context = {"task": new_task}
        return render(request, "task_view.html", context)
