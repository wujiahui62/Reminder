# -*- coding: utf-8 -*-
import pymongo
import private

from pymongo import MongoClient
from bson.objectid import ObjectId

connection_string = "mongodb://{u}:{p}@ds147377.mlab.com:47377/reminders"
client = MongoClient(connection_string.format(u=private.mongo_user, p=private.mongo_password, connect=False))


db = client.reminders
current_reminders = db.current_reminders

def get_reminders():
    reminders = list(current_reminders.find())
    for reminder in reminders:
        reminder['_id'] = str(reminder['_id'])
    return reminders

def get_reminder(reminder_id):
    # Convert from string to ObjectId:
    object_id = ObjectId(reminder_id)
    reminder = current_reminders.find_one({'_id': object_id})
    reminder['_id'] = str(reminder['_id'])
    return reminder

def get_reminder_by_key(key):
    # remove duplicates
    reminders = list(current_reminders.find({"event":{'$regex':key}})) + list(current_reminders.find({"date":{'$regex':key}}))
    reminders_no_repeat = []
    for i in range(len(reminders)):
        if reminders[i] not in reminders[i+1:]:
            reminders_no_repeat.append(reminders[i])
    for reminder in reminders_no_repeat:
        reminder['_id'] = str(reminder['_id'])
    return reminders_no_repeat

def save_reminder(event, date):
    reminder = {"event": event, "date": date}
    reminder_id = current_reminders.insert_one(reminder).inserted_id
    return str(reminder_id)

def delete_reminder(reminder_id):
    object_id = ObjectId(reminder_id)
    print(object_id)
    reminders = current_reminders.delete_one({'_id':object_id})

def update_reminder(reminder_id, event=None, date=None):
    if event:
        update = {'$set':{'event':event}}
        object_id = ObjectId(reminder_id)
        current_reminders.update_one({'_id':object_id}, update)
    if date:
        update = {'$set':{'date':date}}
        object_id = ObjectId(reminder_id)
        current_reminders.update_one({'_id':object_id}, update)
