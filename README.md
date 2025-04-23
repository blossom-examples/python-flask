# Python Flask Tutorial Deploy on Blossom

[![Blossom Badge](https://img.boltops.com/images/blossom/logos/blossom-readme.png)](https://blossom-cloud.com)

A ready-to-deploy Python Flask app to get you started quickly on [Blossom](https://blossom-cloud.com).

## Quick Start

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # or `venv/Scripts/activate` on Windows
source venv/bin/activate.fish  # fish shell

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Visit `http://localhost:5000` in your browser to see the demo application.

<details>
<summary>Additional Information</summary>

### Environment Variables
- `PORT`: Change the port (default: 5000)
- `FLASK_DEBUG`: Enable debug mode (set to 1)

### API Endpoints
```bash
# Get a greeting
curl http://localhost:5000/api/hello?name=John

# Echo a message
curl -X POST -H "Content-Type: application/json" \
     -d '{"message":"Hello"}' http://localhost:5000/api/echo
```
</details>
