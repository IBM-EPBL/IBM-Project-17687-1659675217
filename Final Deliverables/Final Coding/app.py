from flask import Flask,render_template
app=Flask(__name__, template_folder='templates')
@app.route('/')
def bank():
    return render_template('bankai.html')

if __name__ =='__main__':
    app.run(debug = True)
