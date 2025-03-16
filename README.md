# 🚀 Crypto Data & Organization Management System

## 📌 Project Overview

This Django-based system allows organizations to manage cryptocurrency price data efficiently. It fetches real-time prices, stores historical data, and updates prices periodically using Celery.

## 🎯 Features

  - 🏢 Organization Management (CRUD Operations)

  - 💰 Crypto Price Management (CRUD Operations)

  - 🔄 Real-Time Crypto Price Fetching (via CoinGecko API)

  - ⏳ Automated Price Updates (using Celery & Redis every 5 minutes)

  - 🔒 JWT Authentication (with role-based access control)

  - 📂 Historical Data Storage (instead of overwriting previous prices)

  - 🔍 Search & Filtering (for organizations)

  - 📄 Pagination in Crypto Price API

  - 🔔 Django Signals (for logging organization creation/deletion)

## 🏗️ Tech Stack

  - Backend: Django, Django REST Framework (DRF)

  - Database: SQLite (Default) or PostgreSQL

  - Task Queue: Celery with Redis

  - API Integration: CoinGecko API for real-time crypto prices

  - Authentication: JWT (Simple JWT)

## 📌 Installation & Setup

### 1️⃣ Clone the Repository

  - git clone https://github.com/megha-unnikrishnan/crypto_management.git
    
  - cd crypto-management

### 2️⃣ Create & Activate Virtual Environment

  - python -m venv venv
    
  - source venv/bin/activate  # On Mac/Linux
    
  - venv\Scripts\activate  # On Windows

### 3️⃣ Install Dependencies

  - pip install -r requirements.txt

### 4️⃣ Apply Migrations 

  - python manage.py migrate

### 5️⃣ Create Superuser

   - python manage.py runserver

### 6️⃣ Run Development Server

  - python manage.py runserver

### 7️⃣ Start Redis Server (For Celery Tasks)

Ensure Redis is installed and running: *sudo service redis-server start*

### 8️⃣ Start Celery Worker

celery -A project_name worker --loglevel=info

### Start Celery Beat (For Periodic Tasks)

celery -A project_name beat --loglevel=info

## 🌍 API Endpoints

### 🏢 Organization APIs

#### 📌 Create Organization

#### POST /api/organizations/

**Request Body:**

```json
{
  "name": "Crypto Corp"
}

```

*Response:*

```json

{
    "id": "9123a16c-6a04-4fdf-85ae-ab919aed7fad",
    "name": "Crypto Hub",
    "created_at": "2025-03-16T16:00:28.202847Z"
}

```

#### 📌 Get All Organizations

GET /api/organizations/

####  📌 Delete Organization

DELETE /api/organizations/{org_id}/

### 💰 Crypto Price APIs

#### 📌 Create Crypto Price Entry

POST /api/crypto-prices/

*Request Body:*

```json

{
  "org_id": "1234-5678",
  "symbol": "BTC",
  "price": "65000.1234567890"
}

```

*Response:*

```json

{
  "id": 1,
  "org_id": "1234-5678",
  "symbol": "BTC",
  "price": "65000.1234567890",
  "timestamp": "2025-03-16T10:15:00Z"
}

```

#### 📌 Get Crypto Prices (Paginated)

GET /api/crypto-prices/?page=1

📌 Delete Crypto Price Entry

DELETE /api/crypto-prices/{price_id}/


## 🔐 Authentication & Security

  - JWT-based authentication.

  - Users can only access their organization's data.

  - Permissions ensure only organization owners can edit/delete.

### 🛠️ Obtain JWT Token

POST /api/token/

*Request:*

```json

{
  "username": "admin",
  "password": "yourpassword"
}

```

*Response:*

```json

{
  "access": "jwt_access_token",
  "refresh": "jwt_refresh_token"
}

```

## 🎯 Additional Features

  - ✅ Pagination in GET /api/crypto-prices/

  - ✅ Historical price storage (instead of overwriting previous data)

  - ✅ Django Signals (logs when organizations are created/deleted)

  - ✅ Search & Filtering for Organizations

## 🏆 Acknowledgments

  - CoinGecko API for real-time price data

  - Django & Django REST Framework

  - Celery for scheduled tasks
