from django.shortcuts import render

from articles.models import Article, Tag, TagsArticles


def articles_list(request):
    template = 'articles/news.html'
    articles = Article.objects.order_by('-published_at')
    tags = Tag.objects.all()
    context = {
        'articles': articles,
        'tags': tags
    }

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
