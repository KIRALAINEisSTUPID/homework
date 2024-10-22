from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView

from app.models import Blogs


class IndexView(TemplateView):
    template_name = 'index.html'


class BlogView(ListView):
    template_name = 'blog.html'
    model = Blogs
    context_object_name = 'blogs'

class CreateBlogView(CreateView):
    template_name = 'create.html'
    model = Blogs
    fields = ['img', 'title', 'content']
    success_url = '/'


class UpdateBlogView(UpdateView):
    template_name = 'update.html'
    model = Blogs
    fields = ['img', 'title', 'content']
    success_url = '/'

class DeleteBlogView(DeleteView):
    template_name = 'delete.html'
    model = Blogs
    success_url = '/'

class DetailBlogView(DetailView):
    template_name = 'detail.html'
    model = Blogs
    context_object_name = 'blog'