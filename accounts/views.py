import email
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse
from django.views.generic import ListView
from .models import admins, info_site
from django.contrib.auth import get_user_model
try:
    info = info_site.objects.get(id=1)
    title = info.title
except:
    title = "Null"
def about(request):
    return render(request, 'account/about.html')
def signup(request):
    if request.method == 'POST':
        #user has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']: #  در صورتی که دوتا پسورد باهم همخوانی داشته باشه
            try: # سعی میکنه نام کاربری رو از بین کاربران موجود پیدا کنه
 
                # در خط زیر سعی میکنه کاربر با نام کاربری ورودی رو از دیتابیس پیدا کنه
                # اگر همچین کاربری پیدا نشه، ارور زیر پرت میشه
                # User.DoesNotExist
                # که این ارور رو چند خط پایین تر در اکسپت گرفتیم
                # و این ارور به معنی اینه که کاربر جدیده و باید ساخته بشه
                User.objects.get(username=request.POST['username']) # means this username already Exist!

                # در صورتی که در خط قبل کاربر موجود بود، کد به این خط میرسه و این یک پیام رو به صفحه مبدا بر می گردونه
                #  و میگه که نام کاربری قبلا انتخاب شده
                return render(request, 'account/signup.html', {'error':'Username has already been taken!'})
            except:
                try:
                    User.objects.get(email=request.POST['email'])  
                    return render(request, 'account/signup.html', {'error':'Email has already been taken!'})
                except:
                    # اگر نام کاربری از قبل موجود نبود، کاربر جدید رو میسازه
                    # ترتیب یوزرنیم و ایمیل و پسورد در متدزیر مهمه. مثلا اگر کلا ایمیل رو ننویسیم، و پسورد رو بعنوان دومی بنویسیم، پسورد میره بعنوان آدرس ایمیل کاربر ذخیره میشه
                    user = User.objects.create_user(request.POST['username'], request.POST['email'] , request.POST['password1'])
                    # در خط زیر با کاربری که در خط بالا ایجاد کرده در سایت لاگین می کنه
                    auth.login(request,user)
                    # و کاربر لاگین کرده رو زارت میفرسته به صفحه اصلی. البته میشد اینجا با یک پیام به کاربر اعلام کنیم که ثبت نام با موفقیت انجام شد.
                    return HttpResponse('با موفقیت ثبت نام کردید')
 
        else: # در صورتی که دوتا پسورد باهم همخوانی نداشته باشه
            return render(request,'account/signup.html', {'error':'paswords did not match!', 'title':title})
    else:
        # در این حالت متد پست فراخوانی نشده. یعنی کاربر فرم را سابمیت نکرده. بلکه فقط آدرس صفحه را زده که صفحه را ببیند.
        # بنابراین صفحه حاوی فرم به کاربر نمایش داده میشود و پردازشی انجام نمی شود.
        return render(request, 'account/signup.html', {'title':title, "error":"Singup"})
def login(request):
    # اگر رکوئست با متد POST ارسال شده بود یعنی کاربر فرم لاگین را سابمیت کرده است
    if request.method == 'POST':
        # از متد user.authemticate برای یافتن کاربر استفاده میشود. این متد یه متغیر از نوع آبجکت user بر می گرداند
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        # چک می کند که اگر متغیر یوزر خالی نبود، لاگین را با اطلاعات یوزر انجام دهد
        usernamee=request.POST['username']
        if user is not None:
            auth.login(request, user)
            # در اینجا کاربر را به صفحه ای که میخواهیم پس از لاگی
            # ن به وی نمایش دهیم ریدایرکت می کنیم           
            user_name=User.objects.get(username=usernamee)
            return render(request, 'account/sucssesfully.html', {'title':title})
        # در صورتی که متغیر یوزر خالی بود
        # یعنی کاربر با مشخصاتی که در فرم وارد شده است وجود ندارد
        else:
            # کاربر را به همراه یک پیام خطا به صفحه لاگین باز می گرداند
            # این پیغام خطا در قسمت تعبیه شده در بالای صفحه لاگین به نمایش در می آید
            # return render(request, 'account/login.html', {'error':'Invalid Username Or Password'})
            return HttpResponse("not correct")

                    # اگر رکوئست با متد GET ارسال شده بود یعنی کاربر لینک صفحه لاگین را زده و میخواهد صفحه لاگین را ببیند
    else:
        return render(request, 'account/login.html', {'title':title})
        # return render()
def admin_profile(request):
    try:
        us = request.user.username
        la = request.user.last_name
        fi = request.user.first_name
        em = request.user.email
        admins.objects.get(name_admin=us)
        return render(request, "account/admin_profile.html", {'title':title, 'la':la, 'fi':fi, 'em':em})
    except:
        return HttpResponse("Not found")

def notfound(request, exception):
    return render(request,'404.html')

def info_sitte(request):
    try:
        us = request.user.username
        admins.objects.get(name_admin=us)
        try:
            info = info_site.objects.get(id=1)
            title = info.title
            return render(request, "account/info.html", {'title':title})
        except:
            return render(request, "account/info.html", {'title':''})
    except:
        return HttpResponse("Not found")

# class profile(DetailView):
#     model = profile
#     template_name = 'edit_profile.html'
def save_info_site(request):
    if request.method == 'POST':
        title = request.POST['titlle']
        try:
            info = info_site.objects.get(pk=1)
            info.title = title
            info.save()
            return HttpResponse(f'{title} Was save sucssesfully')
        except:
            info = info_site()
            info.title = title
            info.id = 1
            info.save()
            return HttpResponse(f'{title} Was save sucssesfully')


    else:
        return HttpResponse("Not Found")

    
def profile(request):
    try:
        try:
            us = request.user.username
            la = request.user.last_name
            fi = request.user.first_name
            em = request.user.email
            admins.objects.get(name_admin=us)
            return render(request, "account/admin.html", {'title':title})
        except:
            return render(request, "account/admin_profile.html", {'title':title, 'la':la, 'fi':fi, 'em':em, 'us':us})
    except:
        return HttpResponse("Please log in first")
def save_profile(request):
    if request.method == 'POST':
        em = request.user.email
        email = request.POST['email']
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']
        user_one = User.objects.get(email=em)
        if em == email:
            user_one.last_name = last_name            
            user_one.first_name = first_name
            user_one.email = email
            user_one.save()
        else:
            try:
                User.objects.get(email=email)
                return HttpResponse("Email has already been taken!")               
            except:
                user_one.last_name = last_name            
                user_one.first_name = first_name
                user_one.email = email
                user_one.save()
        
        # user_one.last_name = last_name            
        # user_one.first_name = first_name
        # user_one.email = email
        # user_one.save()
        return HttpResponse("your profile save sucsessfull")
    else:
        return HttpResponse("Not Found")
    
def admin_name(request):
    # try:
    users = User.objects.values()
    username = []
    rng = 100
    for i in range(rng):
        try:
            usr = users[i]['username']
            username.append(usr)
        except:
            break
    us = request.user.username
    admins.objects.get(name_admin=us)
        
    return render(request, "account/admin_name.html", {'title':title, "us":username})
    # except:
    #     return HttpResponse("Not Found")
def save_admin(request):
    if request.method == 'POST':
        name = request.POST['admin_name']
        try:
            User.objects.get(username=name)
            try:
                admins.objects.get(name_admin=name)
                return HttpResponse(f'{name}قبلاً ثبت شده است.')
            except:
                admin = admins()
                admin.name_admin = name
                admin.save()
                return HttpResponse("save sucssesfully")
        except:
            return HttpResponse('Username Not found in users')
        
    else:
        return HttpResponse("Not found")
 
class edit_admin(ListView):
    model = admins
    template_name = 'account/edit_admin.html'

def detail_admin(request, pk):
    blog = admins.objects.get(id=pk)
    titlle = blog.name_admin
    return render(request, 'account/detail_admin.html', {'title':titlle,'id':pk})
def save_admins(request, pk):
    try:
        us = request.user.username
        admins.objects.get(name_admin=us)
        if request.method == 'POST':
            try:
                title = request.POST['title']
                User.objects.get(username=title)
                admin = admins.objects.get(id=pk)
                admin.name_admin = title
                admin.save()
                return HttpResponse("save successefully")
            except:
                return HttpResponse('username is not valid')
        else:
            return HttpResponse('Not Found')
    except:
        return HttpResponse('Not Found page')
def delete_admin(request, pk):
    if request.method == 'POST':
        admin = admins.objects.get(id=pk)
        admin.delete()
        return HttpResponse("delete successefully")
    else:
        return HttpResponse('Not Found')
