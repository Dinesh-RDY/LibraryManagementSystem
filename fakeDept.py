import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE" , 'LMS.settings')
import django
django.setup()
from uuid import uuid4
from Library.models import Department
deptNames = ["CSE" , "ECE" ,"CIVIL","MECH" ,'BME','EEE']

for name in deptNames:
    dept = Department.objects.get_or_create(deptName = name , deptid = uuid4())[0]
    dept.save()
    print("Saved")

