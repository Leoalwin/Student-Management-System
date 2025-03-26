from django.shortcuts import get_object_or_404, render
from django.http import *
from.models import student

# Create your views here.

def home(request):
    return render(request,"homepage.html")

def spage(request):
    return render (request,"sregpage.html")

def sdisplay(request):
    student_id=request.POST.get("student_id")
    crollno=request.POST.get("rollno")
    cname=request.POST.get("name")
    cdepartment=request.POST.get("department")
    cphone=request.POST.get("phone")
    ccity=request.POST.get("city")
    print(cname," ",crollno," ",cdepartment," ",cphone," ",ccity)
    #ORM
    student.objects.create(student_id=student_id,rollno=crollno,name=cname,department=cdepartment,phone=cphone,city=ccity,)
    context={"crollno":crollno,"cname":cname,"cdepartment":cdepartment,"cphone":cphone,"ccity":ccity}
    return render(request,"sprocess.html",context)

def allstudentdata(request):
    stud=student.objects.all()
    #srstud=student.objects.filter(rollno__contains="crollno",name__contains="cname",department__contains="cdepartment",phone__contains="cphone",city__contains="ccity").values()
    return render(request,"displaystud.html",{"stud":stud})

def search_student(request):
    if request.method=="GET":
        return render(request,"search.html")
    elif request.method=="POST":
         cname=request.POST.get("name")
         ccity=request.POST.get("city")
         cdepartment=request.POST.get("department")

         print(cname,ccity,cdepartment)
         sresult=student.objects.filter(name__contains=cname,city__contains=ccity,department__contains=cdepartment)
         print(sresult)
         return render(request,"search.html",{"sresult":sresult})

def display_onestudent(request):
   student_id=request.GET.get("student_id")
   print("student id",student_id)

   #Fetches the book from the table else display 404
   Student=get_object_or_404(student,student_id=student_id)
   print(Student)
   return render(request,"displayonestud.html",{"Student":Student})


def update_view(request):
   student_id=request.GET.get("student_id")
   print("student id",student_id)

   #Fetches the book from the table else display 404
   Student=get_object_or_404(student,student_id=student_id)    
   print(Student)
   return render(request,"update1stud.html",{"Student":Student})

def update_studprocess(request):
    student_id=request.POST.get("bid")
    rollno=request.POST["rollno"]
    name=request.POST["name"]
    department=request.POST["department"]
    phone=request.POST["phone"]
    city=request.POST["city"]
    print("student_id:",student_id," ",name," ",rollno," ",department," ",phone," ",city)
    #update
    upd=student.objects.filter(student_id=student_id)[0]
    print("oldstudent_id:",student_id," ",upd.name," ",upd.rollno," ",upd.department," ",upd.phone," ",upd.city)
    upd.rollno=rollno
    upd.name=name
    upd.department=department
    upd.phone=phone
    upd.city=city
    upd.save()
    print("Newstudent_id:",student_id," ",upd.name," ",upd.rollno," ",upd.department," ",upd.phone," ",upd.city)
    return render(request,"updateprocess.html",{"Student":upd})

def delete_onestudent(request):
    student_id=request.GET.get("student_id")
    print("student id",student_id)

   #Fetches the book from the table else display 404
    Student=get_object_or_404(student,student_id=student_id)
    print(Student)
    return render(request,"delete.html",{"Student":Student})


def delete_process(request):
    student_id=request.POST.get("student_id")
    Student = student.objects.get(student_id)
    Student.delete()
    #delete_stud=student.objects.all()
    #print(delete_stud)



    return render(request,"deletesuccess.html",{"Student":Student})

def delete_sucesss(request):
    delete_stud=student.objects.all()
    #print(delete_stud)
    return render(request,"displaystud.html",{"delete_stud":delete_stud})
    



    