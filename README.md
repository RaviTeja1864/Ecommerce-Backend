# 🛒 Ecommerce Backend

A production-ready RESTful backend for an e-commerce platform built with **Django** and **Django REST Framework**. Handles everything from product management and customer authentication to cart operations and order processing.

---

## 🚀 Features

- **Store** — Product listings, collections, and filtering
- **Customers** — User registration, authentication, and profile management
- **Cart** — Add, update, and remove items with session or user-linked carts
- **Orders** — Place orders, track order items, and manage order status
- **Tags** — Flexible content tagging system for products
- **Seed Script** — Quickly populate the database with test data via `seed_db.py`

---

## 🧱 Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.x |
| Framework | Django |
| API | Django REST Framework (DRF) |
| Database | SQLite (dev) / PostgreSQL (prod) |
| Auth | Django Auth / JWT (DRF SimpleJWT) |

---

## 📁 Project Structure

```
Ecommerce-Backend/
│
├── ecommerce/          # Django project settings & root URLs
├── store/              # Products, collections, reviews
├── customers/          # Customer model, auth, profiles
├── carts/              # Cart & cart item logic
├── orders/             # Order placement and management
├── tags/               # Generic tagging system
│
├── seed_db.py          # Database seeding script
├── manage.py
└── db.sqlite3          # Dev database
```

---

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/RaviTeja1864/Ecommerce-Backend.git
cd Ecommerce-Backend
```

### 2. Create & Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> **Note:** If `requirements.txt` is not present, install manually:
> ```bash
> pip install django djangorestframework
> ```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Seed the Database (Optional)

```bash
python seed_db.py
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

API will be available at `http://127.0.0.1:8000/`

---

## 🔌 API Endpoints (Overview)

| Resource | Endpoint |
|---|---|
| Products | `GET /store/products/` |
| Product Detail | `GET /store/products/<id>/` |
| Collections | `GET /store/collections/` |
| Cart | `GET/POST /carts/` |
| Cart Items | `GET/POST /carts/<id>/items/` |
| Customers | `GET/PUT /customers/me/` |
| Orders | `GET/POST /orders/` |

> Full API documentation can be explored via Django REST Framework's browsable API at `http://127.0.0.1:8000/`

---

## 🛠️ Environment Variables

Create a `.env` file in the root directory for production settings:

```env
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
DATABASE_URL=postgres://user:password@host:5432/dbname
```

---

## 🧪 Running Tests

```bash
python manage.py test
```

---

## 📦 Deployment Notes

- Switch `db.sqlite3` to **PostgreSQL** for production
- Set `DEBUG=False` and configure `ALLOWED_HOSTS`
- Use **gunicorn** + **nginx** or deploy to **Railway / Render / AWS**
- Add `whitenoise` for static file serving

---

## 👨‍💻 Author

**Ravi Teja**
B.Tech ISE — Jain (Deemed-to-be University)
GitHub: [@RaviTeja1864](https://github.com/RaviTeja1864)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
