import pkg_resources
from flask_restful import Resource


class ListPyPiPackages(Resource):
    def post(self):
        packages = []
        for package in pkg_resources.working_set:
            packages.append({package.as_requirement().project_name: package.version})

        return packages, 200
