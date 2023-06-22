from django.shortcuts import render
from newsapi import NewsApiClient
#from . import NewsApiClient
import url_to_image
import urllib


# Create your views here.

def index(request):
    
 
    newsapi = NewsApiClient(api_key ='32ab2fe92bfd43459eb4968d931ed3d8')
    top = newsapi.get_top_headlines(sources ='bbc.co.uk, bbc-news, techcrunch, the-verge, al-jazeera-english, cnn, engadget.com')
  
    #l = top['articles']
    l = top.get('articles')
    print(top)
    #desc =[]
    news =[]
    img =[]
    url=[]
    #cont=[]
    pub=[]
  

    #mylist = zip(news, desc, img)
    for i in range(len(l)):
        myarticles  = l[i]
        #news.append(myarticles['title'])  # x = thisdict.get("model")
        news.append(myarticles.get('title'))
        #desc.append(myarticles['description'])
        #desc.append(myarticles.get('description'))
        #img.append(myarticles['urlToImage'])
        img.append(myarticles.get('i.urlToImage'))
        url.append(myarticles.get('url'))
        #cont.append(myarticles.get('content'))
        pub.append(myarticles.get('publishedAt'))


    mylist = zip(news, img, url, pub)
  
    return render(request, 'myapp/index.html', context={'mylist':mylist})

    #return render(request, 'myapp/index.html', context =mylist)

    #context = {'mylist':mylist}

    #return render(request, 'myapp/index.html', context)