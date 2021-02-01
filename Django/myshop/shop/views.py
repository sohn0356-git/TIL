import logging

from django.shortcuts import render, redirect
from django.urls import reverse
from frame.error import Errorcode
from frame.value import User
from frame.userdb import UserDb
from frame.itemdb import ItemDb
from django.utils.http import urlencode
from myshop.settings import UPLOAD_DIR
reuserlist = []
userdb = UserDb()
reitemlist = []
itemdb = ItemDb()

logger = logging.getLogger('users')
logger_item = logging.getLogger('items')
# Create your views here.

class ItemView():
    
    def upload(request):
        if request.method == 'POST':
            name = request.POST.get('name')
            price = request.POST.get('price')
            imgname = request.POST.get('img')
            if 'img' in request.FILES:
                img = request.FILES['img']
                imgname = img._name
                
                fp = open('%s/%s' % (UPLOAD_DIR, imgname) , 'wb')
                for chunk in img.chunks():
                    fp.write(chunk)
                    fp.close()
        try:
            itemdb.insert(name,price,imgname)
        except:
            context = {'section':'error',
                        'error' : 'Errorcode.code["e0001"]'}
            return render(request,'shop2/shop2.html',context)
        return redirect('shop:itemlist')
    
    def update(request):
        id = request.POST.get('id')
        name = request.POST.get('name')
        price = request.POST.get('price')
        imgname = request.POST.get('imgname')
        if 'img' in request.FILES:
            img = request.FILES['img']
            imgname = img._name
            
            fp = open('%s/%s' % (UPLOAD_DIR, imgname) , 'wb')
            for chunk in img.chunks():
                fp.write(chunk)
                fp.close()
        try:
            itemdb.update(id,name,price,imgname)
        except:
            context = {'section':'error',
                        'error' : 'Errorcode.code["e0002"]'}
            return render(request,'shop2/shop2.html',context)
    
        return redirect('../item/'+id)

def userlist(request):
    
    reuserlist = userdb.select()
    context = {
        'section' : 'shop2/userlist.html',
        'reusers' : reuserlist
    }
    return render(request, 'shop2/shop2.html', context)

def userdetail(request, id):
    reuser = userdb.selectone(id)
    context = {
        'section' : 'shop2/userdetail.html',
        'user' : reuser
    }
    return render(request, 'shop2/shop2.html', context)

def userdelete(request, id):
    userdb.delete(id)
    context = {
        'section' : 'userlist',
    }    
    return redirect('shop:userlist')

def userupdate(request, id):
    user = userdb.selectone(id)
    context = {
        'section' : 'shop2/userupdate.html',
        'user' : user
    }
    return render(request, 'shop2/shop2.html', context)

def useraddimpl(request):
    id = request.POST.get('id')
    pwd = request.POST.get('pwd')
    name = request.POST.get('name')
    try:
        userdb.insert(id,pwd,name)
    except:
        context = {'section':'error',
                    'error' : 'Errorcode.code["e0001"]'}
        return render(request,'shop2/shop2.html',context)
 
    return redirect('shop:userlist')

def userupdateimpl(request):
    id = request.POST.get('id')
    pwd = request.POST.get('pwd')
    name = request.POST.get('name')
    print(id,pwd,name)
    try:
        userdb.update(id,pwd,name)
    except:
        context = {'section':'error',
                    'error' : 'Errorcode.code["e0002"]'}
        return render(request,'shop2/shop2.html',context)
    qstr = urlencode({'id':id})
    return redirect('../user/'+id)

def useradd(request):
    context = {
        'section' : 'shop2/useradd.html'
    }
    return render(request, 'shop2/shop2.html', context)

def itemlist(request):
    
    reitemlist = itemdb.select()
    context = {
        'section' : 'shop2/itemlist.html',
        'reitems' : reitemlist
    }
    return render(request, 'shop2/shop2.html', context)

def itemdetail(request, id):
    reitem = itemdb.selectone(id)
    logger_item.debug(reitem.name+' '+str(reitem.price))
    context = {
        'section' : 'shop2/itemdetail.html',
        'item' : reitem
    }
    return render(request, 'shop2/shop2.html', context)

def itemdelete(request, id):
    itemdb.delete(id)
    context = {
        'section' : 'itemlist',
    }    
    return redirect('shop:itemlist')

def itemupdate(request, id):
    item = itemdb.selectone(id)
    context = {
        'section' : 'shop2/itemupdate.html',
        'item' : item
    }
    return render(request, 'shop2/shop2.html', context)

def itemaddimpl(request):
    id = request.POST.get('id')
    name = request.POST.get('name')
    price = request.POST.get('price')
    imgname = request.POST.get('imgname')
    try:
        itemdb.insert(name,price,imgname)
    except:
        context = {'section':'error',
                    'error' : 'Errorcode.code["e0001"]'}
        return render(request,'shop2/shop2.html',context)
 
    return redirect('shop:itemlist')

def itemupdateimpl(request):
    id = request.POST.get('id')
    name = request.POST.get('name')
    price = request.POST.get('price')
    imgname = request.POST.get('imgname')
    print(id,name,price,imgname)
    try:
        itemdb.update(id,name,price,imgname)
    except:
        context = {'section':'error',
                    'error' : 'Errorcode.code["e0002"]'}
        return render(request,'shop2/shop2.html',context)
 
    return redirect('shop:itemlist')

def itemadd(request):
    context = {
        'section' : 'shop2/itemadd.html'
    }
    return render(request, 'shop2/shop2.html', context)

class Mainview():
    def login(request):
        
        context = {
            'section' : 'shop2/login.html'
        }
        return render(request, 'shop2/shop2.html', context)
    
    def logout(request):
        if 'suser' in request.session:
            del(request.session['suser'])
        return render(request, 'shop2/shop2.html')

    def loginimpl(request):
        id = request.POST.get('id')
        pwd = request.POST.get('pwd')
        context = {}
        try:
            user = userdb.selectone(id)
            if user.pwd==pwd:
                context = {
                    'section' : 'shop2/loginok.html',
                    'loginuser' : id
                }
                logger.debug('user id:'+id)
                request.session['suser'] = id
                
            else:
                raise Exception
        except:
            context = {'section':'error',
                        'error' : 'Errorcode.code["e0003"]'}
            return render(request,'shop2/shop2.html',context)
        return render(request,'shop2/shop2.html',context)

def maps(request):
    context = {'section':'shop2/map.html'}
    return render(request, 'shop2/shop2.html', context)