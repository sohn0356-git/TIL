from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# Create your views here.
def getuser(request):
    users = [
        {'id':'id01','name':'name01','age':10},
        {'id':'id02','name':'name02','age':11},
        {'id':'id03','name':'name03','age':12},
        {'id':'id04','name':'name04','age':13},
        {'id':'id05','name':'name05','age':14}
    ]
    context = {'datas':users}
    return JsonResponse(context)

def getid(request):
    id = request.GET['id']
    if id != 'aaa' and id != 'bbb':
        return HttpResponse(1)
    else:
        return HttpResponse(id)


def getgraph(request):
    pk = request.GET.get('pk')
    data =  [{
                'name': 'Installation',
                'data': [43934, 52503, 57177, 69658, 97031, 119931, 137133, 154175]
            }, {
                'name': 'Manufacturing',
                'data': [24916, 24064, 29742, 29851, 32490, 30282, 38121, 40434]
            }, {
                'name': 'Sales & Distribution',
                'data': [11744, 17722, 16005, 19771, 20185, 24377, 32147, 39387]
            }, {
                'name': 'Project Development',
                'data': [0, 0, 7988, 12169, 15112, 22452, 34400, 34227]
            }, {
                'name': 'Other',
                'data': [12908, 5948, 8105, 11248, 8989, 11816, 18274, 18111]
        }]

    data2 =  [{
                'name': 'Manufacturing',
                'data': [123, 124, 32151, 12, 12, 2125, 12, 122142]
            }, {
                'name': 'Other',
                'data': [24916, 24064, 29742, 29851, 32490, 30282, 38121, 40434]
            }, {
                'name': 'Installation',
                'data': [11744, 17722, 16005, 19771, 20185, 24377, 32147, 39387]
            }, {
                'name': 'Project Development',
                'data': [0, 0, 7988, 12169, 15112, 22452, 34400, 34227]
            }, {
                'name': 'Sales & Distribution',
                'data': [12908, 5948, 8105, 11248, 8989, 11816, 18274, 18111]
        }]
    
    context = {}
    if pk=='1':
        context = {'datas':data}    
    else:
        context = {'datas':data2}    
    print(pk)
    return JsonResponse(context)
