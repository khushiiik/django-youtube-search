from django.shortcuts import render
from youtubesearchpython import VideosSearch

def index(request):
    query = request.GET.get('query', None)  
    results = []  
    
    if query:
        try:
            video_search = VideosSearch(query, limit=5)
            search_results = video_search.result().get('result', [])
            
            results = [
                {
                    'title': result.get('title'),
                    'url': result.get('link'),
                    'channel': result.get('channel', {}).get('name')
                }
                for result in search_results
            ]
        except Exception as e:
            print(f"An error occurred: {e}")
    

    return render(request, 'index.html', {'results': results})
