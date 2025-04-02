# Python Flask Tutorial Deploy on Blossom

A ready-to-deploy Python Flask app to get you started quickly on [Blossom](https://blossom-cloud.com). This modern web application showcases Flask capabilities with a beautiful user interface and interactive features.

## Features

- Modern, responsive UI built with Tailwind CSS
- Real-time API interactions
- Visual feedback for all actions
- Clean, professional design
- Interactive demo components:
  - Greeting Generator
  - Echo Service
- Error handling and status notifications

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. Clone this repository
2. Navigate to the project directory
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   ```bash
   # On Windows
   .\venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   # Fish shell
   source venv/bin/activate.fish
   ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Development Mode (with auto-reload)
```bash
FLASK_DEBUG=1 python app.py
```

### Production Mode
```bash
python app.py
```

The server will start on port 5000 by default. You can change this by setting the `PORT` environment variable:

```bash
PORT=3000 python app.py
```

The application will listen on all interfaces (0.0.0.0) and be accessible at:
- http://localhost:3000 (or your configured port)
- http://<your-ip>:3000 (for external access)

## Environment Variables

- `PORT`: The port number to run the server on (default: 5000). The application will listen on all interfaces (0.0.0.0).
- `FLASK_DEBUG`: Enable debug mode when set to 1 (default: 0)
- `FLASK_NO_COLOR`: Disable ANSI color codes in logs when set to 1 (default: 1)
- `PYTHONUNBUFFERED`: Disable Python output buffering when set to 1 (default: 1)

## Demo Features

### Greeting Generator
- Enter your name in the input field
- Click "Get Greeting" to receive a personalized greeting
- See the response displayed in real-time

### Echo Service
- Enter any message in the text area
- Click "Send Message" to see your message echoed back
- View the complete response including timestamp

## Technical Details

The application is built using:
- Flask for the backend
- Tailwind CSS for styling
- Vanilla JavaScript for frontend interactions
- Modern fetch API calls

## API Endpoints

The application exposes two API endpoints:

### GET /api/hello
Returns a greeting message. Optional query parameter:
```
/api/hello?name=YourName
```

### POST /api/echo
Echoes back any JSON data sent in the request body.

## Testing the API

You can test the API endpoints using curl:

```bash
# Test the hello endpoint
curl http://localhost:3000/api/hello
curl http://localhost:3000/api/hello?name=John

# Test the echo endpoint
curl -X POST -H "Content-Type: application/json" -d '{"message":"Hello World"}' http://localhost:3000/api/echo
```
