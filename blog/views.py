from django.http.response import HttpResponse
from django.shortcuts import render
from .models import blogg
from accounts.models import admins, info_site
from django.views.generic import ListView, DetailView
from rest_framework import generics



try:
    info = info_site.objects.get(id=1)
    title = info.title
except:
    title = "Null"

def blog(request):
    try:
        us = request.user.username
        admins.objects.get(name_admin=us)
        if request.method == 'POST':
            titlle = request.POST['title']
            text = request.POST['text']
            try:
                if titlle == "":
                    return HttpResponse("title should not be None")
                elif text == "":
                    return HttpResponse("text should not be None")
                try:
                    blogg.objects.get(title=titlle)
                    return HttpResponse("این موضوع قبلاً انتخاب شده است")
                except:
                    blogg.objects.get(text_blog=text)
                    return HttpResponse("این مطلب قبلاً نوشته شده است")
                    
            except:
                blog_new = blogg(title=titlle, text_blog=text)
                blog_new.save()
                return HttpResponse("save sucsessfully")
        else:
            return render(request, "blog/blog.html", {'title':title})
    except:
        return HttpResponse("Not Found")
class home(ListView):
    model = blogg
    template_name = 'blog/home.html'
class ArticleDetailView(DetailView):
    model = blogg
    template_name = 'blog/detail.html'


class weblog_admin(ListView):
    model = blogg
    template_name = 'blog/weblog.html'

# detail_admin
def detail_admin(request, pk):
    blog = blogg.objects.get(id=pk)
    titlle = blog.title
    text = blog.text_blog
    return render(request, 'blog/detail_admin.html', {'title':titlle, 'text':text, 'id':pk})


def save_blog(request, pk):
    try:
        us = request.user.username
        admins.objects.get(name_admin=us)
        if request.method == 'POST':
            title = request.POST['title']
            text = request.POST['text']
            blog = blogg.objects.get(id=pk)
            blog.title = title
            blog.text_blog = text
            blog.save()
            return HttpResponse("save successefully")
        else:
            return HttpResponse('Not Found')
    except:
        return HttpResponse('Not Found page')

def delete_blog(request, pk):
    if request.method == 'POST':
        blog = blogg.objects.get(id=pk)
        blog.delete()
        return HttpResponse("delete successefully")
    else:
        return HttpResponse('Not Found')
 

def search(request):
        if request.method == 'POST':
            name_search = request.POST['search']
            search_List = []
            Find_title = []
            Find_text_body = []
            for i in range(10):
                try:
                    bl = blogg.objects.get(id=i)
                    search_List.append(bl.title)
                except:
                    pass
            for name_of_search in search_List:
                if name_of_search == name_search:
                    te = blogg.objects.get(title=name_of_search)
                    Find_List_Save = name_of_search
                    text = te.text_blog
                    Find_text_body.append(text)
                    Find_title.append(Find_List_Save)
                elif name_of_search=="":
                    Find_text_body.append("Not Found")
                    Find_title.append("Not Found") 
            Find_title_len = len(Find_title)
            if Find_title_len == 0:
                return render(request, 'blog/NotFound_search.html', {"title":"NOT Found", "text":"NOT Found"})
            else:	
                return render(request, 'blog/find.html', {"title":Find_title, "text":Find_text_body})	

                

