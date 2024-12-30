from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpResponse
from .models import Book


def library_home(request):
    books = Book.objects.all()
    return render(request, 'library_home.html', {'books': books})


def add_book(request):
    if request.method == 'POST':    
        title = request.POST.get('title')
        author = request.POST.get('author')
        available_copies = request.POST.get('available_copies')

        new_book = Book.objects.create(
            title=title,
            author=author,
            available_copies=available_copies
        )
        new_book.save()  
        return redirect('library_home') 
    return render(request, 'library_home.html')





def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id) 
    
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.available_copies = request.POST.get('available_copies')
        book.save() 

        return redirect('library_home') 
    return render(request, 'update_book.html', {'book': book})


def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id) 
    book.delete() 
    return redirect('library_home') 