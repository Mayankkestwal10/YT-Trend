from django.shortcuts import render
from apiclient.discovery import build

# Create your views here.
def root(request):
    API_KEY = 'AIzaSyCF1p49IUi5kTy1s6kyQI-0A-PuWnWnl0I'

    youtube = build('youtube','v3', developerKey=API_KEY)

    req = youtube.videos().list(part=['snippet','statistics'],chart='mostPopular',regionCode='IN',maxResults=10)

    response = req.execute()


    
    idx = []
    title = []
    description = []
    links = []
    images = []
    views = []
    likes = []
    dislikes = []

    init = 'https://www.youtube.com/watch?v='
    i = 0
    for item in response["items"]:
        i+=1
        idx.append(i)
        title.append(item['snippet']['title'])
        description.append(item['snippet']['description'][:400])
        links.append(init+item['id'])
        images.append(item['snippet']['thumbnails']['medium']['url'])
        views.append(item['statistics']['viewCount'])
        likes.append(item['statistics']['likeCount'])
        dislikes.append(item['statistics']['dislikeCount'])


    context = zip(idx, title, description, links, images, views, likes, dislikes)
    
    return render(request, 'root.html', context={'context':context})
