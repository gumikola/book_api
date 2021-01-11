from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.urls import reverse

from book_api.models import Book, Opinion


def map_api(request):
    response_dict = {
        "describe:": "Welcome in Book Api.",
        "links": {
            "self": reverse(map_api),
            "books": reverse(books),
            "search_book": reverse(search_books),
            "opinions": reverse(opinions)
        }
    }

    return JsonResponse(response_dict)


def prepare_book_dict(book_obj):
    book_obj_dict = model_to_dict(book_obj)
    book_obj_dict.pop("id")
    book_obj_dict["author"] = book_obj.author.author
    response_dict = {
        "id": book_obj.id,
        "book_data": book_obj_dict,
        "links": {
            "self": f"{reverse(books)}{book_obj.id}/",
            "opinions": f"{reverse(books)}{book_obj.id}/opinions/"
        }
    }
    return response_dict


def prepare_opinion_dict(opinion_obj):
    opinion_obj_dict = model_to_dict(opinion_obj)
    opinion_obj_dict.pop("id")
    opinion_obj_dict.pop("isbn")

    book_obj = opinion_obj.isbn
    opinion_obj_dict["book"] = f"{book_obj.author.author} - {book_obj.title}"

    response_dict = {
        "id": opinion_obj.id,
        "opinion_data": opinion_obj_dict,
        "links": {
            "self": f"/api/opinions/{opinion_obj.id}/",
        }
    }
    return response_dict


def accept_only_GET(func):
    def inner(*args, **kwargs):
        if args[0].method != "GET":
            return HttpResponse(status=501)
        return func(*args, **kwargs)

    return inner


@accept_only_GET
def books(request):
    all_books = [prepare_book_dict(x) for x in Book.objects.all()]

    return JsonResponse(all_books, safe=False)


@accept_only_GET
def search_books(request):

    if request.GET:
        if request.GET["title"]:
            match_books = [prepare_book_dict(x)
                           for x in Book.objects.filter(title=request.GET["title"])]

        if match_books:
            return JsonResponse(match_books, safe=False)

    return HttpResponse(status=404)


@accept_only_GET
def book(request, book_id):
    book_obj = get_object_or_404(Book, pk=book_id)
    return JsonResponse(prepare_book_dict(book_obj))


@accept_only_GET
def opinions(request, book_id=None):
    if book_id:
        opinion_queryset = get_object_or_404(Book, pk=book_id).opinion_set.all()
    else:
        opinion_queryset = Opinion.objects.all()

    all_opinions = [prepare_opinion_dict(x) for x in opinion_queryset]

    return JsonResponse(all_opinions, safe=False)


@accept_only_GET
def opinion(request, opinion_id):
    opinion_obj = get_object_or_404(Opinion, pk=opinion_id)

    return JsonResponse(prepare_opinion_dict(opinion_obj))
