import webbrowser


class Movie():
    """ class provides a way to store movie related info
        an init method to create movie with title, image
        url and youtube trailer url.
        show triler opens the youtube link """

    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
