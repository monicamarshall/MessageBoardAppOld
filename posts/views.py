from django.views.generic import ListView
from .models import Post

from .forms import PostForm
from django.shortcuts import render


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'

def home(request):
    if request.method == "POST":
        form = PostForm(request.POST)        
        if form.is_valid():
            post = Post(
                text=form.cleaned_data["body"]
            )
            post.save()
        else:
            form = PostForm()
    all_posts_list = Post.objects.all()
    form = PostForm()
    context = {"all_posts_list": all_posts_list,"form": form}
    return render(request, "home.html", context)