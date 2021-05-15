from django.views import generic
from django.shortcuts import render


def index(request):
    # num_books = Book.objects.all().count()
    # num_instances = BookInstance.objects.all().count()
    # num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    # num_authors = Author.objects.all().count()
    # num_genres = Genre.objects.all().count()
    # num_books_with_word = Book.objects.filter(title__contains='ebola').count()

    # num_visits = request.session.get('num_visits', 0)
    # request.session['num_visits'] = num_visits + 1

    return render(
        request,
        'index.html',
        context={
            # 'num_books': num_books,
            # 'num_instances': num_instances,
            # 'num_instances_available': num_instances_available,
            # 'num_authors': num_authors,
            # 'num_genres': num_genres,
            # 'num_books_with_word': num_books_with_word,
            # 'num_visits': num_visits
        },
    )
