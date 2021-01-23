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
        res_data = {}
        r1 = request.POST.get('r1') #.POST['title'],
        if r1=='cr1':
            res_data['r1'] = "경력"
        else:
            res_data['r1'] = "신입"
        c1 = request.POST.get('c1')
        if c1=='ch1':
            res_data['c1'] = "산책"
        elif c1=='ch2':
            res_data['c1'] = "운동"
        else:
            res_data['c1'] = "여행"
        resume = request.POST.get('tt')
        res_data['resume'] = resume
        return render(request, 'resume_page.html', res_data)
    else:
        return render(request, 'resume.html')
