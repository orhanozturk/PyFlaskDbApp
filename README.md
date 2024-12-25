# Flask Quiz Application

This project is a Flask-based quiz application that allows users to answer quiz questions, view their scores, and explore database records. It includes features like displaying the best score in the quiz template and pre-populated example questions.

---

## Requirements

- Python 3.7 or later
- `pip` (Python package manager)

---

## Setting Up the Virtual Environment

1. **Navigate to the project directory:**
   ```bash
   cd <project_directory>
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv myvenv
   ```

3. **Activate the virtual environment:**
   - **Windows:**
     ```bash
     myvenv\Scripts\activate
     ```
   - **Linux/Mac:**
     ```bash
     source myvenv/bin/activate
     ```

4. **Install the required dependencies:**
   ```bash
   pip install flask flask-sqlalchemy
   ```

5. **Optionally, save the dependencies:**
   ```bash
   pip freeze > requirements.txt
   ```

---

## Running the Application

1. **Ensure the virtual environment is activated.**

2. **Start the application:**
   ```bash
   python app.py
   ```

3. **Access the application in your web browser:**
   ```
   http://127.0.0.1:5000/
   ```

---

## Features

1. **Quiz Page**:
   - The quiz form dynamically displays the "Best Score" in the top-right corner.
   - The user can answer multiple-choice questions.

2. **Results Page**:
   - Displays the user's total score.
   - Shows both the user's answers and the correct answers.

3. **Database Records Viewer**:
   - Navigate to `/view_data` to see the list of users and their scores, as well as the quiz questions and correct answers.

---

## Viewing Database Records

To view the database records, navigate to the `/view_data` route in your browser:
```
http://127.0.0.1:5000/view_data
```
This page displays:
- The list of questions and their correct answers.
- Usernames and their best scores.

---

## Application Structure

- **`app.py`**: The main Flask application.
- **`templates/`**: Directory containing HTML templates.
  - `quiz_template.html`: Quiz form and questions.
  - `result.html`: Results page showing the user's score, their answers, and correct answers.
  - `view_data.html`: Page to view database records.
- **`quiz.db`**: SQLite database created automatically on first run.

---

## Database Initialization

The database (`quiz.db`) is automatically created when the application is run for the first time. It also pre-populates with example questions if the `Question` table is empty.

---

## Notes

- **Deactivating the virtual environment:** When done, deactivate the virtual environment:
  ```bash
  deactivate
  ```

- **Reactivating the virtual environment:** To work on the project later, activate the environment again:
  ```bash
  myvenv\Scripts\activate  # On Windows
  source myvenv/bin/activate  # On Linux/Mac
  ```

- **Modifying the questions:** Update the `Question` model data in `app.py` to add or modify predefined questions.

---

## Author

**Orhan OZTURK**
