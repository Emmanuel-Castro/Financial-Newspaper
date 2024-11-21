from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .forms import Article

# Create your views here.
class ArticlesListView(generic.TemplateView):
    template_name = "articles/index.html"

    def get_context_data(self):
        some_txt = "Financial Newspaper project in process"

        return {
            "message": some_txt
        }

# Articles app main view (test)
class ArticleMainView(ListView):
    template_name = "articles/base.html"
    model = Article


# Article creation view.
class ArticleFormView(CreateView):
    model = Article
    fields = ['title', 'subtitle', 'author', 'tag' ,'date', 'content']
    success_url = reverse_lazy('create_article')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)