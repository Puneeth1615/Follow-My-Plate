from dotenv import load_dotenv # NEW
load_dotenv() # NEW

from app import app #

if __name__ == '__main__': #
    app.run(debug=True) #