from django.conf.urls import include, url
from django.contrib import admin

import expenses.views
import users.views

urlpatterns = [
    url(r'^$', expenses.views.HomeView.as_view(), name="home"),
    url(r'^add/$', expenses.views.AddView.as_view(), name="add"),
    url(r'^accounts/login/', users.views.CustomLoginView.as_view()),
    url(r'^accounts/', include('authtools.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
