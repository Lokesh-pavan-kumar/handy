from django.shortcuts import render
from .documents import ProductDocument
from elasticsearch_dsl.query import MultiMatch, Match

# Create your views here.

def search(request):
	q = request.GET.get('q')

	if q:
		products = ProductDocument.search().query('multi_match', query=q, fields=['name', 'category', 'description'])
		print(type(products))
	else:
		products = ''

	return render(request, 'search/search.html', {'products':products})

def filter(request, category):
	products = ProductDocument.search().query('match', category=category)

	return render(request, 'search/search.html', {'products':products})

