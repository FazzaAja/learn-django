from django.shortcuts import render
from perpustakaan.models import Buku
from perpustakaan.forms import FormBuku
# from django.http import HttpResponse

# Create your views here.


def buku(request):
    books = Buku.objects.all()

    konteks = {
        'books': books,
    }

    # return HttpResponse('Halaman Buku')
    return render(request, 'buku.html', konteks)


def penerbit(request):
    return render(request, 'penerbit.html')


def tambah_buku(request):
    form = FormBuku()

    konteks = {
        'form': form
    }

    return render(request, 'tambah-buku.html', konteks)
