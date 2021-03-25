# pymdb
Python  script to scrape data from IMDb Top250 (www.imdb.com/chart/top) and parse xml of movie data from OMDb API (www.omdbapi.com)

## Installation and Usage
`$ git clone https://github.com/kaushiksk/pymdb.git && cd pymdb`

`$ python setup.py install`
   
## Functions
    top250_id()
        Pulls out ImDb Title ID's from the Imdb Top 250 webpage and adds them to a list.
        Returns List
    
    top250_yearcount()
        Creates a dictionary of number of movies of a particular year in the Imdb Top 250.
        Returns a dictionary
    
    top_250()
        Pulls out movie names from the Imdb Top 250 webpage and adds them to a dictionary with its position.
        Returns dictionary
    
    years_top250()
            Creates a dictionary of year of the movies of the top 250 in the order of ranking.
        Returns  dictionary
        

## Using the Movie and MovieId Class
    Initialise:
```python
   >>> m = pymdb.Movie(API_KEY, "The Shawshank Redemption")
   >>> m = pymdb.Movie(API_KEY, "The Shawshank Redemption",1994)
   >>> m = pymdb.MovieId(API_KEY, "tt0111161")
```

    Get info about movie:
```python
   >>> m.year()
   1994
   >>> m.director()
   ['Frank Darabont'] 
   >>> m.getposter()
   Poster saved to The Shawshank Redemption.jpg
   >>m.info()
   The Shawshank Redemption
   Year:  1994                                                                                          
   Rating: 9.3 (1,886,223 votes)
   Language:  English
   Genre:  Crime, Drama
   Director:  Frank Darabon
   Awards:  Nominated for 7 Oscars. Another 19 wins & 29 nominations.

```

      type help(pymdb.Movie) for more.

## Example script: Search for a movie and get info
```python
  >>> from pymdb import Movie, MovieId
  >>> Movie.search(API_KEY, "Amelie")
  Amélie (2001) [tt0211915] {movie} 
  Amelie rennt (2017) [tt5712474] {movie}
  Liebe Amelie (2005) [tt0469116] {movie}
  .
  .
  .
  Ta hand om Amelie (1964) [tt0242926] {movie} 
  Found total 10 matching results
  >>> m = MovieId(API_KEY, 'tt0211915')
  >>> m.info()
  Amélie
  Year:  2001
  Rating: 8.3 (592,382 votes)
  Language:  French, Russian, English
  Genre:  Comedy, Romance
  Director:  Jean-Pierre Jeunet
  Awards:  Nominated for 5 Oscars. Another 58 wins & 65 nominations.
  ```
  
## Example script: Download posters of all movies in IMDb Top250.
    
```python
    import pymdb
    ids = pymdb.top250_id()
    for id in ids:
      m = pymdb.MovieId(API_KEY, id)
      m.getposter()
```

## Bugs
Report any bugs you find at https://github.com/kaushiksk/pymdb/issues.

## Note
Data is fetched from [OMDb API](https://omdbapi.com) to which I am in no way associated. Please be patient if the server is down.
Get your own API Key from OMDbAPI.
