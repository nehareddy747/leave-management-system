# Leave Management System

A complete full-stack web application designed for managing employee leaf requests. Built with Vue.js, Flask, and MongoDB.

## Features

- **Authentication**: Secure JWT-based login and signup with bcrypt password hashing.
- **Roles**: Distinct functionalities mapped to `employee` and `employer` roles.
- **Employee Actions**: Submit leave applications specifying type, dates, and reason. View history and ongoing request status.
- **Employer Actions**: Manage all incoming leaf requests via a dedicated dashboard. Approve or reject request with real-time updates.
- **Dynamic UI**: Uses conditional rendering for routing and views depending on the logged-in user context. Built with Tailwind CSS for modern, intuitive layouts.

## Technology Stack

- **Frontend**: Vue.js (Vite), Tailwind CSS, Vue Router, Axios
- **Backend**: Python, Flask, Flask-Cors, PyJWT, bcrypt, python-dotenv
- **Database**: MongoDB Atlas via PyMongo
- **Architecture**: RESTful API design

---

## Setting Up Locally

### Prerequisites

- Node.js & npm installed
- Python 3.9+ installed
- A MongoDB Cluster URI (or local MongoDB running)

### Setup the Backend
1. Open a terminal and navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Create and activate a Virtual Environment (Optional but recommended):
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Setup Environment Variables:
   The backend expects a `.env` file in the `backend/` directory. (Note: placeholder is provided during initialization)
   ```ini
   MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/leave_db
   SECRET_KEY=super_secret_dev_key
   ```
5. Run the development server:
   ```bash
   python run.py
   ```
   The backend will start at `http://localhost:5000`.

### Setup the Frontend
1. Open up an entirely new terminal in the frontend directory:
   ```bash
   cd frontend
   ```
2. Install npm dependencies:
   ```bash
   npm install
   ```
3. Run the vite dev server:
   ```bash
   npm run dev
   ```
   The frontend will likely run at `http://localhost:5173`. Open this URL in your browser.

---

## API Endpoints List

### Auth (`/api/auth`)
- `POST /signup` - Register a new user (`name`, `email`, `password`, `role`)
- `POST /login` - Login (`email`, `password`) returns JWT token
- `GET /me` - Get logged-in user details (Requires Auth Header)

### Leaves (`/api/leaves`)
- `POST /` - Apply for leave (Requires Auth Header, role: employee)
- `GET /my_leaves` - Get logged-in employee leaves (Requires Auth Header, role: employee)
- `GET /all` - Get all leaves (Requires Auth Header, role: employer)
- `PUT /<leave_id>/status` - Approve or reject leave (Requires Auth Header, role: employer)

---

## Deployment to AWS EC2

### 1. Launch EC2 instance
- Launch an Ubuntu Server instance on AWS EC2.
- Configure Security Group inbound rules to allow Custom TCP on port `5000` (Backend) and port `80` / `443` (Frontend). And keep `22` (SSH) open for remote access.

### 2. Connect to the Instance
```bash
ssh -i "your-key.pem" ubuntu@<your-ec2-public-ip>
```

### 3. Install System Dependencies
```bash
sudo apt update
sudo apt install python3-pip python3-venv nodejs npm nginx -y
```

### 4. Clone Project
Clone your repository containing this project into the EC2 instance.

### 5. Setup Backend (Gunicorn)
1. Navigate to the backend directory and create a virtual environment.
   ```bash
   cd backend
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. Configure your specific `.env` for production values.
3. Test running the app with gunicorn:
   ```bash
   gunicorn -w 4 -b 0.0.0.0:5000 run:app
   ```
   *(For an actual deployment, you would run gunicorn as a background systemd service).*

### 6. Build and Serve Frontend (Nginx)
1. Update `baseURL` inside `frontend/src/axios.js` to point to `http://<your-ec2-public-ip>:5000/api`.
2. Install dependencies and build:
   ```bash
   cd ../frontend
   npm install
   npm run build
   ```
3. Copy the output `dist` folder to Nginx's html folder:
   ```bash
   sudo cp -r dist/* /var/www/html/
   ```
4. Update nginx configuration (`/etc/nginx/sites-available/default`) if needed to handle history fallback for Vue router.
5. Restart nginx:
   ```bash
   sudo systemctl restart nginx
   ```

### 7. Access
Visit your public EC2 IP address inside the browser to use your deployed system!
