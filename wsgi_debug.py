import os

os.environ['DEBUG'] = '1'

from virasana.app import app

if __name__ == '__main__':
    app.run()