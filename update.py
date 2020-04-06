import pyrebase

config = {
    "apiKey": "AIzaSyBxf5MTJh0eI44gPjvaq3fNIAfqhIkFIdo",
  "authDomain": "myattendance-63f2c.firebaseapp.com",
  "databaseURL": "https://myattendance-63f2c.firebaseio.com",
  "projectId": "myattendance-63f2c",
  "storageBucket": "myattendance-63f2c.appspot.com",
  "messagingSenderId": "689901084281",
  "appId": "1:689901084281:web:036d896307c85821587ea8",
  "measurementId": "G-F9GDBD3ZT9"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

#db.child("names").push({"name":"shom"})
#db.child("names").remove({"name":"shouhardiksha"})
#data={"email id":"shomabc@gmail.com"}
#db.child("names").push(data)
#db.child("names").update({"name":"abcd"})
#user=db.child("names").shallow.get()
#names = db.child("names").get()
#print(names.val())
#db.child("france").push({"capital":"Paris"})
#db.child("france").push({"food":"baguette"})


#print(user.key())
#db.child("user").child("id").push({"name":"shomsaha"})
#db.child("user").push({"emil":"abc@gmail.com"})
#db.child("user").push({"password":"1234"})
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def basic():
    if request.method == 'POST':
      data = request.form.get('name')
      
       
      db.child("user").push(data)
      flag = db.child("user").get()
      pl = flag.val()
      return render_template('file.html', t=pl.values())
   
  
      
    return render_template('file.html')



if __name__== "__main__":
   app.run(debug=True)



         
         
         
        
 
     
