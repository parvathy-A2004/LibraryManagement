from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.db.models import Q
from .forms import BookForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')

def book_list(request):

    query = request.GET.get('q', '')

    if query:

        books = Book.objects.filter(

            Q(title__icontains=query) |

            Q(author__icontains=query) |

            Q(category__icontains=query)

        )

    else:

        books = Book.objects.all()

    return render(
        request,
        'book_list.html',
        {
            'books': books,
            'query': query
        }
    )

@login_required
def add_book(request):

    if request.method == 'POST':

        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('book_list')

    else:

        form = BookForm()

    return render(request, 'add_book.html', {'form': form})

@login_required
def edit_book(request, id):

    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect('book_list')

    else:
        form = BookForm(instance=book)

    return render(request, 'add_book.html', {'form': form})

@login_required
def delete_book(request, id):

    book = get_object_or_404(Book, id=id)

    book.delete()

    return redirect('book_list')