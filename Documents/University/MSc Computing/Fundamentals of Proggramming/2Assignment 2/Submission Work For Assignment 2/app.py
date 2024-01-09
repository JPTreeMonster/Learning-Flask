from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3

app = Flask(__name__)

# Database connections
DATABASE_INDEX = 'IndexComments.db'
DATABASE_EDUCATION = 'EducationComments.db'
DATABASE_EXPERIENCE = 'ExperienceComments.db'
DATABASE_WORK = 'WorkComments.db'
DATABASE_LOGIN = 'LoginDetails.db'
DATABASE_INQUIRY = 'Inquiries.db'


# Render routes
@app.route('/Login')
def login():
    return render_template('Login.html')

@app.route('/LoggedIn')
def logged_in_page():
    return render_template('LoggedIn.html')

@app.route('/')
def education():
    comments = fetch_comments(DATABASE_INDEX)
    return render_template('Index.html', comments=comments)

@app.route('/EducationPage')
def education_page():
    comments = fetch_comments(DATABASE_EDUCATION)
    return render_template('Education.html', comments=comments)


@app.route('/Experience')
def experience():
    comments = fetch_comments(DATABASE_EXPERIENCE)
    return render_template('Experience.html', comments=comments)

@app.route('/Work')
def work():
    comments = fetch_comments(DATABASE_WORK)
    return render_template('Work.html', comments=comments)

@app.route('/Inquiry')
def inquiry_page():
    return render_template('Inquiry.html')





# Database routes
@app.route('/Login_Check', methods=['POST'])
def login_post():
    if request.method == 'POST':
        username = request.form.get('username', default='Error')
        password = request.form.get('password', default='Error')
        conn = sqlite3.connect(DATABASE_LOGIN)
        cur = conn.cursor()
        cur.execute("SELECT * FROM LoginDetailsTable WHERE username = ? AND password = ?", (username, password))
        user = cur.fetchone()
        conn.close()
        if user:
            return redirect('/LoggedIn')
        else:
            return redirect('/Login')
        

@app.route('/get_inquiries', methods=['GET'])
def get_inquiries():
    inquiry = fetch_inquiries(DATABASE_INQUIRY)
    return jsonify(inquiry)

def fetch_inquiries(database):
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM InquireTable ORDER BY ID DESC")
    inquiries = cur.fetchall()
    conn.close()
    return inquiries




        


@app.route('/add_comment', methods=['POST'])
def add_comment():
    if request.method == 'POST':
        name = request.form.get('name', default='Error')
        comment_text = request.form.get('comment', default='Error')
        page = request.form.get('page')
    
        insert_comment(name, comment_text, page)

        return redirect(request.referrer)
    
@app.route('/Inquiry', methods=['GET', 'POST'])
def inquiry():
    if request.method == 'POST':
        name = request.form.get('name', default='Error')
        email = request.form.get('email', default='Error')
        inquiry = request.form.get('inquiry', default='Error')
        conn = sqlite3.connect(DATABASE_INQUIRY)
        cur = conn.cursor()
        cur.execute("INSERT INTO InquireTable ('name', 'email', 'inquiry')\
                    VALUES (?, ?, ?)", (name, email, inquiry))
        conn.commit()
        conn.close()
    return render_template('Inquiry.html')



# Helper function to fetch comments from the database
def fetch_comments(database):
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM CommentTable ORDER BY id DESC")
    comments = cur.fetchall()
    conn.close()
    return comments

# Helper function to insert a comment into the appropriate database
def insert_comment(name, comment_text, page):
    database = get_database_for_page(page)
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute("INSERT INTO CommentTable ('name', 'comment') VALUES (?, ?)", (name, comment_text))
    conn.commit()
    conn.close()

# Helper function to determine the appropriate database for a page
def get_database_for_page(page):
    if page == 'Index':
        return DATABASE_INDEX
    elif page == 'Education':
        return DATABASE_EDUCATION
    elif page == 'Experience':
        return DATABASE_EXPERIENCE
    else:
        return DATABASE_WORK

if __name__ == '__main__':
    app.run(debug=True)
