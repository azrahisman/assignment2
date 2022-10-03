from django.shortcuts import render

# Create your views here.
def show_todolist(request):
    return render(request, "todolist.html")