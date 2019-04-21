from django.views.generic import DetailView, ListView
from django.shortcuts import get_object_or_404


from .models import Page
from dashboard.models import HomeMsg


class IndexView(ListView):
    template_name = "merken/pages/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["home_page"] = get_object_or_404(Page, url="index")
        context["message"] = HomeMsg.load()
        return context

    def queryset(self):
        pass


class PageView(DetailView):
    model = Page
    template_name = "merken/pages/page.html"
    slug_field = "url"
