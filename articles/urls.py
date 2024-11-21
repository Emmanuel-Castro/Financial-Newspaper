from django.urls import path
from .views import ArticlesListView, ArticleFormView, ArticleMainView

urlpatterns = [
    path('', ArticlesListView.as_view()),
    path('base/', ArticleMainView.as_view(), name="article_main"),
    path('create/', ArticleFormView.as_view(), name="create_article"),
]