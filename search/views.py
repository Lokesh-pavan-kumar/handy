from django.shortcuts import render
from .documents import ProductDocument
from elasticsearch_dsl.query import MultiMatch, Match
from handy.models import Category

# Create your views here.

def search(request):
	q = request.GET.get('q')

	if q:
		products = ProductDocument.search().query('multi_match', query=q, fields=['name', 'category', 'description'])
	else:
		products = ''

	procat= {
		'products':products,
		'categories':Category.objects.all()
	}

	return render(request, 'search/search.html', procat)

def filter(request, category):
	products = ProductDocument.search().query('match', category=category)

	procat= {
		'products':products,
		'categories':Category.objects.all()
	}

	return render(request, 'search/search.html', procat)

