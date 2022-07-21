from app import StartApp
import os
import app.debug as debug
from dotenv import load_dotenv


# Get env variable
load_dotenv()
app = StartApp()

if __name__ == '__main__':
    debug.log("App started", True)
    app.run(debug=os.getenv("debug", 'False').lower() in ('true'))
