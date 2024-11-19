from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define another route for the About page
@app.route('/about')
def about():
    return render_template('about.html')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
