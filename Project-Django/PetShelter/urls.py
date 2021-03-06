from django.conf.urls import patterns, url
from django.conf import settings
from PetShelter import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^animals/$', views.animals, name='animals'),
    url(r'^animals/(?P<species_id>[^\s/]+)/$', views.animals_species, name='animals_species'),
    url(r'^animal/(?P<species_id>[^\s/]+)/(?P<animal_id>[^\s/]+)/$',
          views.animal_species, name='animal_species'),
    url(r'^animal/(?P<species_id>[^\s/]+)/(?P<animal_id>[^\s/]+)/(?P<file_id>[^\s/]+)/$',
          views.animal_file_species, name='animal_file_species'),
    url(r'^shelters/$', views.shelters, name='shelters'),
    url(r'^shelter/(?P<shelter_id>[^\s/]+)/$', views.shelter, name='shelter'),
    url(r'^staffs/$', views.staffs, name='staffs'),
    url(r'^staff/(?P<staff_id>[^\s/]+)/$', views.staff, name='staff'),
    url(r'^users/$', views.users, name='users'),
    url(r'^user/(?P<user_id>[^\s/]+)/$', views.user, name='user'),
    url(r'^activities/receipts/$', views.act_receipts, name='act_receipts'),
    url(r'^activities/receipt/(?P<receipt_id>[^\s/]+)/$', views.act_receipt, name='act_receipt'),
    url(r'^activities/adoptions/$', views.act_adoptions, name='act_adoptions'),
    url(r'^activities/adoption/(?P<adoption_id>[^\s/]+)/$', views.act_adoption, name='act_adoption'),
    url(r'^activities/surrenders/$', views.act_surrenders, name='act_surrenders'),
    url(r'^activities/surrender/(?P<surrender_id>[^\s/]+)/$', views.act_surrender, name='act_surrender'),
    url(r'^activities/donations/$', views.act_donations, name='act_donations'),
    url(r'^activities/donation/(?P<donation_id>[^\s/]+)/$', views.act_donation, name='act_donation'),
    url(r'^activities/volunteers/$', views.act_volunteers, name='act_volunteers'),
    url(r'^activities/volunteer/(?P<volunteer_id>[^\s/]+)/$', views.act_volunteer, name='act_volunteer'),
    url(r'^applications/adopt/$', views.app_adopt, name='app_adopt'),
    url(r'^applications/surrender/$', views.app_surrender, name='app_surrender'),
    url(r'^applications/donate/$', views.app_donates, name='app_donates'),
    url(r'^applications/donate/(?P<donate_type>[^\s/]+)/$', views.app_donate, name='app_donate'),
    url(r'^applications/volunteer/$', views.app_volunteer, name='app_volunteer'),
    url(r'^login/$', views.login, name='login'),
    url(r'^management/$', views.management, name='management'),
    url(r'^management/receive/$', views.man_receive, name='man_receive'),
    url(r'^management/shelters/$', views.man_shelters, name='man_shelters'),
    url(r'^management/shelter/(?P<shelter_id>[^\s/]+)/$', views.man_shelter, name='man_shelter'),
    url(r'^management/staffs/$', views.man_staffs, name='man_staffs'),
    url(r'^management/staff/(?P<staff_id>[^\s/]+)/$', views.man_staff, name='man_staff'),
    url(r'^management/requests/$', views.man_requests, name='man_requests'),
    url(r'^management/requests/adoptions/$', views.man_req_adoptions, name='man_req_adoptions'),
    url(r'^management/requests/adoption/(?P<adoption_id>[^\s/]+)/$',
          views.man_req_adoption, name='man_req_adoption'),
    url(r'^management/requests/surrenders/$', views.man_req_surrenders, name='man_req_surrenders'),
    url(r'^management/requests/surrender/(?P<surrender_id>[^\s/]+)/$',
          views.man_req_surrender, name='man_req_surrender'),
    url(r'^management/requests/donations/$', views.man_req_donations, name='man_req_donations'),
    url(r'^management/requests/donation/(?P<donation_id>[^\s/]+)/$',
          views.man_req_donation, name='man_req_donation'),
    url(r'^management/requests/volunteers/$', views.man_req_volunteers, name='man_req_volunteers'),
    url(r'^management/requests/volunteer/(?P<volunteer_id>[^\s/]+)/$',
          views.man_req_volunteer, name='man_req_volunteer'),
    url(r'^logout/$', views.logout, name='logout'),
)

