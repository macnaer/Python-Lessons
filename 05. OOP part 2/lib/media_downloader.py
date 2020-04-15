from subprocess import call
import os
if __name__ == "__main__":
    dowanloadr


class dowanloadr():
    def menu(self):
        choice = int(
            input("1. Youtube single movie\n2.Youtube playlist\n0. Exit\n====>>> "))
        return choice

    def download_youtube_single_media(self):
        movie_url = input("Enter mouve URL => ")
        movie_info = "youtube-dl " + movie_url + " -F"
        call(movie_info, shell=False)
        format = input("Enter Format code : ")
        os.chdir("Downloads")
        download_command = "youtube-dl -f " + format + " " + movie_url + " -c"
        call(download_command, shell=False)
