import re
import json
import requests
from PyMovieDb import ImdbParser
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class IMDB:
    """
        A class to represent IMDB API.

        --------------

        Main Methods of the IMDB API
        --------------
            #1. search(name, year=None, tv=False, person=False)
                -- to search a query on IMDB

            #2. get_by_name(name, year=None, tv=False)
                -- to get a Movie/TV-Series info by it's name (pass year also to increase accuracy)

            #3. get_by_id(file_id)
                -- to get a Movie/TV-Series info by it's IMDB-ID (pass year also to increase accuracy)

            #4. person_by_name(name)
                -- to get a person's info by his/her name

            #5. person_by_id( p_id)
                -- to get a person's info by his/her IMDB-ID

            #6. upcoming(region=None)
                -- to get upcoming movies/TV-Series

            #7. popular_movies(genre=None, start_id=1, sort_by=None)
                -- to get IMDB popular movies

            #8. popular_tv(genre=None, start_id=1, sort_by=None)
                -- to get IMDB popular Tv-Series
    """
    def __init__(self, lang="en"):
        self.session = requests.session()
        self.session.headers.update({
           "Accept": "application/json, text/plain, */*",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
           "Referer": "https://www.imdb.com/",
           "Accept-Language": lang
           })
        self.baseURL = "https://www.imdb.com"
        self.search_results = {'result_count': 0, 'results': []}
        self.NA = {"status": 404, "message": "No Result Found!", 'result_count': 0, 'results': []}

    # ..................................method to search on IMDB...........................................
    def search(self, name, year=None, tv=False, person=False):
        """
         @description:- Helps to search a query on IMDB.
         @parameter-1:- <str:name>, query value to search.
         @parameter-2:- <int:year> OPTIONAL, release year of query/movie/tv/file to search.
         @parameter-3:- <bool:tv> OPTIONAL, to filter/limit/bound search results only for 'TV Series'.
         @parameter-4:- <bool:person> OPTIONAL, to filter search results only for person.
         @returns:- A JSON object:
                    - {'result_count': <int:total_search_results>, 'results': <list:list_of_files/movie_info_dict>}
        """
        assert isinstance(name, str)
        self.search_results = {'result_count': 0, 'results': []}

        name = name.replace(" ", "+")

        if year is None:
            url = f"https://www.imdb.com/find?q={name}"
        else:
            assert isinstance(year, int)
            url = f"https://www.imdb.com/find?q={name}+{year}"
        # print(url)

        try:
            response = self.session.get(url)
        except requests.exceptions.ConnectionError as e:
            response = self.session.get(url, verify=False)

        soup = BeautifulSoup(response.content,'html.parser')
        results = soup.find('script', type='application/json').text
        results = json.loads(results)
        results = ImdbParser(results).unescape_json_values
        output = []

        if tv:
            for item in results["props"]["pageProps"]["titleResults"]["results"]:
                if item["imageType"] in ["tvMiniSeries", "tvSeries"]:
                    output.append({
                            "id": item['id'],
                            "name": item['titleNameText'],
                            "url": f"{self.baseURL}/title/{item['id']}",
                            "poster": item.get('titlePosterImageModel', {}).get('url', ''),
                            "type": item["imageType"]
                            })
        
        elif person:
            for item in results["props"]["pageProps"]["nameResults"]["results"]:
                output.append({
                        "id": item['id'],
                        "name": item['displayNameText'],
                        "url": f"{self.baseURL}/name/{item['id']}",
                        "poster": item.get('avatarImageModel', {}).get('url', ''),
                        "type": item["knownForJobCategory"]
                        })
        else:
            for item in results["props"]["pageProps"]["titleResults"]["results"]:
                if item["imageType"] not in ["podcastSeries", "tvSpecial"]:
                    output.append({
                            "id": item['id'],
                            "name": item['titleNameText'],
                            "url": f"{self.baseURL}/title/{item['id']}",
                            "poster": item.get('titlePosterImageModel', {}).get('url', ''),
                            "type": item["imageType"]
                            })
            for item in results["props"]["pageProps"]["nameResults"]["results"]:
                output.append({
                        "id": item['id'],
                        "name": item['displayNameText'],
                        "url": f"{self.baseURL}/name/{item['id']}",
                        "poster": item.get('avatarImageModel', {}).get('url', ''),
                        "type": item["knownForJobCategory"]
                        })

        self.search_results = {'result_count': len(output), 'results': output}
        return self.search_results

    # ..............................methods to get a movie/web-series/tv info..............................
    def get(self, url):
        """
         @description:- helps to get a file's complete info (used by get_by_name() & get_by_id() )
         @parameter:- <str:url>, url of the file/movie/tv-series.
         @returns:- File/movie/TV info as JSON.
        """
        try:
            response = self.session.get(url)
            soup = BeautifulSoup(response.content,'html.parser')
            result = soup.find('script', type='application/ld+json').text
            # print(result)
            # converting JSON object into dict
            result = json.loads(result)
            result = ImdbParser(result).unescape_json_values
        except (json.decoder.JSONDecodeError, IndexError) as e:
            return self.NA

        output = {
            "type": result.get('@type'),
            "name": result.get('name'),
            "alternateName": result.get('alternateName', None),
            "url": self.baseURL + result.get('url'),
            "poster": result.get('image'),
            "description": result.get('description'),
            "review": {
                "author": result.get("review", {'author': {'name': None}}).get('author').get('name'),
                "dateCreated": result.get("review", {"dateCreated": None}).get("dateCreated"),
                "inLanguage": result.get("review", {"inLanguage": None}).get("inLanguage"),
                "heading": result.get("review", {"name": None}).get("name"),
                "reviewBody": result.get("review", {"reviewBody": None}).get("reviewBody"),
                "reviewRating": {
                    "worstRating": result.get("review", {"reviewRating": {"worstRating": None}})
                        .get("reviewRating",{"worstRating": None}).get("worstRating"),
                    "bestRating": result.get("review", {"reviewRating": {"bestRating": None}})
                        .get("reviewRating",{"bestRating": None}).get("bestRating"),
                    "ratingValue": result.get("review", {"reviewRating": {"ratingValue": None}})
                        .get("reviewRating",{"ratingValue": None}).get("ratingValue"),
                },
            },
            "rating": {
                "ratingCount": result.get("aggregateRating", {"ratingCount": None}).get("ratingCount"),
                "bestRating": result.get("aggregateRating", {"bestRating": None}).get("bestRating"),
                "worstRating": result.get("aggregateRating", {"worstRating": None}).get("worstRating"),
                "ratingValue": result.get("aggregateRating", {"ratingValue": None}).get("ratingValue"),
            },
            "contentRating": result.get("contentRating"),
            "genre": result.get("genre"),
            "datePublished": result.get("datePublished"),
            "keywords": result.get("keywords"),
            "duration": result.get("duration"),
            "actor": [
                {"name": actor.get("name"), "url": actor.get("url")} for actor in result.get("actor", [])
            ],
            "director": [
                {"name": director.get("name"), "url": director.get("url")} for director in result.get("director", [])
            ],
            "creator": [
                {"name": creator.get("name"), "url": creator.get("url")} for creator in result.get("creator", [])
                if creator.get('@type') == 'Person'
            ]
        }
        return output

    def get_by_name(self, name, year=None, tv=False):
        """
         @description:- Helps to search a file/movie/tv by name.
         @parameter-1:- <str:name>, query/name to search.
         @parameter-2:- <int:year> OPTIONAL, release year of query/movie/tv/file to search.
         @parameter-3:- <bool:tv> OPTIONAL, to filter/limit/bound search result only for 'TV Series'.
         @returns:- File/movie/TV info as JSON.
        """
        results = self.search(name, year=year, tv=tv)
        all_results = [i for i in self.search_results['results'] if 'title' in i['url']]
        # print(all_results)

        # filtering TV and movies
        if tv:  # for tv/Web-Series only
            results['results'] = all_results
        else:  # for movies only
            results['results'] = [result for result in all_results if "movie" == result['type']]
        # print(results['results'])

        if len(results['results']) > 0:
            return self.get(results['results'][0].get('url'))
        else:
            return self.NA

    def get_by_id(self, file_id):
        """
         @description:- Helps to search a file/movie/tv by its imdb ID.
         @parameter-1:- <str:file_id>, imdb ID of the file/movie/tv.
         @returns:- File/movie/TV info as JSON object.
        """
        assert isinstance(file_id, str)
        url = f"{self.baseURL}/title/{file_id}"
        return self.get(url)

    # ........................................Methods for person profile...................................
    def get_person(self, url):
        """
         @description:- Helps to search a person info by its url, (used by person_by_name() & person_by_id() ).
         @parameter-1:- <str:url>, url of the person's profile page.
         @returns:- Person's info as JSON object.
        """
        try:
            response = self.session.get(url)
            soup = BeautifulSoup(response.content,'html.parser')
            result = soup.find('script', type='application/ld+json').text
            result = json.loads(result)
            result = ImdbParser(result).unescape_json_values
        except (json.decoder.JSONDecodeError, IndexError) as e:
            return self.NA

        del result["@context"]
        result['type'] = result.get('@type')
        del result["@type"]
        return result

    def person_by_name(self, name):
        """
         @description:- Helps to search a person info by its name.
         @parameter-1:- <str:name>, name of the person.
         @returns:- Person's info as JSON object.
        """
        results = self.search(name, person=True)
        url = results['results'][0].get('url')
        return self.get_person(url)

    def person_by_id(self, p_id):
        """
         @description:- Helps to search a person info by its imdb ID.
         @parameter-1:- <str:p_id>, imdb ID of the person's profile.
         @returns:- Person's info as JSON object.
        """
        assert isinstance(p_id, str)
        url = f"{self.baseURL}/name/{p_id}"
        return self.get_person(url)

    # .........................................For Upcoming Movies.........................................
    def upcoming(self, region=None):
        """
         @description:- Helps to get upcoming movies/tv-series.
         @parameter-1:- <str:region> OPTIONAL, country code (like US, IN etc.) to filter results by region/country.
         @returns:- upcoming movies/TV-Series info as JSON object.
        """
        if region is not None:
            assert isinstance(region, str)
            url = f"https://www.imdb.com/calendar?region={region}"
        else:
            url = "https://www.imdb.com/calendar"

        try:
            response = self.session.get(url)
        except requests.exceptions.ConnectionError as e:
            response = self.session.get(url, verify=False)
        soup = BeautifulSoup(response.content,'html.parser')
        script_tag = soup.find('script', type='application/json').text
        script = json.loads(script_tag)
        output = []
        for group in script["props"]["pageProps"]["groups"]:
            for entry in group["entries"]:
                output.append({
                    'id': entry["id"],
                    'name': entry["titleText"],
                    'url': self.baseURL + entry["id"],
                    'release_data': entry["releaseDate"]
                })
        results = {'result_count': len(output), 'results': output}
        if results['result_count'] > 0:
            return results
        else:
            return self.NA

    # ............................................For Popular Movies.......................................
    def get_popular(self, url):
        """
         @description:- Helps to search popular movies/TV-Series by url, (used by popular_movies() & popular_tv() ).
         @parameter-1:- <str:url>, url to search.
         @returns:- Files/Movies/TV-Series info as JSON object.
        """
        assert isinstance(url, str)
        try:
            response = self.session.get(url)
        except requests.exceptions.ConnectionError as e:
            response = self.session.get(url, verify=False)

        soup = BeautifulSoup(response.content,'html.parser')
        links = soup.select('h3 > a')
        years = soup.select('h3 > span:last-child')

        if not bool(links) and bool(years):
            return self.NA

        output = []
        for link, year in zip(links, years):
            href = link.attrs.get('href', "#")
            if 'title' in href:
                # getting year
                if year != "":
                    year = year.text.split('(')[-1].replace(')', '')
                    year = year[:-2] if year[-2:] == "– " else year
                else:
                    year = "unknown"
                # getting poster
                file_id = href.split('/')[2]
                poster = soup.find('img', {'data-tconst': file_id})
                poster = poster.attrs.get('loadlate', 'image_not_found') if bool(poster) else 'image_not_found'
                # creating file object
                output.append({
                    'id': file_id,
                    'name': link.text,
                    'year': year,
                    'url': self.baseURL + href,
                    'poster': poster
                })

        self.search_results = {'result_count': len(output), 'results': output}
        return self.search_results

    def popular_movies(self, genre=None, start_id=1, sort_by=None):
        """
         @description:- Helps to get 50 popular movies starting from <start_id>.
         @parameter-1:- <str:genre> OPTIONAL, to filter results by genre.
         @parameter-2:- <int:start_id> DEFAULT=1, start id to show results (shows results from start_id to start_id+50).
         @parameter-3:- <bool:sort_by> OPTIONAL, to sort results (eg. sort=user_rating,desc OR sort=user_rating,asc).
                        - (visit 'https://www.imdb.com/search/title/?title_type=movie' for more info)
         @returns:- Popular Movies (by genre) info as JSON object.
        """
        assert isinstance(start_id, int)
        if genre is not None:
            assert isinstance(genre, str)
            url = f"https://www.imdb.com/search/title/?title_type=movie&genres={genre}&start={start_id}&sort={sort_by}"
        else:
            url = f"https://www.imdb.com/search/title/?title_type=movie&start={start_id}&sort={sort_by}"
        return self.get_popular(url)

    def popular_tv(self, genre=None, start_id=1, sort_by=None):
        """
         @description:- Helps to get 50 popular TV-Series starting from <start_id>.
         @parameter-1:- <str:genre> OPTIONAL, to filter results by genre.
         @parameter-2:- <int:start_id> DEFAULT=1, start id to show results (shows results from start_id to start_id+50).
         @parameter-3:- <bool:sort_by> OPTIONAL, to sort results (eg. sort=user_rating,desc OR sort=user_rating,asc).
                        - (visit 'https://www.imdb.com/search/title/?title_type=movie' for more info)
         @returns:- Popular TV-Series info as JSON object.
        """
        assert isinstance(start_id, int)
        if genre is not None:
            assert isinstance(genre, str)
            url = f"https://www.imdb.com/search/title/?title_type=tv_series,tv_miniseries&genres={genre}&start={start_id}&sort={sort_by}"
        else:
            url = f"https://www.imdb.com/search/title/?title_type=tv_series,tv_miniseries&start={start_id}&sort={sort_by}"

        return self.get_popular(url)


