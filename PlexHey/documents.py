# from django_elasticsearch_dsl import DocType, Index
# from .models import make1
#
# posts = Index('carmake')
#
# @posts.doc_type
# class PostDocument(DocType):
#     class Meta:
#         model = make1
#
#         fields = [
#             'car_make',
#             'description',
#             'make_image',
#         ]