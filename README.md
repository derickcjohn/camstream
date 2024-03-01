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
- Navigate to the directory where you have extracted the ZIP file to create your virtual environment.
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
### 6. Deactivate Virtual Environment (when finished):
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
