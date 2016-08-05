import webbrowser

class Movie():
    '''
    	this is a movie class which has movie_tittle, movie_storyline, poster_image 
    	and trailer_youtube as attributes, and has a internal function called show_trailer
    	to open the movie trail when it's called
    '''

    VALID_RATINGS = ['G','PG','PG-13','R']

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
