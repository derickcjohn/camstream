# Cam Stream Data: Daily and Weekly Detections

## Install Python and Set Up Virtual Environment
### Before running this application, install Python and set up a virtual environment.
### 1. Install Python:
- Visit the official [Python website](https://www.python.org/downloads/) and download the latest version for your operating system.
- Follow the installation instructions provided on the website.
### 2. Set Up Virtual Environment
- Open a terminal or command prompt.
- To create your virtual environment, navigate to the project's directory using `cd <path to the directory>`. Below is an example
  ```
  cd D:\Documents\Project
  ```
- Use the following command to create a virtual environment named `myenv` or anything you choose:
  ```
  python -m venv myenv
  ```
- Activate Virtual Environment:
  ```
  myenv\Scripts\activate
  ```
#### Your terminal prompt will change to indicate that the virtual environment is active.

## Working with Google Sheets API
### 1. Installing libraries:
- Open the command prompt or the terminal in the project folder, create a virtual environment (optional), and type:
```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
### 2. Creating a project:
- Head over to [Google APIS & services](https://console.cloud.google.com/projectselector2/apis/dashboard?supportedpurview=project) and create a new project.
  ![image](https://github.com/derickcjohn/camstream/assets/96041141/34191cb4-ee8e-4452-8dc1-31ff781069d1)
- Then name your project. Just make sure it's something unique.
  ![image](https://github.com/derickcjohn/camstream/assets/96041141/3992aab2-bd62-405b-9f90-85802f18dc88)
- After adding other details, click `CREATE`.
- Once the project is created, you need to activate it.
- Select the project
  ![image](https://github.com/derickcjohn/camstream/assets/96041141/6b8958a1-4f39-44cb-9698-c53f4f08739a)
- Now, you need to enable the Google Sheets API.
- Search for it, and select `Google Sheets API`.
  ![image](https://github.com/derickcjohn/camstream/assets/96041141/2aedc975-2f10-4a19-a173-e329e85be338)
- Then click on `Enable`.
  ![image](https://github.com/derickcjohn/camstream/assets/96041141/c9f81b59-5a09-467a-9273-ad0b39518444)
- Click on `Create Credentials`
- Select `Application Data`.
  ![image](https://github.com/derickcjohn/camstream/assets/96041141/bde2817b-5959-463f-bfa3-22464b1eef5b)
- Fill in the Service Account details, then click `Create and Continue`.
  ![image](https://github.com/derickcjohn/camstream/assets/96041141/203fd831-f2e6-4eb0-a69e-39d88cd0f2eb)
- Then select the `Editor` role to allow write access.
- Then click `Continue` and `Done`.
- Scroll down and click on Credentials to see the service account there.
  ![image](https://github.com/derickcjohn/camstream/assets/96041141/34aa82da-571c-4293-8c05-efc1f44b7e65)
- Copy the service account ID and give Edit access to it in the Google Sheets.
- Click on the service email ID and select `KEYS` at the top.
  ![image](https://github.com/derickcjohn/camstream/assets/96041141/1a78c606-3060-468b-b6c9-a726819cca03)
- Select `ADD KEY`, then `New Key`.
- The key is going to be `json`
- Save the file to the project directory as `keys.json`.
## Hosting website using Streamlit Cloud
### 1. Creating an account in GitHub:
- Add all the necessary files to the GitHub repository.
### 2. Streamlit Cloud:
- Go to the [Streamlit cloud](https://streamlit.io/cloud) and sign up with your GitHub account.
- Enter your GitHub credentials and click “Authorize Streamlit” to let Streamlit access your GitHub account.
- Click on the down arrow next to "New app", and select "Use existing repo".
  ![image](https://github.com/derickcjohn/camstream/assets/96041141/b6796601-d0a7-4ef9-b764-57ee357a6973)
- Type in the name of your repo, the Branch which will most probably be `main`, the name of the main `.py` file that will be running, and an app URL with which users can access your website.
  ![image](https://github.com/derickcjohn/camstream/assets/96041141/7c1bdca4-89af-4138-9b74-aa7a50df7e75)
- This will spin up a new server. You’ll see the message, “Your app is in the oven.”
- In the bottom right-hand corner, click “Manage app” to see the log messages (use them for debugging and troubleshooting errors)
  ![image](https://github.com/derickcjohn/camstream/assets/96041141/df1d134a-9f00-489d-a802-a4920412619a)
- Once your app finishes compiling, you’ll see the output.

