# api
import todoist
from canvasapi import Canvas

# datetime and conversion
from dateutil import parser
import pytz

# load tokens
import os
from dotenv import load_dotenv

import yaml

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

    # # get course list
    # courses = canvas.get_courses()
    # for course in courses:
    #     print(course)

    course_dict = {79610: "STAT 341", 79615: "LD ST 322", 79522: "ENGL 150", 80521: "COM S-227"}

    events = canvas.get_todo_items()
    todo_dict = {}

    for item in events:
        course_id = item["course_id"]
        course_name = course_dict[course_id]
        title = item["assignment"]["name"]
        url = item["assignment"]["html_url"]

        date = parser.parse(item['assignment']['due_at'])
        formated_date = convertTimeZone(date)
        
        if course_name not in todo_dict:
            todo_dict[course_name] = [{"title": title, "date": formated_date, "url": url}]
        else:
            todo_dict[course_name].append({"title": title, "date": formated_date, "url": url})

    # return dictionary
    return todo_dict

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


def addToTodoist():
    api = todoist.TodoistAPI(getTodoistToken())
    api.sync()
    
    items = api.state["items"]
    for project in api.state['projects']:
        print(project['name'])


def main():
    data = getCanvasAssignments()
    print(yaml.dump(data, default_flow_style=False))


if __name__ == '__main__':
    main()
    # ToDoist()
