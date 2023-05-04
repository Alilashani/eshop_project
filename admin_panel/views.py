from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from article_module.models import Article


def all_articles(request: HttpRequest):
    return render(request, 'admin_panel/article/articles_list.html')


# Todo: Cures "" Class Base Mixin In Django ""


class ArticlesListView(ListView):
    template_name = 'admin_panel/article/articles_list.html'
    model = Article
    paginate_by = 12

    def get_context_data(self, *args, **kwargs):
        context = super(ArticlesListView, self).get_context_data(*args, **kwargs)
        # context['date'] = date2jalali(self.request.user.date_joined)
        return context

    def get_queryset(self):
        query = super(ArticlesListView, self).get_queryset()
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(selected_categories__url_title__iexact=category_name)
        return query



