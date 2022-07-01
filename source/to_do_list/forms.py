from django import forms


class TasksForm(forms.Form):
    task = forms.CharField(max_length=30, required=True, label="task")
    description = forms.CharField(max_length=2500, required=True, label="description")
