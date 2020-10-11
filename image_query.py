import requests
import urllib.request
import psycopg2
import datetime
import os
import db


def query(start_date, end_date):
    file = open('C:/Python/NASA api key/nasa api.txt')
    api_key = file.read().strip()
    file.close()

    # date='2006-06-16'

    #Calling NASA APOD API
    #web service rate limit is 1000 requests per hour

    get_response = requests.get('https://api.nasa.gov/planetary/apod?api_key=' + api_key + '&start_date=' + start_date + '&hd=True' + '&end_date=' + end_date)
    dict_response = get_response.json()
    db.start_db(dict_response, 'insert')


if __name__ == '__main__':
    query()