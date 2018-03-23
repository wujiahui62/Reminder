# -*- coding: utf-8 -*-

import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)
    from bottle import get, post, run, debug, default_app, request, template, static_file, redirect

import mongo_reminder_list as reminder_list

@get('/')
@get('/reminder-list')
def get_reminder_list():
    reminders = reminder_list.get_reminders()
    for reminder in reminders:
        event = reminder['event']
        date = reminder['date']
    return template('reminder_list.tpl', reminders=reminders)

@post('/new-reminder')
def post_new_reminder():
    event = request.forms.event
    date = request.forms.date
    reminder_list.save_reminder(event, date)
    redirect('/reminder-list')

@get('/discard-reminder/<id>')
def get_discard_reminder(id):
    reminder_list.delete_reminder(id)
    redirect('/reminder-list')

@post('/search-results')
def get_search_results():
    key = request.POST.key.strip()
    reminders = reminder_list.get_reminder_by_key(key)
    if reminders == key:
        return template('not_found.tpl', key=key)
    return template('reminder_list.tpl', reminders=reminders)

@get('/edit-reminder/<id>')
def get_edited_reminder(id):
    edit_reminder = reminder_list.get_reminder(id)
    return template('edit_reminder.tpl', reminder = edit_reminder)
    

@post('/edit-reminder/<id>')
def post_edited_reminder(id):
    event = request.forms.event
    date = request.forms.date
    reminder_list.update_reminder(id, event, date)    
    redirect('/reminder-list')

@get('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

#debug(True)
#run(host='localhost', port=8080, reloader=True)
application = default_app()