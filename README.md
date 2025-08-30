# 🏢 Asset Helpdesk Workflow

A comprehensive Django-based asset management and helpdesk system designed to streamline IT asset tracking, maintenance, and support ticket management for organizations.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [Database Configuration](#database-configuration)
- [API Documentation](#api-documentation)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

The Asset Helpdesk Workflow is a full-featured web application that combines asset management with helpdesk functionality. It enables organizations to:

- **Track IT Assets**: Monitor the lifecycle of hardware and software assets
- **Manage Assignments**: Assign assets to employees and track usage
- **Handle Support Tickets**: Create, track, and resolve IT support requests
- **Maintain Assets**: Log maintenance activities and track costs
- **User Management**: Role-based access control for different user types

## ✨ Features

### 🔐 Authentication & Authorization
- JWT-based authentication system
- Role-based access control (Admin, IT Head, IT Staff, Employee)
- Secure user registration and login
- Token refresh functionality

### 📦 Asset Management
- **Asset Tracking**: Complete lifecycle management of IT assets
- **Asset Categories**: Organize assets by type and category
- **Status Tracking**: Monitor asset status (Active, In Maintenance, Retired, Lost, Disposed)
- **Serial Number Management**: Unique identification for each asset
- **Purchase Date Tracking**: Historical asset information

### 👥 Employee Management
- **Department Organization**: Structure employees by departments
- **Role Assignment**: Assign specific roles and permissions
- **Position Tracking**: Track employee positions and responsibilities
- **User Profile Management**: Complete employee profiles

### 🎫 Helpdesk System
- **Ticket Creation**: Create support tickets with detailed descriptions
- **Priority Levels**: Set ticket priority (Low, Medium, High, Urgent)
- **Status Tracking**: Monitor ticket progress (Open, In Progress, Resolved, Closed)
- **Assignment System**: Assign tickets to appropriate staff members
- **Update Logs**: Track all ticket updates and changes
- **Comments System**: Allow communication on tickets

### 🔧 Maintenance Management
- **Maintenance Logging**: Record all maintenance activities
- **Cost Tracking**: Monitor maintenance costs and budgets
- **Technician Assignment**: Assign maintenance tasks to technicians
- **Maintenance Types**: Categorize maintenance (Preventive, Corrective, Emergency)

### 🔗 Asset Assignment
- **Employee Assignment**: Assign assets to specific employees
- **Date Tracking**: Monitor assignment and return dates
- **Assignment History**: Complete audit trail of asset assignments

## 🛠 Technology Stack

- **Backend Framework**: Django 5.2.5
- **API Framework**: Django REST Framework 3.16.1
- **Authentication**: JWT (JSON Web Tokens)
- **Database**: MySQL
- **Python Version**: 3.x
- **Additional Libraries**:
  - `asgiref==3.9.1`
  - `sqlparse==0.5.3`
  - `tzdata==2025.2`

## 📁 Project Structure

```
asset-helpdesk-workflow/
├── asset-helpdesk-workflow/
│   ├── accounts/                 # User authentication and management
│   ├── assets/                   # Asset management models and views
│   ├── employees/                # Employee management
│   ├── helpdesk/                 # Helpdesk ticket system
│   ├── asset_helpdesk_workflow/  # Main Django project settings
│   └── manage.py                 # Django management script
├── env/                          # Virtual environment
├── requirements.txt              # Python dependencies
├── Comprehensive_Test_Checklist.md  # Testing documentation
├── APICheck.md                   # API testing guide
└── README.md                     # This file
```

## 🚀 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- MySQL Server
- pip (Python package installer)

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd asset-helpdesk-workflow
```

### Step 2: Create Virtual Environment

```bash
python -m venv env
```

**Windows:**
```bash
env\Scripts\activate
```

**Linux/Mac:**
```bash
source env/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Database Setup

1. Create a MySQL database named `asset_helpdesk`
2. Update database settings in `asset_helpdesk_workflow/settings.py` if needed
3. Run migrations:

```bash
cd asset-helpdesk-workflow
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create Superuser

```bash
python manage.py createsuperuser
```

### Step 6: Run the Development Server

```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000`

## 🗄 Database Configuration

The project uses MySQL as the database. Default configuration in `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'asset_helpdesk',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'sql_mode': 'STRICT_TRANS_TABLES',
        },
    }
}
```

**Note**: Update the database credentials according to your MySQL setup.

## 📚 API Documentation

The API uses Django REST Framework with JWT authentication. All endpoints return JSON responses.

### 🔐 Authentication Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `POST` | `/auth/register/` | Register new user (Admin only) | Admin Token |
| `POST` | `/auth/login/` | Login and get JWT tokens | No |
| `POST` | `/auth/token/` | Get JWT tokens (alternative) | No |
| `POST` | `/auth/token/refresh/` | Refresh access token | No |
| `GET` | `/auth/user/` | Get current user information | Yes |
| `GET` | `/auth/admin/users/` | List all users (Admin only) | Admin Token |
| `POST` | `/auth/logout/` | Logout user | Yes |

### 👥 Employee Management Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/api/employees/` | List all employees | Yes |
| `POST` | `/api/employees/` | Create new employee | Yes |
| `GET` | `/api/employees/{id}/` | Get specific employee details | Yes |
| `PUT` | `/api/employees/{id}/` | Update employee | Yes |
| `PATCH` | `/api/employees/{id}/` | Partially update employee | Yes |
| `DELETE` | `/api/employees/{id}/` | Delete employee | Yes |

### 🏢 Department Management Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/api/departments/` | List all departments | Yes |
| `POST` | `/api/departments/` | Create new department | Yes |
| `GET` | `/api/departments/{id}/` | Get specific department details | Yes |
| `PUT` | `/api/departments/{id}/` | Update department | Yes |
| `PATCH` | `/api/departments/{id}/` | Partially update department | Yes |
| `DELETE` | `/api/departments/{id}/` | Delete department | Yes |

### 📦 Asset Management Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/api/assets/` | List all assets | Yes |
| `POST` | `/api/assets/` | Create new asset | Yes |
| `GET` | `/api/assets/{id}/` | Get specific asset details | Yes |
| `PUT` | `/api/assets/{id}/` | Update asset | Yes |
| `PATCH` | `/api/assets/{id}/` | Partially update asset | Yes |
| `DELETE` | `/api/assets/{id}/` | Delete asset | Yes |

### 🔗 Asset Assignment Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/api/assignments/` | List all assignments | Yes |
| `POST` | `/api/assignments/` | Create new assignment | Yes |
| `GET` | `/api/assignments/{id}/` | Get specific assignment details | Yes |
| `PUT` | `/api/assignments/{id}/` | Update assignment | Yes |
| `PATCH` | `/api/assignments/{id}/` | Partially update assignment | Yes |
| `DELETE` | `/api/assignments/{id}/` | Delete assignment | Yes |

### 🔧 Maintenance Management Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/api/maintenancelogs/` | List all maintenance logs | Yes |
| `POST` | `/api/maintenancelogs/` | Create new maintenance log | Yes |
| `GET` | `/api/maintenancelogs/{id}/` | Get specific maintenance details | Yes |
| `PUT` | `/api/maintenancelogs/{id}/` | Update maintenance log | Yes |
| `PATCH` | `/api/maintenancelogs/{id}/` | Partially update maintenance log | Yes |
| `DELETE` | `/api/maintenancelogs/{id}/` | Delete maintenance log | Yes |

### 🎫 Helpdesk Ticket Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/api/tickets/` | List all tickets | Yes |
| `POST` | `/api/tickets/` | Create new ticket | Yes |
| `GET` | `/api/tickets/{id}/` | Get specific ticket details | Yes |
| `PUT` | `/api/tickets/{id}/` | Update ticket | Yes |
| `PATCH` | `/api/tickets/{id}/` | Partially update ticket | Yes |
| `DELETE` | `/api/tickets/{id}/` | Delete ticket | Yes |

### 📝 Ticket Category Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/api/ticketcategories/` | List all ticket categories | Yes |
| `POST` | `/api/ticketcategories/` | Create new ticket category | Yes |
| `GET` | `/api/ticketcategories/{id}/` | Get specific category details | Yes |
| `PUT` | `/api/ticketcategories/{id}/` | Update ticket category | Yes |
| `PATCH` | `/api/ticketcategories/{id}/` | Partially update ticket category | Yes |
| `DELETE` | `/api/ticketcategories/{id}/` | Delete ticket category | Yes |

### 💬 Ticket Comment Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/api/ticketcomments/` | List all ticket comments | Yes |
| `POST` | `/api/ticketcomments/` | Create new ticket comment | Yes |
| `GET` | `/api/ticketcomments/{id}/` | Get specific comment details | Yes |
| `PUT` | `/api/ticketcomments/{id}/` | Update ticket comment | Yes |
| `PATCH` | `/api/ticketcomments/{id}/` | Partially update ticket comment | Yes |
| `DELETE` | `/api/ticketcomments/{id}/` | Delete ticket comment | Yes |

### 📋 Ticket Update Log Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/api/ticketupdatelogs/` | List all ticket update logs | Yes |
| `POST` | `/api/ticketupdatelogs/` | Create new ticket update log | Yes |
| `GET` | `/api/ticketupdatelogs/{id}/` | Get specific update log details | Yes |
| `PUT` | `/api/ticketupdatelogs/{id}/` | Update ticket update log | Yes |
| `PATCH` | `/api/ticketupdatelogs/{id}/` | Partially update ticket update log | Yes |
| `DELETE` | `/api/ticketupdatelogs/{id}/` | Delete ticket update log | Yes |

### 🔑 Authentication Headers

For authenticated endpoints, include the JWT token in the Authorization header:

```
Authorization: Bearer <your_jwt_token>
```

### 📝 Request/Response Examples

#### Login Request
```bash
POST /auth/token/
Content-Type: application/json

{
    "username": "your_username",
    "password": "your_password"
}
```

#### Login Response
```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

#### Create Asset Request
```bash
POST /api/assets/
Authorization: Bearer <your_jwt_token>
Content-Type: application/json

{
    "name": "Dell Latitude 5520",
    "category": "Laptop",
    "serial_number": "DL5520-12345",
    "purchase_date": "2023-01-15",
    "status": "active"
}
```

#### Create Ticket Request
```bash
POST /api/tickets/
Authorization: Bearer <your_jwt_token>
Content-Type: application/json

{
    "title": "Printer not working",
    "description": "The office printer is showing error code E-04",
    "category": 1,
    "priority": "high",
    "linked_asset": 1
}
```

## 💻 Usage

### Getting Started

1. **Access the Admin Panel**: Visit `http://localhost:8000/admin/` and login with your superuser credentials
2. **Create Departments**: Set up organizational departments
3. **Add Employees**: Create employee profiles with appropriate roles
4. **Add Assets**: Register IT assets in the system
5. **Create Tickets**: Start managing support requests

### User Roles

- **Admin**: Full system access, user management, all CRUD operations
- **IT Head**: Asset management, ticket assignment, maintenance oversight
- **IT Staff**: Ticket handling, asset maintenance, limited administrative tasks
- **Employee**: Create tickets, view assigned assets, basic system access

### Workflow Examples

#### Asset Assignment Workflow
1. Admin creates an asset in the system
2. Admin assigns asset to an employee
3. Employee can view their assigned assets
4. System tracks assignment dates and history

#### Support Ticket Workflow
1. Employee creates a support ticket
2. IT Staff reviews and assigns ticket
3. Ticket status updates through resolution process
4. Comments and updates logged throughout the process

## 🧪 Testing

The project includes comprehensive testing documentation:

- **Postman Collection**: Use the provided Postman collection for API testing


### API Testing with Postman

1. Import the provided Postman collection
2. Set up environment variables for base URL and tokens
3. Follow the comprehensive test checklist
4. Verify all endpoints and functionality

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 Python style guidelines
- Write comprehensive tests for new features
- Update documentation for any API changes
- Ensure all tests pass before submitting PR

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For support and questions:
- Create an issue in the repository
- Contact the development team
- Check the comprehensive documentation

---

**Built with ❤️ using Django and Django REST Framework**
