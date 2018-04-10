import os
from server.core.factory import create_app

from server.apis import api


config = os.environ.get('APP_SETTINGS', 'config.DevelopmentConfig')

app = create_app(config)
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
