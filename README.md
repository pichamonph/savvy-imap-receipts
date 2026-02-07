# Savvy - Intelligent Expense Management System

A full-stack **expense management system** that automatically extracts receipt data from emails via IMAP integration. The system covers everything from email receipt parsing and expense categorization to budget tracking, spending analytics, and financial reporting — all through an interactive dashboard.

## Table of Contents

- [Features](#features)
- [Screenshots](#screenshots)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Database Schema](#database-schema)
- [API Routes](#api-routes)
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

## Database Schema

The system uses **MySQL** with **SQLAlchemy ORM**. Below is the entity-relationship overview:

```
User ──< Receipts >── Category
          │
          │              │
User ──< Budgets >───── Category

User ──< ImapSettings
```

### Key Models

| Model | Description |
|-------|-------------|
| `User` | User accounts with email-based authentication and bcrypt password hashing |
| `Receipt` | Expense records with vendor, amount, currency, and email metadata |
| `ReceiptItem` | Individual line items within a receipt (name, quantity, price, total) |
| `Category` | Expense categories with default flag for system-provided categories |
| `Budget` | Monthly budget limits per category per user, unique per (user, category, month, year) |
| `ImapSetting` | Email account configurations with encrypted passwords and sync tracking |

### Tables

#### `users`

| Column | Type | Constraints |
|--------|------|-------------|
| `id` | Integer | PK, Auto Increment |
| `username` | String(50) | Unique, Not Null |
| `email` | String(100) | Unique, Not Null |
| `password_hash` | String(255) | Not Null |
| `full_name` | String(100) | Nullable |
| `created_at` | DateTime | Default: now() |
| `updated_at` | DateTime | Default: now(), On Update: now() |

#### `receipts`

| Column | Type | Constraints |
|--------|------|-------------|
| `id` | Integer | PK, Auto Increment |
| `user_id` | Integer | FK → users.id (CASCADE), Not Null |
| `category_id` | Integer | FK → categories.id (SET NULL), Nullable |
| `amount` | Float | Not Null |
| `currency` | String(3) | Default: "THB" |
| `vendor_name` | String(100) | Nullable |
| `receipt_date` | DateTime | Nullable, Indexed |
| `receipt_number` | String(50) | Nullable |
| `payment_method` | String(50) | Nullable |
| `notes` | Text | Nullable |
| `receipt_file_path` | String(255) | Nullable |
| `email_id` | String(255) | Nullable, Indexed |
| `email_subject` | String(255) | Nullable |
| `email_from` | String(100) | Nullable, Indexed |
| `email_date` | DateTime | Nullable |
| `created_at` | DateTime | Default: now() |

#### `receipt_items`

| Column | Type | Constraints |
|--------|------|-------------|
| `id` | Integer | PK, Auto Increment |
| `receipt_id` | Integer | FK → receipts.id (CASCADE), Not Null |
| `name` | String(255) | Not Null |
| `quantity` | Float | Default: 1 |
| `price` | Float | Not Null |
| `total` | Float | Not Null |

#### `categories`

| Column | Type | Constraints |
|--------|------|-------------|
| `id` | Integer | PK, Auto Increment |
| `name` | String(100) | Not Null |
| `description` | String(255) | Nullable |
| `is_default` | Boolean | Default: false |
| `created_at` | DateTime | Default: now() |

#### `budgets`

| Column | Type | Constraints |
|--------|------|-------------|
| `id` | Integer | PK, Auto Increment |
| `user_id` | Integer | FK → users.id (CASCADE), Not Null |
| `category_id` | Integer | FK → categories.id (CASCADE), Not Null |
| `amount` | Float | Not Null |
| `month` | Integer | Not Null (1–12) |
| `year` | Integer | Not Null |
| `created_at` | DateTime | Default: now() |

#### `imap_settings`

| Column | Type | Constraints |
|--------|------|-------------|
| `id` | Integer | PK, Auto Increment |
| `user_id` | Integer | FK → users.id (CASCADE), Not Null |
| `email` | String(100) | Not Null |
| `server` | String(100) | Not Null |
| `port` | Integer | Default: 993 |
| `username` | String(100) | Not Null |
| `password_encrypted` | String(255) | Not Null |
| `use_ssl` | Boolean | Default: true |
| `folder` | String(50) | Default: "INBOX" |
| `last_sync` | DateTime | Nullable |
| `created_at` | DateTime | Default: now() |

## API Routes

### Auth

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/token` | Login with email & password, returns JWT access token |

### Users

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/users` | Register a new user |
| GET | `/api/v1/users/me` | Get current user profile |
| PUT | `/api/v1/users/me` | Update current user profile |

### Receipts

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/receipts` | Create a receipt |
| GET | `/api/v1/receipts` | List receipts with filters (vendor, category, date range, amount range) |
| GET | `/api/v1/receipts/{id}` | Get receipt details |
| PUT | `/api/v1/receipts/{id}` | Update a receipt |
| DELETE | `/api/v1/receipts/{id}` | Delete a receipt |

### Categories

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/categories` | Create a category |
| GET | `/api/v1/categories` | List all categories |
| GET | `/api/v1/categories/{id}` | Get category details |
| PUT | `/api/v1/categories/{id}` | Update a category |

### Budgets

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/budgets` | Create a budget (unique per user/category/month/year) |
| GET | `/api/v1/budgets` | List budgets (filter by month, year) |
| GET | `/api/v1/budgets/{id}` | Get budget details |
| PUT | `/api/v1/budgets/{id}` | Update a budget |
| DELETE | `/api/v1/budgets/{id}` | Delete a budget |
| GET | `/api/v1/budgets/budget-comparison` | Compare budget vs actual spending per category |

### IMAP Settings

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/imap-settings` | List user's email account settings |
| POST | `/api/v1/imap-settings` | Add an email account (IMAP config) |
| POST | `/api/v1/imap-settings/{id}/test` | Test IMAP connection |
| POST | `/api/v1/imap-settings/{id}/sync` | Trigger background email sync |

### Analytics

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/analytics/summary` | Overall expense stats (total, avg, max, min, count) |
| GET | `/api/v1/analytics/monthly` | Monthly spending trends |
| GET | `/api/v1/analytics/vendors` | Top vendors by spending |
| GET | `/api/v1/analytics/categories` | Top categories by spending |
| GET | `/api/v1/analytics/categories-summary` | Category breakdown for a date range |
| GET | `/api/v1/analytics/budget-comparison` | Budget vs actual per category |

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
