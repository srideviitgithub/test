from django.shortcuts import render,redirect
from django.http import HttpResponse
from. models import employee,Department
from django.db.models import Sum,Avg,Max,Min


# Create your views here.


def createfun(req):
    return HttpResponse('table created')


def insertfun(req):
    if req.method=='POST':
        sno=int(req.POST['t1'])
        sname=req.POST['t2']
        sal=int(req.POST['t3'])
        sdno=int(req.POST['t4'])

        dept=Department.objects.filter(deptno=sdno)
        if len(dept)>0:
            emps=employee(empno=sno,empname=sname,salary=sal,department=dept[0])
            emps.save()
            return HttpResponse('data inserted')
        else:
            return HttpResponse('department is not existed')
    depts=Department.objects.all()
    return render(req,'sapp/insert.html',{'det':depts})



def selectfun(req):
    emps=employee.objects.all()
    total_salary=employee.objects.aggregate(Sum('salary'))['salary__sum']
    avg_salary=employee.objects.aggregate(avg_sal=Avg('salary'))['avg_sal']
    max_salary=employee.objects.aggregate(max_sal=Max('salary'))['max_sal']
    min_salary=employee.objects.aggregate(min_sal=Min('salary'))['min_sal']
    #print(emps)
    ##for e in emps:
        #print(e.empno,e.empname,e.salary)
   # return HttpResponse('DATA RETRIVED')
    return render(req,'sapp/select.html',{'start':emps,'total_salary':total_salary,'avg':avg_salary,'max':max_salary,'min':min_salary})


def updatefun(req,eno):
    if req.method=='POST':
        sno=int(req.POST['t1'])
        sname=req.POST['t2']
        sal=int(req.POST['t3'])
        emps=employee(empno=sno,empname=sname,salary=sal)
        emps.save()
        return redirect('selecturl')

    emps=employee.objects.filter(empno=eno)
    return render(req,'sapp/update.html',{'start':emps})


def deletefun(req,eno):
    emps=employee.objects.get(empno=eno)
    emps.delete()
    return redirect('selecturl')

    