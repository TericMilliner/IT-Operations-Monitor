
# IT Operations Monitoring Dashboard

A Python-based IT infrastructure monitoring application
that tracks computer performance, checks network
connectivity, and stores historical data using SQLite.

## Project Overview

This project was developed to gain hands-on experience
with IT infrastructure monitoring, Python programming,
network troubleshooting, and database management.

The application provides a web-based dashboard using
Streamlit to visualize system performance and monitor
network connectivity.

## Features

- CPU usage monitoring
- RAM utilization monitoring
- Disk usage monitoring
- System health alerts
- Network connectivity monitoring
- TCP connection response time measurement
- Network traffic statistics
- SQLite performance data storage
- Historical performance charts
- Automatically refreshing dashboard

## Technologies Used

- Python
- Streamlit
- Psutil
- Pandas
- SQLite
- Git and GitHub

## Project Structure

- `monitor.py` - System monitoring script
- `network.py` - Network monitoring functions
- `database.py` - SQLite database operations
- `dashboard.py` - Web dashboard
- `requirements.txt` - Project dependencies

## Installation

1. Install Python 3.
2. Clone this repository.
3. Open a terminal in the project folder.
4. Install dependencies:

   python -m pip install -r requirements.txt

5. Start the application:

   python -m streamlit run dashboard.py

6. Open http://localhost:8501 in your browser.

## How It Works

The application uses Psutil to collect CPU, RAM,
disk, and network traffic measurements.

It also tests a TCP connection to a public endpoint
to monitor connectivity.

Performance measurements are stored in a local
SQLite database, allowing users to review historical
data through Streamlit charts and tables.

## Screenshots

Screenshots of the application are available
in the screenshots folder.

## Future Improvements

- Email notifications for system alerts
- Exportable performance reports
- Additional network monitoring features
- Multi-device monitoring support

## Author

**Teric Milliner**
Computer Information Systems Student
Robert Morris University

**LinkedIn:** https://www.linkedin.com/in/teric-milliner-1903b5388/