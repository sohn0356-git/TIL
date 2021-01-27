from django.shortcuts import render

# Create your views here.

def login(request):
    id = request.POST.get('id')
    pwd = request.POST.get('pwd')
    return render(request, 'ok.html', {'id':id,'pwd':pwd})