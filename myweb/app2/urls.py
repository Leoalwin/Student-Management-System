from django.urls import path
from.import views
urlpatterns=[
    path("home",views.home,name="home"),
    path("sregpage",views.spage,name="sregpage"),
    path("sprocess",views.sdisplay,name="sprocess"),
    path("allstudent",views.allstudentdata,name="allstudent"),
    path("search",views.search_student,name="search"),
    path("one_student",views.display_onestudent,name="one_student"),
    path("updstudent",views.update_view,name="updstudent"),
    path("updstudentprocess",views.update_studprocess,name="updstudentprocess"),
    path("delete_one",views.delete_onestudent,name="delete_one"),
    path("deletestudent",views.delete_process,name="deletestudent"),
    path("deletesuccess",views.delete_sucesss,name="deletesuccess")



]   