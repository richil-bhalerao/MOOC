'''
Created on Apr 30, 2013

@author: rbhalerao
'''

from data.storage import Storage
from bson.objectid import ObjectId
import traceback

class Message(object):
    
    def __init__(self):
        print 'message created'
        # create storage 
        self.__store = Storage()
        
    
    def add(self, data):
        print 'In message.add method'
        try:
            return self.__store.add('message', data)
        except:
            traceback.print_exc()
            return 'failed'
        
    def get(self, value):
        print 'In message.get method'
        try:
            return self.__store.get('message', '_id', ObjectId(value))
        except:
            traceback.print_exc()
            return 'failed'
    
    def update(self, value, data):
        print 'In message.update method'
        try:
            return self.__store.update('message', '_id', ObjectId(value), data)
        except:
            traceback.print_exc()
            return 'failed'    
        
    def remove(self, value):
        print 'In message.remove method'
        try:
            return self.__store.remove('message', '_id', ObjectId(value))
        except:
            traceback.print_exc()
            return 'failed'
     
    def getAll(self):
        print 'In message.getAll method'
        try:
            return self.__store.getAll('message')
        except:
            traceback.print_exc()
            return 'failed'    