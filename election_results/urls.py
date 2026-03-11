from django.urls import path
from . import views

urlpatterns = [

    path("", views.pollingUnitResults, name="polling_unit_results"),

    path("lga-results/", views.lgaResults, name="lga_results"),

    path("add-results/", views.addResults, name="add_results"),

]