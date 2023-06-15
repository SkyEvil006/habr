from django.urls import path
from articleapp.views import *
from .views import create_block,view_art, like, unlike
app_name ='articleapp'
urlpatterns=[

    path('',home, name='home' ),
    path('view-art-<int:art_id>',view_art,name='view_art'),
    path('create-article/', create_article, name='create-article'),
    path('change-article-<int:art_id>/', change_article, name='change-article'),
    path('view-article-<int:art_id>/', view_article, name='view_article'),
    path('delete-article-<int:art_id>/', delete_article, name='delete_article'),
    path('change-article-<int:art_id>/create-block/', create_block, name='create-block'),
    path('change-block-<int:block_id>/', change_block, name='change_block'),
    path('delete-block-<int:block_id>/', delete_block, name='delete_block'),
    path('article/<int:art_id>/like/', like, name='like'),
    path('article/<int:art_id>/unlike/', unlike, name='unlike')





]