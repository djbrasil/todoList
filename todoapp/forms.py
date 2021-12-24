from django import forms 
from .models import TodoListItem 
  
class TodoListItemForm(forms.ModelForm):  
     
    class Meta:
        model = TodoListItem
        fields = ('category', 'link')
 
 
