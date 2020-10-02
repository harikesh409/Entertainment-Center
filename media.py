import webbrowser

class Movie():
    """ This class provides a way to store movie related information """
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline

        if poster_image == None:
            self.poster_image_url = 'https://us.123rf.com/450wm/sabelskaya/sabelskaya2009/sabelskaya200900867/154940163-stock-vector-poster-for-the-children-cinema-boy-in-3d-glasses-watch-a-movie-childrens-movie-party-colorful-flat-v.jpg?ver=6'
        else:
            self.poster_image_url = poster_image
            
        self.trailer_youtube_id = trailer_youtube
    def show_trailer(self):
        webbrowser.open("https://www.youtube.com/watch?v="+self.trailer_youtube_id)