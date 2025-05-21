import urllib.request
import urllib.parse
import json


def post_to_localhost():
    url = "http://localhost:8888/"  # Example endpoint, adjust as needed

    # Example data to send (can be any dictionary)
    data_dict = {
        "id": 0,
        "amount": 200,
    }

    # Encode the data to bytes
    data_encoded = json.dumps(data_dict).encode('utf-8')

    # Create the request object
    req = urllib.request.Request(url, data=data_encoded, method='POST')
    req.add_header('Content-Type', 'application/json') # Specify content type as JSON

    try:
        with urllib.request.urlopen(req) as response:
            response_data = response.read()
            status_code = response.getcode()
            print(f"Response status code: {status_code}")
            print(f"Response data: {response_data.decode('utf-8')}")
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} {e.reason}")
        print(f"Response body: {e.read().decode('utf-8') if e.fp else 'No response body'}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
    except ConnectionRefusedError:
        print(f"Connection Refused: Ensure the server is running at {url}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    post_to_localhost()
