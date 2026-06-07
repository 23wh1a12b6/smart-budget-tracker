💰 Smart Budget Tracker

A full-stack personal finance management application that helps users track income and expenses, manage transactions, and visualize financial insights through an interactive dashboard.
✨ Features
🔐 Authentication
User Registration
User Login
JWT-based authentication
Protected routes
💸 Transaction Management
Add income and expense transactions
Edit transactions
Delete transactions
View all transactions
📊 Dashboard & Analytics
Real-time balance calculation
Income vs Expense tracking
Transaction summary dashboard
Sidebar-based navigation
🧭 UI / UX Features
Responsive modern UI
Sidebar navigation dashboard
Landing page with background image
Auth choice page (Login/Register)
Clean card-based layout
🛠️ Tech Stack
Backend
FastAPI (Python)
JWT Authentication
MySQL / SQLite
Uvicorn
Frontend
React.js
React Router DOM
Axios
HTML, CSS, JavaScript
🧱 Project Structure
backend/
├── main.py
├── models/
├── routes/
├── auth/
├── database/

frontend/
├── src/
│   ├── pages/
│   │   ├── Home.js
│   │   ├── AuthChoice.js
│   │   ├── Login.js
│   │   ├── Register.js
│   │   ├── Dashboard.js
│   │   ├── AddTransaction.js
│   │   ├── EditTransaction.js
│   │   ├── DeleteTransaction.js
│   │   ├── ViewTransactions.js
│   │   └── Analysis.js
│   ├── components/
│   │   └── SidebarLayout.js
│   ├── App.js
│   └── index.js
🚀 Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/your-username/finance-tracker.git
2️⃣ Backend Setup (FastAPI)
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

Backend runs on:

http://127.0.0.1:8000
3️⃣ Frontend Setup (React)
cd frontend
npm install
npm start

Frontend runs on:

http://localhost:3000
🔐 Environment Variables (Backend)

Create .env file:

SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url
📊 API Endpoints
Auth
POST /register
POST /login
Transactions
GET /transactions
POST /transactions
PUT /transactions/{id}
DELETE /transactions/{id}
🎯 Learning Outcomes

This project helped me learn:

Full-stack web development
REST API design using FastAPI
JWT authentication
React routing and state management
CRUD operations
UI design with component-based architecture
Backend–frontend integration
🚀 Future Enhancements
📈 Charts & data visualization (Recharts)
📅 Monthly budget system
📤 Export reports (PDF/Excel)
📱 Mobile responsive UI improvements
☁️ Cloud deployment (AWS/Vercel)
👨‍💻 Author

Navya

GitHub: https://github.com/23wh1a12b6
Project: Personal Finance Tracker
