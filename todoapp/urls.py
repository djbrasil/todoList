from django.urls import path
from .views import todoappView, deleteTodoView 
 
urlpatterns = [ 
	path('', todoappView.as_view(), name='todoapp'), 
	path('deleteTodoItem/<int:pk>/', deleteTodoView.as_view(), name='deleteTodoItem'),    
]
 