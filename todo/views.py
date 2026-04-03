from django.shortcuts import render

def home_view(request):
    """
    Renders the main task list and creation form.
    """
    return render(request, 'todo/index.html')
