from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_todos),
    path('<int:todo_id>', views.todo_detail_view),
    path('cbv/', views.TodosListApiView.as_view()),
    path('cbv/<int:todo_id>', views.TodosDetailApiView.as_view()),
    path('mixins/', views.TodosListMixinApiView.as_view()),
    path('mixins/<pk>', views.TodosDetailMixinApiView.as_view()),
    path('generics/', views.TodosGenericsApiView.as_view()),
    path('generics/<pk>', views.TodoGenericsDetailView.as_view()),
]
