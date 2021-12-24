from django.shortcuts import redirect, render 
from django.urls import reverse_lazy 
from django.views.generic.edit import CreateView, DeleteView 
from .models import TodoListItem
from .forms import TodoListItemForm
 
class todoappView(CreateView):
    model = TodoListItem 
    class_form = TodoListItemForm
    template_name = 'todolist.html'  
    fields = {"category","link"}
 
    def post(self, request, *args, **kwargs):    
        form = TodoListItemForm(request.POST)   
        if request.method == "POST": 
            if form.is_valid():
                form.save()
                return redirect('/')
        form = TodoListItemForm() 
        page = {"form" : form}  
        return render(request, 'todolist.html', page) 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = self.model.objects.all()
        return context
 
class deleteTodoView(DeleteView):
    model = TodoListItem 
    template_name = 'todolist.html'
    success_url = reverse_lazy('todoapp')



    