# api
import todoist
from canvasapi import Canvas

# datetime and conversion
from dateutil import parser
import pytz

# load tokens
import os
from dotenv import load_dotenv

load_dotenv()


def getCanvasToken():
    canvas_token = os.getenv("CANVAS_TOKEN")
    return canvas_token


def getTodoistToken():
    todoist_token = os.getenv("TODOIST_TOKEN")
    return todoist_token


def getCanvasAssignments():
    """"Get assignment title and date from Canvas"""
    API_URL = "https://canvas.iastate.edu"
    canvas = Canvas(API_URL, getCanvasToken())

    events = canvas.get_upcoming_events()
    events_dict = {}

    for item in events:
        if 'assignment' in item:
            date = parser.parse(item['assignment']['due_at'])

            formated_date = convertTimeZone(date)

            title = item['title']

            if formated_date in events_dict:
                events_dict[formated_date].append(title)
            else:
                events_dict[formated_date] = [title]

    return events_dict


def list_courses():
    API_URL = "https://canvas.iastate.edu"
    canvas = Canvas(API_URL, getCanvasToken())

    courses = canvas.get_courses()
    for course in courses:
        print(course)


def convertTimeZone(date):
    """Converts TimeZone from UTC+0 to UTC+8"""
    # format for returning time
    fmt = "%Y-%m-%d %H:%M:%S"
    # set timezone as KL
    localTimeZone = pytz.timezone('Asia/Kuala_Lumpur')

    # tell datetime object it's UTC
    utc = date.replace(tzinfo=pytz.utc)

    localDatetime = utc.astimezone(localTimeZone)
    my_time = localDatetime.strftime(fmt)

    return my_time


def ToDoist():
    api = todoist.TodoistAPI(getTodoistToken())
    api.sync()
    full_name = api.state['user']['full_name']
    for project in api.state['projects']:
        print(project['name'])


def main():
    print(getCanvasAssignments())


if __name__ == '__main__':
    main()
    # ToDoist()
