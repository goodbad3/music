from django.urls import path
from django.views.generic import TemplateView 
from .views import AboutView, CourseListView,ManageCourseListView,CreateCourseView,DeleteCourseView,UpdateCourseView,\
CreateLessonView,ListLessonsView,DetailLessonView

app_name = "course" 
urlpatterns = [ 
    path('about/', AboutView.as_view(), name="about"),	
    path('course-list/', CourseListView.as_view(), name="course_list"), 
    path('manage-course/', ManageCourseListView.as_view(), name="manage_course"),
    path('create-course/', CreateCourseView.as_view(), name="create_course"),
    path('delete-course/<int:pk>/', DeleteCourseView.as_view(),name="delete_course"),
    path('update-course/<int:pk>/', UpdateCourseView.as_view(),name="update_course"),
    path('create-lesson/', CreateLessonView.as_view(), name="create_lesson"),
    path('list-lessons/<int:course_id>/', ListLessonsView.as_view(), name="list_lessons"),
    path('detail-lesson/<int:lesson_id>/', DetailLessonView.as_view(), name="detail_lesson"),

    ]


