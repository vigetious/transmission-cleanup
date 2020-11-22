import sys
import requests
import base64
import json
import os
import shutil

def runCommand(payload):
    sessionId = "123"
    url = "http://" + sys.argv[1] + "/transmission/rpc"

    usernamePass = sys.argv[3] + ":" + sys.argv[4]
    authorization = base64.b64encode(usernamePass.encode('ascii'))

    while True:
        response = requests.post(url, json=payload, headers={"X-Transmission-Session-Id": sessionId, "Authorization": "Basic " + authorization.decode('ascii')})

        if response.status_code == 409:
            sessionId = response.headers["X-Transmission-Session-Id"]
            continue
        if response.status_code != 200:
            print("Could not communicate with the server. Please check your IP, username or password.")
        break

    return response

def main():
    torrentArary = json.loads(runCommand({
        "arguments": {
            "fields": ["name"]
        },
        "method": "torrent-get",
    }).text)
    print("Recieved torrent list...")

    files = []
    for i in torrentArary["arguments"]["torrents"]:
        files.append(i["name"])

    filesToBeRemoved = list(
        set(os.listdir(sys.argv[2])) - set(files))

    for i in filesToBeRemoved:
        print("Removing " + i)
        if os.path.isfile(sys.argv[2] + i):
            os.remove(sys.argv[2] + i)
        if os.path.isdir(sys.argv[2] + i):
            shutil.rmtree(sys.argv[2] + i)
    print("Done.")


if __name__ == '__main__':
    main()


