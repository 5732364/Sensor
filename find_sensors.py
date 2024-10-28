import os
import re
import sqlite3
import hashlib

SENSOR_KEYWORDS = {
    "TYPE_PROXIMITY": r"TYPE_PROXIMITY|android.hardware.sensor.proximity|sensorManager.getDefaultSensor\(8\)",
    "TYPE_LIGHT": r"TYPE_LIGHT|android.hardware.sensor.light|sensorManager.getDefaultSensor\(5\)",
    "TYPE_ACCELEROMETER": r"TYPE_ACCELEROMETER|android.hardware.sensor.accelerometer|sensorManager.getDefaultSensor\(1\)",
    "TYPE_ORIENTATION": r"TYPE_ORIENTATION|android.hardware.sensor.orientation|sensorManager.getDefaultSensor\(3\)",
    "TYPE_GYROSCOPE": r"TYPE_GYROSCOPE|android.hardware.sensor.gyroscope|sensorManager.getDefaultSensor\(4\)",
    "TYPE_MAGNETIC_FIELD":r"TYPE_MAGNETIC_FIELD|android.hardware.sensor.magnetic_field|sensorManager.getDefaultSensor\(2\)",
    "TYPE_LINEAR_ACCELERATION": r"TYPE_LINEAR_ACCELERATION|android.hardware.sensor.linear_acceleration|sensorManager.getDefaultSensor\(10\)",
    "TYPE_ROTATION_VECTOR": r"TYPE_ROTATION_VECTOR|android.hardware.sensor.rotation_vector|sensorManager.getDefaultSensor\(11\)",
    "TYPE_GRAVITY": r"TYPE_GRAVITY|android.hardware.sensor.gravity|sensorManager.getDefaultSensor\(9\)",
    "TYPE_RELATIVE_HUMIDITY": r"TYPE_RELATIVE_HUMIDITY|android.hardware.sensor.relative_humidity|sensorManager.getDefaultSensor\(12\)",
    "TYPE_TEMPERATURE": r"TYPE_TEMPERATURE|android.hardware.sensor.temperature|sensorManager.getDefaultSensor\(7\)",
    "TYPE_AMBIENT_TEMPERATURE": r"TYPE_AMBIENT_TEMPERATURE|android.hardware.sensor.ambient_temperature|sensorManager.getDefaultSensor\(13\)",
    "TYPE_HEART_RATE": r"TYPE_HEART_RATE|android.hardware.sensor.heartrate|sensorManager.getDefaultSensor\(21\)|sensorManager.getDefaultSensor\(31\)",
    "TYPE_PRESSURE": r"TYPE_PRESSURE|android.hardware.sensor.pressure|sensorManager.getDefaultSensor\(6\)"
}

PERMISSION_KEYWORDS = {
    "android_permission_INTERNET": "android.permission.INTERNET", 
    "android_permission_ACCESS_NETWORK_STATE": "android.permission.ACCESS_NETWORK_STATE", 
    "android_permission_ACCESS_WIFI_STATE": "android.permission.ACCESS_WIFI_STATE",
    "android_permission_BLUETOOTH": "android.permission.BLUETOOTH", 
    "android_permission_BLUETOOTH_ADMIN": "android.permission.BLUETOOTH_ADMIN", 
    "android_permission_VIBRATE": "android.permission.VIBRATE",
    "android_permission_READ_CONTACTS": "android.permission.READ_CONTACTS",
    "android_permission_WRITE_CONTACTS": "android.permission.WRITE_CONTACTS",
    "android_permission_READ_EXTERNAL_STORAGE": "android.permission.READ_EXTERNAL_STORAGE",
    "android_permission_WRITE_EXTERNAL_STORAGE": "android.permission.WRITE_EXTERNAL_STORAGE",
    "android_permission_CAMERA": "android.permission.CAMERA",
    "android_permission_RECORD_AUDIO": "android.permission.RECORD_AUDIO",
    "android_permission_ACCESS_FINE_LOCATION": "android.permission.ACCESS_FINE_LOCATION", 
    "android_permission_ACCESS_COARSE_LOCATION": "android.permission.ACCESS_COARSE_LOCATION",
    "android_permission_READ_PHONE_STATE": "android.permission.READ_PHONE_STATE",
    "android_permission_CALL_PHONE": "android.permission.CALL_PHONE",
    "android_permission_SEND_SMS": "android.permission.SEND_SMS",
    "android_permission_READ_SMS": "android.permission.READ_SMS", 
    "android_permission_SYSTEM_ALERT_WINDOW": "android.permission.SYSTEM_ALERT_WINDOW",
    "android_permission_WRITE_SETTINGS": "android.permission.WRITE_SETTINGS"
}
'''SENSOR_KEYWORDS = {
    "TYPE_PROXIMITY": r"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"
}'''

def find_files_with_keyword(directory, file_type, keyword):
    """
    Args:
        directory
        keyword

    Returns:
        True/False
    """
    print(directory)
    print(keyword)

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(file_type):
                file_path = os.path.join(root, file)
                #print(file_path)
                try:
                    f = open(file_path, 'r', encoding='utf-8')                          
                    if re.search(keyword,f.read()):
                        print(file_path)
                        f.close()
                        return True
                    f.close()
                except:
                    print("Error to process file:{}".format(file_path))
    return False

if __name__ == "__main__":
    directory = "Weather"

    data = {
        "id": "",
        "category": "",
        "name": "",
        "TYPE_PROXIMITY": 0,
        "TYPE_LIGHT": 0,
        "TYPE_ACCELEROMETER": 0,
        "TYPE_ORIENTATION": 0,
        "TYPE_GYROSCOPE": 0,
        "TYPE_MAGNETIC_FIELD": 0,
        "TYPE_LINEAR_ACCELERATION": 0,
        "TYPE_ROTATION_VECTOR": 0,
        "TYPE_GRAVITY": 0,
        "TYPE_RELATIVE_HUMIDITY": 0,
        "TYPE_TEMPERATURE": 0,
        "TYPE_AMBIENT_TEMPERATURE": 0,
        "TYPE_HEART_RATE": 0,
        "TYPE_PRESSURE": 0,
        "android_permission_INTERNET": 0, 
        "android_permission_ACCESS_NETWORK_STATE": 0, 
        "android_permission_ACCESS_WIFI_STATE": 0,
        "android_permission_BLUETOOTH": 0, 
        "android_permission_BLUETOOTH_ADMIN": 0, 
        "android_permission_VIBRATE": 0,
        "android_permission_READ_CONTACTS": 0,
        "android_permission_WRITE_CONTACTS": 0,
        "android_permission_READ_EXTERNAL_STORAGE": 0,
        "android_permission_WRITE_EXTERNAL_STORAGE": 0,
        "android_permission_CAMERA": 0,
        "android_permission_RECORD_AUDIO": 0,
        "android_permission_ACCESS_FINE_LOCATION": 0, 
        "android_permission_ACCESS_COARSE_LOCATION": 0,
        "android_permission_READ_PHONE_STATE": 0,
        "android_permission_CALL_PHONE": 0,
        "android_permission_SEND_SMS": 0,
        "android_permission_READ_SMS": 0, 
        "android_permission_SYSTEM_ALERT_WINDOW": 0,
        "android_permission_WRITE_SETTINGS": 0

    }
       
    

    conn = sqlite3.connect('D:\\projects\\students\\apk_sensor\\apk.db')
    cursor = conn.cursor()
    query = """INSERT INTO app_detail(id, category,name,TYPE_PROXIMITY,TYPE_LIGHT,TYPE_ACCELEROMETER,TYPE_ORIENTATION,
        TYPE_GYROSCOPE,TYPE_MAGNETIC_FIELD,TYPE_LINEAR_ACCELERATION,TYPE_ROTATION_VECTOR,TYPE_GRAVITY,
        TYPE_RELATIVE_HUMIDITY,TYPE_TEMPERATURE,TYPE_AMBIENT_TEMPERATURE,TYPE_HEART_RATE,TYPE_PRESSURE,android_permission_INTERNET,
        android_permission_ACCESS_NETWORK_STATE,android_permission_ACCESS_WIFI_STATE,android_permission_BLUETOOTH, 
        android_permission_BLUETOOTH_ADMIN,android_permission_VIBRATE,android_permission_READ_CONTACTS,
        android_permission_WRITE_CONTACTS,android_permission_READ_EXTERNAL_STORAGE,android_permission_WRITE_EXTERNAL_STORAGE,
        android_permission_CAMERA,android_permission_RECORD_AUDIO,android_permission_ACCESS_FINE_LOCATION, 
        android_permission_ACCESS_COARSE_LOCATION,android_permission_READ_PHONE_STATE,android_permission_CALL_PHONE,
        android_permission_SEND_SMS,android_permission_READ_SMS,android_permission_SYSTEM_ALERT_WINDOW,
        android_permission_WRITE_SETTINGS) VALUES 
        (:id,:category,:name,:TYPE_PROXIMITY,:TYPE_LIGHT,:TYPE_ACCELEROMETER,:TYPE_ORIENTATION,
        :TYPE_GYROSCOPE,:TYPE_MAGNETIC_FIELD,:TYPE_LINEAR_ACCELERATION,:TYPE_ROTATION_VECTOR,:TYPE_GRAVITY,
        :TYPE_RELATIVE_HUMIDITY,:TYPE_TEMPERATURE,:TYPE_AMBIENT_TEMPERATURE,:TYPE_HEART_RATE,:TYPE_PRESSURE,:android_permission_INTERNET,
        :android_permission_ACCESS_NETWORK_STATE,:android_permission_ACCESS_WIFI_STATE,:android_permission_BLUETOOTH, 
        :android_permission_BLUETOOTH_ADMIN,:android_permission_VIBRATE,:android_permission_READ_CONTACTS,
        :android_permission_WRITE_CONTACTS,:android_permission_READ_EXTERNAL_STORAGE,:android_permission_WRITE_EXTERNAL_STORAGE,
        :android_permission_CAMERA,:android_permission_RECORD_AUDIO,:android_permission_ACCESS_FINE_LOCATION, 
        :android_permission_ACCESS_COARSE_LOCATION,:android_permission_READ_PHONE_STATE,:android_permission_CALL_PHONE,
        :android_permission_SEND_SMS,:android_permission_READ_SMS,:android_permission_SYSTEM_ALERT_WINDOW,
        :android_permission_WRITE_SETTINGS)"""

    for dir_name in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, dir_name)):
            print("Processing directory:{}".format(os.path.join(directory, dir_name)))
            data["name"] = dir_name
            data["id"] =  hashlib.md5(data["name"].encode()).hexdigest()
            data["category"] = directory

            for key in SENSOR_KEYWORDS:
                keyword = SENSOR_KEYWORDS[key]
                print("Searching keyword:{}".format(keyword))  
                result = find_files_with_keyword(os.path.join(directory, dir_name),".java",keyword)
                if result:
                    data[key] = 1
                    print("found")
                else:
                    data[key] = 0
                    print("not found")

            for key in PERMISSION_KEYWORDS:
                keyword = PERMISSION_KEYWORDS[key]
                print("Searching keyword:{}".format(keyword))  
                result = find_files_with_keyword(os.path.join(directory, dir_name),".xml",keyword)
                if result:
                    data[key] = 1
                    print("found")
                else:
                    data[key] = 0
                    print("not found")
            
            cursor.execute(query,data)
            conn.commit()