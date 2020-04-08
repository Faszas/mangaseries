
# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
import requests
from bs4 import BeautifulSoup
from django.urls import reverse_lazy
from .models import Nanatsu, Overlord, Konosuba, Onepunchman, Demon_Slayer, Prison_school, myManga, Conan
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout

# Create your views here.

context = {'nanatsu': Nanatsu, 'overlord': Overlord,
           'konosuba': Konosuba, 'onepunchman': Onepunchman,
           'demonslayer':Demon_Slayer, 'prisonschool': Prison_school,'conan': Conan ,'all': myManga}


def get_img_links(url):
    src = requests.get(str(url))

    soup = BeautifulSoup(src.text, features = 'html.parser')
    # lấy tất cả link ảnh mà có chữ h nằm ở đầu tiên
    link_imgs = []
    try:
        link_imgs = [x['src'] for x in soup.findAll('img') if x['src'][0] == 'h']
    except:
        pass
    return '\n'.join(link_imgs)




def homePage(request):
    return render(request, 'home.html')

class ListView(View):
    def get(self, request, name):
        global context
        obj = context[name].objects.all().order_by('-chapter')
        # temp = context[name].objects.get(chapter = 1)
        # name = temp.title
        return render(request, 'index.html', {'obj': obj})

class DetailView(View):
    def get(self, request, name,  chap):
        global context
        obj = context[name].objects.get(chapter = chap)
        img_link = obj.url.split("\n")
        count = len(context[name].objects.all())
        return render(request, 'detail.html', {'obj': obj, 'imgs': img_link, 'count': count})



class UploadView(LoginRequiredMixin, View):

    login_url = '/login/'

    def get(self, request):
        return render(request, 'upload.html')


    def post(self, request):
        global context
        if request.method == 'POST':
            title = request.POST.get('title')
            chapter = request.POST.get('chapter')
            url = request.POST.get('url')
            category = request.POST.get('category')
            author = request.POST.get('author')
            nameModel = request.POST.get('namemodel')
            try:
                context[nameModel]
            except KeyError:
                return HttpResponse("Name Model is not valid")

            for index in range(1050, 0, -1):

                titlenew = title + "chapter " + str(index)
                chapter = str(index)

                urlnew = url + "-{}/".format(str(index))

                obj = context[nameModel].objects.create(title = titlenew, chapter = chapter,
                                                        url = get_img_links(urlnew), Category = category,
                                                        Author = author)
                obj.save()
                print("Created ", index)
            return HttpResponse("Success")



class LoginView(View):

    def get(self, request):
        logout(request)
        return render(request, 'login.html')

    def post(self, request):
        if request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user=user)
                return redirect(reverse_lazy('manga:home'))
            else:
                return HttpResponse("Username or password is not valid")
        return HttpResponse("not valid")


class DeleteOneView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, name, chap):
        return render(request, 'delete1.html')

    def post(self, request, name, chap):
        global context
        if request.method == 'POST':
            temp = context[name].objects.get(chapter = chap)
            temp.delete()
            return redirect(reverse_lazy('manga:home'))


class UpdateOneView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, name, chap):
        global context
        return render(request, 'update1.html', {'obj': context[name].objects.get(chapter = chap)})

    def post(self, request, name, chap):
        global context
        if request.method == 'POST':
            obj = context[name].objects.get(chapter = chap)
            obj.title = request.POST.get('title')
            obj.chapter = request.POST.get('chapter')
            obj.Author = request.POST.get('author')
            obj.Category = request.POST.get('category')
            obj.url = request.POST.get('url')
            obj.save()
            return redirect(reverse_lazy('manga:home'))


class DeleteAllView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, name):
        return render(request, 'deleteall.html')

    def post(self, request, name):
        global context
        if request.method == 'POST':
            context[name].objects.all().delete()
            return redirect(reverse_lazy('manga:home'))


class UpdateAllView(LoginRequiredMixin, View):

    login_url = '/login/'

    def get(self, request, name):
        return render(request, 'updateall.html')

    def post(self, request, name):
        if request.method == 'POST':
            context[name].objects.all().update(Category=request.POST.get('category'),
                                               Author=request.POST.get('author'))
            return HttpResponse("You have update successfully")



class SearchView(View):

    def get(self, request):
        global context
        context = {'nanatsu': Nanatsu, 'overlord': Overlord,
                   'konosuba': Konosuba, 'onepunchman': Onepunchman,
                   'demonslayer': Demon_Slayer, 'prisonschool': Prison_school, 'all': myManga}

        obj1 = context['nanatsu'].objects.all().filter(title__contains = request.GET.get('searching'))
        obj2 = context['overlord'].objects.all().filter(title__contains = request.GET.get('searching'))
        obj3 = context['konosuba'].objects.all().filter(title__contains = request.GET.get('searching'))
        obj4 = context['onepunchman'].objects.all().filter(title__contains = request.GET.get('searching'))
        obj5 = context['demonslayer'].objects.all().filter(title__contains = request.GET.get('searching'))
        obj6 = context['prisonschool'].objects.all().filter(title__contains = request.GET.get('searching'))
        obj7 = context['conan'].objects.all().filter(title__contains = request.GET.get('searching'))

        return render(request, 'search.html', {'obj1': obj1, 'obj2': obj2, 'obj3': obj3,
                                               'obj4': obj4, 'obj5': obj5, 'obj6': obj6,
                                               'obj7': obj7
                                               })


def videoView(request):
    return render(request, 'video.html')




