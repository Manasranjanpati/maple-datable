from django.contrib import admin
from django.conf.urls import url, include

from rest_framework import routers

from navyapp import views


router = routers.DefaultRouter()
router.register(r'aircrafts', views.AircraftViewSet)
router.register(r'origins', views.OriginViewSet)


urlpatterns = [
    url('^admin/', admin.site.urls),
    url('^api/', include(router.urls)),
    url('^api/post-list/aircrafts', views.AircraftPostListView.as_view(), name='aircraft_post_list'),
    url('', views.index, name='aircrafts')
]
