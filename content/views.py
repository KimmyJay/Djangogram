from django.shortcuts import render
from rest_framework.views import APIView
from content.models import * #import all models from content application


# Create your views here.

class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all # select * from content_feed;
        recommendations_list = Recommendations.objects.all
        return render(request, 'main.html', context=dict(feed_list=feed_list, recommendations_list=recommendations_list))