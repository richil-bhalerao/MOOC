'''
Created on Apr 24, 2013

@author: rbhalerao
'''

from data.storage import Storage
from bson.objectid import ObjectId
import traceback

class Quiz(object):
    
    def __init__(self):
        print 'quiz created'
        # create storage 
        self.__store = Storage()
        
    
    def add(self, data):
        print 'In quiz.add method'
        try:
            return self.__store.add('quiz', data)
        except:
            traceback.print_exc()
            return 'failed'
        
    def get(self, value):
        print 'In quiz.get method'
        try:
            return self.__store.get('quiz', '_id', ObjectId(value))
        except:
            traceback.print_exc()
            return 'failed'
    
    def update(self, value, data):
        print 'In quiz.update method'
        try:
            return self.__store.update('quiz', '_id', ObjectId(value), data)
        except:
            traceback.print_exc()
            return 'failed'    
        
    def remove(self, value):
        print 'In quiz.remove method'
        try:
            return self.__store.remove('quiz', '_id', ObjectId(value))
        except:
            traceback.print_exc()
            return 'failed'
     
    def getAll(self):
        print 'In quiz.getAll method'
        try:
            return self.__store.getAll('quiz')
        except:
            traceback.print_exc()
            return 'failed'    