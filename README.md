# Set Up Azure Pipelines 

The purpose of this project is to set up an Azure pipeline.

## Steps
1. Run **commands\deploy_app.ps1**. This will create a webapp and deploy it to the web.
2. Create an Azure DevOps project
3. Set up a new service connection via Azure Resource Manager (go into **project settings**)
    - Scope Level : Subscription
    - Service Connection name : Flask ML App Service
    - Security : grant access to all pipelines
4. Create a new pipeline -> Configure **Python to Linux Web App on Azure**

You can test your application on Postman.
