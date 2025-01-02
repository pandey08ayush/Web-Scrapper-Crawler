from django.shortcuts import render
from django.http import JsonResponse
from scrapper.script import scraper_imdb_news
from scrapper.models import News
def run_scraper(request):
    """
    View to trigger the IMDb news scraper.
    Returns a JSON response with the status of the scraper execution.
    """
    try:
        # Run the scraper function
        scraper_imdb_news()
        return JsonResponse({
            "status": True,
            "message": "Scraper executed successfully."
        })
    except Exception as e:
        # Handle errors gracefully
        return JsonResponse({
            "status": False,
            "message": f"Error occurred while executing scraper: {str(e)}"
        })

def index(request):
    """
    View to render the homepage.
    Displays the index.html template.
    """
    news=News.objects.all()
    return render(request, 'index.html', context={'news':news})
