class SongRegisterController:  # substantivo pras classes
    def insert(self, new_song_informations: dict) -> dict:
        try:   # acoes pra metodos
            self.__verify_songs_infos(new_song_informations)
            self.__verify_if_song_already_registred(new_song_informations)
            self.__insert_song(new_song_informations)
            return self.__format_response(new_song_informations)
        except Exception as exception:
            return self.__format_error_response(exception)

    # def __verify_songs_infos(self, new_song_informations: dict) -> None:
    #     if len(new_song_informations["title"]) > 100:
    #         raise Exception("Título da música com mais de 100 caracteres")
    #
    #     year = int(new_song_informations["year"])
    #     if year >= 2026:
    #         raise Exception("Ano de música inválido")

    #Tratamento melhor:
    def __verify_songs_infos(self, new_song_informations: dict) -> None:
        title = new_song_informations["title"]
        artist = new_song_informations["artist"]
        year_str = new_song_informations["year"]

        if not title.strip():
            raise Exception("Título não pode ser vazio")

        if not artist.strip():
            raise Exception("Artista não pode ser vazio")

        if not year_str.isdigit():
            raise Exception("Ano deve ser numérico")

        year = int(year_str)

        if year < 1800:
            raise Exception("Ano muito antigo")

        if year > 2025:
            raise Exception("Ano inválido")


    def __verify_if_song_already_registred(self, new_song_informations: dict) -> None:
        # Interacao com Models
        pass

    def __insert_song(self, new_song_informations: dict) -> None:
        # Interacao com Models
        pass

    def __format_response(self, new_song_informations: dict) -> dict:
        return {
            "success": True,
            "count": 1,
            "attributes":{
                "title": new_song_informations["title"]
            }
        }

    def __format_error_response(self, error: Exception) -> dict:
        return {
            "success": False,
            "error": str(error)
        }
