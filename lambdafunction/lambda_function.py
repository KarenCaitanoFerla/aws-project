import json
import mysql.connector as mysql

def lambda_handler(event, context):
    print(event)
    i = event["Records"][0]["body"]
    i = json.loads(i)
    name = i["Name/Alias"]
    gender = i["Gender"]
    url = i["URL"]
    appearance = i["Appearances"]
    intro = i["Full/Reserve Avengers Intro"] + ', ' + i["Year"]
    
    item = (name, gender, url, appearance, intro)
    insertAWStoMySQL(item)

def testConection():
    coon = mysql.connect(host='host', database='database', user ='user', password = 'senha')
    return coon

def insertAWStoMySQL(item):

    with testConection() as coon:
        cursor = coon.cursor()
        sql = """INSERT INTO avengersAWS (Name_Avenger, Gender, Url, Appearance, Intro) VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(sql, item)
        coon.commit()
        cursor.close()

if __name__ == '__main__':

    insertAWStoMySQL()