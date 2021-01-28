from django.shortcuts import render, redirect
from frame.userdb import UserDb
from frame.error import Errorcode
from frame.value import User



# Create your views here.
def userlist(request):
    rsuserlist = UserDb().select()
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
    try:
        Userdb().insert(id,pwd,name)
    except:
        context = {'section':'error',
                    'error' : 'Errorcode.code["e0001"]'}
        return render(request,'shop2/shop2.html',context)    
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