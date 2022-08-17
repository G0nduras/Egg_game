import sqlite3
import time


class DataBase:
    def __init__(
            self,
            path: str,
    ):
        self._path = path
        self._connection = sqlite3.connect(self._path)
        self._cursor = self._connection.cursor()
        self._cursor.execute('''CREATE TABLE IF NOT EXISTS EggGameScores
                      (id INT, login TEXT, score INT, timestamp INT)''')
        self._connection.commit()

    def write(self, login: str, score: int):
        try:
            id_player = list(self._cursor.execute("SELECT MAX(id) FROM EggGameScores"))[0][0] + 1
        except Exception:
            id_player = 0
        times = int(time.time())
        self._cursor.execute(f"INSERT INTO EggGameScores VALUES ('{id_player}', '{login}', '{score}', '{times}')")
        self._connection.commit()
        print(list(self._cursor.execute("SELECT * FROM EggGameScores")))

    def read(self, login: str) -> tuple:
        necessary_timestamp = list(self._cursor.execute(f"SELECT MAX(timestamp) FROM EggGameScores WHERE login = '{login}'"))[0][0]
        overall_max_score = list(self._cursor.execute("SELECT MAX(score) FROM EggGameScores"))[0][0]
        player_max_score = list(self._cursor.execute(f"SELECT MAX(score) FROM EggGameScores WHERE login = '{login}'"))[0][0]
        our_player_score = list(self._cursor.execute(f"SELECT score FROM EggGameScores WHERE timestamp = '{necessary_timestamp}'"))[0][0]
        output = (overall_max_score, player_max_score, our_player_score)
        return output
