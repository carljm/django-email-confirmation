from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns("emailconfirmation.views",
    url(r"^confirm/(\w+)/$", "confirm", name="emailconfirmation_confirm"),
    url(r"^delete/$", "delete", name="emailconfirmation_delete"),
    url(r"^delete/done/$", direct_to_template,
        {"template": "emailconfirmation/deleted.html"},
        name="emailconfirmation_delete_done")
)
