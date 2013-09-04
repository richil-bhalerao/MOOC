'''
Created on Apr 24, 2013

@author: rbhalerao
'''

from data.storage import Storage
from bson.objectid import ObjectId

class Category(object):
    
    def __init__(self):
        print 'Category created'
        # create storage 
        self.__store = Storage()
        
    
    def add(self, data):
        print 'In Category.add method'
        try:
            return self.__store.add('category', data)
        except:
            return 'failed'
        
    def get(self, value):
        print 'In Category.get method'
        try:
            return self.__store.get('category', '_id', ObjectId(value))
        except:
            return 'failed'
    
    def update(self, value, data):
        print 'In Category.update method'
        try:
            return self.__store.update('category', '_id', ObjectId(value), data)
        except:
            return 'failed'    
        
    def remove(self, value):
        print 'In Category.remove method'
        try:
            return self.__store.remove('category', '_id', ObjectId(value))
        except:
            return 'failed'
     
    def getAll(self):
        print 'In Category.getAll method'
        try:
            return self.__store.getAll('category')
        except:
            return 'failed'    