from django.shortcuts import render,get_object_or_404
from .models import Bloglist
# Create your views here.

def allblogs(request):
    bloglists = Bloglist.objects
    return render(request,'bloglist/allblogs.html',{'bloglists':bloglists})

def detail(request,blog_id):
    detailblog = get_object_or_404(Bloglist,pk=blog_id)
    return render(request,'bloglist/detail.html',{'blog':detailblog})
