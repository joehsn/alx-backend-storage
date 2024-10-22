#!/usr/bin/env python3
"""
    12. Log stats task's module.
"""

from pymongo import MongoClient


def main():
    """
        A script that provides some stats about
        Nginx logs stored in MongoDB.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx

    print('{} logs'.format(nginx.count_documents({})))
    print('Methods:')

    for method in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']:
        method_count = len(list(nginx.find({ 'method': method })))
        print('\tmethod {}: {}'.format(method, method_count))

    status_checks = len(list(
        nginx.find({ 'method': 'GET', 'path': '/status' })
    ))
    print('{} status check'.format(status_checks))

if __name__ == '__main__':
    main()
