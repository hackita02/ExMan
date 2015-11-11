from django.conf.urls import include, url
from django.contrib import admin

import expenses.views

urlpatterns = [
    url(r'^$', expenses.views.HomeView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
]
