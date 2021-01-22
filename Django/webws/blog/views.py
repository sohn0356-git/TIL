from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def resume(request):
    return render(request, 'resume.html')

def table(request):
    return render(request, 'table.html')

def multi(request):
    return render(request, 'multi.html')

def resume(request):
    if request.method == 'POST':
        title = request.POST.get('title'), #.POST['title'],
        content = request.POST.get('content'),
        regdate = datetime.now()     
        return HttpResponseRedirect('resume_page.html',{'t':'a','e':'s','d':'c'}) # 추가후 목록 보기로 돌아감
    else:
        return render(request, 'resume.html')

def result(request):
    return render(request, 'result.jsp')