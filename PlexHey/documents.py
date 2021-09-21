from django_elasticsearch_dsl import Document, Index
from django_elasticsearch_dsl import Index, Document
from django_elasticsearch_dsl.documents import DocType
from .models import make1

posts = Index('carmake')

@posts.document
class PostDocument(Document):
    class Django:
        model = make1

        fields = [
            'car_make',
            'description',
            'make_image',
        ]