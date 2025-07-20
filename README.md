📝 Notes App

A simple and user-friendly Notes App built with **Flask** and **SQLite**. 
This app allows users to create, view, edit, and delete notes, making it a handy tool for quick note-taking and reminders.

---

🚀 Features

-  ✍️ Add a new note with a title and content
-  📋 View all notes on the homepage
-  ✏️ Edit existing note titles
-  🗑️ Delete notes with one click
-  🗃️ Persistent local storage using SQLite

---

🛠️ Tech Stack

- **Backend:** Python (Flask)
- **Frontend:** HTML, CSS (via `/static/style.css`)
- **Database:** SQLite

---

📦 Installation

1. Clone the repository:

   
git clone https://github.com/yourusername/notes-app.git

cd notes-app 


2. Create and activate a virtual environment (optional but recommended):

   
python -m venv venv

source venv/bin/activate  # Windows: venv\Scripts\activate


3. Install dependencies:


pip install flask


▶️ Running the App


python app.py

Visit http://127.0.0.1:5000 in your browser to start using the app.


📂 Project Structure


notes-app/ 

│

├── app.py                  # Main Flask application

├── notes.db                # SQLite database (auto-created on first run)

├── templates/

│   └── index.html          # HTML interface using Jinja2 templating

├── static/

│   └── style.css           # (Optional) Custom CSS styles 

└── README.md               # You're here!

🖼️ Screenshots


![UI Preview]
<p align="center">
  <img src="screenshots/ui1.heic" width="600"/>
  <img src="screenshots/ui2.heic" width="600"/>
</p>


📄 License
This project is licensed under the MIT License — feel free to use, modify, and share.

🙋‍♀️ Author

Built with ❤️ by Deepa M
https://github.com/deepa-m-dev
