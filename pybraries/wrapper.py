import requests
from requests.exceptions import HTTPError
import fire
import os

# api_key = os.environ['LIBRARIES_API_KEY']
class API:
    def __init__(self):
        self.api_key = os.environ['LIBRARIES_API_KEY']

        # check for valid API key

    def __call_api(self, thing, *args, **kwargs):
        """
        Call the API.
        Args:
            manager (str): package manager
            package (str): package name
        Returns:
            r.json (json): response from libraries.io
        """

        if thing == "project":
            manager = kwargs['manager'] 
            package = kwargs['package']

            try:
                r = requests.get(
                    f'https://libraries.io/api/{manager}/{package}',
                    params=dict(api_key=self.api_key),
                    timeout=5,
                )
                r.raise_for_status()
            except HTTPError as http_err:
                print(f'HTTP error occurred: {http_err}')  # Python 3.6
            except Exception as err:
                print(f'Other error occurred: {err}')  # Python 3.6

            response = r.json()

        return response


    def project(self, *args, **kwargs):
        """
        Return information about a package and its versions.
        Args:
            manager (str): package manager
            package (str): package name
        Returns:
            r.json (json): response from libraries.io
        """

        my_call = self.__call_api("project", *args, **kwargs)

        return my_call

api = API()
pkg = api.project(manager="pypi", package="plotly")

# From the command line you can call any function by name with arguments
if __name__ == "__main__":
    fire.Fire()
