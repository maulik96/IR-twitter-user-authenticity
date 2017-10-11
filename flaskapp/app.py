from flask import Flask,request,send_from_directory
from flask_compress import Compress
from flask_assets import Bundle, Environment

import config
import shared_variables as var
from assets import getAssets
from routes import routes_module

# Initialize and configure app
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = config.static_file_max_age
app.config['MONGO_DBNAME'] = config.db_name

# Apply extensions on flaskapp
Compress(app)
assets = Environment(app)
assets.register(getAssets())
var.mongo.init_app(app, config_prefix='MONGO')

# Blueprint routes
app.register_blueprint(routes_module)

# Run app
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
