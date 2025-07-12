

> 📝 **Assignment Submission**  
> Product Review System built using Django & Django REST Framework  
> Submitted for the **Back End Developer Role – Pfactorial Technologies**  
> Deadline: **13th July 2025**

# Product Review System

A RESTful API backend that enables users to browse and review products, with admin-controlled product management. Developed using Django and DRF as part of a job interview assignment.



## Features
- Admin users can manage (add, edit, delete) products
- Regular users can browse products and submit reviews
- All users can view products and their aggregated ratings
- Role-based access control
- Token-based authentication
- Prevents duplicate reviews per user per product
- Product ratings are aggregated and displayed
- Users can only update or delete their own reviews (ownership enforced)

## Setup Instructions

### 1. Clone the repository
```
git clone <your-repo-url>
cd <project-folder>
```

### 2. Create and activate a virtual environment
```
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Apply migrations
```
python manage.py migrate
```

### 5. Create a superuser (admin)
```
python manage.py createsuperuser
```

### 6. Run the development server
```
python manage.py runserver
```

## API Endpoints

### Authentication
- `POST /api/auth/register/` — Register a new user
- `POST /api/auth/login/` — Login and get token
- `POST /api/auth/logout/` — Logout

### Products
- `GET /api/products/` — List all products
- `GET /api/products/<id>/` — Retrieve product details
- `POST /api/products/` — Create product (admin only)
- `PUT/PATCH /api/products/<id>/` — Update product (admin only)
- `DELETE /api/products/<id>/` — Delete product (admin only)

### Reviews
- `GET /api/reviews/?product=<product_id>` — List reviews for a product
- `POST /api/reviews/` — Create a review (regular user, one per product)
- `PUT /api/reviews/<id>/` — Update a review (owner only)
- `PATCH /api/reviews/<id>/` — Partially update a review (owner only)
- `DELETE /api/reviews/<id>/` — Delete a review (owner only)

## API Testing

All endpoints were tested using Postman. For authenticated requests, include the header:

```
Authorization: Token <your_token>
```

### Example: Register a User
POST /api/auth/register/
Body:
```json
{
  "username": "testuser",
  "email": "testuser@example.com",
  "password": "yourpassword"
}
```

### Example: Login
POST /api/auth/login/
Body:
```json
{
  "username": "testuser",
  "password": "yourpassword"
}
```

### Example: Create a Review
POST /api/reviews/
Body:
```json
{
  "product": 1,
  "rating": 5,
  "feedback": "Great product!"
}
```



### Example: Add a Product (Admin Only)
POST /api/products/
Body:
```json
{
  "name": "Sample Product",
  "description": "This is a sample product.",
  "price": "99.99"
}
```

### Example: Update a Product (Admin Only)
PUT /api/products/1/
Body:
```json
{
  "name": "Updated Product Name",
  "description": "Updated description.",
  "price": "120.00"
}
```

### Example: Delete a Product (Admin Only)
DELETE /api/products/1/

### Example: Update a Review
PATCH /api/reviews/1/
Body:
```json
{
  "rating": 4
}
```

### Example: Delete a Review
DELETE /api/reviews/1/

You should receive a 403 Forbidden error if you try to update or delete a review that you do not own.

## Usage Notes
- Use the token from login in the `Authorization: Token <token>` header for authenticated requests.
- Only admin users can manage products.
- Regular users can submit one review per product.
- Ratings must be between 1 and 5.
- Users can only update or delete their own reviews; attempts to modify others' reviews will result in a 403 Forbidden error.