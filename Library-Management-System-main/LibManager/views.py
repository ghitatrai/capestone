from django.shortcuts import render,redirect
from .models import Book
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')  # Redirect to login after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page after successful login
        else:
            # Handle invalid login (e.g., show error message)
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    return render(request, 'login.html')

def viewBookList(request):
    book_list = Book.objects.all()
    context = {'book_list': book_list}
    return render(request, 'bookList.html', context)

def addBook(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        genre = request.POST.get('genre')
        copies = request.POST.get('copies')
        book = Book(title=title, author=author, genre=genre, copies=copies)
        book.save()
        return redirect('bookView', book_id=book.id)
    
    return render(request, 'addBook.html')

def bookView(request, book_id):
    book = Book.objects.get(pk=book_id)
    context = {'book': book}
    return render(request, 'viewBook.html', context)

def deleteBook(request):
    if request.method == 'POST':
        query = request.POST['query']
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
        if len(books) == 1:
                books.delete()
                return redirect('viewBookList')
        elif len(books) > 1:
            for book in books:
                book.delete()
            return redirect('viewBookList')
        else:
            context = {
            'title': 'Book not found',
            'message': 'Please enter a valid book title or author name.'
            }
            return render(request, 'ErrorHandler.html', context)
    else:
        return render(request, 'deleteBook.html')



def searchBook(request):
    if request.method == 'POST':
        query = request.POST['query']
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))

        if len(books) == 1:
            # Redirect to the first book found (assuming you want to display the first result)
            return redirect('bookView', book_id=books[0].id)
        elif len(books) > 1:
            # Display a list of books
            context = {'books': books}
            return render(request, 'bookList.html', context)
        else:
            context = {
            'title': 'Book not found',
            'message': 'Please enter a valid book title or author name.'
            }
            return render(request, 'ErrorHandler.html', context)
    else:
        return render(request, 'search.html')

  