import os
from server.api.factory import create_app


config = os.environ.get('APP_SETTINGS', 'config.DevelopmentConfig')

app = create_app(config)

if __name__ == '__main__':
    app.run(debug=True)
