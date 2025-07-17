# 🥗 Follow My Plate

A personalized health and diet planning web application built with Flask.
Users can register, set fitness goals (gain, lose, or maintain weight), log their daily food intake, track calorie consumption, and receive meal suggestions based on their profile and goals.

---

## 🚀 Live Demo

🌐 [https://follow-my-plate.onrender.com](https://follow-my-plate.onrender.com)
*(Note: This link will work once the Render deployment issue with Python 3.13 and psycopg2 is resolved by Render support or a workaround is found.)*

---

## 💡 Features

- ✅ User registration and secure login/logout (password hashing with Werkzeug).
- 📝 Comprehensive profile setup: name, age, gender, height, weight, and fitness goal.
- 🎯 Dynamic daily calorie target calculation based on user profile and fitness goal (gain/lose/maintain weight).
- 🍱 **Detailed Food Logging:** Users can log individual food items with descriptions, calorie counts, and meal types (breakfast, lunch, dinner, snack).
- 📊 **Interactive Dashboard:** Displays daily calorie summary (target, consumed, remaining) and a weekly calorie consumption chart (powered by Chart.js).
- 🗑️ Ability to delete individual food entries from the dashboard.
- 💡 Personalized meal recommendations based on overall fitness goal.
- 📱 Responsive Bootstrap 5 UI for a seamless experience on various devices.

---

## 🛠 Tech Stack

| Tool             | Purpose                                  |
|------------------|------------------------------------------|
| Python           | Programming Language                     |
| Flask            | Web framework                            |
| **PostgreSQL** | **Production Database (hosted on Render)** |
| SQLAlchemy       | ORM (Object Relational Mapper)           |
| **Flask-Migrate**| **Database Migrations** |
| Flask-WTF        | Form handling & CSRF protection          |
| Flask-Login      | User authentication & session management |
| Werkzeug         | Password hashing and WSGI utilities      |
| `psycopg2-binary`| PostgreSQL adapter                       |
| `python-dotenv`  | Environment variable management          |
| Chart.js         | Interactive data visualization           |
| Render           | Cloud Deployment Platform                |
| Gunicorn         | WSGI HTTP Server for production          |

---

## ⚙️ Local Development Setup

Follow these steps to get the application running on your local machine:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Puneeth1615/Follow-My-Plate.git](https://github.com/Puneeth1615/Follow-My-Plate.git)
    cd Follow-My-Plate
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create a `.env` file:**
    In the root directory of your project, create a file named `.env` and add the following:
    ```
    SECRET_KEY='YOUR_VERY_LONG_AND_RANDOM_SECRET_KEY'
    DATABASE_URL='postgresql://follow_my_plate_db_user:nxsvBMiWdCEpoDwuYLpk5r8gSYxn0pqz@dpg-d1mdl963jp1c73em85e0-a.singapore-postgres.render.com/follow_my_plate_db'
    ```
    * **Replace `YOUR_VERY_LONG_AND_RANDOM_SECRET_KEY`** with a strong, randomly generated key. You can generate one in Python: `import os; print(os.urandom(24).hex())`.
    * The `DATABASE_URL` connects to the Render PostgreSQL database. Ensure connectivity to Render's database from your local machine (e.g., firewall rules).

5.  **Initialize and run database migrations:**
    *(Ensure your virtual environment is active and you are in the project root)*
    ```bash
    flask db init          # Only run once for the project
    flask db migrate -m "Initial database schema with User and FoodEntry models"
    flask db upgrade
    ```
    *These commands will connect to your specified PostgreSQL database (from `.env`) and create the necessary tables.*

6.  **Run the application:**
    ```bash
    python run.py
    ```
    The application will be available at `http://127.0.0.1:5000`.

---

## ☁️ Deployment

This application is configured for deployment on Render using a `render.yaml` blueprint.

**Deployment Steps:**

1.  **Push code to GitHub:** Ensure your latest code is pushed to your `main` branch.
2.  **Configure Environment Variables on Render:** In your Render dashboard, go to your web service settings and add `SECRET_KEY` as an environment variable with your strong generated key. The `DATABASE_URL` is already in `render.yaml`.
3.  **Deploy:** Render will automatically build and deploy your service. Monitor the deployment logs for progress and any issues.

---


## 📄 License

This project is licensed under the MIT License.