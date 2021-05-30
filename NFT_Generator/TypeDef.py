class Audio:
    def __init__(self, file: str):
        self._file = file

    @property
    def file(self):
        return self._file


class Music:
    def __init__(self, rawMusic: Audio):
        self._rawMusic = rawMusic


class Token:
    def __init__(self, t: str):
        self._token = t
