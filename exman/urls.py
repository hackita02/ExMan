from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

import expenses.views

router = routers.DefaultRouter()
router.register(r'expenses', expenses.views.ExpenseViewSet)

urlpatterns = [
    url(r'^$', expenses.views.HomeView.as_view(), name="home"),
    url(r'^add/$', expenses.views.AddView.as_view(), name="add"),

    url(r'^accounts/', include('authtools.urls')),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^api/v1/', include(router.urls)),

    url(r'^admin/', include(admin.site.urls)),
]
