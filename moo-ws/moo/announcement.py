'''
Created on Apr 30, 2013

@author: rbhalerao
'''

from data.storage import Storage
import traceback
from bson.objectid import ObjectId

class Announcement(object):
    
    def __init__(self):
        print 'Announcement created'
        # create storag 
        self.__store = Storage()
        
    
    def add(self, data):
        print 'In announcement.add method'
        try:
            return self.__store.add('announcement', data)
        except:
            traceback.print_exc()
            return 'failed'
        
    def get(self, value):
        print 'In announcement.get method'
        try:
            return self.__store.get('announcement', '_id', ObjectId(value))
        except:
            traceback.print_exc()
            return 'failed'
    
    def update(self, value, data):
        print 'In announcement.update method'
        try:
            return self.__store.update('announcement', '_id', ObjectId(value), data)
        except:
            traceback.print_exc()
            return 'failed'    
        
    def remove(self, value):
        print 'In announcement.remove method'
        try:
            return self.__store.remove('announcement', '_id', ObjectId(value))
        except:
            traceback.print_exc()
            return 'failed'
     
    def getAll(self):
        print 'In announcement.getAll method'
        try:
            return self.__store.getAll('announcement')
        except:
            traceback.print_exc()
            return 'failed'