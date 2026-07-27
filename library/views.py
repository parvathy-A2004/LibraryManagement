from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Student, IssueBook
from django.db.models import Q
from .forms import BookForm, StudentForm, IssueBookForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone

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


@login_required
def student_list(request):

    query = request.GET.get('q', '')

    if query:
        students = Student.objects.filter(
            Q(name__icontains=query) |
            Q(roll_no__icontains=query) |
            Q(department__icontains=query)
        )
    else:
        students = Student.objects.all()

    return render(
        request,
        'student_list.html',
        {
            'students': students,
            'query': query
        }
    )


@login_required
def add_student(request):

    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:

        form = StudentForm()

    return render(request, 'add_student.html', {'form': form})


@login_required
def edit_student(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':

        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:

        form = StudentForm(instance=student)

    return render(request, 'add_student.html', {'form': form})


@login_required
def delete_student(request, id):

    student = get_object_or_404(Student, id=id)

    student.delete()

    return redirect('student_list')


@login_required
def issue_list(request):

    issues = IssueBook.objects.all()

    return render(
        request,
        'issue_list.html',
        {
            'issues': issues
        }
    )


@login_required
def issue_book(request):

    if request.method == 'POST':

        form = IssueBookForm(request.POST)

        if form.is_valid():

            issue = form.save()

            # Reduce available quantity
            issue.book.quantity -= 1
            issue.book.save()

            return redirect('issue_list')

    else:

        form = IssueBookForm()

    return render(
        request,
        'issue_book.html',
        {
            'form': form
        }
    )

@login_required
def return_book(request, id):

    issue = get_object_or_404(IssueBook, id=id)

    if issue.status == "Issued":

        issue.status = "Returned"
        issue.return_date = timezone.now().date()
        issue.save()

        issue.book.quantity += 1
        issue.book.save()

    return redirect('issue_list')