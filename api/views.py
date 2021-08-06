from django.shortcuts import render
from rest_framework.parsers import JSONParser
from .serializers import *
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# to convert the date posted to local time
from django.utils.formats import localize
# Create your views here.
def fetchtweets (request):
    posts = Post.objects.all().order_by('-DatePosted')

    # now we have to break the queryset Posts, so as to format the date, because we can't have the standard date for mat on the UI, so we have to make it humanize or to local time 
    tweets = list ()
    for tweet in posts:
        eachtweet = {}
        eachtweet['Name'] = tweet.Name
        eachtweet['Message'] = tweet.Message
        eachtweet['DatePosted'] = localize(tweet.DatePosted)
        tweets.append(eachtweet)
    # postserializer = PostSerializer(posts, many=True)
    return JsonResponse(tweets, safe=False)

@csrf_exempt
def fetchtweetsfilter (request):
    data = JSONParser().parse(request)

    # just incase we want to have some other forms of filter in the future
    if data['value'] == 'Name':
        posts = Post.objects.all().order_by('Name')

        # now we have to break the queryset Posts, so as to format the date, because we can't have the standard date for mat on the UI, so we have to make it humanize or to local time 
        tweets = list ()
        for tweet in posts:
            eachtweet = {}
            eachtweet['Name'] = tweet.Name
            eachtweet['Message'] = tweet.Message
            eachtweet['DatePosted'] = localize(tweet.DatePosted)
            tweets.append(eachtweet)
        # postserializer = PostSerializer(posts, many=True)
        return JsonResponse(tweets, safe=False)

@csrf_exempt
def addtweets (request):
    data= JSONParser().parse(request)
    print(data)
    addpostserializer = AddPostSerializer(data=data)
    if addpostserializer.is_valid():
        addpostserializer.save()
        return JsonResponse({'status' : True}, safe=False)    
    return JsonResponse({'status':False}, safe=False)