import pyodbc
import Display_Video
import datetime
DRIVER_NAME = 'SQL SERVER'
SERVER=f"localhost\\sqlexpress"
DATABASE_NAME="Gp"
SERVER_NAME= "DESKTOP-2KON84S\SQLEXPRESS"
connection_string = f"""
DRIVER={{{DRIVER_NAME}}};
SERVER={SERVER_NAME};
DATABASE={DATABASE_NAME};
Trust Connection=yes;
"""
def Add_Violence_Incidences(current_datetime,path):
    conn = pyodbc.connect(connection_string)
    SQL_QUERY = """
    INSERT INTO Violence_Incidences 
    VALUES (?, ?)
    """

    cursor = conn.cursor()
    cursor.execute(SQL_QUERY,(current_datetime,path))
    conn.commit()
    cursor.close()

def Diplay_Violence_Incidences():
    conn = pyodbc.connect(connection_string)
    SQL_QUERY="select * from Violence_Incidences "
    cursor = conn.cursor()
    cursor.execute(SQL_QUERY)
    records = cursor.fetchall()
    for r in records:
        print(f"{r.Id} {r.Date} {r.path}")
        #Display_Video.Display_Video(r.path)
    cursor.close()
    conn.close()
#Diplay_Violence_Incidences()