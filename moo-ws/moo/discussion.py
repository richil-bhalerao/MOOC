'''
Created on Apr 30, 2013

@author: rbhalerao
'''

from data.storage import Storage
from bson.objectid import ObjectId
import traceback

class Discussion(object):
    
    def __init__(self):
        print 'discussion created'
        # create storage 
        self.__store = Storage()
        
    
    def add(self, data):
        print 'In discussion.add method'
        try:
            return self.__store.add('discussion', data)
        except:
            traceback.print_exc()
            return 'failed'
        
    def get(self, value):
        print 'In discussion.get method'
        try:
            return self.__store.get('discussion', '_id', ObjectId(value))
        except:
            traceback.print_exc()
            return 'failed'
    
    def update(self, value, data):
        print 'In discussion.update method'
        try:
            return self.__store.update('discussion', '_id', ObjectId(value), data)
        except:
            traceback.print_exc()
            return 'failed'    
        
    def remove(self, value):
        print 'In discussion.remove method'
        try:
            return self.__store.remove('discussion', '_id', ObjectId(value))
        except:
            traceback.print_exc()
            return 'failed'
     
    def getAll(self):
        print 'In discussion.getAll method'
        try:
            return self.__store.getAll('discussion')
        except:
            traceback.print_exc()
            return 'failed'    