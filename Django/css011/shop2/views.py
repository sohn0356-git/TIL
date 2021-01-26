from django.shortcuts import render, redirect


reuserlist = [
        {'id':'id01','pwd':'pwd01', 'name':'james01'},
        {'id':'id02','pwd':'pwd02', 'name':'james02'},
        {'id':'id03','pwd':'pwd03', 'name':'james03'},
        {'id':'id04','pwd':'pwd04', 'name':'james04'},
        {'id':'id05','pwd':'pwd05', 'name':'james05'}
    ]

# Create your views here.
def userlist(request):

    context = {
        'section' : 'userlist',
        'reusers' : reuserlist
    }
    return render(request, 'shop2/shop2.html', context)

def userdetail(request, id):
    context = {
        'section' : 'userdetail'
    }
    for reuser in reuserlist:
        if reuser['id']==id:
            context['user'] = reuser 
    
    return render(request, 'shop2/shop2.html', context)

def useraddimpl(request):
    id = request.POST.get('id')
    pwd = request.POST.get('pwd')
    name = request.POST.get('name')
    reuserlist.append({'id':id,'pwd':pwd,'name':name})
    print(reuserlist)
    return redirect('/shop2/user')

def useradd(request):
    context = {
        'section' : 'userlist'
    }
    return render(request, 'shop2/useradd.html', context)

def itemlist(request):
    context = {
        'section' : 'itemlist'
    }
    return render(request, 'shop2/shop2.html', context)

def itemadd(request):
    context = {
        'section' : 'itemadd'
    }
    return render(request, 'shop2/shop2.html', context)