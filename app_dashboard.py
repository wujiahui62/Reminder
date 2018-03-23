import warnings
import json
with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)
    from bottle import get, post, run, debug, default_app, request, template, static_file, redirect
import mongo_reminder_list as reminder_list

# transform the data retrieve from database into json format using Monthly plug-in
# Monthly is in static file
@get('/events')
def get_reminder_in_json():
    reminders = reminder_list.get_reminders()
    reminders_dict = {}
    events_list = []
    reminders_dict["monthly"] = events_list
    id = 1
    for reminder in reminders:
        event_dict = {}
        event_dict["id"] = id
        event_dict["name"] = reminder["event"]
        date = reminder["date"]
        date = date[6:] + "-" + date[0:2] + "-" + date[3:5]
        event_dict["startdate"] = date 
        id = id + 1      
        events_list.append(event_dict)
    return json.dumps(reminders_dict)


@get('/')
@get('/reminder-dashboard')
def get_reminder_list():
    return template('reminder_dashboard.tpl')

@get('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./')

#debug(True)
run(host='0.0.0.0', port=8080, reloader=True)
#application = default_app()