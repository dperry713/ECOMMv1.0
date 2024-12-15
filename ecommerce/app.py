from flask import Flask, request
from flask_graphql import GraphQLView
from models.models import db
from schemas.schema import schema
from config import Config
import logging

app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
db.init_app(app)

# Logging
logging.basicConfig(filename='logs/app.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s')

@app.before_request
def log_request():
    logging.info(f"Request: {request.method} {request.path}")

# GraphQL endpoint
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
