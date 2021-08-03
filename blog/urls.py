from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include
from posts.views import index, post, author, blog, search, list_by_category
from django.conf.urls import url
from mains.views import mains
from team.views import team, team_member

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('post/<pk>/', post, name='post-detail'),
    url(r'^author/(?P<pk>[-\w]+)/$', view=author, name='author'),
    path('blog/', blog, name = "post-list"),
    path('search/', search, name = "search"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('mains/<pk>/', mains, name='mains-post'),
    path('team/', team, name='team'),
    path('team_member/<pk>', team_member, name='team-member'),

    

    url(r'^cat/(?P<pk>[-\w]+)/$', view=list_by_category, name='list_by_category'),

    url(r'hitcount/', include('hitcount.urls', namespace='hitcount')),

   
    path('oauth/', include('social_django.urls', namespace='social')),
    
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


