"""sjtulost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^initdb/$', 'lost.db.initdb.init_database_found', name='init_database_found'),

    url(r'^$', 'lost.app.views.home', name='home'),
    url(r'^finding/$', 'lost.app.views.finding', name='finding'),
    url(r'^found/$', 'lost.app.views.found', name='found'),
    url(r'^rank/$', 'lost.app.views.rank', name='rank'),
    url(r'^me/$', 'lost.app.views.me', name='me'),
    url(r'^publishfinding/$', 'lost.app.views.publish_finding', name='publish_finding'),
    url(r'^publishfound/$', 'lost.app.views.publish_found', name='publish_found'),
    url(r'^publishfinding/(\d+)/$', 'lost.app.views.publish_finding_with_id', name='publish_finding_with_id'),
    url(r'^publishfound/(\d+)/$', 'lost.app.views.publish_found_with_id', name='publish_found_with_id'),
    url(r'^searchfinding/(.+)/$', 'lost.app.views.search_finding', name='search_finding'),
    url(r'^searchfound/(.+)/$', 'lost.app.views.search_found', name='search_found'),
    url(r'^searchfinding/$', 'lost.app.views.search_finding_without_keyword', name='search_finding_without_keyword'),
    url(r'^searchfound/$', 'lost.app.views.search_found_without_keyword', name='search_found_without_keyword'),

    url(r'^loginwithjaccount/$', 'lost.app.user.login_with_jaccount', name='login_with_jaccount'),
    url(r'^getaccesstoken/$', 'lost.app.user.get_access_token', name='get_access_token'),
    url(r'^getuserinfo/$', 'lost.app.user.get_user_info', name='get_access_token'),
    url(r'^updateuserinfo/$', 'lost.app.user.update_user_info', name='update_user_info'),
    url(r'^getuserfindings/$', 'lost.app.user.get_user_findings', name='get_user_findings'),
    url(r'^userfindingsdone/$', 'lost.app.user.user_findings_done', name='user_findings_done'),
    url(r'^getuserfounds/$', 'lost.app.user.get_user_founds', name='get_user_founds'),
    url(r'^userfoundsdone/$', 'lost.app.user.user_founds_done', name='user_founds_done'),
    url(r'^logout/$', 'lost.app.user.logout', name='logout'),

    url(r'^findingview/(\d+)/$', 'lost.app.views.findingview', name='findingview'),
    url(r'^foundview/(\d+)/$', 'lost.app.views.foundview', name='foundview'),

    url(r'^getfindings/$', 'lost.app.finding.get_all_findings', name='get_all_findings'),
    url(r'^getfounds/$', 'lost.app.found.get_all_founds', name='get_all_founds'),
    url(r'^getitems/$', 'lost.app.item.get_all_item_types', name = 'get_all_item_types'),
    url(r'^getplaces/$', 'lost.app.place.get_all_places', name='get_all_places'),
    url(r'^getrank/$', 'lost.app.rank.get_all_ranks', name='get_all_ranks'),

    url(r'^getfindingswithfilter/$', 'lost.app.finding.get_findings_with_filter', name='get_findings_with_filter'),
    url(r'^getfoundswithfilter/$', 'lost.app.found.get_founds_with_filter', name='get_founds_with_filter'),

    url(r'^getfindingswithid/$', 'lost.app.finding.get_findings_with_id', name='get_findings_with_id'),
    url(r'^getfoundswithid/$', 'lost.app.found.get_founds_with_id', name='get_founds_with_id'),

    url(r'^getfindingswithkeyword/$', 'lost.app.finding.get_findings_with_keyword', name='get_findings_with_keyword'),
    url(r'^getfoundswithkeyword/$', 'lost.app.found.get_founds_with_keyword', name='get_founds_with_keyword'),

    url(r'^publishfindinguploadimage/$', 'lost.app.finding.publish_finding_upload_image', name='publish_finding_upload_image'),
    url(r'^createfinding/$', 'lost.app.finding.create_finding',name='create_finding'),
    url(r'^updatefinding/$', 'lost.app.finding.update_finding', name='update_finding'),

    url(r'^publishfounduploadimage/$', 'lost.app.found.publish_found_upload_image', name='publish_found_upload_image'),
    url(r'^createfound/$', 'lost.app.found.create_found', name='create_found'),
    url(r'^updatefound/$', 'lost.app.found.update_found', name='update_found'),

    url(r'^admin/', include(admin.site.urls)),
]
