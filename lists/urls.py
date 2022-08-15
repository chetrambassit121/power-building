from django.urls import path

from lists.views import lists_page

urlpatterns = [
    path("lists_page/", lists_page, name="lists_page"),
]


# from django.conf.urls import url
# from lists import views

# urlpatterns = [
#     url(r'^$lists_page/', views.lists_page, name='lists_page'),
# ]
