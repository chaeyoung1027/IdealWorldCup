import mysql.connector
from mysql.connector import Error

def main():
    try:

        connection = mysql.connector.connect(
            host='localhost',
            database='ideal_worldcup',
            user='root',
            password='mirim'
        )

        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)

            query = """  """

            cursor.execute(query)
            results = cursor.fetchall()

            print(results)

    except Error as e:
        print('디비 관련 에러 발생', e)

    finally:
        cursor.close()
        connection.close()
        print("MySQL 커넥션 종료")

if __name__ == '__main__':
    main()