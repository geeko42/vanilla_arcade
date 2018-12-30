from django.conf.urls import url
from django.urls import path
from . import views

#TEMPLATE TAGGING
app_name = 'first_app'
urlpatterns = [
    path(form_submit,views.add_contact),
    # path(r'^index/', include('index.urls',namespace="index")),
    # url(r'^$',views.index,name='index',namespace="index"),
]
