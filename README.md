# 🛍️ FastAPI E-Commerce Backend

A minimal and efficient backend for handling basic e-commerce functionality like product listings and user orders using **FastAPI** and **MongoDB**.

---

## 🚀 Getting Started

### 🔧 Requirements

- Python 3.8+
- MongoDB instance (local or cloud, e.g., MongoDB Atlas)

### 📦 Installation

```bash
git clone https://github.com/your-username/fastapi-ecommerce-backend.git
cd fastapi-ecommerce-backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

### 📘 API Endpoints Overview

| Method | Endpoint     | Description                        | Parameters                                                                                         | Success Response | Error Response                |
|--------|--------------|------------------------------------|----------------------------------------------------------------------------------------------------|------------------|-------------------------------|
| GET    | `/products`  | List products with filters         | `name` (string, optional) — Filter by name<br>`size` (string, optional)<br>`limit` (int, required)<br>`offset` (int, required) | 200 OK: Product list with pagination | 500: Database connection error |
| POST   | `/orders`    | Create a new order                 | Body:<br>`userId` (string, required)<br>`items[]` with `productId` (string) & `quantity` (int)     | 201 Created: Order ID             | 500: Failed to insert order    |
| GET    | `/orders`    | Get orders by user with pagination | `userId` (string, required)<br>`limit` (int, required)<br>`offset` (int, required)                 | 200 OK: Orders with pagination    | 500: Query failed              |
