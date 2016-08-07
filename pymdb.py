import string
import urllib
import re
import xml.etree.ElementTree as ET


def top_250():
    """Pulls out movie names from the Imdb Top 250 webpage and adds them to a dictionary with its position.
    Returns dictionary"""

    movielist=dict()
    i=1
    url='http://www.imdb.com/chart/top'
    file= urllib.urlopen(url).read()
    link = re.findall('title=".*?dir.*?>(.*?)</a>',file)
    for links in link:
        
        movielist[i]=links
        i+=1
    return movielist

def top250_yearcount():
    """Creates a dictionary of number of movies of a particular year in the Imdb Top 250.
    Returns a dictionary"""

    i=1
    yearcount=dict()
    
    url='http://www.imdb.com/chart/top'
    file= urllib.urlopen(url).read()

            
         
    years = re.findall('secondaryInfo">\((.*?)\)</span>',file)
    for year in years:
        
        yearcount[year] = yearcount.get(year,0) + 1
    return yearcount


def years_top250() :
    """Creates a dictionary of year of the movies of the top 250 in the order of ranking.
    Returns  dictionary"""

    i=1
    year250=dict()
    
    url='http://www.imdb.com/chart/top'
    file= urllib.urlopen(url).read()

            
         
    years = re.findall('secondaryInfo">\((.*?)\)</span>',file)
    for year in years:
        year250[i]=year
        i+=1
    return year250

def top250_id() :
    """Pulls out ImDb Title ID's from the Imdb Top 250 webpage and adds them to a list.
    Returns List"""

    

    
    movielist= []

   

    url2='http://www.imdb.com/chart/top'
    file= urllib.urlopen(url2).read()
    links = re.findall('<div class=".*?tconst="(.*?)"></div>',file)


    for link in links:
        movielist.append(link)
    return movielist

class Movie():
    """Enter movie title as parameter. Year is an optional argument"""
    def __init__(self, title,year=None):
        """Fetches XML for given Movie from omdbapi.com"""
        serviceurl = 'http://www.omdbapi.com/?'
	url = serviceurl+urllib.urlencode({'t':title,
                                           'type':'movie',
                                           'y':year,
                                           'plot':'short',
                                           'tomatoes':'true',
                                           'r':'xml'})
        data = urllib.urlopen(url)
        input = data.read()
        self.stuff = ET.fromstring(input)


    def info(self):
        """Prints basic Info from IMDb"""
        print self.stuff.find('movie').get("title")
        print "Year: ", self.stuff.find('movie').get("year")
        print "Rating: ", self.stuff.find('movie').get("imdbRating")
        print "Language: ", self.stuff.find('movie').get("language")
        print "Genre: ", self.stuff.find('movie').get("genre")
        print "Director: ", self.stuff.find('movie').get("director")
        print "Awards: ", self.stuff.find('movie').get("awards")

    def tomatoes(self):
        """Prints Rotten Tomatoes Info"""
        print "Rotten Tomatoes Info: \n"
        print self.stuff.find('movie').get("title")
        print "TomatoMeter: ", self.stuff.find('movie').get("tomatoMeter"), "%"
        print "Critic Consensus: ", self.stuff.find('movie').get("tomatoConsensus")
        print "Audience Score: ", self.stuff.find('movie').get("tomatoUserMeter"), "%"
        print "For more visit: ", self.stuff.find('movie').get("tomatoeURL")

    def getposter(self):
        """Saves poster of movie in current directory.
        To check current directort type 'os.getcwd()'
        To change current directory type 'os.chdir('path you wish')'
        """
        link= self.stuff.find('movie').get('poster')
        image= urllib.urlopen(link).read()
        outfile = open('%s.jpg'%self.stuff.find('movie').get("title").translate(None,string.punctuation),'wb')
        outfile.write(image)
        outfile.close()

    def year(self):
        """Prints Year of Movie"""
        return int(self.stuff.find('movie').get("year"))

    def rating(self):
        """Prints IMDb and RT ratings"""
        return float(self.stuff.find('movie').get("imdbRating"))
        
    def RTrating(self):
        return float(self.stuff.find('movie').get("tomatoMeter"))
    
    def director(self):
        """Print Name of Director"""
        return  self.stuff.find('movie').get("director")

    def actors(self):
        """Prints premier cast"""
        print  self.stuff.find('movie').get("actors")

    def plot(self):
        """Prints Short Plot"""
        print self.stuff.find('movie').get("plot")
        print "For more visit: ", self.stuff.find('movie').get("tomatoeURL")
        print "http://www.imdb.com/title/%s"% self.stuff.find('movie').get("imdbID")

    def awards(self):
        print  self.stuff.find('movie').get("awards")

    def reviews(self):
        """Prints Rotten Tomatoes Critics Consensus"""
        print  self.stuff.find('movie').get("tomatoConsensus")
        print "For more visit: ", self.stuff.find('movie').get("tomatoeURL")
        print "http://www.imdb.com/title/%s/reviews?ref_=tt_ov_rt"% self.stuff.find('movie').get("imdbID")


class MovieId(Movie):
    """Takes IMDb ID as parameter instead of title"""
    def __init__(self,id):
        url=urllib.urlopen("http://www.omdbapi.com/?i=%s&y=&plot=short&r=xml"% id)
        input=url.read()
        self.stuff = ET.fromstring(input)
    def title(self):
        return  self.stuff.find('movie').get("title")
