# Process Documentation Management System

A backend service for managing process documentation with authentication,
authorization, and document ownership.

## What this project shows

- OAuth2 Password Flow authentication
- JWT-based authorization
- User registration and login
- Secure password hashing (Argon2)
- Document CRUD operations
- Document ownership enforcement
- Clean separation of routers, services, models, and schemas

## What this project intentionally does NOT include

- File uploads
- Document versioning
- Search or indexing
- Tagging or categorization
- Analytics or reporting
- Machine learning features
- Frontend or UI

## How to run

### Requirements
- Python 3.10+

### Setup

```bash
git clone <repository-url>
cd process-documentation-management-system
python -m venv venv
