# RMM System Prototype

This project is a simplified Remote Monitoring and Management (RMM) system, designed to monitor and manage client machines remotely. It consists of two main components:

**Web-Based Dashboard**: A Django and Django REST Framework (DRF)-based platform for administrators.


## Features

### Web-Based Dashboard
- **Client Machine Management**:
  - List, add, and remove client machines.
- **Remote Commands**:
  - Send commands to selected client machines.
- **Log Viewing**:
  - View logs of API calls and client activities.
- **Authentication**:
  - API-key-based authentication for secure communication.

### Prerequisites

Ensure the following is installed on your system:

- **Python** (version 3.10 or higher)

### Clone the project & Go to the project directory

```bash
git clone https://github.com/suriya-mca/rmm_backend.git
cd rmm_backend
```

### Create .env file

```bash
SECRET_KEY=secret_key
DEBUG=False
DOMAIN=http://your-domain.com
```

### On Mac/Linux

```bash
chmod +x install.sh
./install.sh
```

### On Windows

```bash
./install.bat
```

## Endpoints

### Base URL

API endpoint: http://127.0.0.1:8000/api/v1
Admin: http://127.0.0.1:8000/admin

### Machine Endpoints

1. **List All Machines**
   - **URL**: `/machines/`
   - **Method**: `GET`
   - **Description**: Retrieves a list of all registered machines.

2. **Create a New Machine**
   - **URL**: `/machines/`
   - **Method**: `POST`
   - **Description**: Registers a new machine.

3. **Retrieve, Update, or Delete a Specific Machine**
   - **URL**: `/machines/<uuid:machine_id>/`
   - **Methods**: 
     - `GET`: Retrieves details of a specific machine.
     - `PUT`: Updates the machine’s information.
     - `DELETE`: Deletes the specified machine.

4. **Update Machine Status**
   - **URL**: `/machines/<uuid:machine_id>/status/`
   - **Method**: `POST`
   - **Description**: Updates the status of a specific machine.

5. **Manage Machine Logs**
   - **URL**: `/machines/<uuid:machine_id>/logs/`
   - **Methods**:
     - `GET`: Lists logs of a specific machine.
     - `POST`: Creates a new log entry for the machine.


## Notes

- This API requires proper authentication using API keys.
- Ensure that all requests follow the specified methods for each endpoint.