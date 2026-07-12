# Asset_flow-Odoo
# AssetFlow

### Intelligent Enterprise Asset & Resource Management

**AssetFlow** is a centralized enterprise platform for managing the complete lifecycle of organizational assets — from allocation and booking to transfers, maintenance, audits, and reporting.

Built for the **Odoo Hackathon 2026**, AssetFlow transforms fragmented asset tracking into a structured, transparent, and data-driven workflow.

> **One platform. Every asset. Complete visibility.**

---

## The Problem

Organizations often manage assets across spreadsheets, emails, paper records, and disconnected systems. This creates:

* Poor visibility into asset ownership and availability
* Double bookings and scheduling conflicts
* Delayed maintenance
* Difficult asset transfers
* Weak accountability and audit trails
* Limited insight into asset utilization

AssetFlow provides a **single source of truth** for enterprise assets and their complete operational lifecycle.

---

## Our Solution

AssetFlow combines asset management, resource allocation, booking, maintenance, auditing, notifications, and analytics into one unified platform.

The system is designed around a simple principle:

**Every asset should have a clear status, owner, history, and next action.**

---

## Key Features

### Intelligent Dashboard

A centralized command center providing real-time visibility into:

* Total assets
* Available assets
* Allocated assets
* Assets under maintenance
* Department-wise allocation
* Category distribution
* Recent activity
* Operational insights

---

### Asset Lifecycle Management

Track assets throughout their complete lifecycle:

**Available → Allocated → Returned → Maintenance → Available**

Each asset maintains structured information about its status, allocation, usage, and operational history.

---

### Asset Allocation & Return Workflow

Administrators can:

* Allocate assets to employees
* Define expected return dates
* Track active allocations
* Process asset returns
* Record check-in notes
* Maintain allocation history

This creates clear accountability for every assigned asset.

---

### Smart Booking System

Shared organizational resources can be reserved through a structured booking workflow.

Features include:

* Time-based reservations
* Booking status tracking
* Upcoming and ongoing bookings
* Conflict-aware resource management
* Centralized booking visibility

---

### Maintenance Management

Asset issues can be tracked through a complete maintenance workflow:

**Requested → Approved → In Progress → Completed**

The system supports:

* Maintenance requests
* Approval tracking
* Issue descriptions
* Resolution notes
* Maintenance history

This helps organizations reduce downtime and improve asset reliability.

---

### Asset Transfer Workflow

Assets can move between employees, teams, or departments through a controlled transfer process.

This ensures that asset ownership changes remain transparent and traceable.

---

### Audit Trail

AssetFlow is designed with accountability in mind.

Important actions can be recorded to provide:

* Historical visibility
* Operational traceability
* Better accountability
* Support for organizational audits

---

### Notification System

Users can receive notifications for important events involving:

* Allocations
* Transfers
* Bookings
* Maintenance
* Audits
* System updates

---

### Reports & Analytics

AssetFlow converts operational data into actionable information through:

* Asset status reports
* Allocation analytics
* Category distribution
* Department-level insights
* Visual dashboards

---

## What Makes AssetFlow Different?

AssetFlow is not simply an asset inventory.

It connects the **entire operational journey of an asset**:

```text
Asset Registration
        ↓
Availability
        ↓
Allocation / Booking
        ↓
Usage
        ↓
Transfer / Return
        ↓
Maintenance
        ↓
Audit & Reporting
        ↓
Operational Insights
```

By connecting these workflows, AssetFlow provides organizations with a unified view of **where an asset is, who is responsible for it, what condition it is in, and how it is being used**.

---

## System Architecture

```text
┌──────────────────────────────────────────────┐
│               React Frontend                 │
│     Dashboard • Assets • Reports • UI        │
└──────────────────────┬───────────────────────┘
                       │ REST API
                       ▼
┌──────────────────────────────────────────────┐
│               FastAPI Backend                │
│                                              │
│  API Layer → Service Layer → Data Models     │
│                                              │
│  Allocation • Booking • Transfer             │
│  Maintenance • Notification • Audit          │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│                 Database                     │
│          SQLAlchemy ORM / SQL Storage        │
└──────────────────────────────────────────────┘
```

The backend follows a layered architecture:

```text
API Routes
    ↓
Service Layer
    ↓
SQLAlchemy Models
    ↓
Database
```

This separation keeps business logic reusable and the system easier to extend.

---

## Technology Stack

### Frontend

* React
* TypeScript
* Tailwind CSS
* Framer Motion
* Chart.js
* Axios
* React Router
* Lucide React
* React Hot Toast

### Backend

* Python
* FastAPI
* SQLAlchemy
* Pydantic
* Uvicorn
* REST APIs

### Database

* SQL-based persistence
* SQLAlchemy ORM
* SQLite for local development

### Development & Collaboration

* Git
* GitHub
* VS Code
* Swagger / OpenAPI

---

## Core Backend Modules

```text
app/
├── api/
│   └── allocations.py
│
├── models/
│   ├── allocation.py
│   ├── audit.py
│   ├── booking.py
│   ├── maintenance_request.py
│   ├── notification.py
│   └── transfer.py
│
├── schemas/
│   ├── allocation.py
│   ├── audit.py
│   ├── booking.py
│   ├── maintenance.py
│   ├── notification.py
│   └── transfer.py
│
├── services/
│   ├── allocation_service.py
│   ├── booking_service.py
│   ├── maintenance_service.py
│   ├── notification_service.py
│   └── transfer_service.py
│
├── database.py
└── main.py
```

---

## API Example

### Create an Allocation

```http
POST /allocations/
```

```json
{
  "asset_id": 1,
  "employee_id": 12,
  "allocated_by": 3,
  "expected_return_date": "2026-07-20T10:00:00"
}
```

### Get All Allocations

```http
GET /allocations/
```

### Return an Asset

```http
PUT /allocations/{allocation_id}/return
```

Example response:

```json
{
  "allocation_id": 1,
  "asset_id": 1,
  "employee_id": 12,
  "allocated_by": 3,
  "status": "RETURNED"
}
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Asset_flow-Odoo
```

### 2. Set Up the Backend

```bash
cd backend
python -m venv venv
```

Activate the virtual environment.

**Windows:**

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the API server:

```bash
uvicorn app.main:app --reload
```

The backend runs on:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

### 3. Set Up the Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## Engineering Principles

AssetFlow was built around several core engineering principles:

* **Modularity** — business domains are separated into models, schemas, services, and APIs.
* **Reusability** — shared services and frontend components reduce duplication.
* **Scalability** — the architecture can evolve from a hackathon prototype into a larger enterprise platform.
* **Traceability** — operational workflows are designed around clear asset history and accountability.
* **User Experience** — complex enterprise workflows are presented through a clean and accessible interface.

---

## Future Scope

AssetFlow can be extended with:

* AI-powered asset utilization recommendations
* Predictive maintenance
* QR and barcode-based asset check-in/check-out
* Role-based access control
* Automated approval workflows
* Email and push notifications
* Multi-organization support
* Cloud deployment
* Advanced utilization forecasting
* Integration with ERP and HR systems

---

## Vision

Modern organizations should not have to ask:

> “Where is this asset?”

They should already know.

AssetFlow aims to become an **intelligent operational layer for enterprise resources**, giving organizations complete visibility from acquisition to allocation, maintenance, audit, and retirement.

---

## Built for Odoo Hackathon 2026

**AssetFlow — Track smarter. Allocate better. Operate with clarity.**
