import os
import requests


def main():
    url = os.environ["INPUT_URL"]
    user = os.environ["INPUT_USER"]
    passw = os.environ["INPUT_PASSW"]

    response = requests.post(url, auth=(user, passw))

    print(f"::set-output name=Status::{response.status_code}")
    print(f"::set-output name=Response::{response.text}")


if __name__ == "__main__":
    main()
