/* empty css             *//* empty css                     */import{_ as c,r as v,c as u,a as d,b as e,w as n,u as m,x as _,F as y,E as S,o as h,e as o,f,g}from"./index-BhSee-FG.js";const E={class:"Header"},T={__name:"index",setup(A){const t=f();var l=v("4");const p=s=>{console.log(s),l.value=s,s==1?t.push("/Main"):s==2?t.push("/Categories"):s==3?t.push("/Application"):s==4&&t.push("/Sensors")};return(s,a)=>{const i=g,r=S;return h(),u(y,null,[d("div",E,[a[4]||(a[4]=d("div",{class:"logo"},null,-1)),e(r,{"default-active":m(l),class:"el-menu-demo",mode:"horizontal",onSelect:p,style:{width:"80%"}},{default:n(()=>[e(i,{index:"1"},{default:n(()=>a[0]||(a[0]=[o("Home")])),_:1}),e(i,{index:"2"},{default:n(()=>a[1]||(a[1]=[o("Categories")])),_:1}),e(i,{index:"3"},{default:n(()=>a[2]||(a[2]=[o("Applications")])),_:1}),e(i,{index:"4"},{default:n(()=>a[3]||(a[3]=[o("Sensors/Permission Data")])),_:1})]),_:1},8,["default-active"])]),a[5]||(a[5]=_('<div class="main" data-v-86d25e72><h1 class="title" data-v-86d25e72>Description</h1><div class="introduce" data-v-86d25e72><h2 data-v-86d25e72>About Sensor</h2><div class="information" data-v-86d25e72> Sensors are essential in today&#39;s mobile devices, it can be used to pick up stuffs like motion, light, and temperature. Sensors enable responsive interactions, allowing apps more functionality while also raising concerns of over collecting data.: </div><ul class="list" data-v-86d25e72><li class="list_one" data-v-86d25e72><span class="Sensor_Type" data-v-86d25e72>Proximity Sensor:</span><span class="Explanation" data-v-86d25e72>Detects the presence of objects near the device, useful for gesture-based controls or turning off the display during reading sessions. May be misused to track user proximity without explicit knowledge.</span></li><li class="list_one" data-v-86d25e72><span class="Sensor_Type" data-v-86d25e72>Light Sensor:</span><span class="Explanation" data-v-86d25e72>Adjusts screen brightness based on ambient light, enhancing readability of educational content in varying lighting conditions. Minimal privacy risk, but could infer environmental context.</span></li><li class="list_one" data-v-86d25e72><span class="Sensor_Type" data-v-86d25e72>Accelerometer:</span><span class="Explanation" data-v-86d25e72>Tracks motion and movement, allowing for interactive experiences like virtual experiments or simulations. Could be used to track precise movements and behavior patterns, raising privacy concerns if misused.</span></li><li class="list_one" data-v-86d25e72><span class="Sensor_Type" data-v-86d25e72>Orientation Sensor:</span><span class="Explanation" data-v-86d25e72>The Orientation Sensor detects the angular position of a device along its axes but is now deprecated. It has been replaced by more accurate sensors like the Rotation Vector Sensor for better tracking in modern applications requiring device orientation.</span></li><li class="list_one" data-v-86d25e72><span class="Sensor_Type" data-v-86d25e72>Gyroscope:</span><span class="Explanation" data-v-86d25e72>The Gyroscope measures the device’s rotation rate around its axes, providing precise data for tracking 3D movement. It&#39;s commonly used in AR/VR applications, gaming, and simulations to enhance motion tracking and improve user interaction.</span></li><li class="list_one" data-v-86d25e72><span class="Sensor_Type" data-v-86d25e72>Magnetic Field Sensor:</span><span class="Explanation" data-v-86d25e72>Detects the Earth’s magnetic field to provide compass functionality. Limited use in education apps but could raise concerns about location tracking if combined with GPS.</span></li><li class="list_one" data-v-86d25e72><span class="Sensor_Type" data-v-86d25e72>Linear Acceleration Sensor:</span><span class="Explanation" data-v-86d25e72>Measures acceleration excluding gravity, rarely used in educational apps. Could raise privacy concerns if tracking detailed movement data without user consent.</span></li><li class="list_one" data-v-86d25e72><span class="Sensor_Type" data-v-86d25e72>Rotation Vector Sensor:</span><span class="Explanation" data-v-86d25e72>Tracks device rotation in 3D space, useful in AR/VR-based educational simulations. Privacy concerns may arise from unnecessary collection of orientation data.</span></li><li class="list_one" data-v-86d25e72><span class="Sensor_Type" data-v-86d25e72>Gravity Sensor:</span><span class="Explanation" data-v-86d25e72>Detects the device’s orientation relative to gravity, useful in specific physics-related educational content. Minimal risk, but its collection may be unnecessary.</span></li><li class="list_one" data-v-86d25e72><span class="Sensor_Type" data-v-86d25e72>Pressure Sensor:</span><span class="Explanation" data-v-86d25e72>Measures atmospheric pressure, typically used in environmental science apps or altitude-related educational content. Minimal privacy risk as it collects general environmental data.</span></li><li class="list_one" data-v-86d25e72><span class="Sensor_Type" data-v-86d25e72>Relative Humidity Sensor:</span><span class="Explanation" data-v-86d25e72>Measures environmental humidity, rarely relevant to educational content. Minimal risk due to its limited functionality.</span></li><li class="list_one" data-v-86d25e72><span class="Sensor_Type" data-v-86d25e72>Temperature Sensor:</span><span class="Explanation" data-v-86d25e72>Measures the device’s internal temperature, irrelevant to educational content. Minimal privacy risk due to its deprecated status.</span></li><li class="list_one" data-v-86d25e72><span class="Sensor_Type" data-v-86d25e72>Ambient Temperature Sensor:</span><span class="Explanation" data-v-86d25e72>Measures surrounding environmental temperature, potentially useful for environmental science education but generally irrelevant to most educational apps. Could infer whether a user is indoors or outdoors, leading to indirect privacy concerns.</span></li><li class="list_one" data-v-86d25e72><span class="Sensor_Type" data-v-86d25e72>Heart Rate Monitor:</span><span class="Explanation" data-v-86d25e72>Monitors heart rate, mainly relevant in fitness or health education apps. Raises significant privacy concerns due to the sensitive nature of health data.</span></li></ul></div><div class="introduce" data-v-86d25e72><h2 data-v-86d25e72>About Permission</h2><div class="information" data-v-86d25e72> Permissions in Android apps manage access to key device features like location, camera and contacts. They let apps function properly while giving users control over their data.: </div><ul class="list" data-v-86d25e72><li class="list_one" data-v-86d25e72><span class="Sensor_Type" data-v-86d25e72>android.permission.INTERNET:</span><span class="Explanation" data-v-86d25e72>Allows apps to access the internet. Required for apps that need to fetch data from the web or use web services.</span></li><li class="list_one" data-v-86d25e72><span class="Sensor_Type" data-v-86d25e72>android.permission.ACCESS_NETWORK_STATE:</span><span class="Explanation" data-v-86d25e72>Allows apps to check if the device is connected to a network (Wi-Fi, mobile data). Commonly used to monitor network status.</span></li><li class="list_one" data-v-86d25e72><span class="Sensor_Type" data-v-86d25e72>android.permission.ACCESS_WIFI_STATE:</span><span class="Explanation" data-v-86d25e72>Allows apps to access information about Wi-Fi networks, such as connection status. Often used for connectivity or data sync.</span></li><li class="list_one" data-v-86d25e72><span class="Sensor_Type" data-v-86d25e72>android.permission.BLUETOOTH:</span><span class="Explanation" data-v-86d25e72>Enables apps to communicate with Bluetooth devices such as headphones, fitness trackers, and smartwatches.</span></li><li class="list_one" data-v-86d25e72><span class="Sensor_Type" data-v-86d25e72>android.permission.BLUETOOTH_ADMIN:</span><span class="Explanation" data-v-86d25e72>Allows apps to pair with and manage Bluetooth connections, used for managing connected Bluetooth devices.</span></li><li class="list_one" data-v-86d25e72><span class="Sensor_Type" data-v-86d25e72>android.permission.VIBRATE:</span><span class="Explanation" data-v-86d25e72>Allows apps to control the vibration of the device. Common in gaming, notifications, or haptic feedback in apps.</span></li><li class="list_one" data-v-86d25e72><span class="Sensor_Type" data-v-86d25e72>android.permission.READ_CONTACTS:</span><span class="Explanation" data-v-86d25e72>Allows apps to read the user’s contact list, typically used in social media or communication apps for accessing friends or contacts.</span></li><li class="list_one" data-v-86d25e72><span class="Sensor_Type" data-v-86d25e72>android.permission.WRITE_CONTACTS:</span><span class="Explanation" data-v-86d25e72>Allows apps to modify or delete the user’s contacts, typically seen in contact management or sync apps.</span></li><li class="list_one" data-v-86d25e72><span class="Sensor_Type" data-v-86d25e72>android.permission.READ_EXTERNAL_STORAGE:</span><span class="Explanation" data-v-86d25e72>Allows apps to read data from external storage, such as photos or documents stored on an SD card.</span></li><li class="list_one" data-v-86d25e72><span class="Sensor_Type" data-v-86d25e72>android.permission.WRITE_EXTERNAL_STORAGE:</span><span class="Explanation" data-v-86d25e72>Allows apps to write data to external storage. Common for apps that store files, such as media or document apps.</span></li><li class="list_one" data-v-86d25e72><span class="Sensor_Type" data-v-86d25e72>android.permission.CAMERA:</span><span class="Explanation" data-v-86d25e72>Allows apps to access the device’s camera for taking pictures, recording videos, or scanning QR codes. Common in social media, video conferencing, and AR apps.</span></li><li class="list_one" data-v-86d25e72><span class="Sensor_Type" data-v-86d25e72>android.permission.RECORD_AUDIO:</span><span class="Explanation" data-v-86d25e72>Allows apps to record audio using the device&#39;s microphone, used in voice recording apps, video calls, and voice assistants.</span></li><li class="list_one" data-v-86d25e72><span class="Sensor_Type" data-v-86d25e72>android.permission.ACCESS_FINE_LOCATION:</span><span class="Explanation" data-v-86d25e72>Allows apps to access precise location using GPS. Commonly used in navigation, mapping, and location-based apps.</span></li><li class="list_one" data-v-86d25e72><span class="Sensor_Type" data-v-86d25e72>android.permission.ACCESS_COARSE_LOCATION:</span><span class="Explanation" data-v-86d25e72>MAllows apps to access approximate location using network-based location services. Used in weather apps and services that don’t need precise location.</span></li><li class="list_one" data-v-86d25e72><span class="Sensor_Type" data-v-86d25e72>android.permission.READ_PHONE_STATE:</span><span class="Explanation" data-v-86d25e72>MeasuAllows apps to access information about the device’s phone state, such as the number, network status, or ongoing calls.</span></li><li class="list_one" data-v-86d25e72><span class="Sensor_Type" data-v-86d25e72>android.permission.CALL_PHONE:</span><span class="Explanation" data-v-86d25e72>Allows apps to initiate phone calls directly from the app. Used in dialers and contact apps.</span></li><li class="list_one" data-v-86d25e72><span class="Sensor_Type" data-v-86d25e72>android.permission.SEND_SMS:</span><span class="Explanation" data-v-86d25e72>Allows apps to send SMS messages. Used in messaging apps or for verification codes sent via text.</span></li><li class="list_one" data-v-86d25e72><span class="Sensor_Type" data-v-86d25e72>android.permission.READ_SMS:</span><span class="Explanation" data-v-86d25e72>Allows apps to read incoming SMS messages. Common in messaging apps and for receiving verification codes.</span></li><li class="list_one" data-v-86d25e72><span class="Sensor_Type" data-v-86d25e72>android.permission.SYSTEM_ALERT_WINDOW:</span><span class="Explanation" data-v-86d25e72>Allows apps to create floating windows on top of other apps, like chat bubbles or heads-up notifications.</span></li><li class="list_one" data-v-86d25e72><span class="Sensor_Type" data-v-86d25e72>android.permission.WRITE_SETTINGS:</span><span class="Explanation" data-v-86d25e72>Allows apps to modify system settings, such as changing Wi-Fi, screen brightness, or Bluetooth settings.</span></li></ul></div></div>',1))],64)}}},k=c(T,[["__scopeId","data-v-86d25e72"]]);export{k as default};
