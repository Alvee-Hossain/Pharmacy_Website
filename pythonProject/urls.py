from django.contrib import admin
from django.urls import path
import Pharmacy_Website.views
import django.contrib.auth.views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Pharmacy_Website.views.pharmacy),
    path('pharmacy', Pharmacy_Website.views.pharmacy,name="pharmacy"),
    path('login',Pharmacy_Website.views.login,name="login"),
    path('forgotpassword', Pharmacy_Website.views.forgotpassword,name="forgotpassword"),
    path('otp', Pharmacy_Website.views.otp,name="otp"),
    path('resetpassword', Pharmacy_Website.views.resetpassword,name="resetpassword"),
    path('umedicinelist', Pharmacy_Website.views.umedicinelist,name="umedicinelist"),
    path('admin', Pharmacy_Website.views.admin,name="admin"),
    path('employee', Pharmacy_Website.views.employee,name="employee"),
    path('aemployee', Pharmacy_Website.views.aemployee,name="aemployee"),
    path('ainventory', Pharmacy_Website.views.ainventory,name="ainventory"),
    path('asales', Pharmacy_Website.views.asales,name="asales"),
    path('aprebooklists', Pharmacy_Website.views.aprebooklists,name="aprebooklists"),
    path('echeckbookeddrugs', Pharmacy_Website.views.echeckbookeddrugs,name="echeckbookeddrugs"),
    path('ereciepts', Pharmacy_Website.views.ereciepts,name="ereciepts"),
    path('echeckid', Pharmacy_Website.views.echeckid,name="echeckid"),
    path('search_drugs', Pharmacy_Website.views.search_drugs,name="search_drugs"),
    path('esearchdrugs1', Pharmacy_Website.views.esearchdrugs1,name="esearchdrugs1"),
    path('esearchdrugs2', Pharmacy_Website.views.esearchdrugs2, name="esearchdrugs2"),
    path('pharmacy', Pharmacy_Website.views.pharmacy, name="pharmacy"),
]
