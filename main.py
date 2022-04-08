from flask import Flask,render_template,request


app=Flask(__name__)
app.config['SECRET_KEY'] = "cc7c83c25c81641609b40dbaf2038e12"

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template("about.html")

@app.route('/help', methods=['GET', 'POST'])
def help():
    return render_template("help.html")

@app.route('/CheckExam', methods=['GET', 'POST'])
def CheckExam():
    examtime=0
    result=0
    seatlocation=0
    print(type(request.form.get("Examdatedept")))
    print(request.form.get("Examdateyr"))
    print(request.form.get("checkseatrollno"))
    print(request.form.get("checkseatdept"))
    print(request.form.get("checkseatyr"))
    
    if request.form.get("Examdatedept")=="BSCIT" or request.form.get("Examdatedept")=="BSCCS":
        if request.form.get("Examdateyr")=="first":
            examtime=[["10-apr","11.00 am-1.00 pm","Maths"],["11-apr","11.00 am-1.00 pm","Microprocessor"],["12-apr","11.00 am-1.00 pm","Graphics"],
                        ["14-apr","11.00 am-1.00 pm","OS"],["15-apr","11.00 am-1.00 pm","Network"],["16-apr","11.00 am-1.00 pm","OOPS"]]
        elif request.form.get("Examdateyr")=="second":
            examtime=[["10-apr","09.00 am-11.00 am","Java"],["11-apr","09.00 am-11.00 am","Python"],["12-apr","09.00 am-11.00 am","embedded"],
                        ["14-apr","09.00 am-11.00 am","Computing"],["15-apr","09.00 am-11.00 am","WebProj"],["16-apr","09.00 am-11.00 am","Network"]]
        elif request.form.get("Examdateyr")=="final":
            examtime=[["10-apr","02.00 pm-04.00 pm","IOT"],["11-apr","02.00 pm-04.00 pm","Cyberlaw"],["12-apr","02.00 pm-04.00 pm","NGT"],
                        ["14-apr","02.00 pm-04.00 pm","SIC"],["15-apr","02.00 pm-04.00 pm","GIS"],["16-apr","02.00 pm-04.00 pm","BI"]]
        else:
            examtime=0
        return render_template("exam.html",exam=1,seat=0,examdetails=examtime,location=seatlocation)
        
    seatingarr={"bscit":{"first":[{"roomno":"IT-10","rollno":[0,25]},{"roomno":"IT-11","rollno":[25,50]}],
                    "second":[{"roomno":"IT-20","rollno":[0,25]},{"roomno":"IT-21","rollno":[25,50]}],
                    "final":[{"roomno":"IT-30","rollno":[0,25]},{"roomno":"IT-31","rollno":[25,50]}]
                    },
                "bsccs":{"first":[{"roomno":"CS-10","rollno":[0,25]},{"roomno":"CS-11","rollno":[25,50]}],
                        "second":[{"roomno":"CS-20","rollno":[0,25]},{"roomno":"CS-21","rollno":[25,50]}],
                        "final":[{"roomno":"CS-30","rollno":[0,25]},{"roomno":"CS-31","rollno":[25,50]}]
                    }
                }

    if request.form.get("checkseatdept")=="BSCIT":
        if str(request.form.get("checkseatrollno"))!="None" and str(request.form.get("checkseatrollno"))!="":
            rollno=str(request.form.get("checkseatrollno"))
            if rollno[0:2]=="IT":
                result=seatingarr["bscit"]
            if rollno[0:2]=="CS":
                result=seatingarr["bsccs"]
            if rollno[2:4]=="01":
                result=result["first"]
            if rollno[2:4]=="02":
                result=result["second"]
            if rollno[2:4]=="03":
                result=result["final"]
            lastdigit=rollno[4:6]
            for norange in result:
                if int(lastdigit)<=norange["rollno"][1] and int(lastdigit)>norange["rollno"][0]:
                    seatlocation=norange["roomno"]
        return render_template("exam.html",exam=0,seat=1,location=seatlocation, examdetails=examtime)
    return render_template("exam.html",exam=0,seat=0,location=seatlocation,examdetails=examtime)

@app.route('/FillFees', methods=['GET', 'POST'])
def FillFees():
    return render_template("adminfees.html")

@app.route('/RegisterEvents', methods=['GET', 'POST'])
def RegisterEvents():
    return render_template("events.html")

if __name__=="__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)