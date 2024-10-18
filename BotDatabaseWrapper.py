import sqlite3

from enum import Enum

class APIType(Enum):
    MajorOrder = 1
    Dispatch = 2
    SteamNews = 3

class DBWrapper:
    def __init__(self, db_name: str):
        self.conn = sqlite3.connect(db_name)
        self.InitDB()
    
    def InitDB(self):
        data = self.conn.execute(
            """SELECT * FROM sqlite_master WHERE type='table' AND name='HelldiverIDS';"""
        ).fetchall()

        print(data)
        
        if data == []:
            print("Initializing DB")
            self.conn.execute('''CREATE TABLE HelldiverIDS(apitype INT PRIMARY KEY NOT NULL, idvalue INT NOT NULL);''')
            self.conn.commit()
        else:
            print("DB previously initialized")
            cursor = self.conn.execute("SELECT * FROM HelldiverIDS")

            for row in cursor:
                print(row)

    def UpdateID(self, type: APIType, id: int):
        print(f'Updating {type.name}')
        self.conn.execute(
            f"""REPLACE INTO HelldiverIDS (apitype, idvalue) VALUES ({type.value}, {id})"""
        ) # Hacky way to insert/update at the same time, kinda nasty
        self.conn.commit()

    def GetID(self, type:APIType) -> int:
        print(f"Getting value for {type.name}")
        data = self.conn.execute(f"""SELECT idvalue FROM HelldiverIDS WHERE apitype = {type.value}""").fetchone()
        return -1 if data is None else data[0]

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    wrapper = DBWrapper("BotDataBase.sqlite3")
    wrapper.close()