# Smart Budget Tracker

A full-stack personal finance management application that helps users track income and expenses, manage transactions, and visualize financial insights through an interactive dashboard.

---

## Features

### Authentication
- User registration
- User login
- JWT-based authentication
- Protected routes

---

### Transaction Management
- Add income and expense transactions
- Edit transactions
- Delete transactions
- View all transactions

---

### Dashboard and Analytics
- Real-time balance calculation
- Income vs expense tracking
- Recent transactions overview
- Sidebar navigation dashboard

---

### UI and UX Features
- Modern responsive user interface
- Landing page with background image
- Authentication choice page (login/register)
- Sidebar-based dashboard layout
- Clean card-based design

---

## Tech Stack

### Frontend
- React.js
- JavaScript (ES6)
- HTML5
- CSS3
- React Router DOM
- Axios

### Backend
- FastAPI (Python)
- JWT Authentication
- MySQL or SQLite
- Uvicorn

---

## Project Structure

backend/
├── main.py
├── models/
├── routes/
├── auth/
├── database/

frontend/
├── src/
│ ├── pages/
│ │ ├── Home.js
│ │ ├── AuthChoice.js
│ │ ├── Login.js
│ │ ├── Register.js
│ │ ├── Dashboard.js
│ │ ├── AddTransaction.js
│ │ ├── EditTransaction.js
│ │ ├── DeleteTransaction.js
│ │ ├── ViewTransactions.js
│ │ └── Analysis.js
│ ├── components/
│ │ └── SidebarLayout.js
│ ├── App.js
│ └── index.js


---

## Installation and Setup

### Clone Repository
```bash
git clone https://github.com/23wh1a12b6/smart-budget-tracker.git
----
### Backend Setup (FastAPI)
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

### Backend runs at:

http://127.0.0.1:8000
