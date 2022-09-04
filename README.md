
# PyMovieDb 
PyMovieDb is a python wrapper to represent the [IMDB](https://www.imdb.com) API. It helps you to get files i.e. Movies/TV-Series information from IMDB by scraping.

PyMovieDb is:
* Extremely Simple
* Reliable
* Lightweight
* Free & easy to use.

****
_*PyMovieDb is just arrived in the web/IT market, don't hesitate to fork and add new features/updates/issues etc. to it.*_
****

## Installation
Use ```pip``` to install the module from pypi like

```pip install PyMovieDb```


## Documentation 
**1) Getting a Movie/Tv-Series info :-**

Use ``` get_by_name(<name>, tv=False) ``` method to get information of a movie/TV-Series.

The ``` tv ``` is an optional argument, if ``` tv=True``` it will get data from ```TV Series``` files only.

On the other hand, if ```tv=False``` (default), it will find your file in ```Movies + TV Series``` results
```python
>>> from PyMovieDb import IMDB
>>> imdb = IMDB()
>>> res = imdb.get_by_name('House Of The Dragon', tv=True)
>>> print(res)
>>> {
  "type": "TVSeries",
  "name": "House of the Dragon",
  "url": "https://www.imdb.com/title/tt11198330/",
  "poster": "https://m.media-amazon.com/images/M/MV5BZDBkZjRiNGMtZGU2My00ODdkLWI0MGYtNGU4MmJjN2MzOTkxXkEyXkFqcGdeQXVyMDM2NDM2MQ@@._V1_.jpg",
  "description": "House of the Dragon tells the story of an internal succession war within House Targaryen at the height of its power, 172 years before the birth of Daenerys Targaryen.",
  "review": {
    "author": "lmahesa",
    "dateCreated": "2022-08-21",
    "inLanguage": "English",
    "heading": "Very, very promising.",
    "reviewBody": "Last week, I binged seasons 1-7 of GoT so those episodes are still very fresh in my mind and I am unaffected by rose tinted nostalgia.\n\nI&apos;ve just watched episode 1 of House of the Dragon.\n\nHow can I sum it up? So far, so good.\n\nThe music is sufficiently different to be fresh while remaining recognizable. The production quality and cinematography are as expected - fantastic, epic and awe inspiring, aside from a couple of excessively dark scenes that were over and done with very quickly.\n\nThere is gore aplenty. Nudity, vomit, sex and depravity. Incidental background humor. A promise of things to come.\n\nThe casting seems to be on point - I saw no issue with any of the characters, and the leads were well chosen for their roles.\n\nThe writing seems to be up to par. As an introduction, this episode was written and directed well. I want to see and know more - a good sign.\n\nSo far I&apos;m pleased with this return to the land of Westeros. Valar morghulis!",
    "reviewRating": {
      "worstRating": 1,
      "bestRating": 10,
      "ratingValue": 9
    }
  },
  "rating": {
    "ratingCount": 77710,
    "bestRating": 10,
    "worstRating": 1,
    "ratingValue": 8.8
  },
  "contentRating": "A",
  "genre": ["Action","Adventure","Drama"],
  "datePublished": "2022-08-22",
  "keywords": "kingdom,prequel,knight,castle,sword",
  "duration": null,
  "actor": [
    {
      "name": "Paddy Considine",
      "url": "/name/nm0175916/"
    },
    {
      "name": "Matt Smith",
      "url": "/name/nm1741002/"
    },
    {
      "name": "Rhys Ifans",
      "url": "/name/nm0406975/"
    }
  ],
  "director": [],
  "creator": [
    {
      "name": "Ryan J. Condal",
      "url": "/name/nm2952284/"
    },
    {
      "name": "George R.R. Martin",
      "url": "/name/nm0552333/"
    }
  ]
}
>>> 

```
**2) Getting a file Info by it's IMDB ID :-**

Use ```get_by_id(<ID>)``` method to get a file information by it's IMDB ID.
```python
>>> from PyMovieDb import IMDB
>>> imdb = IMDB()
>>> res = imdb.get_by_id("tt12593682")
>>> print(res)
>>> {
  "type": "Movie",
  "name": "Bullet Train",
  "url": "https://www.imdb.com/title/tt12593682/",
  "poster": "https://m.media-amazon.com/images/M/MV5BMDU2ZmM2OTYtNzIxYy00NjM5LTliNGQtN2JmOWQzYTBmZWUzXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_.jpg",
  "description": "Five assassins aboard a fast moving bullet train find out their missions have something in common.",
  "review": {
    "author": "jonny_mcclatch",
    "dateCreated": "2022-08-03",
    "inLanguage": "English",
    "heading": "Stupid Fun...",
    "reviewBody": "I&apos;ll admit i&apos;ve skewed my rating a bit, i&apos;ve ranked it so highly rated based on the fact I knew what movie I was buying a ticket for. I&apos;m not rating it highly because it&apos;s a modern classic, i&apos;m doing it based on wanting to see a funny and entertaining action movie and in that respect it delivers pretty much everything I went to the cinema for.\n\nThe premise of the film is basic, the cast is solid, the characters are excellent including mini side characters. The humour has a few misses but generally it is a pretty funny movie throughout, they also pay off everything that is set up along the way which makes it a satisfying watch. Also if you are yet to see it, stay through the credits as it does tie up one or two of those loose ends.\n\nThe slight downside for me, were that the run time does sag a little toward the end but it is over 2 hours long and otherwise moved along at a steady rate.",
    "reviewRating": {
      "worstRating": 1,
      "bestRating": 10,
      "ratingValue": 9
    }
  },
  "rating": {
    "ratingCount": 67632,
    "bestRating": 10,
    "worstRating": 1,
    "ratingValue": 7.5
  },
  "contentRating": "A",
  "genre": [
    "Action",
    "Comedy",
    "Thriller"
  ],
  "datePublished": "2022-08-04",
  "keywords": "train,japan,assassin,revenge,mount fuji",
  "duration": "PT2H7M",
  "actor": [
    {
      "name": "Brad Pitt",
      "url": "/name/nm0000093/"
    },
    {
      "name": "Joey King",
      "url": "/name/nm1428821/"
    },
    {
      "name": "Aaron Taylor-Johnson",
      "url": "/name/nm1093951/"
    }
  ],
  "director": [
    {
      "name": "David Leitch",
      "url": "/name/nm0500610/"
    }
  ],
  "creator": [
    {
      "name": "Zak Olkewicz",
      "url": "/name/nm5599654/"
    },
    {
      "name": "K\u00f4tar\u00f4 Isaka",
      "url": "/name/nm2157655/"
    }
  ]
}
```

**3) Searching on IMDB :-**

* Use ```search(<name>, year=None, tv=False, person=False)``` method to search a file/movie/tv on IMDB.

* ```year``` ```tv``` & ```person``` are **Optional args.
* ```tv=True``` will return only Tv Series search results.
* ```person=True``` will return only people profile results. Use this if you are searching a celebrity info.

_**Recommendation -** Pass ```year``` argument to increase the accuracy to hit requested file._

```python
>>> from PyMovieDb import IMDB
>>> imdb = IMDB()
>>> res = imdb.search('liger', year=2022)
>>> print(res)
>>> {
  "result_count": 6,
  "results": [
    {
      "id": "tt4435072",
      "name": "Liger (2022)",
      "url": "https://www.imdb.com/title/tt4435072/?ref_=fn_al_tt_1",
      "poster": "https://m.media-amazon.com/images/M/MV5BOGFjYjFhMGUtZDE3Mi00OGE0LWI4YjUtZmRhZGEyYzliMWJmXkEyXkFqcGdeQXVyMTUzOTcyODA5._V1_UX32_CR0,0,32,44_AL_.jpg"
    },
    {
      "id": "tt18924468",
      "name": "Message and the Messenger 2022",
      "url": "https://www.imdb.com/title/tt18924468/?ref_=fn_al_tt_2",
      "poster": "https://m.media-amazon.com/images/M/MV5BZjBlYzBjN2ItNWVmMi00YjRjLWExMGItMzBiZmY4ODU0N2I1XkEyXkFqcGdeQXVyMTAxMDI5ODc5._V1_UX32_CR0,0,32,44_AL_.jpg"
    },
    {
      "id": "tt21027022",
      "name": "Football Manager 2022 (2021) (Video Game)",
      "url": "https://www.imdb.com/title/tt21027022/?ref_=fn_al_tt_7",
      "poster": "https://m.media-amazon.com/images/M/MV5BZTg4YWVmNDctMjIxNi00YmM4LThhMWYtY2Q2YWQ1OTZkNTgyXkEyXkFqcGdeQXVyNzcwNzU5MTE@._V1_UY44_CR0,0,32,44_AL_.jpg"
    },
    {
      "id": "tt19832702",
      "name": "21. apr. 2022 - Vestlige ledere i Kyiv (2022) (TV Episode) - Dagsrevyen (1958) (TV Series)",
      "url": "https://www.imdb.com/title/tt19832702/?ref_=fn_al_tt_8",
      "poster": "https://m.media-amazon.com/images/M/MV5BZDdkYjE1ZTYtYzY0NC00ZTQ4LTg3ZTUtYTg2Y2FiYzYyMWQxXkEyXkFqcGdeQXVyODI4NDE1MDk@._V1_UY44_CR23,0,32,44_AL_.jpg"
    },
    {
      "id": "tt21866526",
      "name": "8. aug. 2022 - Budrunder pa leieboliger (2022) (TV Episode) - Dagsrevyen (1958) (TV Series)",
      "url": "https://www.imdb.com/title/tt21866526/?ref_=fn_al_tt_9",
      "poster": "https://m.media-amazon.com/images/M/MV5BZDdkYjE1ZTYtYzY0NC00ZTQ4LTg3ZTUtYTg2Y2FiYzYyMWQxXkEyXkFqcGdeQXVyODI4NDE1MDk@._V1_UY44_CR23,0,32,44_AL_.jpg"
    },
    {
      "id": "tt20898300",
      "name": "25. mai 2022 - Billigere enn pa lenge (2022) (TV Episode) - Kveldsnytt (1965) (TV Series)",
      "url": "https://www.imdb.com/title/tt20898300/?ref_=fn_al_tt_10",
      "poster": "https://m.media-amazon.com/images/M/MV5BMmY0ZjAzZDktNGJmZi00NzdiLWEwODItOTcxZDIyZGI3OTM5XkEyXkFqcGdeQXVyMzkyNTYxMjE@._V1_UY44_CR23,0,32,44_AL_.jpg"
    }
  ]
}
```

**4) Getting a Person/Celebrity Profile Information:-**

* Use ```person_by_name(<name>)``` method to get profile info by name from IMDB.
* Use ```person_by_id(<IMDB_ID>)``` method to get profile info by it's ID.


```python
>>> from PyMovieDb import IMDB
>>> imdb = IMDB()
>>> res = imdb.person_by_name('Rajkummar Rao') #OR imdb.person_by_id("nm3822770")
>>> print(res)
>>> {
    "url": "/name/nm3822770/",
    "name": "Rajkummar Rao",
    "image": "https://m.media-amazon.com/images/M/MV5BMzAxNWIzOWItMDM1NC00NGMyLWIwMDEtNWZjODEyOTFiZjQ4XkEyXkFqcGdeQXVyNjY1MTg4Mzc@._V1_.jpg",
    "jobTitle": "Actor",
    "description": "Raj Kumar is also known as Rajkummar Rao. He was born in Gurgaon. He finished his schooling in Gurgaon and graduated in Arts from Delhi University. He was simultaneously doing theatre with Kshitij Repertory and SRC in Delhi. He is an Acting graduate from Pune's Film and Television Institute of India. Raj Kumar's debut film was Dibakar Banerjee's ...",
    "birthDate": "1984-08-31",
    "type": "Person"
    }
>>> 
```

## Other Useful Methods:
* #### Get Upcoming Movies List :

```python
from PyMovieDb import IMDB
imdb = IMDB()
res = imdb.upcoming(region=None)
# returns upcomming movies info as json
```
```region``` is an **Optional argument. Use country ISO codes (eg. IN/US/DE/AE etc.)
to filter results for a particular region.
* #### Getting Popular Movies List by Genre :
The ```popular_movies()``` method will return 50 popular movies results starting from ```start_id``` 
```python
from PyMovieDb import IMDB
imdb = IMDB()
res = imdb.popular_movies(genre=None, start_id=1, sort_by=None)
# returns top 50 popular movies starting from start id
```
```genre, start_id & sort_by``` are **Optional args

To see ```sort_by``` options visit [Movies by genre - IMDB](https://www.imdb.com/search/title/?genres=sci-fi&explore=title_type,genres)

* #### Getting Popular TV Series List by Genre :
The ```popular_tv()``` method will return 50 popular TV-Series starting from ```start_id``` 
```python
from PyMovieDb import IMDB
imdb = IMDB()
res = imdb.popular_tv(genre=None, start_id=1, sort_by=None)
# returns top 50 popular TV Series starting from start id
```
```genre, start_id & sort_by``` are **Optional args

To see ```sort_by``` options visit [TV Series by genre - IMDB](https://www.imdb.com/search/title/?title_type=tv_series,tv_miniseries&genres=action&view=advanced)

## Disclaimer
The PyMovieDb is tested with small amount of data found on [IMDB.com](https://www.imdb.com).
This package is developed for educational purpose only. The author does not encourage anyone to 
use this module for any illegal or un-ethical project/purpose.





