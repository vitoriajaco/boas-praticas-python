from src.models.entities.music import Music

#verificar porque do uso pois nao é comum usar em nome de classe e sim nos metodos
class __MusicsRepository:
    def __init__(self):
        self.__music_list =[]

    def insert_music(self, music: Music) -> None:
        self.__music_list.append(music)

    def find_music(self, music_title:str) -> Music:
        for music in self.__music_list:
            if music.title.lower() == music_title.lower():
                return music

        return None

    def get_all_songs(self) -> list[Music]:
       return self.__music_list

#SingleTon (IA disse que nao era agora acredito em quem?)
musics_repository  = __MusicsRepository()