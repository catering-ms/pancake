export FLASK_ENV=development
export FLASK_APP=src/runner:app
export SQLALCHEMY_DATABASE_URI=mysql://root:openmysql@localhost/guacamole

export FLASK_DEBUG=1
export FLASK_RUN_HOST=0.0.0.0
export FLASK_RUN_PORT=5001