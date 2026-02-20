from src.controller.song_register_controller import SongRegisterController
from src.view.song_registrer_view import SongRegisterView


def song_register_process():
    song_register_view = SongRegisterView()
    song_register_controller = SongRegisterController()

    new_song_informations = song_register_view.registry_song_initial()
    response = song_register_controller.insert(new_song_informations)

    if response["success"]:
        song_register_view.registry_song_success(response)
    else:
        song_register_view.registry_song_fail(response)
