from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page


urlpatterns = [
   path('', cache_page(60)(NewsList.as_view()), name='news_list'),
   path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
   path('search/', SearchList.as_view(), name='news_search'),
   path('news/create/', NewsCreate.as_view(), name='nw_create'),
   path('articles/create/', ArticlesCreate.as_view(), name='ar_create'),
   path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='nw_update'),
   path('articles/<int:pk>/edit/', ArticlesUpdate.as_view(), name='ar_update'),
   path('news/<int:pk>/delete/', NewsDelete.as_view(), name='nw_delete'),
   path('articles/<int:pk>/delete/', ArticlesDelete.as_view(), name='ar_delete'),
   path('categories/<int:pk>/', CategoryList.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
]
