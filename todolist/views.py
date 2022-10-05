from django.shortcuts import render
from todolist.models import ItemTodolist, User

# Create your views here.
def show_todolist(request):
    data_todolist_item = ItemTodolist.objects.all()
    user =  User(first_name='Azra', last_name='Hisman', email='azra.batrisyia11@ui.ac.id')
    user.save()
    context = {
    'list_item': data_todolist_item,
    'name': 'Azra'
}
    return render(request, "todolist.html", context)