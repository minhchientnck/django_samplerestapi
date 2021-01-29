
from myapi.models import Question
from myapi.serializers import QuestionSerializer
from rest_framework import viewsets


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
