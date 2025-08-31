# 📚 Asset Helpdesk Workflow - API Testing Guide

Welcome to the Asset Helpdesk Workflow API testing guide! This comprehensive guide will help you test and interact with all the features of our asset management and helpdesk system through API endpoints using Postman.

## 🎯 Table of Contents

1. [Getting Started with Postman](#getting-started-with-postman)
2. [API Authentication Setup](#api-authentication-setup)
3. [Testing Environment Setup](#testing-environment-setup)
4. [User Roles & Permissions](#user-roles--permissions)
5. [API Endpoint Testing](#api-endpoint-testing)
6. [Common Testing Workflows](#common-testing-workflows)
7. [Troubleshooting](#troubleshooting)

---

## 🚀 Getting Started with Postman

### Prerequisites

- **Postman**: Download and install [Postman](https://www.postman.com/downloads/)
- **Running Server**: Ensure your Django server is running on `http://localhost:8000`
- **Database**: MySQL database should be set up and migrated

### Postman Setup

1. **Install Postman**
   - Download from [postman.com](https://www.postman.com/downloads/)
   - Install and create a free account

2. **Create a New Collection**
   - Click "New" → "Collection"
   - Name it "Asset Helpdesk Workflow API"
   - This will organize all your API requests

3. **Set Up Environment Variables**
   - Click "Environments" → "New Environment"
   - Name it "Asset Helpdesk Local"
   - Add these variables:
     - `base_url`: `http://localhost:8000`
     - `access_token`: (leave empty, will be filled after login)
     - `refresh_token`: (leave empty, will be filled after login)
     - `admin_token`: (for admin-specific tests)

---

## 🔐 API Authentication Setup

### Step 1: Create a Superuser (First Time Only)

If you haven't created a superuser yet:

```bash
cd asset-helpdesk-workflow
python manage.py createsuperuser
```

### Step 2: Get Authentication Tokens

1. **Create Login Request**
   - Method: `POST`
   - URL: `{{base_url}}/auth/login/`
   - Headers: `Content-Type: application/json`
   - Body (raw JSON):
   ```json
   {
     "email": "your_admin_email@example.com",
     "password": "your_password"
   }
   ```

2. **Save Tokens**
   - After successful login, you'll receive:
   ```json
   {
     "access": "your_access_token_here",
     "refresh": "your_refresh_token_here"
   }
   ```
   - Copy these tokens to your environment variables

3. **Set Authorization Header**
   - For all subsequent requests, add header:
   - `Authorization: Bearer {{access_token}}`

### Step 3: Test Authentication

Create a test request to verify your token:

- Method: `GET`
- URL: `{{base_url}}/auth/user/`
- Headers: `Authorization: Bearer {{access_token}}`

You should receive your user information if authentication is working.

---

## 🧪 Testing Environment Setup

### Initial Data Setup

Before testing, you'll need some basic data. Here's the recommended order:

1. **Create Departments**
2. **Create Employees**
3. **Create Assets**
4. **Create Ticket Categories**
5. **Test Assignments and Tickets**

### Sample Test Data

Keep these sample data structures ready for testing:

**Department:**
```json
{
  "name": "IT Department",
  "description": "Information Technology Department"
}
```

**Employee:**
```json
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@company.com",
  "position": "Software Developer",
  "role": "employee",
  "department": 1
}
```

**Asset:**
```json
{
  "name": "Dell Latitude Laptop",
  "category": "Laptop",
  "serial_number": "DL123456789",
  "purchase_date": "2024-01-15",
  "status": "active"
}
```

---

## 👥 User Roles & Permissions

### 🔐 Admin
**Full API access and control**
- All CRUD operations on all endpoints
- User management and system configuration
- Access to admin-specific endpoints

**Key Endpoints:**
- `/auth/admin/users/` - Manage all users
- All employee, asset, ticket, and maintenance endpoints

### 🏢 IT Head
**Department oversight and strategic management**
- View and manage all assets and tickets
- Assign tickets to IT staff
- Approve maintenance requests
- Generate reports

**Key Endpoints:**
- All asset and ticket management endpoints
- Assignment and maintenance endpoints

### 🛠 IT Staff
**Technical operations and support**
- Handle support tickets
- Perform asset maintenance
- Update ticket status
- Create maintenance logs

**Key Endpoints:**
- Ticket management endpoints
- Maintenance log endpoints
- Asset assignment endpoints

### 👤 Employee
**Basic user access**
- Submit support tickets
- View assigned assets
- Update personal information
- Track ticket progress

**Key Endpoints:**
- Limited ticket creation and viewing
- Personal asset viewing
- Profile management

---

## 🔧 API Endpoint Testing

### 1. Employee Management Testing

#### Create Department
- **Method**: `POST`
- **URL**: `{{base_url}}/api/departments/`
- **Headers**: `Authorization: Bearer {{access_token}}`
- **Body**:
```json
{
  "name": "IT Department",
  "description": "Information Technology Department"
}
```

#### Create Employee
- **Method**: `POST`
- **URL**: `{{base_url}}/api/employees/`
- **Headers**: `Authorization: Bearer {{access_token}}`
- **Body**:
```json
{
  "first_name": "Jane",
  "last_name": "Smith",
  "email": "jane.smith@company.com",
  "position": "IT Technician",
  "role": "it_staff",
  "department": 1
}
```

#### Get All Employees
- **Method**: `GET`
- **URL**: `{{base_url}}/api/employees/`
- **Headers**: `Authorization: Bearer {{access_token}}`

#### Update Employee
- **Method**: `PUT`
- **URL**: `{{base_url}}/api/employees/1/`
- **Headers**: `Authorization: Bearer {{access_token}}`
- **Body**: Updated employee data

### 2. Asset Management Testing

#### Create Asset
- **Method**: `POST`
- **URL**: `{{base_url}}/api/assets/`
- **Headers**: `Authorization: Bearer {{access_token}}`
- **Body**:
```json
{
  "name": "HP LaserJet Printer",
  "category": "Printer",
  "serial_number": "HP987654321",
  "purchase_date": "2024-02-01",
  "status": "active"
}
```

#### Get Assets with Filters
- **Method**: `GET`
- **URL**: `{{base_url}}/api/assets/?status=active&category=Laptop`
- **Headers**: `Authorization: Bearer {{access_token}}`

#### Update Asset Status
- **Method**: `PATCH`
- **URL**: `{{base_url}}/api/assets/1/`
- **Headers**: `Authorization: Bearer {{access_token}}`
- **Body**:
```json
{
  "status": "in_maintenance"
}
```

### 3. Helpdesk System Testing

#### Create Ticket Category
- **Method**: `POST`
- **URL**: `{{base_url}}/api/ticketcategories/`
- **Headers**: `Authorization: Bearer {{access_token}}`
- **Body**:
```json
{
  "name": "Hardware Issue",
  "description": "Problems with computer hardware"
}
```

#### Create Support Ticket
- **Method**: `POST`
- **URL**: `{{base_url}}/api/tickets/`
- **Headers**: `Authorization: Bearer {{access_token}}`
- **Body**:
```json
{
  "title": "Laptop not turning on",
  "description": "My laptop won't start up, shows black screen",
  "category": 1,
  "status": "open",
  "priority": "high",
  "reported_by": 2,
  "linked_asset": 1
}
```

#### Update Ticket Status
- **Method**: `PATCH`
- **URL**: `{{base_url}}/api/tickets/1/`
- **Headers**: `Authorization: Bearer {{access_token}}`
- **Body**:
```json
{
  "status": "in_progress",
  "assigned_to": 3
}
```

#### Add Ticket Comment
- **Method**: `POST`
- **URL**: `{{base_url}}/api/ticketcomments/`
- **Headers**: `Authorization: Bearer {{access_token}}`
- **Body**:
```json
{
  "ticket": 1,
  "commenter": 3,
  "comment_text": "Working on the issue. Will update soon."
}
```

### 4. Maintenance Management Testing

#### Create Maintenance Log
- **Method**: `POST`
- **URL**: `{{base_url}}/api/maintenancelogs/`
- **Headers**: `Authorization: Bearer {{access_token}}`
- **Body**:
```json
{
  "asset": 1,
  "maintenance_type": "corrective",
  "description": "Replaced faulty power supply",
  "date": "2024-03-15",
  "maintenance_date": "2024-03-15",
  "cost": "150.00",
  "technician": "Mike Johnson",
  "performed_by": 3
}
```

#### Get Maintenance History
- **Method**: `GET`
- **URL**: `{{base_url}}/api/maintenancelogs/?asset=1`
- **Headers**: `Authorization: Bearer {{access_token}}`

### 5. Asset Assignment Testing

#### Assign Asset to Employee
- **Method**: `POST`
- **URL**: `{{base_url}}/api/assignments/`
- **Headers**: `Authorization: Bearer {{access_token}}`
- **Body**:
```json
{
  "asset": 1,
  "employee": 2,
  "assigned_date": "2024-03-01",
  "return_date": "2024-12-31"
}
```

#### Get Assignment History
- **Method**: `GET`
- **URL**: `{{base_url}}/api/assignments/?employee=2`
- **Headers**: `Authorization: Bearer {{access_token}}`

---

## 🎯 Common Testing Workflows

### Workflow 1: Complete Asset Lifecycle

1. **Create Department**
   ```bash
   POST {{base_url}}/api/departments/
   ```

2. **Create Employee**
   ```bash
   POST {{base_url}}/api/employees/
   ```

3. **Create Asset**
   ```bash
   POST {{base_url}}/api/assets/
   ```

4. **Assign Asset**
   ```bash
   POST {{base_url}}/api/assignments/
   ```

5. **Create Maintenance Log**
   ```bash
   POST {{base_url}}/api/maintenancelogs/
   ```

6. **Update Asset Status**
   ```bash
   PATCH {{base_url}}/api/assets/1/
   ```

### Workflow 2: Support Ticket Resolution

1. **Create Ticket Category**
   ```bash
   POST {{base_url}}/api/ticketcategories/
   ```

2. **Create Support Ticket**
   ```bash
   POST {{base_url}}/api/tickets/
   ```

3. **Assign Ticket**
   ```bash
   PATCH {{base_url}}/api/tickets/1/
   ```

4. **Add Progress Comment**
   ```bash
   POST {{base_url}}/api/ticketcomments/
   ```

5. **Update Ticket Status**
   ```bash
   PATCH {{base_url}}/api/tickets/1/
   ```

6. **Create Maintenance Log**
   ```bash
   POST {{base_url}}/api/maintenancelogs/
   ```

### Workflow 3: Role-Based Testing

#### Admin Testing
- Test all CRUD operations
- Verify user management endpoints
- Check admin-specific permissions

#### IT Head Testing
- Test ticket assignment
- Verify asset oversight
- Check reporting capabilities

#### IT Staff Testing
- Test ticket handling
- Verify maintenance logging
- Check asset assignment

#### Employee Testing
- Test ticket creation
- Verify asset viewing
- Check profile management

---

## 🔍 Testing Best Practices

### 1. Environment Management
- Use separate environments for different test scenarios
- Keep production and development environments separate
- Use environment variables for dynamic data

### 2. Request Organization
- Group related requests in folders
- Use descriptive names for requests
- Add comments to explain test scenarios

### 3. Data Validation
- Always verify response status codes
- Check response body structure
- Validate data integrity across requests

### 4. Error Testing
- Test with invalid data
- Test with missing required fields
- Test with unauthorized access
- Test with expired tokens

### 5. Performance Testing
- Test with large datasets
- Monitor response times
- Test concurrent requests

---

## 🔍 Troubleshooting

### Common Issues

**Authentication Errors (401)**
- Check if token is expired
- Verify token format: `Bearer <token>`
- Re-authenticate and get new tokens

**Permission Errors (403)**
- Verify user role has required permissions
- Check if endpoint requires admin access
- Ensure user is properly authenticated

**Validation Errors (400)**
- Check required fields in request body
- Verify data format (dates, emails, etc.)
- Ensure foreign key relationships exist

**Not Found Errors (404)**
- Verify endpoint URL is correct
- Check if resource ID exists
- Ensure proper URL parameters

**Server Errors (500)**
- Check server logs for detailed errors
- Verify database connection
- Ensure all migrations are applied

### Debugging Tips

1. **Check Response Headers**
   - Look for error messages in response headers
   - Verify content type is application/json

2. **Use Postman Console**
   - View detailed request/response information
   - Check for network errors

3. **Test with cURL**
   - Use cURL for command-line testing
   - Compare with Postman results

4. **Check Django Logs**
   - Monitor Django development server output
   - Look for Python tracebacks

### Getting Help

**For API Issues:**
- Check the API documentation in README.md
- Verify endpoint URLs and methods
- Test with Postman collection

**For Authentication Issues:**
- Verify superuser credentials
- Check JWT token expiration
- Test login endpoint separately

**For Database Issues:**
- Ensure MySQL is running
- Check database migrations
- Verify connection settings

---

## 📞 Support Contacts

- **API Documentation**: Check README.md for complete endpoint reference
- **Testing Issues**: Review this guide and troubleshooting section
- **System Issues**: Check Django server logs and database status

---

## 🔄 Testing Checklist

### Pre-Testing Setup
- [ ] Postman installed and configured
- [ ] Django server running on localhost:8000
- [ ] Database migrated and superuser created
- [ ] Environment variables set up
- [ ] Authentication tokens obtained

### Core Functionality Testing
- [ ] Authentication endpoints working
- [ ] Employee management CRUD operations
- [ ] Asset management CRUD operations
- [ ] Ticket system functionality
- [ ] Maintenance logging
- [ ] Asset assignment system

### Role-Based Testing
- [ ] Admin permissions verified
- [ ] IT Head permissions tested
- [ ] IT Staff permissions tested
- [ ] Employee permissions tested

### Error Handling
- [ ] Invalid authentication tested
- [ ] Missing required fields tested
- [ ] Unauthorized access tested
- [ ] Invalid data formats tested

---

*This API testing guide is designed for developers and testers using Postman to verify the Asset Helpdesk Workflow system functionality.*

**Last Updated**: [Current Date]
**Version**: 1.0
