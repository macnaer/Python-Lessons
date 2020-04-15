from lib.media_downloader import dowanloadr

media_file = dowanloadr()

exit = False
while not exit:
    choice = media_file.menu()
    if choice == 1:
        media_file.download_youtube_single_media()
    elif choice == 2:
        print("User choice => ", choice)
    elif choice == 0:
        exit = True
        print("Bye!")
    else:
        print("R.T.F.M.")
