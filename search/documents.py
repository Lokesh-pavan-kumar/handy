from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from handy.models import Product
from elasticsearch_dsl import analyzer

@registry.register_document
class ProductDocument(Document):

	category = fields.TextField(attr='category.category')

	class Index:
		name = 'products'
		settings = {
			'number_of_shards': 1,
			'number_of_replicas': 0
		}

	class Django:
		model = Product

		fields = [
			'id', 'name', 'description', 'image', 'price'
		]

