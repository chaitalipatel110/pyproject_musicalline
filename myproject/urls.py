"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from myapp.views import home, MusicalStoreRegEditView, MusicalStoreLogoutView, get_current_time, PersonInfo, PersonListView, MusicalStoreHomeView, MusicalStoreRegView, MusicalStoreRegAddView, MusicalStoreRegShow, MusicalStoreInstrumentDetail, MusicalStoreInstrumentView, AllEmails, MusicalStoreLoginView, MusicalStoreLoginAddView, MusicalStoreAboutusView, MusicalStoreContactusView


urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('current_time/', get_current_time, name='current_time'),
    path("display_person/<slug:pk>", PersonInfo.as_view()),
    path("people/", PersonListView.as_view(), name='people-list'),
    path("people/emails", AllEmails.as_view(), name='people-emails-list'),
    path("musical_store_home/", MusicalStoreHomeView.as_view(), name='musical_store_home'),
    path("musical_store_reg_add_view/", MusicalStoreRegAddView.as_view(), name='musical_store_reg_add'),
    path("musical_store_reg_edit_view/", MusicalStoreRegEditView.as_view(), name='musical_store_reg_edit'),
    path("musical_store_reg_view/", MusicalStoreRegView.as_view(), name='musical_store_reg'),
    path("musical_store_reg_show/", MusicalStoreRegShow.as_view(), name='musical_store_reg_show'),
    path("musical_store_instrument/", MusicalStoreInstrumentView.as_view(), name='musical_store_instrument'),
    path("musical_store_instrument_detail/<int:id>/", MusicalStoreInstrumentDetail.as_view(), name='musical_store_instrument_detail'),
    path("musical_store_login_view/", MusicalStoreLoginView.as_view(), name='musical_store_login'),
    path("musical_store_logout_view/", MusicalStoreLogoutView.as_view(), name='musical_store_logout'),
    path("musical_store_login_add_view/", MusicalStoreLoginAddView.as_view(), name='musical_store_login_add'),
    path("musical_store_aboutus_view/", MusicalStoreAboutusView.as_view(), name='musical_store_aboutus'),
    path("musical_store_contactus_view/", MusicalStoreContactusView.as_view(), name='musical_store_contactus'),



]

# Appending the static urls for dev environment
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
