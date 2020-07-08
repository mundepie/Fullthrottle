from .models import Employees
import json
from django.db import IntegrityError

# Create your views here.
# class Database for all database functions
class Database:
    # populate the database
    def populatedb():
        f = open("C:\\Users\DELL\\Desktop\\FT\\transfer_info\\Test.json")
        data = json.load(f)
        for i in range(len(data["members"])):
            id = data["members"][i]["id"]
            name = data["members"][i]["real_name"]
            location = data["members"][i]["tz"]
            activity_per = data["members"][i]["activity_periods"]
            duration = ""
            for j in range(len(activity_per)):
                number = str(j+1)
                duration = duration + " --------- " + number + " : " + activity_per[j]["start_time"] + " to "+ activity_per[j]["end_time"]
            try:
                Employees.objects.create(id = id, name = name, location = location, duration = duration)
            except IntegrityError:
                # ignores if we add the same id again(could be made better)
                continue
