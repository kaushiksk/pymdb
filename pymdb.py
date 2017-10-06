import string
import urllib
import re
import xml.etree.ElementTree as eT
import json


def top_250():
    """
    Pulls out IMDb Top 250 movies names.
    :return: dictionary
    """

    url = 'http://www.imdb.com/chart/top'
    try:
        raw_file = urllib.urlopen(url).read()
        titles = re.findall('title=".*?dir.*?>(.*?)</a>', raw_file)
        return {i: title for i, title in enumerate(titles, 1)}
    except EnvironmentError:
        print "NetWorkError: [Please make sure you are connected to internet]"
        return {}


def top250_year_count():
    """
    Pulls out number of movies of a particular year in the IMDb Top 250
    :return: dictionary
    """

    year_count = {}

    url = 'http://www.imdb.com/chart/top'
    try:
        raw_file = urllib.urlopen(url).read()
        years = re.findall('secondaryInfo">\((.*?)\)</span>', raw_file)
        for year in years:import string
import urllib
import re
import xml.etree.ElementTree as eT


def top_250():
    """
    Pulls out IMDb Top 250 movies names.
    :return: dictionary
    """

    url = 'http://www.imdb.com/chart/top'
    try:
        raw_file = urllib.urlopen(url).read()
        titles = re.findall('title=".*?dir.*?>(.*?)</a>', raw_file)
        return {i: title for i, title in enumerate(titles, 1)}
    except EnvironmentError:
        print "NetWorkError: [Please make sure you are connected to internet]"
        return {}


def top250_year_count():
    """
    Pulls out number of movies of a particular year in the IMDb Top 250
    :return: dictionary
    """

    year_count = {}

    url = 'http://www.imdb.com/chart/top'
    try:
        raw_file = urllib.urlopen(url).read()
        years = re.findall('secondaryInfo">\((.*?)\)</span>', raw_file)
        for year in years:
            year_count[year] = year_count.get(year, 0) + 1
        return year_count
    except EnvironmentError:
        print "NetWorkError: [Please make sure you are connected to internet]"
        return year_count


def years_top250():
    """
    Pulls out IMDb Top 250 movies years
    :return: dictionary
    """

    url = 'http://www.imdb.com/chart/top'
    try:
        raw_file = urllib.urlopen(url).read()
        years = re.findall('secondaryInfo">\((.*?)\)</span>', raw_file)
        return {i: year for i, year in enumerate(years, 1)}
    except EnvironmentError:
        print "NetWorkError: [Please make sure you are connected to internet]"
        return {}


def top250_id():
    """
    Pulls out IMDb Top 250 movies IDs
    :return: list
    """

    url2 = 'http://www.imdb.com/chart/top'
    try:
        raw_file = urllib.urlopen(url2).read()
        return re.findall('<div class=".*?tconst="(.*?)" data-recordmetrics="true"></div>', raw_file)
    except EnvironmentError:
        print "NetWorkError: [Please make sure you are connected to internet]"
        return []


class Movie:
    """Enter movie title as parameter. Year is an optional argument"""

    def __init__(self, title, year=None):
        """Fetches XML for given Movie from omdbapi.com"""
        service_url = 'http://www.omdbapi.com/?'
        url = service_url + urllib.urlencode({'t': title, 'type': 'movie', 'y': year, 'plot': 'short',
                                              'tomatoes': 'true', 'r': 'xml'})
        try:
            data = urllib.urlopen(url)
            url_input = data.read()
            self.stuff = eT.fromstring(url_input)
        except EnvironmentError:
            print "NetWorkError: [Please make sure you are connected to internet]"
            exit()

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

    def get_poster(self):
        """Saves poster of movie in current directory or raise exception if anything goes wrong
        To check current directort type 'os.getcwd()'
        To change current directory type 'os.chdir('path you wish')'
        """
        try:
            link = self.stuff.find('movie').get('poster')
            image = urllib.urlopen(link).read()
            outfile = open('%s.jpg' % self.stuff.find('movie').get("title").translate(None, string.punctuation), 'wb')
            outfile.write(image)
            outfile.close()
        except AttributeError:
            print "Error: [ Something went wrong while downloading image, Did you entered correct name or ID ]"
        except IOError:
            print "IOError: [ No such Image Exist ]"

    def year(self):
        """
        :return: Year of Movie
        """
        return int(self.stuff.find('movie').get("year"))

    def rating(self):
        """
        :return: IMDb rating
        """
        return float(self.stuff.find('movie').get("imdbRating"))

    def rt_rating(self):
        """
        :return: Rotten tomatoes rating
        """
        return float(self.stuff.find('movie').get("tomatoMeter"))

    def director(self):
        """
        :return: list of Name of Directors of movie
        """
        return map(str, self.stuff.find('movie').get("director").split(","))

    def actors(self):
        """
        :return: list of Name of Cast in movie
        """
        return map(str, self.stuff.find('movie').get("actors").split(","))

    def plot(self):
        """Prints Short Plot"""
        print self.stuff.find('movie').get("plot")
        print "For more visit:\n ", self.stuff.find('movie').get("tomatoeURL")
        print "http://www.imdb.com/title/%s" % self.stuff.find('movie').get("imdbID")

    def awards(self):
        """
        :return: rewards earned by the movie
        """
        return self.stuff.find('movie').get("awards")

    def reviews(self):
        """Prints Rotten Tomatoes Critics Consensus"""
        print self.stuff.find('movie').get("tomatoConsensus")
        print "For more visit: ", self.stuff.find('movie').get("tomatoeURL")
        print "http://www.imdb.com/title/%s/reviews?ref_=tt_ov_rt" % self.stuff.find('movie').get("imdbID")


class MovieId(object, Movie):
    """Takes IMDb ID as parameter instead of title"""

    def __init__(self, movie_id):
        super(MovieId, self).__init__()
        try:
            url = urllib.urlopen("http://www.omdbapi.com/?i=%s&y=&plot=short&r=xml" % movie_id)
            url_input = url.read()
            self.stuff = eT.fromstring(url_input)
        except EnvironmentError:
            print "NetWorkError: [Please make sure you are connected to internet]"
            exit()

    def title(self):
        """
        :return: Title of movie which has this particular id on IMDb
        """
        return self.stuff.find('movie').get("title")

            year_count[year] = year_count.get(year, 0) + 1
        return year_count
    except EnvironmentError:
        print "NetWorkError: [Please make sure you are connected to internet]"
        return year_count


def years_top250():
    """
    Pulls out IMDb Top 250 movies years
    :return: dictionary
    """

    url = 'http://www.imdb.com/chart/top'
    try:
        raw_file = urllib.urlopen(url).read()
        years = re.findall('secondaryInfo">\((.*?)\)</span>', raw_file)
        return {i: year for i, year in enumerate(years, 1)}
    except EnvironmentError:
        print "NetWorkError: [Please make sure you are connected to internet]"
        return {}


def top250_id():
    """
    Pulls out IMDb Top 250 movies IDs
    :return: list
    """

    url2 = 'http://www.imdb.com/chart/top'
    try:
        raw_file = urllib.urlopen(url2).read()
        return re.findall('<div class=".*?tconst="(.*?)"></div>', raw_file)
    except EnvironmentError:
        print "NetWorkError: [Please make sure you are connected to internet]"
        return []


class Movie:
    """Enter movie title as parameter. Year is an optional argument"""

    def __init__(self, title, year=None):
        """Fetches XML for given Movie from omdbapi.com"""
        service_url = 'http://www.omdbapi.com/?'
        url = service_url + urllib.urlencode({'t': title, 'type': 'movie', 'y': year, 'plot': 'short',
                                              'tomatoes': 'true', 'r': 'json'})
        try:
            self.stuff = json.loads(urllib.urlopen(url).read())
        except EnvironmentError:
            print "NetWorkError: [Please make sure you are connected to internet]"
            exit()

    def info(self):
        """Prints basic Info from IMDb"""
        print str(self.stuff['Title'].encode('ascii', 'ignore'))
        print "Year: ", str(self.stuff['Year'].encode('ascii', 'ignore'))
        print "Rating: ", str(self.stuff['imdbRating'].encode('ascii', 'ignore'))
        print "Language: ", str(self.stuff['Language'].encode('ascii', 'ignore'))
        print "Genre: ", str(self.stuff['Genre'].encode('ascii', 'ignore'))
        print "Director: ", str(self.stuff['Director'].encode('ascii', 'ignore'))
        print "Awards: ", str(self.stuff['Awards'].encode('ascii', 'ignore'))

    def tomatoes(self):
        """Prints Rotten Tomatoes Info"""
        print "Rotten Tomatoes Info: \n"
        print str(self.stuff['Title'])
        print "TomatoMeter: ", float(self.stuff['tomatoMeter']), "%"
        print "Critic Consensus: ", str(self.stuff['tomatoConsensus'].encode('ascii', 'ignore'))
        print "Audience Score: ", str(self.stuff['tomatoUserMeter'].encode('ascii', 'ignore')), "%"
        print "For more visit: ", str(self.stuff['tomatoURL'].encode('ascii', 'ignore'))

    def get_poster(self):
        """Saves poster of movie in current directory or raise exception if anything goes wrong
        To check current directort type 'os.getcwd()'
        To change current directory type 'os.chdir('path you wish')'
        """
        try:
            link = str(self.stuff['Poster'])
            image = urllib.urlopen(link).read()
            outfile = open('%s.jpg' % str(self.stuff['Title'].encode('ascii', 'ignore')).translate(None, string.punctuation), 'wb')
            outfile.write(image)
            outfile.close()
        except AttributeError:
            print "Error: [ Something went wrong while downloading image, Did you entered correct name or ID ]"
        except IOError:
            print "IOError: [ No such Image Exist ]"

    def year(self):
        """
        :return: Year of Movie
        """
        return int(self.stuff['Year'])

    def rating(self):
        """
        :return: IMDb rating
        """
        return float(self.stuff['imdbRating'])

    def rt_rating(self):
        """
        :return: Rotten tomatoes rating
        """
        return float(self.stuff['tomatoRating'])

    def director(self):
        """
        :return: list of Name of Directors of movie
        """
        return map(str, self.stuff['Director'].encode('ascii', 'ignore').split(","))

    def actors(self):
        """
        :return: list of Name of Cast in movie
        """
        return map(str, self.stuff['Actors'].encode('ascii', 'ignore').split(","))

    def plot(self):
        """Prints Short Plot"""
        print str(self.stuff['Plot'].encode('ascii', 'ignore'))
        print "For more visit:\n ", str(self.stuff['tomatoURL'].encode('ascii', 'ignore'))
        print "http://www.imdb.com/title/%s" % str(self.stuff['imdbID'].encode('ascii', 'ignore'))

    def awards(self):
        """
        :return: rewards earned by the movie
        """
        return str(self.stuff['Awards'])

    def reviews(self):
        """Prints Rotten Tomatoes Critics Consensus"""
        print str(self.stuff['tomatoConsensus'].encode('ascii', 'ignore'))
        print "For more visit: ", str(self.stuff['tomatoURL'].encode('ascii', 'ignore'))
        print "http://www.imdb.com/title/%s/reviews?ref_=tt_ov_rt" % str(self.stuff['imdbID'].encode('ascii', 'ignore'))


class MovieId(object, Movie):
    """Takes IMDb ID as parameter instead of title"""

    def __init__(self, movie_id):
        super(MovieId, self).__init__()
        try:
            raw_page = urllib.urlopen("http://www.omdbapi.com/?i=%s&y=&plot=short&r=json" % movie_id)
            self.stuff = json.loads(raw_page.read())
            if str(self.stuff['Response']) == 'False':
                print "Error: [  Please enter correct IMDB ID ]"
                exit()
            else:
                print "I came here"
                pass

        except EnvironmentError:
            print "NetWorkError: [Please make sure you are connected to internet]"
            exit()

    def title(self):
        """
        :return: Title of movie which has this particular id on IMDb
        """
        return str(self.stuff['Title'].encode('ascii', 'ignore'))
