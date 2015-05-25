from django.conf.urls import patterns, include, url
from bars import views
from rest_framework import routers
from django.contrib import admin
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'bars', views.BarViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'barfindr_.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^b/', views.index),
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),


)
