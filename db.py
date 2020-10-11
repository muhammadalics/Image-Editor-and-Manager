import psycopg2
import os
import urllib.request

def start_db(json_dict={}, execute='create database'):

    connection = psycopg2.connect(database = 'test',
                                        user='postgres',
                                        password='inspiron15',
                                        host='localhost',
                                        port='5432')

    print('connected')

    cur = connection.cursor()

    #This query will return None if table named 'test' is not present
    cur.execute("SELECT * FROM information_schema.tables WHERE table_name='test';")
    print(cur.fetchone())

    if execute == 'insert':

        if cur.fetchone() is None: #Create table named test if it is not present in db.
            cur.execute(
                'CREATE TABLE test (id serial PRIMARY KEY, copyright varchar, date date, explanation varchar,hdurl varchar, media_type varchar, title varchar, url varchar, img_file varchar);')

        current_dir = os.getcwd()
        new_dir = current_dir+'/apod/'
        if os.path.isdir(new_dir) == False: #make directory if not already present
            os.mkdir(new_dir)

        for item in json_dict:

            print(os.path.basename(item['hdurl']))
            filepath_on_disk = current_dir+'/apod/' + os.path.basename(item['hdurl'])

            #don't download if the file already exists on disk
            if os.path.isfile(filepath_on_disk) == False:
                urllib.request.urlretrieve(item['hdurl'], filepath_on_disk)

            item['filepath_on_disk'] = filepath_on_disk


            if 'copyright' not in item.keys():
                item['copyright'] = 'none'

            for key in item.keys():
                item[key] = item[key].replace("'", "''")

            #this query is used to check if title in api response already exists in the db table.
            cur.execute('SELECT title FROM test WHERE title =' + "'" + item['title'] + "'" )

            if cur.fetchone() is None: #don't insert row if it already exists.

                cur.execute("INSERT INTO test(copyright, date, explanation, hdurl, media_type, title, url, img_file) \n" 
                            "VALUES("
                            +"'"+ item['copyright'] + "',"
                            +"'"+ item['date'] + "',"
                            +"'"+ item['explanation'] + "',"
                            +"'"+ item['hdurl'] + "',"
                            +"'"+ item['media_type'] + "',"
                            +"'"+ item['title'] + "',"
                            +"'"+ item['url']+"',"
                            +"'"+ item['filepath_on_disk'] + "');")

    connection.commit()
    cur.close()
    connection.close()

def create_table(dict_keys):
    pass


if __name__ == '__main__':
    start_db()