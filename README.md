# pymdb
Python  script to scrape data from IMDb Top250 (www.imdb.com/chart/top) and parse xml of movie data from OMDb API (www.omdbapi.com)

##Installation
Download the pymdb.py script into your Python27 folder and import it in your scripts.

##Usage
Put the source in the folder where you want to use it.
    import pymdb
   
##Functions
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
        
##Using the Movie and MovieId Class
    Initialise:
      m = pymdb.Movie("The Shawshank Redemption")
      m = pymdb.Movie("The Shawshank Redemption",1994)
      m = pymdb.MovieId("tt0111161")
  
    Use Class functions:
      m.year()
      m.director()
      m.getposter()
      .
      .
      type help(pymdb.Movie) for more.
  
  
##Example script: Download posters of all movies in IMDb Top250.
    
    import pymdb
    ids = pymdb.top250_id()
    for id in ids:
      m = pymdb.MovieId(id)
      m.getposter()


P.S. The Movie class works for any movie. It doesn't have to be in the Top 250.
