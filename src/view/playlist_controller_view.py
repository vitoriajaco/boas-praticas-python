import os

class PlaylistCreatorView:
    def playlist_creator_sucess(self, controller_response) -> None:
        self.__clear()
        print('Playlist criada com sucesso! \n \n')

        for music in controller_response["playlist"]:
            message = (
                f"Título da música: {music.title}\n"
                f"Artista: {music.artist}\n"
                f"Ano de publicação: {music.year}\n"
            )
            print(message)


    def playlist_creator_fail(self, controller_response) -> None:
        self.__clear()
        message = (
            "Playlist criada com falha\n\n"
            f"* Error: {controller_response['error']}\n"
        )
        print(message)

    def __clear(self):
        if os.getenv("TERM"):
            os.system("cls" if os.name == "nt" else "clear")