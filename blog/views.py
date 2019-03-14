from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Article, Tag


class BlogView(ListView):
    model = Article
    context_object_name = "articles"
    template_name = "blog/blog.html"
    paginate_by = 5


class ArticleView(DetailView):
    model = Article
    template_name = "blog/article.html"
    slug_field = "url"


class TagView(ListView):
    context_object_name = "articles"
    template_name = 'blog/blog.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        kwargs['tag'] = self.tag
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, title=self.kwargs.get('slug'))
        queryset = self.tag.article_set.all()
        return queryset
