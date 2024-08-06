from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import login_table, user_table,notification_table,complaint_table,Feedback


def login(request):
    # return render(request,"login.html")
    return render(request,"login_index.html")


def login_code(request):
    un=request.POST['textfield']
    ps=request.POST['textfield2']
    try:
        ob=login_table.objects.get(username=un,password=ps)
        if ob.type=="admin":
            return HttpResponse('''<script>alert('welcome admin');window.location='/admin_home'</script>''')
        elif ob.type=="user":
            request.session['lid']=ob.id
            return HttpResponse('''<script>alert('Welcome User');window.location='/user_home'</script>''')
        else:
            return HttpResponse('''<script>alert('invalid');window.location='/login'</script>''')
    except:
        return HttpResponse('''<script>alert('invalid');window.location='/login'</script>''')



def registration(request):
    return render(request,"registration index.html")


def register_code(request):
    name=request.POST['textfield']
    place=request.POST['textfield2']
    post=request.POST['textfield3']
    pin=request.POST['textfield4']
    phone=request.POST['textfield5']
    gender=request.POST['radiobutton']
    email=request.POST['textfield6']
    username=request.POST['textfield7']
    password=request.POST['textfield8']



    ob=login_table()
    ob.username=username
    ob.password=password
    ob.type='user'
    ob.save()

    ob1=user_table()
    ob1.Name=name
    ob1.Place=place
    ob1.Post=post
    ob1.Pin=pin
    ob1.Phone=phone
    ob1.Gender=gender
    ob1.Email=email
    ob1.LOGIN=ob
    ob1.save()
    return HttpResponse('''<script>("registration complete");window.location="/"</script>''')




# ___________________________ADMIN____________________________________________
def admin_home(request):
    return  render(request,"ADMIN/admin index.html")

def view_user(request):
    data=user_table.objects.all()
    return  render(request,"ADMIN/admin vu.html",{"d1":data})


def view_complaint(request):
    data=complaint_table.objects.all()
    return  render(request,"ADMIN/admin vc.html",{"d1":data})


def view_reply(request):
    return  render(request,"ADMIN/admin r.html")



def edit_notification(request,id):
    request.session['Noti_id']=id
    ob=notification_table.objects.get(id=id)

    return  render(request,"ADMIN/edit_n.html",{'val':ob})


def edit_notification_post(request):
    noti=request.POST['text']
    ob=notification_table.objects.get(id=request.session['Noti_id'])
    ob.Notification=noti
    ob.Date=datetime.today()
    ob.save()
    return HttpResponse('''<script> alert("notification Edited");window.location="/view_manage_notification"</script>''')


def reply_notification(request,id):
    request.session['cid']=id
    return render(request,"ADMIN/reply.html")
    # ob=notification_table.objects.get(id=id)
    # ob.reply_notification()

def reply_send(request):
    rply=request.POST['text']
    ob=complaint_table.objects.get(id=request.session['cid'])
    ob.Reply=rply
    ob.save()
    return HttpResponse('''<script> alert("reply send");window.location="/view_complaint"</script>''')




def view_notification(request):
    return render(request,"ADMIN/admin n.html")


def delete_noti(request,id):
    ob=notification_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script> alert("notification deleted");window.location="/view_manage_notification"</script>''')




def notification_post(request):
    notification = request.POST['text']
    ob =  notification_table()
    ob.Notification = notification
    ob.Date = datetime.now().today()
    ob.save()
    return HttpResponse('''<script> alert("notification send");window.location="/view_manage_notification#constructions"</script>''')


def view_manage_notification(request):
    data = notification_table.objects.all()
    return  render(request,"ADMIN/admin mn.html",{"d1":data})


def view_feedback(request):
    data=Feedback.objects.all()
    return  render(request,"ADMIN/admin fb.html",{"d1":data})

#_________________________________user_________________________________________________


def user_home(request):
    return  render(request,"USER/user index.html")



def view_send_rating(request):
    return  render(request,"USER/user sr.html")


def view_send_complaint(request):
    data=complaint_table.objects.all()
    return  render(request,"USER/user sc.html",{'d1':data})


def view_send_new_notification(request):
    data=notification_table.objects.all()
    return  render(request,"USER/user new n.html",{'d1':data})



def view_send_add_complaint(request):
    return render(request,"USER/user ac.html")



def reply_rating_feedback(request):
    rating=request.POST['select']
    feedback=request.POST['textfield']
    ob=Feedback()
    ob.Feedback=feedback
    ob.Rating=rating
    ob.Date=datetime.today()
    ob.USER =user_table.objects.get(LOGIN__id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script> alert("reply send");window.location="/view_complaint"</script>''')


def  user_profile(request,):
    data = user_table.objects.get(LOGIN__id=request.session['lid'])
    return render(request, "user/profile user.html", {"val": data})











































