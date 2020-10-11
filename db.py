import psycopg2

def start_db(json_dict=[], execute='create database'):
    connection = psycopg2.connect(database = 'test',
                                        user='postgres',
                                        password='inspiron15',
                                        host='localhost',
                                        port='5432')

    print('connected')

    cur = connection.cursor()






    if execute == 'create database':
        cur.execute('CREATE TABLE test (id serial PRIMARY KEY, copyright varchar, date date, explanation varchar,hdurl varchar, media_type varchar, title varchar, url varchar);')

    if execute == 'insert':

        for item in json_dict:

            if 'copyright' not in item.keys():
                item['copyright'] = 'none'

            for key in item.keys():
                item[key] = item[key].replace("'", "''")

            print(item)

            # cur.execute('INSERT INTO test(copyright, date, explanation, hdurl, media_type, title, url) \n'
            #             'VALUES('
            #             +'\''+ item['copyright'] + '\','
            #             +'\''+ item['date'] + '\','
            #             # +'\''+ json_dict['explanation'] + '\','
            #             + '\'' + 'none' + '\','
            #             +'\''+ item['hdurl'] + '\','
            #             +'\''+ item['media_type'] + '\','
            #             +'\''+ item['title'] + '\','
            #             +'\''+ item['url']+'\');')

            cur.execute("INSERT INTO test(copyright, date, explanation, hdurl, media_type, title, url) \n" 
                        "VALUES("
                        +"'"+ item['copyright'] + "',"
                        +"'"+ item['date'] + "',"
                        # +'\''+ json_dict['explanation'] + '\','
                        + "'" + 'none' + "',"
                        +"'"+ item['hdurl'] + "',"
                        +"'"+ item['media_type'] + "',"
                        +"'"+ item['title'] + "',"
                        +"'"+ item['url']+"');")


    connection.commit()
    cur.close()
    connection.close()

def create_table(dict_keys):
    pass


if __name__ == '__main__':
    start_db()