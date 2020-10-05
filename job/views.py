from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .forms import JobImageForm,ResumeForm
from .models import JobPosts,Resume
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        jobs=JobPosts.objects.all()
        resume=Resume.objects.all()
        count=len(jobs)
        res=len(resume)
        country=[]
        resentjob=[]
        for job in jobs:
            if job.location not in country:
                country.append(job.location)
            if job.job_title not in resentjob:
                resentjob.append(job)
        con=len(country)
        return render(request,'index.html',{'count':count,'res':res,'con':con,'resentjobs':resentjob})
    else:
        return redirect('login/')

def login(request):
    if request.method=='POST':
        gmail=request.POST['email']
        password=request.POST['password']
        user=auth.authenticate(username=gmail,password=password)
        #None user always because username in database should email address only
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        return render(request,'login.html')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        gmail=request.POST['email']
        password=request.POST['password']
        comfirm_password=request.POST['rpassword']
        if gmail!="":
            if password==comfirm_password:
                if User.objects.filter(email=gmail).exists():
                    messages.info(request,'Gmail already exist')
                    return redirect('register')
                else:
                    user=User.objects.create_user(email=gmail,first_name=first_name,last_name=last_name,password=password,username=gmail)
                    user.save()
                    return redirect('login')
            else:
                messages.info(request,'Password incorrect')
                return redirect('register')
        return redirect('register')
    else:
        return render(request,'register.html')

def frpass(request):
    return render(request,'forgot-password.html')


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def post_job(request):
   ''' if request.method=='POST':
        form = JobImageForm(request.FILES)
        print(form)
        if form.is_valid():
            form.save()
        print(form.errors)'''
   if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        job_type=request.POST['job-type']
        salary = request.POST['salary']
        title = request.POST['title']
        company = request.POST['company']
        location = request.POST['location']
        description = request.POST['description']

        post=JobPosts(job_title=title,company=company,location=location,description=description,salary=salary,job_type=job_type,image=filename)
        post.save()
        return redirect('browse_job')
   else:
        form = JobImageForm()
        return render(request, 'post_job.html', {'imageform': form})



def browse_job(request):
    posts=JobPosts.objects.all()
    return render(request,'browse_job.html',{'posts':posts})

def add_resume(request):
    if request.method=='POST':
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        resume=Resume(resume=filename,user_id=request.user.id)
        resume.save()
        return redirect('home')
    else:

        return render(request,'submit_resume.html')

def job_details(request,id=None):
    job=JobPosts.objects.filter(id=id)
    return render(request,'job_detail.html',{'job':job})

def search_job(request):
    search=request.POST['search']
    if search:
        match=JobPosts.objects.filter(Q(job_title__icontains=search) | Q(company__icontains=search) | Q(job_type__icontains=search))
        if match:
            return render(request,'browse_job.html',{'posts':match})
        else:
            messages.error(request,'No Data Found')
            return render(request,'browse_job.html')
    else:
        return redirect('home')
def faq(request):
    return render(request,'faq.html')

def blog(request):
     return render(request,'blog_left_img.html')


def jobindex(request):
    return redirect('home')

def reindex(request):
    return redirect('home')