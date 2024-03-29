"""Define url patterns for learnig_logs"""

from django.urls import path
from . import views
app_name = 'learning_logs'
urlpatterns = [
    # home page
    path('', views.index, name='index'),

    # show all topics
    path('topics/', views.topics, name='topics'),
    # show entries
    path('topics/<int:topic_id>/', views.topic, name= 'topic'),

    # adding new topic by user
    path('new_topic/', views.new_topic, name='new_topic'),

    # adding new enties
    path('new_entries/<int:topic_id>', views.new_entry, name='new_entry'),

    # adding edit entry link
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry')
]