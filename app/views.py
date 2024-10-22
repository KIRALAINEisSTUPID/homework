from django.views.generic import TemplateView, ListView

from app.models import Blogs


class IndexView(TemplateView):
    template_name = 'index.html'


class BlogView(ListView):
    template_name = 'blog.html'
    model = Blogs
    context_object_name = 'blogs'