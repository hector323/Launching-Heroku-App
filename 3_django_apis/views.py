from datetime import datetime

import requests
from django.shortcuts import render


def homepage(request):
    context = {
    }
    return render(request, 'homepage.html', context)


def search_results(request):

    search_type = request.GET['stype']
    search_query = request.GET['searchterm']

    context = {
        'result_count': 0,
        'search_message': None,
        'search_term': search_query,
        'search_type': search_type,
    }

    if search_type == 'booksearch':
        context['search_message'] = 'Books'
        context['results_count'] = 0
        # API example: http://openlibrary.org/search.json?q=Mockingjay
        # TODO Unfinished...
        url = 'http://openlibrary.org/search.json?q='
        url += search_query
        response = request.get(url)
        books_data = response.json()
        results_list = books_data['docs']
        results_list = news_data['response']['results']
        context['results_count'] = books_data['num_Found']['total']
        print(results_list)
        context['books_results'] = results_list


    elif search_type == 'newssearch':
        context['search_message'] = 'Headlines'
        context['results_count'] = 0
        # TODO Unfinished...
        #url ='http://content.guardianapis.com/search?api-key=a938fccc-00e9-41ca-905c-741615da8be1&page-size=50&q='
        url = 'http://content.guardianapis.com/search?q='
        url += search_query
        url += '&api-key=a938fccc-00e9-41ca-905c-741615da8be1'

        response = requests.get(url)
        news_data = response.json()

        results_list = news_data['response']['results']
        context['results_count'] = news_data['response']['total']
        print(results_list)
        context['news_results'] = results_list

        # return render(request, 'news.html', context)

    # ---------------------
    elif search_type == 'musicsearch':
        context['search_message'] = 'Music'
        context['results_count'] = 0
        # API example: http://musicbrainz.org/ws/2/release/?fmt=json&query=cardi+b
        # TODO Unfinished...
        url = 'http://musicbrainz.org/ws/2/release/?fmt=json&query='
        url += search_query
        response = request.get(url)
        data = response.json()
        results_list = data['releases']
        results_list = news_data['response']['results']
        context['results_count'] = data['count']
        print(results_list)
        context['music_results'] = results_list

    else:
        context['search_message'] = 'Unknown search, bug?'

    return render(request, 'search_results.html', context)


def giggle_news(request):

    # Do a GET request using the API key to get the latest Guardian headlines
    # The parameters are detailed here:
    # https://open-platform.theguardian.com/documentation/search
    url = 'http://content.guardianapis.com/search?api-key=a938fccc-00e9-41ca-905c-741615da8be1&page-size=50&q='
    url += search_query
    response = requests.get(url)
    news_data = response.json() # Interpret response as JSON

    # The Guardian API responds with a JSON dictionary, that has a key called
    # 'response', which in turn is another dictionary with a key called
    # 'results'. This final key has the list that we want
    results_list = news_data['response']['results']

    context = {
        'news_results': results_list,
    }
    return render(request, 'news.html', context)

