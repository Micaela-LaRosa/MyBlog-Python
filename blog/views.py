from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
from .forms import UserEditForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

def home(req):
    return render(req, "home.html", {})

def about(req):
    return render(req, "about.html", {})

class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    context_object_name = "blogs"
    template_name = "blog_list.html"

class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = "blog_detail.html"

class BlogCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Blog
    template_name = "blog_create.html"
    success_url = reverse_lazy('PagesList')
    fields = ('__all__')

    def test_func(self):
        return self.request.user.is_staff

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    template_name = "blog_edit.html"
    success_url = reverse_lazy('PagesList')
    fields = ('__all__')
    context_object_name = "blogs"

    def test_func(self):
        return self.request.user.is_staff

class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    template_name = "blog_delete.html"
    success_url= reverse_lazy('PagesList')
    context_object_name = "blogs"

    def test_func(self):
        return self.request.user.is_staff
    
@login_required
def blogSearch(req):
    return render(req, 'blogSearch.html')

@login_required
def search(req):
    if req.GET["title"]:
        title= req.GET["title"]
        blogs = Blog.objects.filter(title__icontains=title)
        return render(req, 'resultSearch.html', {"blogs": blogs, "title": title})
    else: answer = "Please sent some info"
    return HttpResponse(answer)

def login_view(req):
    if req.method == "POST":
        myForm = AuthenticationForm(req, data=req.POST)
        if myForm.is_valid():
            data = myForm.cleaned_data
            usern = data["username"]
            psw = data["password"]
            user =authenticate(username=usern, password=psw)
            if user:
                login(req, user)
                return render(req, "home.html", {"message": f"Welcome {usern}"})    
            else:
                return render(req, "home.html", {"message": "Wrong information"})    
        else:
            return render(req, "home.html", {"message": "Invalid information"})
    else:
        myForm = AuthenticationForm()
        return render(req, "login.html", {"myForm": myForm})
    
def register(req):
    if req.method == "POST":
        myForm = UserCreationForm(req.POST)
        if myForm.is_valid():
            data = myForm.cleaned_data
            usern = data["username"]
            myForm.save()
            return render(req, "home.html", {"message": f"User {usern} created successfully"})    
        else:
            return render(req, "home.html", {"message": "Invalid information"})
    else:
        myForm = UserCreationForm()
        return render(req, "signin.html", {"myForm": myForm})

@login_required    
def edit_profile(req):
    user = req.user
    if req.method == 'POST':
        myForm = UserEditForm(req.POST, instance=req.user)
        if myForm.is_valid():
            data = myForm.cleaned_data
            user.username = data['username']
            user.email = data['email']
            user.set_password(data["password1"])
            user.save()
            return render(req, "home.html", {"message": "Information successfully update"})
        else:
            return render(req, "edit_user.html", {"myForm": myForm})
    else:
        myForm = UserEditForm(instance=req.user)
        return render(req, "edit_user.html", {"myForm": myForm})
