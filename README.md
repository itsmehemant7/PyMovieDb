
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
PyMovieDb is available on [pypi](https://pypi.org/project/PyMovieDb/). 
Use ```pip``` to install the module from pypi

```pip install PyMovieDb```


## Documentation 

**_NOTE: The API will return data as JSON not dict_**

**1) Getting a Movie/Tv-Series info :-**

Use ``` get_by_name(<name>, tv=False) ``` method to get information of a movie/TV-Series.

The ``` tv ``` is an optional argument, if ``` tv=True``` it will get data from ```TV Series``` files only.

On the other hand, if ```tv=False``` (default), it will find your file in ```Movies + TV Series``` results
```python
>>> from PyMovieDb import IMDB
>>> imdb = IMDB()
>>> res = imdb.get_by_name('Reacher', tv=True)
>>> print(res)
>>> {
  "type": "TVSeries",
  "name": "Reacher",
  "url": "https://www.imdb.com/tt9288030/",
  "poster": "https://m.media-amazon.com/images/M/MV5BOWRiZjYwZjUtYmIwMy00ZDUzLTk2NjktZmJkZjRkNjU0MDE3XkEyXkFqcGdeQXVyMDM2NDM2MQ@@._V1_.jpg",
  "description": "Jack Reacher was arrested for murder and now the police need his help. Based on the books by Lee Child.",
  "review": {
    "author": "TxMike",
    "dateCreated": "2022-02-07",
    "inLanguage": "English",
    "heading": "Jack Reacher, never looks for a fight but then never backs down from one.",
    "reviewBody": "New TV series streaming from Amazon, my wife and I watched two episodes on each of four successive nights. Sort of like movie nights. This is not high art, the writing has lots of humor, in real life Reacher couldn&apos;t get away with everything depicted. BUT ... it is a very entertaining series. Especially for those of us who enjoy seeing a smart, mild-mannered, well-spoken, well-trained, big tough guy put the bad guys in their places. Some simple thugs, some unruly prison inmates, some dirty cops. Ritchson is a r real good pick for the role. (In an interview he said he gained 30 pounds for the role.)\n\nReacher is an ex-military man, he takes a bus to the small Georgia town, walks to town to look up an old blues singer&apos;s home, immediately gets arrested for murder, but eventually works with local law enforcement to help solve the mysteries, and there are several.\n\nMost episodes are roughly 45 to 50 minutes long, set in a fictional Georgia town not far from Atlanta. Cast and characters are interesting. The story is not too deep but surprisingly interesting, just good entertainment. Streaming on Amazon.",
    "reviewRating": {
      "worstRating": null,
      "bestRating": null,
      "ratingValue": null
    }
  },
  "rating": {
    "ratingCount": 155124,
    "bestRating": 10,
    "worstRating": 1,
    "ratingValue": 8.1
  },
  "contentRating": "A",
  "genre": [
    "Action",
    "Crime",
    "Drama"
  ],
  "datePublished": "2022-02-04",
  "keywords": "jack reacher character,reboot,reboot of series,based on book series,assassin",
  "duration": null,
  "actor": [
    {
      "name": "Alan Ritchson",
      "url": "https://www.imdb.com/name/nm2024927/"
    },
    {
      "name": "Maria Sten",
      "url": "https://www.imdb.com/name/nm3080233/"
    },
    {
      "name": "Malcolm Goodwin",
      "url": "https://www.imdb.com/name/nm0329511/"
    }
  ],
  "director": [],
  "creator": [
    {
      "name": "Nick Santora",
      "url": "https://www.imdb.com/name/nm1238801/"
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





