
from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

# Sample table
sample_table = {
    "test@example.com": {"name": "John Doe", "points": 100},
    "user@example.com": {"name": "Jane Smith", "points": 200},
    "another@example.com": {"name": "Alice Johnson", "points": 150}
}

class UserInfo(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True, help='Email is required')
        args = parser.parse_args()
        
        email = args['email']

        if email in sample_table:
            return sample_table[email]
        else:
            return {"error": "Email not found"}, 404

api.add_resource(UserInfo, '/get_info')

if __name__ == '__main__':
    app.run(debug=True)
