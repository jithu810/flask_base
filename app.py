from flask import Flask,render_template,request,make_response,jsonify,session,redirect
app = Flask(__name__)
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)




#-----------------------------------------------DATABASE-------------------------------------------------------------------
import pymongo
from pymongo import MongoClient
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["baseapp"]
mycol = mydb["register"]

#----------------------------------------------------------------------------------------------------------------------------




@app.route('/',methods=['GET','POST'])
def Login():
    if request.method == 'POST':
        data=request.get_json()
        if (len(data))==4:
            print("signup")
            email_exists=mycol.count_documents({"email": data['email']})
            username_exists=mycol.count_documents({"username": data['username']})
            if (email_exists ==0 and username_exists == 0):
                password = bytes(data['password'], 'utf-8')
                password = hashing(password)
                data['password']=password
                mydict = {"_id":mycol.find().count()+1 ,"username":data['username'],"email":data['email'],"password":data['password']}
                x = mycol.insert_one(mydict)
                return "success"
            else:
                return "exists"
        elif(len(data))==2:
            print("login")
            username_exists = mycol.count_documents({"username" : data['username']})
            user = mycol.find({"username" : data['username']})
            if username_exists > 0:
                for i in user:
                    get_hashed_password=i['password']
                    if verify_pass(get_hashed_password,data['password']):
                        print("loged in")
                        return "success"
                    else:
                        return "error"
            else: 
                return "error"
    return render_template("login.html")


@app.route('/user/<username>',methods=['GET','POST'])
def Home(username):
    return render_template("home.html")





def hashing(password):
    pw_hash = bcrypt.generate_password_hash(password)
    return pw_hash
def verify_pass(password,password1):
    return bcrypt.check_password_hash(password,password1)


if __name__=="__main__":
    app.run()
    app.run(debug=True)