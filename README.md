# 🌍 Vacado – Your Vacation, Planned in Seconds ✈️

Vacado is a travel planning web app prototype that helps users plan their dream vacation by selecting duration, trip theme, accommodation type, and budget. 
The app then generates a personalized trip plan – all within seconds.

This repository includes:
- Backend structure with endpoints, JWT security, and PorstgreSQL handling
- Frontend structure with endpoints and HTML templates
- A landing page introducing the app
- A trip configuration form
- A user login, registration and profile page
- ChatGPT-compatible prompt generation structure

---

##  Features

-  **Landing Page** – Clean, responsive introduction to the Vacado app
-  **Login Page** - User Login or redirect to Registration
-  **User Page** - Showing previous planed Trips and User Data (all changeable and stored in Database)
-  **Trip Planner Form** – Collects user preferences (duration, theme, budget, accommodation)
-  **Registration Page** – Simple user sign-up form (username + password + email)
-  **ChatGPT Prompt Generator** – Ready-to-use prompt template to feed into AI models
-  User Login and Registration with Hashed password in PostgreSQL Database

---

##  File Structure

```bash
vacado/
├── README.md               # You're here!
├── main.py                 # FastAPI and Router implemetation
  /frontend
    ├── root.html               # Welcome / Landing page
    ├── user-template.html      # User profile and history
    ├── make_vacation.html      # Trip planning form
    ├── onboarding.html         # User registration page
    ├── login.html              # User login page
    ├── prompt.json             # Sample ChatGPT prompt with placeholder values
  /backend
    ├── backend_endpoints.py  # CRUD endpoints for all DB-Tables
    ├── data_handling.py      # PostgreSQL communication
    ├── security.py           # JWT authentication, User management




    
