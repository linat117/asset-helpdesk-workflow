# 📚 Asset Helpdesk Workflow - User Guide

Welcome to the Asset Helpdesk Workflow system! This comprehensive guide will help you navigate and effectively use all the features of our asset management and helpdesk platform.

## 🎯 Table of Contents

1. [Getting Started](#getting-started)
2. [User Roles & Permissions](#user-roles--permissions)
3. [Dashboard Overview](#dashboard-overview)
4. [Asset Management](#asset-management)
5. [Employee Management](#employee-management)
6. [Helpdesk System](#helpdesk-system)
7. [Maintenance Management](#maintenance-management)
8. [Asset Assignment](#asset-assignment)
9. [Common Tasks](#common-tasks)
10. [Troubleshooting](#troubleshooting)

---

## 🚀 Getting Started

### First Time Setup

1. **Access the System**
   - Open your web browser
   - Navigate to: `http://localhost:8000` (or your server URL)
   - You'll see the login page

2. **Login**
   - Enter your email address and password
   - Click "Login" to access the system
   - If you don't have credentials, contact your system administrator

3. **Dashboard Welcome**
   - After login, you'll be redirected to your personalized dashboard
   - The dashboard shows relevant information based on your role

### System Navigation

The system has a clean, intuitive interface with the following main sections:

- **🏠 Dashboard**: Overview and quick actions
- **📦 Assets**: Asset management and tracking
- **👥 Employees**: Employee and department management
- **🎫 Helpdesk**: Support ticket system
- **🔧 Maintenance**: Asset maintenance logs
- **📋 Assignments**: Asset assignment tracking
- **👤 Profile**: Your account settings

---

## 👥 User Roles & Permissions

### 🔐 Admin
**Full system access and control**
- Create and manage all users
- Configure system settings
- Access all reports and analytics
- Manage departments and roles
- Full asset lifecycle management

### 🏢 IT Head
**Department oversight and strategic management**
- View all IT assets and tickets
- Assign tickets to IT staff
- Approve maintenance requests
- Generate department reports
- Manage asset assignments

### 🛠 IT Staff
**Technical operations and support**
- Handle support tickets
- Perform asset maintenance
- Update ticket status
- Create maintenance logs
- Assign assets to employees

### 👤 Employee
**Basic user access**
- Submit support tickets
- View assigned assets
- Update personal information
- Track ticket progress
- Request asset assignments

---

## 📊 Dashboard Overview

### What You'll See

**For Admins & IT Heads:**
- Total assets count and status breakdown
- Active tickets by priority
- Recent maintenance activities
- Asset assignment overview
- Quick action buttons

**For IT Staff:**
- Assigned tickets
- Pending maintenance tasks
- Recent asset updates
- Quick ticket creation

**For Employees:**
- Your assigned assets
- Your submitted tickets
- Recent system updates
- Quick ticket submission

### Quick Actions

From the dashboard, you can quickly:
- Create new tickets
- Add new assets
- Assign assets
- View reports
- Update your profile

---

## 📦 Asset Management

### Viewing Assets

1. **Navigate to Assets**
   - Click "Assets" in the main menu
   - You'll see a list of all assets (filtered by your permissions)

2. **Asset List Features**
   - **Search**: Use the search bar to find specific assets
   - **Filter**: Filter by status, category, or department
   - **Sort**: Click column headers to sort
   - **View Details**: Click on any asset to see full details

### Asset Statuses

- **🟢 Active**: Asset is in use and functioning
- **🔧 In Maintenance**: Asset is being repaired or serviced
- **🔴 Retired**: Asset is no longer in use
- **⚠️ Lost**: Asset cannot be located
- **🗑️ Disposed**: Asset has been disposed of

### Adding New Assets

**Only Admins and IT Heads can add assets**

1. **Click "Add Asset"**
2. **Fill in the required information:**
   - **Name**: Descriptive name for the asset
   - **Category**: Type of asset (e.g., Laptop, Printer, Software)
   - **Serial Number**: Unique identifier (required)
   - **Purchase Date**: When the asset was acquired
   - **Status**: Initial status (usually "Active")
3. **Click "Save"**

### Editing Assets

1. **Find the asset** you want to edit
2. **Click on the asset** to view details
3. **Click "Edit"**
4. **Make your changes**
5. **Click "Save"**

### Asset Details Page

When you click on an asset, you'll see:
- **Basic Information**: Name, category, serial number
- **Status History**: Timeline of status changes
- **Assignment History**: Who has used this asset
- **Maintenance Logs**: All maintenance activities
- **Related Tickets**: Support tickets for this asset

---

## 👥 Employee Management

### Viewing Employees

1. **Navigate to Employees**
   - Click "Employees" in the main menu
   - View all employees (filtered by your permissions)

2. **Employee List Features**
   - Search by name or email
   - Filter by department or role
   - Sort by any column
   - Click to view detailed profiles

### Employee Roles

- **Admin**: Full system access
- **IT Head**: Department oversight
- **IT Staff**: Technical support
- **Employee**: Basic user access

### Adding New Employees

**Only Admins can add employees**

1. **Click "Add Employee"**
2. **Fill in the information:**
   - **First Name** and **Last Name**
   - **Email**: Must be unique
   - **Position**: Job title
   - **Role**: Access level
   - **Department**: Organizational unit
3. **Click "Save"**

### Employee Profile

Each employee profile shows:
- **Personal Information**: Name, email, position
- **Department**: Organizational unit
- **Role**: System access level
- **Assigned Assets**: Currently assigned assets
- **Submitted Tickets**: Support tickets they've created
- **Assignment History**: Past asset assignments

---

## 🎫 Helpdesk System

### Creating Support Tickets

1. **Navigate to Helpdesk**
   - Click "Helpdesk" in the main menu
   - Click "Create New Ticket"

2. **Fill in Ticket Details:**
   - **Title**: Brief description of the issue
   - **Description**: Detailed explanation of the problem
   - **Category**: Type of issue (Hardware, Software, Network, etc.)
   - **Priority**: How urgent the issue is
   - **Linked Asset**: Which asset is affected (if applicable)

3. **Submit the Ticket**
   - Click "Submit" to create the ticket
   - You'll receive a ticket number for tracking

### Ticket Priorities

- **🟢 Low**: Minor issues, non-urgent
- **🟡 Medium**: Standard issues, normal priority
- **🟠 High**: Important issues, needs attention
- **🔴 Urgent**: Critical issues, immediate attention required

### Ticket Statuses

- **📝 Open**: Ticket created, waiting for assignment
- **🔄 In Progress**: Work has begun on the ticket
- **✅ Resolved**: Issue has been fixed
- **🔒 Closed**: Ticket completed and closed

### Managing Your Tickets

**For Employees:**
- View all tickets you've submitted
- Track progress and updates
- Add comments to provide more information
- Close tickets when resolved

**For IT Staff:**
- View assigned tickets
- Update ticket status
- Add progress notes
- Assign tickets to other staff if needed

**For IT Heads:**
- View all tickets in the system
- Assign tickets to appropriate staff
- Monitor ticket progress
- Generate ticket reports

### Ticket Updates and Comments

1. **View Ticket Details**
   - Click on any ticket to see full details

2. **Add Updates**
   - **For IT Staff**: Add progress notes and status updates
   - **For Employees**: Add comments with additional information

3. **Track Progress**
   - View the complete history of updates
   - See who made each update and when

---

## 🔧 Maintenance Management

### Creating Maintenance Logs

**Only IT Staff and IT Heads can create maintenance logs**

1. **Navigate to Maintenance**
   - Click "Maintenance" in the main menu
   - Click "Add Maintenance Log"

2. **Fill in Maintenance Details:**
   - **Asset**: Select the asset being maintained
   - **Maintenance Type**: 
     - **Preventive**: Regular maintenance
     - **Corrective**: Fixing issues
     - **Emergency**: Urgent repairs
   - **Description**: What work was performed
   - **Date**: When maintenance was performed
   - **Cost**: Maintenance expenses (optional)
   - **Technician**: Who performed the work
   - **Performed By**: Employee record of the technician

3. **Save the Log**
   - Click "Save" to record the maintenance

### Maintenance Types

- **🛡️ Preventive**: Regular maintenance to prevent issues
- **🔧 Corrective**: Fixing existing problems
- **🚨 Emergency**: Urgent repairs for critical issues

### Viewing Maintenance History

1. **Asset-Specific History**
   - Go to any asset's detail page
   - View the "Maintenance Logs" section
   - See all maintenance performed on that asset

2. **System-Wide History**
   - Navigate to Maintenance section
   - View all maintenance logs
   - Filter by date, type, or technician

---

## 📋 Asset Assignment

### Assigning Assets to Employees

**Only Admins, IT Heads, and IT Staff can assign assets**

1. **Navigate to Assignments**
   - Click "Assignments" in the main menu
   - Click "Assign Asset"

2. **Fill in Assignment Details:**
   - **Asset**: Select the asset to assign
   - **Employee**: Choose who will receive the asset
   - **Assigned Date**: When the assignment begins
   - **Return Date**: Expected return date (optional)

3. **Save Assignment**
   - Click "Save" to create the assignment

### Managing Assignments

**Viewing Current Assignments:**
- See all active asset assignments
- Filter by employee or asset
- Track assignment dates

**Returning Assets:**
- Update the return date when assets are returned
- The asset status will automatically update

### Assignment History

Each asset and employee has a complete assignment history showing:
- When assets were assigned
- Who had possession
- Assignment duration
- Return dates

---

## 🎯 Common Tasks

### For Employees

**Submitting a Support Ticket:**
1. Go to Helpdesk → Create New Ticket
2. Fill in the issue details
3. Submit and track progress

**Checking Your Assets:**
1. Go to Dashboard or Assets section
2. View your currently assigned assets
3. Check asset status and details

**Updating Your Profile:**
1. Click your name in the top right
2. Select "Profile"
3. Update your information

### For IT Staff

**Handling Support Tickets:**
1. Go to Helpdesk → View Assigned Tickets
2. Update ticket status as you work
3. Add progress notes
4. Mark as resolved when complete

**Performing Maintenance:**
1. Go to Maintenance → Add Maintenance Log
2. Record the work performed
3. Update asset status if needed

**Assigning Assets:**
1. Go to Assignments → Assign Asset
2. Select asset and employee
3. Set assignment dates

### For IT Heads

**Managing the Team:**
1. Go to Helpdesk → View All Tickets
2. Assign tickets to appropriate staff
3. Monitor progress and performance

**Asset Oversight:**
1. Go to Assets → View All Assets
2. Monitor asset status and health
3. Approve maintenance requests

**Generating Reports:**
1. Use Dashboard analytics
2. Export data for reporting
3. Monitor system usage

### For Admins

**User Management:**
1. Go to Employees → Add Employee
2. Set appropriate roles and permissions
3. Manage departments

**System Configuration:**
1. Configure system settings
2. Manage categories and departments
3. Set up initial data

---

## 🔍 Troubleshooting

### Common Issues

**Can't Login?**
- Check your email and password
- Contact your administrator if locked out
- Ensure you're using the correct URL

**Can't See Certain Features?**
- Check your user role and permissions
- Contact your administrator for access
- Some features are role-specific

**Ticket Not Updating?**
- Refresh the page
- Check if you have permission to update
- Contact IT support if issues persist

**Asset Status Not Changing?**
- Ensure you have permission to modify assets
- Check if the asset is currently assigned
- Contact your administrator

### Getting Help

**For Technical Issues:**
- Submit a support ticket through the helpdesk
- Include detailed error messages
- Provide screenshots if possible

**For Access Issues:**
- Contact your system administrator
- Provide your employee ID and role
- Explain what access you need

**For Training:**
- Review this user guide
- Contact your IT department
- Request additional training sessions

---

## 📞 Support Contacts

- **System Administrator**: [Admin Email]
- **IT Support**: [IT Support Email]
- **Emergency Contact**: [Emergency Phone]

---

## 🔄 System Updates

The system is regularly updated with new features and improvements. You'll be notified of:
- New features and capabilities
- System maintenance schedules
- Important security updates
- Training opportunities

---

*This user guide is maintained by the IT department. For the most current version, please check the system help section or contact your administrator.*

**Last Updated**: [Current Date]
**Version**: 1.0
