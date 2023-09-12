from flask import Flask, request, g, jsonify, abort ,make_response
from app import vaccine_app
import  appointments 
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import re
import Config
from datetime import datetime
from appointments import Apponiments

app = Flask(__name__)
limiter = Limiter(get_remote_address, app= app,  
    default_limits=["5 per second"]
)


appointments.add_appointments()

@app.route('/checkslots/', methods = ['GET'])
def check_slots():
     return Apponiments.get_available_appointments()

@app.route('/bookslots/', methods = ['POST'])  
@limiter.limit("5 per second")
def book_slots() :
     data = request.get_json()
     date = data.get('date')
     time = data.get('time')
     hospital_name = data.get('hospital_name')
     validate_date_time(date, time)
     return Apponiments.book_slots(date, time, hospital_name)
     
@app.route('/cancelslots/<int:appointment_id>', methods = ['DELETE']) 
def cancel_slots(appointment_id):
     return Apponiments.cancel_solts(appointment_id)

@app.route('/rescheduleslots/<int:appointment_id>', methods = ['POST']) 
def reschedule_slots(appointment_id):
     data = request.get_json()
     date = data.get('date')
     time = data.get('time')
     hospital_name = data.get('hospital_name')
     validate_date_time(date, time)
     return Apponiments.get_reschedule_appointments(appointment_id, date, time, hospital_name)


def validate_date_time(date, time):
    try:
        # Attempt to parse the input time using the specified format
        if bool(re.match(Config.TIME_FORMAT, time)):
            datetime.strptime(date, Config.DATE_FORMAT) 
        else:
            abort(make_response(jsonify(message="Invalid time format"), 400))
        return True
    except ValueError:
        # If parsing fails, the date is invalid
        abort(make_response(jsonify(message='Invalid date format'), 400))

if __name__ == '__main__':
     app.run(debug= True)
     

#Date_time validations can be included

