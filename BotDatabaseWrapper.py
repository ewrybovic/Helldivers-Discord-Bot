import sqlite3

from enum import Enum

class APIType(Enum):
    MajorOrder = 1
    Dispatch = 2

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
            self.conn.execute(f"""INSERT INTO HelldiverIDS(apitype, idvalue) VALUES ({APIType.MajorOrder.value}, 0);""")
            self.conn.execute(f'''INSERT INTO HelldiverIDS(apitype, idvalue) VALUES ({APIType.Dispatch.value}, 0);''')
            self.conn.commit()
        else:
            print("DB previously initialized")
            cursor = self.conn.execute("SELECT * FROM HelldiverIDS")

            for row in cursor:
                print(row)

    def UpdateID(self, type: APIType, id: int):
        print(f'Updating {type.name}')
        self.conn.execute(
            f"""UPDATE HelldiverIDS SET idvalue = {id} WHERE apitype = {type.value}"""
        )
        self.conn.commit()

    def GetID(self, type:APIType) -> int:
        print(f"Getting value for {type.name}")
        return self.conn.execute(f"""SELECT idvalue FROM HelldiverIDS WHERE apitype = {type.value}""").fetchone()[0]

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    wrapper = DBWrapper("BotDataBase.sqlite3")
    wrapper.close()