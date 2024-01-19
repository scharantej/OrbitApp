
# Import necessary modules
from flask import Flask, render_template

# Create a Flask application
app = Flask(__name__)

# Define the main route
@app.route('/')
def index():
    """
    Renders the main page of the application.
    """
    return render_template('index.html')

# Define the route for the projects page
@app.route('/projects')
def projects():
    """
    Renders the projects page, displaying a list of all projects.
    """
    projects = [
        {'name': 'Project 1', 'description': 'Description of Project 1', 'lead': 'Lead 1'},
        {'name': 'Project 2', 'description': 'Description of Project 2', 'lead': 'Lead 2'},
        {'name': 'Project 3', 'description': 'Description of Project 3', 'lead': 'Lead 3'}
    ]
    return render_template('projects.html', projects=projects)

# Define the route for a specific project page
@app.route('/project/<project_name>')
def project(project_name):
    """
    Renders the dedicated page for a specific project.
    """
    project = {
        'name': project_name,
        'description': 'Detailed description of the project',
        'historical_context': 'Historical context, challenges, and achievements',
        'images': ['image1.png', 'image2.png']
    }
    return render_template('project-name.html', project=project)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
