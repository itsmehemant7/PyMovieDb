from imdb import IMDB


name = "Skyscraper"
imdb = IMDB()

# m1 = i.search(name,year=2018)
# print(m1)

# res = imdb.get_by_name('Reacher', tv=True)
res = imdb.get_by_id("tt12593682")
# res = imdb.search('liger', year=2022)
# res = imdb.person_by_name('Rajkummar Rao')
# res = imdb.person_by_id("nm3822770")
# res = imdb.upcoming(region=None)
# res = imdb.popular_movies(genre=None, start_id=1, sort_by=None)
# res = imdb.popular_tv(genre=None, start_id=1, sort_by=None)
print(res)



