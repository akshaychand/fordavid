import os

from server.core import create_app


config = os.environ.get('APP_SETTINGS', 'config.DevelopmentConfig')

app = create_app(config)

if __name__ == '__main__':
    app.run(debug=True)
