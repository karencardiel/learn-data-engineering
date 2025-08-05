# <img src="https://github.com/user-attachments/assets/ffc3a777-8863-4de5-944b-8b609f7be8ce" width="50" /> Learn Data Engineering 

Welcome to **Learn Data Engineering**, a web platform designed to centralize and organize high-quality resources for aspiring data engineers. This project aims to solve the problem of information overload by offering a curated catalog that makes it easier to start and advance in the data engineering field.

<img width="1335" height="969" alt="image" src="https://github.com/user-attachments/assets/af1f97a3-550b-4611-bcd5-98cf016bd331" />

## ✨ Features

- **Resource Visualization:** A modern and attractive grid with a "frosted glass" effect.
- **Search and Filtering:** A powerful search bar and dynamic filters by type and difficulty level.
- **Admin Panel:** A complete administration interface to perform CRUD (Create, Read, Update, Delete) operations on resources.
- **Responsive Design:** An interface adaptable to different screen sizes.
- **Dynamic UI:** Animated backgrounds and titles with CSS for an engaging user experience.

## 🛠️ Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML5, CSS3 (Flexbox, Animations, Variables), JavaScript  
- **Database:** PostgreSQL (psycopg2, psql)

## ⚙️ Installation and Setup

Follow these steps to run the project on your local machine.

### Prerequisites

- Python 3.x installed  
- `pip` (Python's package manager) installed

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/learn-data-engineering.git
   cd learn-data-engineering

2. **Create and activate a virtual environment:**

   * **On macOS/Linux:**

     ```bash
     python3 -m venv venv
     source venv/bin/activate

   * **On Windows:**

     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**

   Run the setup script to create the necessary database and tables.

   ```bash
   python db_setup.py
   ```

5. **Run the application:**

   ```bash
   flask run
   ```

   ✅ Done! The app should now be running at `http://127.0.0.1:5000`

## 🚀 Usage

* **Homepage:** Browse, search, and filter the available resources.
* **Admin Panel:** Access the `/admin` route to manage content (create, edit, or delete resources).

## 📂 Project Structure

```
/
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── app.js
│   └── images/
│       └── logo.png
├── templates/
│   ├── admin/
│   │   ├── index.html
│   │   └── resource_form.html
│   └── index.html
├── app.py
├── db_setup.py
├── .gitignore
├── README.md
└── requirements.txt
```

## <img src="https://slackmojis.com/emojis/220-bananadance/download" width="35" /> Notes
This program was developed as part of an academic project. 

⭐ **Star this repository if you find it helpful!**
