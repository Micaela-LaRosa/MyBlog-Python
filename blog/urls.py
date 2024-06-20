from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('', home, name="Home"),
    path('about/', about, name="about"),
    path('pages/', BlogListView.as_view(), name= "PagesList"),
    path('blog/addnew', BlogCreateView.as_view(), name= "NewPage"),
    path('pages/<pk>', BlogDetailView.as_view(), name= "DetailBlog"),
    path('pages/<pk>/edit', BlogUpdateView.as_view(), name= "EditBlog"),
    path('pages/<pk>/delete', BlogDeleteView.as_view(), name= "DeleteBlog"),
    path('blogSearch/', blogSearch, name="blogSearch"),
    path('search/', search, name="search"),
    path('login/', login_view, name="Login"),
    path('signin/', register, name="Signin"),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path('editProfile/', edit_profile, name="EditProfile"),
]

