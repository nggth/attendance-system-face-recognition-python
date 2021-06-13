# attendance-system-face-recognition-python
Face Recognition Based Attendance Management System (using Python)

### Create enviroment 
First open the terminal or command line in the IDE.Then write the following code.
`python -m venv env`
Then activate the enviroment using the code below for windows.
`.\env\Scripts\activate`

### All Steps
- Download my Repository 
- Create a `TrainingImage` folder in a project. 
- Run `pip install -r requirements.txt` to create all libraries below.
- Run `py AMS_Run.py`. (or `py AMS_Handle.py` instead)

### Code Requirements
- Opencv
- Opencv-contrib
- Tkinter(Available in Python)
- PIL
- Pandas
- PyMySQL

### Project Structure
- After running, you need to give your face data to system so enter your ID and name in box than click on `Take Images` button.
- It will collect 200 images of your faces, it save a images in `TrainingImage` folder
- After that we need to train a model(for train a model click on `Train Image` button.
- It will take 5-10 minutes for training(for 10 person data).
- After training click on `Automatic Attendance` ,it can fill attendance by your face using our trained model (model will save in `TrainingImageLabel` )
- it will create `.csv` file of attendance according to time & subject.
- You can store data in database (install wampserver),change the DB name according to your in `AMS_Run.py`.
- `Manually Fill Attendace` Button in UI is for fill a manually attendance (without facce recognition),it's also create a `.csv` and store in a database.

### Notes
- It will require high processing power(I have 8 GB RAM & 2 GB GC)
- It's not possible to recognise persons just like another humans.
- Noisy images can reduce your accuracy so quality of images matter.
