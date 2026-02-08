# Savvy - Intelligent Expense Management System

A full-stack **expense management system** that automatically extracts receipt data from emails via IMAP integration. The system covers everything from email receipt parsing and expense categorization to budget tracking, spending analytics, and financial reporting — all through an interactive dashboard.

## Table of Contents

- [Features](#features)
- [Screenshots](#screenshots)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Role-Based Access](#role-based-access)

## Features

### User-Facing
- **Email Receipt Extraction** — Connect email accounts via IMAP to automatically fetch, parse, and store receipt data
- **Multi-Vendor Support** — Intelligent parsing for Apple, K Plus (Kasikornbank), Steam, and generic receipt formats
- **Expense Dashboard** — Real-time overview with spending trends, category breakdowns, and summary metrics
- **Budget Management** — Set monthly budgets per category and compare actual spending against targets
- **Auto Categorization** — Automatically assigns expense categories based on vendor name mapping
- **Analytics & Reports** — Analyze spending by vendor, category, and time period with interactive charts
- **Receipt Management** — View, edit, filter, and organize all receipts with advanced search

### Account & Security
- **User Registration & Login** — Account management with JWT-based authentication
- **Secure Credential Storage** — Email passwords encrypted with Fernet symmetric encryption
- **Password Hashing** — User passwords hashed with bcrypt before storage
- **Token-Based Auth** — JWT access tokens with configurable expiry

## Screenshots

### Dashboard
| Expense Dashboard |
|:---:|
| ![Dashboard](sourceCode/Frontend/public/dashboard-preview.png) |

## Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | Next.js 15 (App Router), React, TypeScript |
| **Styling** | Tailwind CSS 4, Shadcn/ui (Radix UI) |
| **Charts** | Recharts, Chart.js, React ChartJS 2 |
| **Backend** | FastAPI, Python 3.11, Uvicorn |
| **ORM** | SQLAlchemy 2.0 |
| **Validation** | Pydantic 2 |
| **Database** | MySQL (PyMySQL) |
| **Auth** | JWT (python-jose), bcrypt, passlib |
| **Encryption** | cryptography (Fernet) |
| **Date Handling** | date-fns, React Day Picker |
| **Deployment** | Heroku-ready (Procfile) |

## Project Structure

```
sourceCode/
├── Frontend/                          # Next.js application
│   ├── app/                           # Pages (App Router)
│   │   ├── page.tsx                   # Landing page
│   │   ├── login/                     # Login page
│   │   ├── register/                  # Registration page
│   │   ├── contact/                   # Contact page
│   │   ├── doc/                       # Documentation page
│   │   ├── faq/                       # FAQ page
│   │   └── user/                      # Protected user pages
│   │       ├── dashboard/             #   Expense dashboard
│   │       ├── budgetmanagement/      #   Budget CRUD
│   │       ├── billandreceipt/        #   Receipt list & details
│   │       ├── mailmanagement/        #   Email rule management
│   │       └── settings/              #   User settings
│   ├── components/                    # Reusable React components
│   │   ├── charts/                    #   Chart components
│   │   │   ├── ExpenseTrendsChart.tsx
│   │   │   ├── ExpenseCategoriesChart.tsx
│   │   │   ├── BudgetComparisonChart.tsx
│   │   │   └── RecentExpensesList.tsx
│   │   ├── budget/                    #   Budget modals
│   │   ├── navbar/                    #   Public navigation
│   │   ├── loggednavbar/              #   Authenticated navigation
│   │   └── ui/                        #   Shadcn/ui primitives
│   ├── lib/                           # API client & utilities
│   │   ├── api.ts                     #   Axios API client
│   │   └── utils.ts                   #   Helper functions
│   ├── types/                         # TypeScript type definitions
│   ├── public/                        # Static assets & images
│   ├── package.json
│   ├── tsconfig.json
│   └── next.config.js
│
└── Backend/                           # FastAPI application
    ├── app/
    │   ├── main.py                    # App entry point & CORS setup
    │   ├── config.py                  # Settings & environment config
    │   ├── database.py                # Database connection
    │   ├── models/                    # SQLAlchemy models
    │   │   ├── user.py
    │   │   ├── receipt.py
    │   │   ├── receipt_item.py
    │   │   ├── budget.py
    │   │   ├── category.py
    │   │   └── imap_setting.py
    │   ├── schemas/                   # Pydantic request/response DTOs
    │   ├── api/routes/                # REST API route handlers
    │   │   ├── auth.py
    │   │   ├── users.py
    │   │   ├── receipts.py
    │   │   ├── categories.py
    │   │   ├── budgets.py
    │   │   ├── imap_settings.py
    │   │   └── analytics.py
    │   └── services/                  # Business logic
    │       ├── auth_service.py        #   JWT & password handling
    │       ├── imap_service.py        #   Email fetching via IMAP
    │       ├── receipt_extractor.py   #   Receipt parsing per vendor
    │       ├── category_service.py    #   Auto-categorization
    │       ├── encryption_service.py  #   Fernet credential encryption
    │       └── init_data.py           #   Initial data seeding
    ├── requirements.txt
    ├── run.py                         # Dev server entry point
    ├── runtime.txt                    # Python version (3.11.4)
    └── Procfile                       # Heroku deployment config
```

## Getting Started

### Prerequisites

- **Node.js** v18 or higher
- **Python** 3.11
- **MySQL** database server
- **npm** or **yarn**

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/<your-username>/savvy.git
   cd savvy
   ```

2. **Set up the Backend**

   ```bash
   cd sourceCode/Backend

   # Create and activate virtual environment
   python3.11 -m venv venv
   source venv/bin/activate        # macOS/Linux
   # venv\Scripts\activate         # Windows

   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Configure environment variables**

   Create a `.env` file in the `sourceCode/Backend/app/` directory:

   ```env
   DATABASE_URL=mysql+pymysql://username:password@localhost:3306/savvy_db
   SECRET_KEY=your-secret-key
   ENCRYPTION_KEY=your-fernet-base64-key
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

4. **Start the Backend server**

   ```bash
   python run.py
   ```

   API available at [http://localhost:8000](http://localhost:8000) with interactive docs at [http://localhost:8000/docs](http://localhost:8000/docs).

5. **Set up the Frontend**

   ```bash
   cd sourceCode/Frontend

   # Install dependencies
   npm install

   # Start development server
   npm run dev
   ```

   App available at [http://localhost:3000](http://localhost:3000).

### Available Scripts

#### Frontend

| Command | Description |
|---------|-------------|
| `npm run dev` | Start development server |
| `npm run build` | Build for production |
| `npm run start` | Start production server |
| `npm run lint` | Run ESLint |

#### Backend

| Command | Description |
|---------|-------------|
| `python run.py` | Start development server (Uvicorn) |
| `pytest` | Run test suite |

## Role-Based Access

The system implements two access levels protected by JWT middleware:

| Role | Access | Description |
|------|--------|-------------|
| **Public** | `/token`, `/users` (register), `/categories` | No authentication required — open registration, login, and category browsing |
| **Authenticated User** | `/users/me`, `/receipts/*`, `/budgets/*`, `/imap-settings/*`, `/analytics/*` | Requires valid JWT token — users can only access **their own data** via row-level isolation |

### How It Works

- Users authenticate via **JWT Bearer tokens** obtained from the `POST /token` endpoint
- Tokens expire after **30 minutes** (configurable via `ACCESS_TOKEN_EXPIRE_MINUTES`)
- Every authenticated query is filtered by `current_user.id`, ensuring **row-level data isolation**
- IMAP email credentials are encrypted per-user with **Fernet symmetric encryption**
- Passwords are hashed using **bcrypt** before storage
