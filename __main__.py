from flask import Flask, render_template, request, redirect, url_for
from flask_restful import Api, Resource
import pkg_resources


# Define the basic config
PORT = 2612
# ----------------------------------------------------

# Create the application instance
# __name__ is the name of the current module
app = Flask(__name__, template_folder='html', static_folder='static', root_path='.')
app_api = Api(app)

class ListPyPi(Resource):
    def _get(self):
        packages = []
        for package in pkg_resources.working_set:
            packages.append({package.as_requirement(): package.version})
        
        return packages, 200

    def get(self):
        return self._get()
        

@app.route('/')
def startpage():
    return render_template('index.html')

def main():
    app_api.add_resource(ListPyPi, '/api/packages')
    app.run(debug=True, port=PORT)

if __name__ == '__main__':
    main()
