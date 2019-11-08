from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author


def index(request):
    context = {
        "all_books": Book.objects.all()
    }
    return render(request, "index.html", context)

def addbook(request):
    title = request.POST["title"]
    desc = request.POST["desc"]
    # Add the book to the db by calling the object
    Book.objects.create(title=title, desc=desc)
    # redirect to book homepage
    return redirect('/')

def book(request, book_id):
    # book id is passed via url params
    context = {"book": Book.objects.get(id=book_id)}
    # assigning the book authors
    context["book_authors"]=Book.objects.get(id=book_id).authors.all()
    context["all_authors"] = Author.objects.exclude(id__in=Book.objects.get(id=book_id).authors.all())
    return render(request, "book.html", context)

def authors(request):
    context = {
        "all_authors": Author.objects.all()
    }
    return render(request,"authors.html",context)

def addauthor(request):
    first = request.POST["first"]
    last = request.POST["last"]
    notes = request.POST["notes"]
    # Add the book to the db by calling the object
    Author.objects.create(first_name=first, last_name=last,notes=notes)
    # redirect to book homepage
    return redirect('/authors')

def linkauthor(request,book_id,author_id):
    author = Author.objects.get(id=author_id)
    book = Book.objects.get(id=book_id)
    author.books.add(book)
    return redirect(f'/authors/{author_id}')

def authordeets(request,author_id):
     # author id is passed via url params
    context = {"author": Author.objects.get(id=author_id)}
    # assigning the books
    context["author_books"]=Author.objects.get(id=author_id).books.all()
    context["all_books"] = Book.objects.exclude(id__in=Author.objects.get(id=author_id).books.all())
    return render(request, "author_details.html", context)

def linkbook(request,book_id,author_id):
    author = Author.objects.get(id=author_id)
    book = Book.objects.get(id=book_id)
    author.books.add(book)
    return redirect(f'/books/{book_id}')