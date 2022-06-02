# Set Up Azure Pipelines 

The purpose of this project is to set up an Azure pipeline.

## Steps
1. Run **commands\deploy_app.ps1**. This will create a webapp and deploy it to the web. You can test your application on Postman.
2. Create an Azure DevOps project
3. Set up a new service connection via Azure Resource Manager (go into **project settings**)
    - Scope Level : Subscription
    - Service Connection name : Flask ML App Service
    - Security : grant access to all pipelines
4. Create a new pipeline -> Configure **Python to Linux Web App on Azure**. IMPORTANT : you need to have no **azure-pipelines.yml** at that point in your repo, otherwise you won't have the opportunity to choose your configuration.

A that point, you can see the pipeline in action in the Azure Pipelines.
