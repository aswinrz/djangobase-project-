from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [

    path ('',views.login,name="login"),
    path ('login_code',views.login_code,name="login_code"),
    path ('registration',views.registration,name="registration"),
    path ('admin_home',views.admin_home,name="admin_home"),
    path('view_user',views.view_user,name="view_user"),
    path('view_complaint',views.view_complaint,name="view_complaint"),
    path('view_reply',views.view_reply,name="view_reply"),
    path('view_notification',views.view_notification,name="view_notification"),
    path('notification_post',views.notification_post,name="notification_post"),
    path('delete_noti/<int:id>',views.delete_noti,name="delete_noti"),
    path('view_manage_notification',views.view_manage_notification,name="view_manage_notification"),
    path('view_feedback',views.view_feedback,name="view_feedback"),
    path('edit_notification/<int:id>',views.edit_notification,name="edit_notification"),
    path('edit_notification_post',views.edit_notification_post,name="edit_notification_post"),
    path('reply_notification/<int:id>',views.reply_notification,name="reply_notification"),
    path('reply_send',views.reply_send,name="reply_send"),

    #____________________________________________usre____________________________

    path('user_home',views.user_home,name="user_home"),
    path('view_send_new_notification',views.view_send_new_notification,name="view_send_new_notification"),
    path('view_send_rating',views.view_send_rating,name="view_send_rating"),
    path('view_send_complaint',views.view_send_complaint,name="view_send_complaint"),
    path('view_send_new_notification',views.view_send_new_notification,name="view_send_new_notification"),
    path('view_send_add_complaint', views.view_send_add_complaint, name="view_send_add_complaint"),
    path('register_code', views.register_code, name="register_code"),
    path('reply_rating_feedback', views.reply_rating_feedback, name="reply_rating_feedback"),
    path('user_profile',views.user_profile, name="user_profile"),






    ]
