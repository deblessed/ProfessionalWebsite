import cherrypy
from common.common import get_server_root
from src.page import Page
from util.file_reader import read_file

__author__ = 'Jon'

class Home(Page):
    """
        The page object for the homepage.
    """

    def main_content(self):
        """
            Return the central HTML content of this page
        """
        return read_file("content/pages/home.html")

    def title(self):
        return "Jon Tedesco &#183; Home"


    def sidebar(self):
        """
            Get the sidebar code (traditionally the contact information)
        """
        return read_file("content/sidebar.html") % "home"

    @cherrypy.expose
    def index(self):
        """
            Returns the content of this page
        """
        self.build_content()
        return self.content

