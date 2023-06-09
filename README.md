This is a demo project setup where following steps were followed in creating a end to end project with FLASK App and deployment on AWS beanstalk-->

1. creat a project directory on local and on github with name as "mlproject"
2. on local - create a python environment
3. sync local and git using the PAT (personal access token) using --> git remote set-url origin https://<--PAT Token-->@github.com/<--username-->/<--git project name-->
4. create .gitignore file on git and make sure the above python environment is part of this, so that it doesn't unnecessarily takes backup of these files.
5. add a requirements.txt file, in the end add "-e ." so that it keeps the installation in editable mode. As this whole project is created like a python library, and setup.py is reponsible to control the package hence, while doing the development suppose we are doing "from mlproject import xyz" followed by further commands, in this case if we update our mlproject then we don't need to do " pip install mlproject or python setup.py" but these things will get updated in real time as we have already install the project in editable mode using "-e .". to fix and finalize the installation we need to comment the "-e ." once the development is complete.
6. folder structure -->
    - notebook : to store analysis and dataset based on jupyter notebooks
    - src : contains subfolder as components(e.g. data ingestion, data transformation etc.), pipeline(e.g. prediction pipeline, train pipeline etc.) and some important files as exception (for showing custom expection), logger(to log all the information in separate file), utils(for important utility functions)
    - setup.py : this file handles the python library hence we define all the project details and meta data here, it will also be using requirement.txt to install the libraries
    - logs : the custom logger defined in src folder will be using this folder to store all the relevant informations here
    - artifacts : the ingestion and transformation function will be saving the transformed version of the data in this folder for further analysis
7. useful git commands - 
    - git init [it will initialize the git in the current folder]
    - git add . [it will add all the untracked file/ untracked file changes to git]
    - git commit -m 'your commit message here' [it will commit the changes locally with the given message]
    - git status [it will let you know the sync status between local branch vs github branch e.g. how many commits are required to sync them, which files are not tracked etc.]
    - git branch -M main [enters you in the main branch]
    - git remote set-url origin https://<--PAT Token-->@github.com/<--username-->/<--git project name--> [connect the local git with github]
    - git push -u origin main [push all the local committed changes to remote github branch to make them in sync]
8. useful CMD commands - 
    - python -m venv venv [it will create a virtual environment "venv"]
    - "venv/Scripts/activate" [it activates the virtual environment, here "venv" is the python virtual environment]

9. Process to setup Flask app - 
    - create app.py which controls the flask web app
    - create template folder which will contain all the html pages for the web app
    - app.py will be routing to different pages from template folder itself

10. Deployment to AWS - 
    - Elastic Beanstalk AWS service will be used to host the web app
    - we need to create .ebextentions folder in the project with config files
    - In order to host the web app here we need to rename our app.py to application.py
    - codepipeline aws service will be used for continuous deployment (CD), it integrates with the github repository and if there is any changes on the github repository it will automatically ask whether to deploy those changes on the server (Elastic beanstalk here) 

11. For some reason, AWS Beanstalk was not working when we click on submit button on "/predictdata" page, To resolve this we need to remove the deployment through github and instead upload the zip file and then try deploying the application it worked fine and the model was also able to do the predictions.
    
