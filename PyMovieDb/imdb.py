import re
import json
import requests
from PyMovieDb import ImdbParser
from requests_html import HTMLSession
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
    def __init__(self):
        self.session = HTMLSession()
        self.headers = {
           "Accept": "application/json, text/plain, */*",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
           "Referer": "https://www.imdb.com/"
           }
        self.baseURL = "https://www.imdb.com"
        self.search_results = {'result_count': 0, 'results': []}
        self.NA = json.dumps({"status": 404, "message": "No Result Found!", 'result_count': 0, 'results': []})

    # ..................................method to search on IMDB...........................................

    def search(self, name, year=None, tv=False, person=False):
        """
         @description:- Helps to search a query on IMDB.
         @parameter-1:- <str:name>, query value to search.
         @parameter-2:- <int:year> OPTIONAL, release year of query/movie/tv/file to search.
         @parameter-3:- <bool:tv> OPTIONAL, to filter/limit/bound search results only for 'TV Series'.
         @parameter-4:- <bool:person> OPTIONAL, to filter search results only for person.
         @returns:- A JSON string:
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

        # results = response.html.xpath("//table[@class='findList']/tr")
        results = response.html.xpath("//section[@data-testid='find-results-section-title']/div/ul/li")
        # print(len(results))
        if tv is True:
            results = [result for result in results if "TV" in result.text]

        if person is True:
            results = response.html.xpath("//section[@data-testid='find-results-section-name']/div/ul/li")
            results = [result for result in results if 'name' in result.find('a')[0].attrs['href']]
        # print(results)
        output = []
        for result in results:
            name = result.text.replace('\n', ' ')
            url = result.find('a')[0].attrs['href']
            if ('Podcast' not in name) and ('Music Video' not in name):
                try:
                    image = result.xpath("//img")[0].attrs['src']
                    file_id = url.split('/')[2]
                    output.append({
                        'id': file_id,
                        "name": name,
                        "url": f"https://www.imdb.com{url}",
                        "poster": image
                       })
                except IndexError:
                    pass
                self.search_results = {'result_count': len(output), 'results': output}
        return json.dumps(self.search_results, indent=2)

    # ..............................methods to get a movie/web-series/tv info..............................
    def get(self, url):
        """
         @description:- helps to get a file's complete info (used by get_by_name() & get_by_id() )
         @parameter:- <str:url>, url of the file/movie/tv-series.
         @returns:- File/movie/TV info as JSON string.
        """
        try:
            response = self.session.get(url)

            result = response.html.xpath("//script[@type='application/ld+json']")[0].text
            result = ''.join(result.splitlines())  # removing newlines
            result = f"""{result}"""
            # print(result)
        except IndexError:
            return self.NA
        try:
            # converting json string into dict
            result = json.loads(result)
        except json.decoder.JSONDecodeError as e:
            # sometimes json is invalid as 'description' contains inverted commas or other html escape chars
            try:
                to_parse = ImdbParser(result)
                # removing trailer & description schema from json string
                parsed = to_parse.remove_trailer
                parsed = to_parse.remove_description
                # print(parsed)
                result = json.loads(parsed)
            except json.decoder.JSONDecodeError as e:
                try:
                    # removing reviewBody from json string
                    parsed = to_parse.remove_review_body
                    result = json.loads(parsed)
                except json.decoder.JSONDecodeError as e:
                    # invalid char(s) is/are not in description/trailer/reviewBody schema
                    return self.NA

        output = {
            "type": result.get('@type'),
            "name": result.get('name'),
            "url": self.baseURL + result.get('url').split("/title")[-1],
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
        return json.dumps(output, indent=2)

    def get_by_name(self, name, year=None, tv=False):
        """
         @description:- Helps to search a file/movie/tv by name.
         @parameter-1:- <str:name>, query/name to search.
         @parameter-2:- <int:year> OPTIONAL, release year of query/movie/tv/file to search.
         @parameter-3:- <bool:tv> OPTIONAL, to filter/limit/bound search result only for 'TV Series'.
         @returns:- File/movie/TV info as JSON string.
        """
        results = json.loads(self.search(name, year=year))
        all_results = [i for i in self.search_results['results'] if 'title' in i['url']]
        # print(all_results)

        # filtering TV and movies
        if tv is True:  # for tv/Web-Series only
            tv_only = [result for result in all_results if "TV" in result['name']]
            if year is not None:
                tv_only = [result for result in tv_only if str(year) in result['name']]
            # double checking by file name
            if bool(tv_only):
                tv_only_checked = [result for result in tv_only if result['name'].lower().startswith(name.split(" ")[0].lower())]
                tv_only = tv_only_checked if bool(tv_only_checked) else tv_only
            results['results'] = tv_only if bool(tv_only) else all_results

        else:  # for movies only
            movie_only = [result for result in all_results if "TV" not in result['name']]
            if year is not None:
                movie_only = [result for result in movie_only if str(year) in result['name']]
            # double checking by file name
            if bool(movie_only):
                movie_only_checked = [result for result in movie_only if result['name'].lower().startswith(name.split(" ")[0].lower())]
                movie_only = movie_only_checked if bool(movie_only_checked) else movie_only
            results['results'] = movie_only if bool(movie_only) else all_results
        # print(results['results'])

        if len(results['results']) > 0:
            return self.get(results['results'][0].get('url'))
        else:
            return self.NA

    def get_by_id(self, file_id):
        """
         @description:- Helps to search a file/movie/tv by its imdb ID.
         @parameter-1:- <str:file_id>, imdb ID of the file/movie/tv.
         @returns:- File/movie/TV info as JSON string.
        """
        assert isinstance(file_id, str)
        url = f"{self.baseURL}/title/{file_id}"
        return self.get(url)

    """
     @description:- Helps to search a list of tv episodes by the tv show's imdb ID.
     @parameter-1:- <str:file_id>, imdb ID of the tv show.
     @parameter-2:- <str:season_id>, optional season number (fetches all seasons if None).
     @returns:- A JSON string:
                - {
                   'season_count': <int:total_seasons>,
                   'seasons': <list:season_info_dict>
                  }
                  where <season_info_dict>:
                  {
                    'id': <int:season_number>,
                    'episode_count': <int:total_episodes_in_season>,
                    'episodes': <list:episode_info_dict>
                  }
                  where <episode_info_dict>:
                  {
                    'id': <int:episode_number>,
                    'sid': <int:season_number>,
                    'fqid': <str:S#E#>,
                    'name': <str: episode_name>
                  }
    """
    def get_episodes(self, file_id, season_id=None):
        assert isinstance(file_id, str)
        assert (season_id is None or isinstance(season_id, int) or
                (isinstance(season_id, str) and season_id.isdigit()))

        # <div class="ipc-title__text">S{#}.E{#} <middle-dot> {EpisodeName}</div>
        episode_matcher = re.compile(r'^S(?P<sid>[0-9]+).E(?P<eid>[0-9]+)\s+.+?\s+(?P<name>.+)$')

        initial_season_id = season_id if season_id else '1'
        more_season_ids = []
        episodes_by_season = {}

        def do_request(s_id):
            url = f"{self.baseURL}/title/{file_id}/episodes?season={s_id if s_id else '1'}"
            try:
                r = self.session.get(url)
            except requests.exceptions.ConnectionError as e:
                r = self.session.get(url, verify=False)
            return r

        def extract_episodes(r) -> list:
            episodes = []
            for episode_text in r.html.xpath("//div[@class='ipc-title__text']/text()"):
                match = episode_matcher.search(episode_text)
                if match:
                    sid, eid = match.group('sid'), match.group('eid')
                    episodes.append(
                        {
                            'id': match.group('eid'),
                            'sid': match.group('sid'),
                            'fqid': f"S{sid:0>2}E{eid:0>2}",
                            'name': match.group('name'),
                        }
                    )
            return episodes

        # Load the initial page
        response = do_request(initial_season_id)

        # Grab the remaining season numbers if a season_id is not explicitly specified
        if not season_id:
            # <li ... data-testid="tab-season-entry">{SeasonNumber}</li>
            more_season_ids = [
                s for s in
                response.html.xpath("//li[@data-testid='tab-season-entry']/text()")
                if s != '1'
            ]
        # Grab initial page episodes
        episodes_by_season[initial_season_id] = extract_episodes(response)

        # Fetch the other seasons' episodes from their pages if needed
        for s in more_season_ids:
            response = do_request(s)
            episodes_by_season[s] = extract_episodes(response)

        return json.dumps(
            {
                'season_count': len(episodes_by_season),
                'seasons': [
                    {'id': sid, 'episode_count': len(eps), 'episodes': eps}
                    for (sid, eps)
                    in episodes_by_season.items()
                ],
            },
            indent=2)

    # ........................................Methods for person profile...................................
    def get_person(self, url):
        """
         @description:- Helps to search a person info by its url, (used by person_by_name() & person_by_id() ).
         @parameter-1:- <str:url>, url of the person's profile page.
         @returns:- Person's info as JSON string.
        """
        try:
            response = self.session.get(url)
            result = response.html.xpath("//script[@type='application/ld+json']")[0].text
            result = f"""{result}"""
            result = json.loads(result)
        except json.decoder.JSONDecodeError as e:
            return self.NA

        del result["@context"]
        result['type'] = result.get('@type')
        del result["@type"]
        return json.dumps(result, indent=2)

    def person_by_name(self, name):
        """
         @description:- Helps to search a person info by its name.
         @parameter-1:- <str:name>, name of the person.
         @returns:- Person's info as JSON string.
        """
        results = json.loads(self.search(name, person=True))
        # print(results)
        url = results['results'][0].get('url')
        return self.get_person(url)

    def person_by_id(self, p_id):
        """
         @description:- Helps to search a person info by its imdb ID.
         @parameter-1:- <str:p_id>, imdb ID of the person's profile.
         @returns:- Person's info as JSON string.
        """
        assert isinstance(p_id, str)
        url = f"{self.baseURL}/name/{p_id}"
        return self.get_person(url)

    # .........................................For Upcoming Movies.........................................
    def upcoming(self, region=None):
        """
         @description:- Helps to get upcoming movies/tv-series.
         @parameter-1:- <str:region> OPTIONAL, country code (like US, IN etc.) to filter results by region/country.
         @returns:- upcoming movies/TV-Series info as JSON string.
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

        output = []
        div = response.html.xpath("//main")[0]
        # movies are divided/enlisted within article tag
        articles = div.find('article')
        for article in articles:
            h3 = article.find('h3')[0]
            ul = article.xpath('//ul')[0].xpath('//li')
            for li in ul:
                try:
                    movie = li.find('a')[0]
                    poster = ul[0].find('img')[0].attrs.get('src')
                    output.append({
                          'id': movie.attrs['href'].split('/')[2],
                          'name': movie.text,
                          'url': self.baseURL + movie.attrs['href'],
                          'release_data': h3.text,
                          'poster': poster.split(',')[0]
                    })
                except IndexError:
                    pass

        results = {'result_count': len(output), 'results': output}
        if results['result_count'] > 0:
            return json.dumps(results, indent=2)
        else:
            return self.NA

    # ............................................For Popular Movies.......................................
    def get_popular(self, url):
        """
         @description:- Helps to search popular movies/TV-Series by url, (used by popular_movies() & popular_tv() ).
         @parameter-1:- <str:url>, url to search.
         @returns:- Files/Movies/TV-Series info as JSON string.
        """
        assert isinstance(url, str)
        try:
            response = self.session.get(url)
        except requests.exceptions.ConnectionError as e:
            response = self.session.get(url, verify=False)

        all_li = response.html.xpath('//ul[@role="presentation"]/li')

        output = []
        # for link, year in zip(links, years):
        for li in all_li:
            for obj in li.find('a'):
                if ("title" in obj.attrs.get('href')) and (". " in obj.text):
                    href = obj.attrs.get('href')
                    name = obj.text.split(". ")[-1]
                    break

            # getting year
            for span in li.find('span'):
                if len(span.text.strip()) == 4:
                    try:
                        year = int(span.text.strip())
                        break
                    except:
                        year = "N/A"

            # getting poster
            try:
                file_id = href.split('/')[2]
                poster = li.xpath("//img[@loading='lazy']")
                poster = poster[0].attrs.get('src')
                poster = poster if bool(poster) else 'image_not_found'
            except:
                poster = 'image_not_found'
            # creating file object
            output.append({
                'id': file_id,
                'name': name,
                'year': year,
                'url': self.baseURL + href,
                'poster': poster
            })

        self.search_results = {'result_count': len(output), 'results': output}
        return json.dumps(self.search_results, indent=2)

    def popular_movies(self, genre=None, start_id=1, sort_by=None):
        """
         @description:- Helps to get 50 popular movies starting from <start_id>.
         @parameter-1:- <str:genre> OPTIONAL, to filter results by genre.
         @parameter-2:- <int:start_id> DEFAULT=1, start id to show results (shows results from start_id to start_id+50).
         @parameter-3:- <bool:sort_by> OPTIONAL, to sort results (eg. sort=user_rating,desc OR sort=user_rating,asc).
                        - (visit 'https://www.imdb.com/search/title/?title_type=movie' for more info)
         @returns:- Popular Movies (by genre) info as JSON string.
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
         @returns:- Popular TV-Series info as JSON string.
        """
        assert isinstance(start_id, int)
        if genre is not None:
            assert isinstance(genre, str)
            url = f"https://www.imdb.com/search/title/?title_type=tv_series,tv_miniseries&genres={genre}&start={start_id}&sort={sort_by}"
        else:
            url = f"https://www.imdb.com/search/title/?title_type=tv_series,tv_miniseries&start={start_id}&sort={sort_by}"

        return self.get_popular(url)


