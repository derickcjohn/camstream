# Cam Stream Data: Daily and Weekly Detections

## Install Python and Set Up Virtual Environment
### Before running this application, install Python and set up a virtual environment.
### 1. Install Python:
- Visit the official [Python website](https://www.python.org/downloads/) and download the latest version for your operating system.
- Follow the installation instructions provided on the website.
### 2. Downloading the Github repo:
- Click the "Code" button and select "Download ZIP".
### 3. Extract the downloaded file:
- Once the download is complete, locate the downloaded ZIP file on your system.
- Extract the contents of the ZIP file to your desired location.
### 4. Set Up Virtual Environment
- Open a terminal or command prompt.
- Navigate to the directory where you have extracted the ZIP file using `cd` to create your virtual environment.
  ```
  cd <path to the directory>
  ```
- Use the following command to create a virtual environment named `myenv` or anything you choose:
  ```
  python -m venv myenv
  ```
### 5. Activate Virtual Environment:
- In Windows OS:
  ```
  myenv\Scripts\activate
  ```
- In macOS/Linux OS:
  ```
  source myenv/bin/activate
  ```
#### Your terminal prompt will change to indicate that the virtual environment is active.
### 6. Install Dependencies:
- Run the following command to install dependencies from the `requirements.txt` file:
  ```
  pip install -r requirements.txt
  ```
### 7. Running the Streamlit app:
- After the dependencies are installed, type the below command in the terminal to run the Streamlit app:
  ```
  streamlit run Live.py
  ```
- You will see this below, and the Streamlit app will run in your browser.
![image](https://github.com/derickcjohn/camstream/assets/96041141/85b4eb26-c04b-4c61-a186-0708ac959d7e)
- To make this app available online for others to access, you need to use ngrok.
### 8. Downloading ngrok:
- Go to the [ngrok](https://ngrok.com/download) website.
- Select the 'Windows' version and download the ZIP file. 
- Extract the downloaded ZIP file to C drive.
- Also, signup in ngrok, to get the `authtoken`, which will be required in the upcoming steps.
### 9. Setting up Environment variables:
- Type `env` in the windows search bar and select `Edit the system environment variables` option.
![image](https://github.com/derickcjohn/camstream/assets/96041141/166d81c4-4b57-46fb-a9d3-2ef36cda2743)
- Click on `Environment variables..` option in the System properties dialogue box.
  ![image](https://github.com/derickcjohn/camstream/assets/96041141/366924ca-ea09-4b6c-845d-629221aedf3d)
- Select `Path` within `System variables` and then click `Edit`.
![image](https://github.com/derickcjohn/camstream/assets/96041141/54e9997b-c402-4c32-ad40-386e17481ecb)
- Go to the extracted ngrok directory and copy the path to the directory, it would be something like this:
  ```
  C:\ngrok
  ```
- In the `Edit environment variable` dialogue box, click on `New` and paste the path to the ngrok directory.
![image](https://github.com/derickcjohn/camstream/assets/96041141/dbce7384-9cf3-4024-9428-89dd6d28a1cf)
- Then click `OK` on all three tabs.

### 8. Deactivate Virtual Environment (when finished):
```
deactivate
```
This will deactivate the virtual environment and return you to your system-wide Python installation.
  
## Live
This application offers a user-friendly interface for visualizing daily and weekly object detection data sourced from an Excel spreadsheet. Users can choose a specific date to explore corresponding daily detection counts for each hour and weekly detection counts for the selected week.

## Demo
Explore real-time object detection using our custom-trained YOLOv5 model on this page.

---

**Note: ** Please make sure you install the required dependencies before running the application.
