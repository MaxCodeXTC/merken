from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Article, Tag


class BlogSitemap(Sitemap):
    protocol = "https"

    def items(self):
        return ["blog_app:blog"]

    def location(self, item):
        return reverse(item)


class ArticleSitemap(Sitemap):
    protocol = "https"
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        articles = Article.objects.all()
        return articles.published()

    def lastmod(self, obj):
        return obj.created_at


class TagSitemap(Sitemap):
    protocol = "https"

    def items(self):
        return Tag.objects.all()
