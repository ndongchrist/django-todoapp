from django.urls import path, include
from .views import CreateTodoView, EditTodoView, DeleteTodoView,AcceptTodoView

urlpatterns = [
    path('', CreateTodoView.as_view(), name="hello"),
    path('edit/<int:task_id>', EditTodoView.as_view(), name="edit" ),
    path('delete/<int:task_id>', DeleteTodoView.as_view(), name="delete"),
    path('done', AcceptTodoView.as_view(), name="done")
]