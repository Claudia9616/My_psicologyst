import os

from app import create_app

app = create_app()

@app.route('/')
def index():
    return 'Hello world'

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)