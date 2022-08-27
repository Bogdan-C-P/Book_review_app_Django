from django.shortcuts import render,redirect,get_object_or_404
from .models import Book,Review
from .forms import ReviewForm,CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import PermissionDenied
from .decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .filters import MyModelFilter

# Create your views here.

@unauthenticated_user
def loginPage(request):
    
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('book_list')
        else:
            messages.info(request,"Username or password are incorrect")
            return redirect('login')
    context={}
    return render(request,'reviews/login.html',context)

@unauthenticated_user
def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			messages.success(request, 'Account was created for ' + username)

			return redirect('login')
		

	context = {'form':form}
	return render(request, 'reviews/register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


def BookList(request):
    books = Book.objects.all()
    
    myFilter= MyModelFilter(request.GET,queryset=books)
    books=myFilter.qs
    paginator = Paginator(books, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'books':page_obj,
        'myFilter':myFilter,
      
        
    }
    
    return render(request, 'reviews/book_list.html',context)

@login_required(login_url='login')
def BookDetail(request,pk):
    book = Book.objects.get(pk=pk)
    reviews=Review.objects.filter(book=book)
    count = len(reviews)
    paginator = Paginator(reviews, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 
    form = ReviewForm()
   
    user_review = Review.objects.filter(book=book, user=request.user) 
    if request.method == "POST":
        if user_review:
            return redirect('book_detail',pk)
            #aise PermissionDenied('You have already given your review on this post.')
        else:
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.book = Book.objects.get(pk=pk)
                review.user = request.user
                review.save()
                messages.success(request, "Review saved")
                return redirect('book_detail',pk)
            else:
                messages.error(request,'error in form')
            return redirect('book_detail',pk)

    context={
        'book':page_obj,
        'form':form,
        'books':book,
        'count':count
        
        
    }
    return render(request,'reviews/book_detail.html',context)

@login_required(login_url='login')
def ReviewUpdate(request,pk):
    review = Review.objects.get(pk=pk)
    form =ReviewForm(instance=review)

    if request.method =='POST' and request.user==review.user:
        #print(request.POST)
        form = ReviewForm(request.POST,instance=review)
        if form.is_valid():
            form.save()
            return redirect('book_list')
   
    context ={
        'form':form,
        'review':review,
    }
    return render(request,'reviews/review_detail.html',context)

@login_required(login_url='login')
def deleteReview(request,pk):
    review = Review.objects.get(pk=pk)
    if request.method == "POST" and request.user==review.user:
        review.delete()
        return redirect('/')
    context ={
        'item':review
    }
    return render(request,'reviews/delete.html',context)
