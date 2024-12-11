from typing import Union
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

import sqlite3

DB_CONNECTION =None
DB_CURSOR =None


SENSOR_EXPECTATION ={"Communication":{"TYPE_PROXIMITY":1,"TYPE_LIGHT":-1,"TYPE_ORIENTATION":1,"TYPE_ACCELEROMETER":1,"TYPE_GYROSCOPE":1,
                                      "TYPE_GRAVITY":-1,"TYPE_MAGNETIC_FIELD":-1,"TYPE_PRESSURE":-1,"TYPE_RELATIVE_HUMIDITY":-1,
                                      "TYPE_LINEAR_ACCELERATION":-1,"TYPE_ROTATION_VECTOR":1,"TYPE_TEMPERATURE":-1,
                                      "TYPE_AMBIENT_TEMPERATURE":-1,"TYPE_HEART_RATE":-1},
                    "Education":{"TYPE_PROXIMITY":1,"TYPE_LIGHT":1,"TYPE_ORIENTATION":-1,"TYPE_ACCELEROMETER":1,"TYPE_GYROSCOPE":-1,
                                      "TYPE_GRAVITY":-1,"TYPE_MAGNETIC_FIELD":-1,"TYPE_PRESSURE":-1,"TYPE_RELATIVE_HUMIDITY":-1,
                                      "TYPE_LINEAR_ACCELERATION":-1,"TYPE_ROTATION_VECTOR":-1,"TYPE_TEMPERATURE":-1,
                                      "TYPE_AMBIENT_TEMPERATURE":-1,"TYPE_HEART_RATE":-1},
                    "Game":{"TYPE_PROXIMITY":-1,"TYPE_LIGHT":1,"TYPE_ORIENTATION":1,"TYPE_ACCELEROMETER":1,"TYPE_GYROSCOPE":-1,
                                      "TYPE_GRAVITY":1,"TYPE_MAGNETIC_FIELD":-1,"TYPE_PRESSURE":-1,"TYPE_RELATIVE_HUMIDITY":-1,
                                      "TYPE_LINEAR_ACCELERATION":1,"TYPE_ROTATION_VECTOR":1,"TYPE_TEMPERATURE":-1,
                                      "TYPE_AMBIENT_TEMPERATURE":-1,"TYPE_HEART_RATE":-1},
                    "Health":{"TYPE_PROXIMITY":-1,"TYPE_LIGHT":-1,"TYPE_ORIENTATION":-1,"TYPE_ACCELEROMETER":1,"TYPE_GYROSCOPE":1,
                                      "TYPE_GRAVITY":-1,"TYPE_MAGNETIC_FIELD":-1,"TYPE_PRESSURE":-1,"TYPE_RELATIVE_HUMIDITY":-1,
                                      "TYPE_LINEAR_ACCELERATION":-1,"TYPE_ROTATION_VECTOR":1,"TYPE_TEMPERATURE":-1,
                                      "TYPE_AMBIENT_TEMPERATURE":-1,"TYPE_HEART_RATE":1},
                    "Map":{"TYPE_PROXIMITY":-1,"TYPE_LIGHT":-1,"TYPE_ORIENTATION":1,"TYPE_ACCELEROMETER":1,"TYPE_GYROSCOPE":1,
                                     "TYPE_GRAVITY":-1,"TYPE_MAGNETIC_FIELD":1,"TYPE_PRESSURE":-1,"TYPE_RELATIVE_HUMIDITY":-1,
                                     "TYPE_LINEAR_ACCELERATION":-1,"TYPE_ROTATION_VECTOR":1,"TYPE_TEMPERATURE":-1,
                                     "TYPE_AMBIENT_TEMPERATURE":-1,"TYPE_HEART_RATE":-1},
                    "Music_Audio":{"TYPE_PROXIMITY":1,"TYPE_LIGHT":1,"TYPE_ORIENTATION":-1,"TYPE_ACCELEROMETER":1,"TYPE_GYROSCOPE":1,
                                     "TYPE_GRAVITY":1,"TYPE_MAGNETIC_FIELD":-1,"TYPE_PRESSURE":-1,"TYPE_RELATIVE_HUMIDITY":-1,
                                     "TYPE_LINEAR_ACCELERATION":-1,"TYPE_ROTATION_VECTOR":1,"TYPE_TEMPERATURE":-1,
                                     "TYPE_AMBIENT_TEMPERATURE":-1,"TYPE_HEART_RATE":-1},
                    "Weather":{"TYPE_PROXIMITY":-1,"TYPE_LIGHT":-1,"TYPE_ORIENTATION":-1,"TYPE_ACCELEROMETER":-1,"TYPE_GYROSCOPE":1,
                                     "TYPE_GRAVITY":-1,"TYPE_MAGNETIC_FIELD":-1,"TYPE_PRESSURE":1,"TYPE_RELATIVE_HUMIDITY":1,
                                     "TYPE_LINEAR_ACCELERATION":-1,"TYPE_ROTATION_VECTOR":1,"TYPE_TEMPERATURE":-1,
                                     "TYPE_AMBIENT_TEMPERATURE":1,"TYPE_HEART_RATE":-1}                    
                     
                    }
SENSOR_EXPLANATION = {"TYPE_PROXIMITY":"Proximity Sensor - Detects the presence of objects near the device, useful for gesture-based controls such as turning off the display during calls or enabling gesture-based controls. \
It raises concerns about unnecessary proximity tracking and potential misuse for gathering sensitive user behavior data.",
                      "TYPE_LIGHT":"Light Sensor - Adjusts screen brightness based on the surrounding light levels, improving user visibility in various conditions.\
content in varying lighting conditions. Minimal privacy risk, but could infer environmental context.",                       
                      "TYPE_ORIENTATION":"Orientation Sensor - The Orientation Sensor detects the angular position of a device along its axes.\
 It has been replaced by more accurate sensors like the Rotation Vector Sensor for better tracking in modern applications requiring device orientation.",
                      "TYPE_ACCELEROMETER":"Accelerometer - Tracks motion and movement, allowing for interactive experiences like virtual \
experiments or simulations. Could be used to track precise movements and behavior patterns, raising privacy concerns if misused.",
                      "TYPE_GYROSCOPE":"Gyroscope - The Gyroscope measures the device’s rotation rate around its axes, providing \
precise data for tracking 3D movement. It's commonly used in AR/VR applications, gaming, and simulations to enhance motion tracking and improve user interaction.",
                      "TYPE_GRAVITY":"Gravity Sensor - Detects the device’s orientation relative to gravity, useful in specific physics-related\
Unless the app is related to physics experiments or simulations involving force, its collection may be unnecessary.",
                      "TYPE_MAGNETIC_FIELD":"Magnetic Field Sensor - Detects the Earth’s magnetic field to provide compass functionality. \
Accessed without a clear purpose, may lead to concerns about unnecessary and more precise location tracking.",
                      "TYPE_PRESSURE":"Pressure Sensor - Measures atmospheric pressure, typically used in environmental science apps or \
altitude-related educational content. Outside of weather applications, this sensor’s usage may indicate redundant environmental data collection.",
                      "TYPE_RELATIVE_HUMIDITY":"Relative Humidity Sensor - Tracks humidity levels, which is only vital for determining weather conditions such as humidity and precipitation. \
Minimal risk due to its limited functionality.",
                       "TYPE_LINEAR_ACCELERATION":"Linear Acceleration Sensor - Measures acceleration excluding gravity, Found in apps requiring precise motion data.\
Could raise concerns if tracking detailed movement data without user consent.",
                       "TYPE_ROTATION_VECTOR":"Rotation Vector Sensor - Tracks device rotation in 3D space, useful in AR/VR-based educational \
simulations. Privacy concerns may arise from unnecessary collection of orientation data.",
                       "TYPE_TEMPERATURE":"Temperature Sensor - Measures the device’s internal temperature, Relevant in specific apps dealing with device performance or environmental monitoring. \
Minimal privacy risk due to its deprecated status.",
                       "TYPE_AMBIENT_TEMPERATURE":"Ambient Temperature Sensor - Measures surrounding environmental temperature, potentially useful for \
environmental science education but generally irrelevant to most categories. Could infer whether a user is indoors or outdoors, leading to indirect information concerns.",
                       "TYPE_HEART_RATE":"Heart Rate Monitor - Monitors heart rate, mainly relevant in tracking user well-being and physical activity.. \
Raises significant privacy concerns due to the sensitive nature of health data."
                       }

PERMISSIONS = ["android_permission_INTERNET",
               "android_permission_ACCESS_NETWORK_STATE",
               "android_permission_ACCESS_WIFI_STATE",
               "android_permission_BLUETOOTH",
               "android_permission_BLUETOOTH_ADMIN",
               "android_permission_VIBRATE",
               "android_permission_READ_CONTACTS",
               "android_permission_WRITE_CONTACTS",
               "android_permission_READ_EXTERNAL_STORAGE",
               "android_permission_WRITE_EXTERNAL_STORAGE",
               "android_permission_CAMERA",
               "android_permission_RECORD_AUDIO",
               "android_permission_ACCESS_FINE_LOCATION",
               "android_permission_ACCESS_COARSE_LOCATION",
               "android_permission_READ_PHONE_STATE",
               "android_permission_CALL_PHONE",
               "android_permission_SEND_SMS",
               "android_permission_READ_SMS",
               "android_permission_SYSTEM_ALERT_WINDOW",
               "android_permission_WRITE_SETTINGS"
               ]



def getdb_cursor():
    global DB_CONNECTION 
    DB_CONNECTION = sqlite3.connect(DB_FILE)
    DB_CONNECTION.row_factory = sqlite3.Row
    global DB_CURSOR
    DB_CURSOR = DB_CONNECTION.cursor()
    return DB_CURSOR


def closedb_cursor():   
    global DB_CURSOR,DB_CONNECTION

    DB_CURSOR.close()
    DB_CONNECTION.close()


#DB_FILE='D:\\projects\\students\\apk_sensor\\final_corrected_apk.db'
DB_FILE='./final_corrected_apk.db'



app = FastAPI()
#app.mount("/", StaticFiles(directory="root"), name="root")

#@app.get("/")
#async def read_root():
#    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(
        item_id: int,
        q: str = 'default',
):
    return {"item_id": item_id, "q": q}

@app.get("/api/homepage_rand")
async def homepage_rand():
    cur = getdb_cursor()
    query = "select id, new_names,risk_score from v_app_detail ORDER BY RANDOM() LIMIT 8"
    cur.execute(query)
    rows = cur.fetchall()
    
    closedb_cursor()
    return rows

@app.get("/api/get_all_apps")
async def get_all_apps():
    cur = getdb_cursor()
    query = "select id, category,new_names,risk_score from v_app_detail ORDER BY category"
    cur.execute(query)
    rows = cur.fetchall()
    
    closedb_cursor()
    return rows

@app.get("/api/category_data")
async def category_data():
    cur = getdb_cursor()
    query = "select category, avg(risk_score) as risk_score,sum(TYPE_PROXIMITY) as TYPE_PROXIMITY,\
             sum(TYPE_LIGHT) as TYPE_LIGHT,sum(TYPE_ORIENTATION) as TYPE_ORIENTATION,sum(TYPE_ACCELEROMETER) as TYPE_ACCELEROMETER,\
             sum(TYPE_GYROSCOPE) as TYPE_GYROSCOPE, sum(TYPE_GRAVITY) as TYPE_GRAVITY,sum(TYPE_MAGNETIC_FIELD) as TYPE_MAGNETIC_FIELD,\
             sum(TYPE_PRESSURE) as TYPE_PRESSURE,sum(TYPE_RELATIVE_HUMIDITY) as TYPE_RELATIVE_HUMIDITY,\
            sum(TYPE_LINEAR_ACCELERATION) as TYPE_LINEAR_ACCELERATION,sum(TYPE_ROTATION_VECTOR) as TYPE_ROTATION_VECTOR,\
            sum(TYPE_TEMPERATURE) as TYPE_TEMPERATURE,sum(TYPE_AMBIENT_TEMPERATURE) as TYPE_AMBIENT_TEMPERATURE,\
            sum(TYPE_HEART_RATE) as TYPE_HEART_RATE,\
            sum(android_permission_INTERNET) as android_permission_INTERNET,\
            sum(android_permission_ACCESS_NETWORK_STATE) as android_permission_ACCESS_NETWORK_STATE,\
            sum(android_permission_ACCESS_WIFI_STATE) as android_permission_ACCESS_WIFI_STATE,\
            sum(android_permission_BLUETOOTH) as android_permission_BLUETOOTH,\
            sum(android_permission_BLUETOOTH_ADMIN) as android_permission_BLUETOOTH_ADMIN,\
            sum(android_permission_VIBRATE) as android_permission_VIBRATE,\
            sum(android_permission_READ_CONTACTS) as android_permission_READ_CONTACTS,\
            sum(android_permission_WRITE_CONTACTS) as android_permission_WRITE_CONTACTS,\
            sum(android_permission_READ_EXTERNAL_STORAGE) as android_permission_READ_EXTERNAL_STORAGE,\
            sum(android_permission_WRITE_EXTERNAL_STORAGE) as android_permission_WRITE_EXTERNAL_STORAGE,\
            sum(android_permission_CAMERA) as android_permission_CAMERA,\
            sum(android_permission_RECORD_AUDIO) as android_permission_RECORD_AUDIO,\
            sum(android_permission_ACCESS_FINE_LOCATION) as android_permission_ACCESS_FINE_LOCATION,\
            sum(android_permission_ACCESS_COARSE_LOCATION) as android_permission_ACCESS_COARSE_LOCATION,\
            sum(android_permission_READ_PHONE_STATE) as android_permission_READ_PHONE_STATE,\
            sum(android_permission_CALL_PHONE) as android_permission_CALL_PHONE,\
            sum(android_permission_SEND_SMS) as android_permission_SEND_SMS,\
            sum(android_permission_READ_SMS) as android_permission_READ_SMS,\
            sum(android_permission_SYSTEM_ALERT_WINDOW) as android_permission_SYSTEM_ALERT_WINDOW,\
            sum(android_permission_WRITE_SETTINGS) as android_permission_WRITE_SETTINGS\
            from v_app_detail group BY category"
    cur = getdb_cursor() 
    cur.execute(query)
    rows = cur.fetchall()
    closedb_cursor()
    
    if rows == None:
        return {}
    
    retval_list = {}
    
    for row in rows:
        expected = 0
        unexpected = 0

        sensor_e_data =  SENSOR_EXPECTATION[row["category"]]
        print(sensor_e_data)
        for key in sensor_e_data:
            print("debug:"+key)
            if sensor_e_data[key]==-1:
                unexpected+=row[key]              
            elif sensor_e_data[key]==1:
                expected+=row[key]
                
        permission_count = 0
        for item in PERMISSIONS:
            permission_count+=row[item]
    
        retval ={}
        retval["risk_score"]=row["risk_score"]
        retval["unexpected"]=unexpected
        retval["expected"]=expected  
        #retval["expected_list"]=expected_list
        #retval["unexpected_list"]=unexpected_list
        retval["permission_count"]=permission_count
        retval_list[row["category"]]=retval
    
    return retval_list






@app.get("/api/get_by_id/{id}")
async def get_by_id(id:str):
    query = "select * from v_app_detail where id=:id"
    data = {"id":id}
    return one_app_by_query(query,data)

@app.get("/api/search_by_name/{name}")
async def search_by_name(name:str):
    query = "select * from v_app_detail where new_names like :name limit 1"
    data = {"name":'%'+name+'%'}
    return one_app_by_query(query,data)



def one_app_by_query(query,data):
    cur = getdb_cursor() 
    cur.execute(query,data)
    row = cur.fetchone()
    closedb_cursor()
    
    if row == None:
        return {}
    
    expected = 0
    unexpected = 0
    expected_list=[]
    unexpected_list=[]

    sensor_e_data =  SENSOR_EXPECTATION[row["category"]]
    print(sensor_e_data)
    for key in sensor_e_data:
        if sensor_e_data[key]*row[key]==-1:
            unexpected+=1
            unexpected_list.append(SENSOR_EXPLANATION[key])
        elif sensor_e_data[key]*row[key]==1:
            expected+=1
            expected_list.append(SENSOR_EXPLANATION[key])

    permission_list = []
    for item in PERMISSIONS:
        if row[item]==1:
            permission_list.append(item)

    
    retval = {}
    retval["risk_score"]=row["risk_score"]
    retval["unexpected"]=unexpected
    retval["expected"]=expected
    retval["id"]=row["id"]
    retval["new_names"]=row["new_names"]
    retval["category"]=row["category"]
    retval["expected_list"]=expected_list
    retval["unexpected_list"]=unexpected_list
    retval["permission_list"]=permission_list

   
    return retval






app.mount("/", StaticFiles(directory="root",html=True), name="root")

