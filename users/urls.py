from django.urls import path
from . import views

urlpatterns = [
    path("logout/", views.logoutUser, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("accountsummary/", views.accountsummary, name="accountsummary"),
    path("accountdetails/", views.accountdetails, name="accountdetails"),
    path("creditcards/", views.creditcards, name="creditcards"),
    path("contactus/", views.contactus, name="contactus"),
    path("billpaycenter/", views.billpaycenter, name="billpaycenter"),
    path("deletepaytoaccount/", views.deletepaytoaccount, name="deletepaytoaccount"),
    path("paynow/", views.paynow, name="paynow"),
    path("paynowc/", views.paynowc, name="paynowc"),
    path("searchpaytolist/", views.searchpaytolist, name="searchpaytolist"),
    path("beneficiary/", views.beneficiary, name="beneficiary"),
    path("add-beneficiery/", views.addbeneficiery, name="add-beneficiery"),
    path("profile", views.profile, name="profile"),
    path("Change-Pin", views.changepin, name="changepin"),
    path("Change-Password", views.changepassword, name="changepassword"),
    path("transfer/", views.transfer, name="transfer"),
    path("deposit/", views.deposit, name="deposit"),
    path("spending/", views.spending, name="spending"),
    path("confirm-transfer/", views.confirm_transfer, name="confirmtransfer"),
    path("transfer-success/", views.successful, name="successful"),
]