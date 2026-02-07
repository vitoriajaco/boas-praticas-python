from src.view.song_registrer_view import SongRegistrerView


def song_register_process():
    song_register_view = SongRegistrerView()

    new_song_informations = song_register_view.registry_song_initial()
