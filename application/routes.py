from application import app, db
from flask import render_template,url_for
from flask import request,json,Response,redirect,flash,session
from application.models import User,Course,Enrollment
from application.forms import LoginForm,RegisterForm
courseData = [{"courseID":"1111","title":"PHP 101","description":"Intro to PHP","credits":3,"term":"Fall, Spring"}, {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":4,"term":"Spring"}, {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":3,"term":"Fall"}, {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":3,"term":"Fall, Spring"}, {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":4,"term":"Fall"}]

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html",index=True)

@app.route("/login",methods = ['GET','POST'])
def login():
    if session.get('username'):
        return redirect((url_for('index')))

    form = LoginForm()
    if form.validate_on_submit()==True:
        email = form.email.data
        password = form.password.data
        user = User.objects(email=email).first()


        if user and user.get_password(password):  
            flash(f"{user.first_name}, You are successfully logged in!","success")
            session['user_id']=user.user_id
            session['username'] = user.first_name
            return redirect("/index")
        else:
            flash("Something went wrong.","danger")
    return render_template("login.html",title = "Login", form = form, login=True)



@app.route("/logout")
def logout():
    session["user_id"] = False
    session.pop("username",None)
    return redirect(url_for("index"))    





@app.route("/courses/",methods = ['GET','POST'])
@app.route("/courses/<term>")
def courses(term = None):
    if term is None:
        term = "Spring 2019"
    
    classes = Course.objects.all()


    return render_template("courses.html",courseData=classes,courses=True,term=term)



@app.route("/register",methods = ['GET','POST'])
def register():
    if session.get("username"):
        return redirect((url_for('index')))
    form = RegisterForm()
    if form.validate_on_submit():
        user_id = User.objects.count()
        user_id +=1
        email = form.email.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        user = User(user_id=user_id,email = email, first_name= first_name,last_name = last_name)
        user.set_password(password)
        user.save()
        flash("You are succesfuly registered","success")
        return redirect(url_for("index"))


    return render_template("register.html",title = "Register",form=form,register=True)




@app.route("/enrollment",methods = ["GET","POST"])
def enrollment():
    if not session.get('username'):
        return redirect((url_for('login')))
    
    courseID = request.form.get('courseID')
    courseTitle = request.form.get('title')
    user_id = session.get("user_id")

    if courseID:
        if Enrollment.objects(user_id=user_id, courseID=courseID):
            flash(f"Oops! You are already registered in this course {courseTitle}!", "danger")
            return redirect(url_for("courses"))
        else:
            Enrollment(user_id=user_id, courseID=courseID).save()
            flash(f"You are enrolled in {courseTitle}!", "success")

    # Get enrollments
    enrollments = Enrollment.objects(user_id=user_id)
    courseData = []
    for enrollment in enrollments:
        # Get the full course details for each enrollment
        course = Course.objects(courseID=enrollment.courseID).first()
        if course:
            # Convert the course document to a dictionary format matching your template
            courseData.append({
                "courseID": course.courseID,
                "title": course.title,
                "description": course.description,
                "credits": course.credits,
                "term": course.term
            })

    return render_template("enrollment.html", enrollment=True, title="Enrollment",
                        courseData=courseData)  # Changed classes to courseData


@app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):
    if(idx == None):
        jdata = courseData
    else:
        jdata = courseData[int(idx)]
    
    return Response(json.dumps(jdata),mimetype= "application/json")



@app.route("/user")
def user():
    #User(user_id=1,first_name = "Christian",last_name="Hur",email = "christian@uta.com",password = "abc1234").save()
    #User(user_id=2,first_name = "Marry",last_name="Williams",email = "marry@sda.com",password = "dexter1234").save()

    users = User.objects.all()
    return render_template("user.html",users=users)

