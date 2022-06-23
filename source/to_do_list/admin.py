from django.contrib import admin

# Register your models here.
from to_do_list.models import Tasks


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'task', 'date_of_completion']
    list_display_links = ['task']
    list_filter = ['task']
    search_fields = ['date_of_completion']
    fields = ['task', 'date_of_completion']


admin.site.register(Tasks, TaskAdmin)
