## **Flask Application Design: Columbia Space Project**

### **HTML Files**

**1. index.html:**
- **Purpose:** Serves as the main page of the application, introducing the Columbia Space Project.
- **Content:**
 - Header with title: Columbia Space Project
 - Brief introduction to the project
 - Link to the /projects page for further details

**2. projects.html:**
- **Purpose:** Displays a list of all the projects undertaken as part of the Columbia Space Project.
- **Content:**
 - Header with title: Projects
 - Table with the following columns: Project Name, Project Description, Project Lead
 - Link to each project's individual page on the /project/* route

**3. project-name.html:**
- **Purpose:** Dedicated page for each project, providing detailed information and historical context.
- **Content:**
 - Header with project name as title
 - Detailed description of the project
 - Historical context, challenges, and achievements
 - Images or diagrams related to the project

### **Routes**

**1. @app.route('/')** (GET):
- **Purpose:** Displays the main page of the application.
- **Functionality:** Renders the index.html file, introducing the Columbia Space Project.

**2. @app.route('/projects')** (GET):
- **Purpose:** Displays a list of all the projects undertaken as part of the Columbia Space Project.
- **Functionality:** Renders the projects.html file, displaying the list of projects in a tabular format, with links to individual project pages.

**3. @app.route('/project/<project_name>')** (GET):
- **Purpose:** Displays the dedicated page for a specific project.
- **Functionality:** Renders the project-name.html file, providing detailed information and historical context for the project. The <project_name> variable in the route captures the name of the project, allowing for dynamic page generation.