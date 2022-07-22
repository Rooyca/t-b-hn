import os, requests

def main():
    try:
        url = os.environ["INPUT_URL"]
    except KeyError:
        print("::set-output name=Response::No URL provided")
        return

    try:
        user = os.environ["INPUT_USER"]
        passw = os.environ["INPUT_PASSW"]
    except KeyError:
        user, passw = None, None

    method = os.environ["INPUT_METHOD"]

    def response(res):
        print(f"::set-output name=Status::{res.status_code}")
        print(f"::set-output name=Response::{res.text}")

    if method == "POST":
        res_post = requests.post(url, auth=(user, passw))
        response(res_post)
    elif method == "PUT":
        resp_put = requests.put(url, auth=(user, passw))
        response(resp_put)
    elif method == "DELETE":
        resp_del = requests.delete(url, auth=(user, passw))
        response(resp_del)
    else:
        resp_get = requests.get(url, auth=(user, passw))
        response(resp_get)

if __name__ == "__main__":
    main()