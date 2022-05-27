#!env python3
import json
import logging
import os
import sys

import requests


def update(hostname):
    """Updates Linode DNS for the given hostname argiment with the client's address. Expects that the A record you're updating
    is in a hosted domain, e.g. to update foo.bar.example.com, you most be hosting bar.example.com.
    Use LINODE_API_KEY env var to supply your key.
    """
    key = os.getenv("LINODE_API_KEY")
    assert key, "You need to set the LINODE_API_KEY environment variable for this to work..."

    url = "https://api.linode.com/v4/domains"
    headers = {"Authorization": "Bearer " + key, "Content-Type": "application/json"}
    host, domain = hostname.split(".", 1)

    domains = requests.get(url, headers=headers).json()["data"]
    domain_id = [x["id"] for x in domains if x["domain"] == domain][0]

    records = requests.get(url + f"/{domain_id}/records", headers=headers).json()["data"]
    record_id = [x["id"] for x in records if x["name"] == host][0]

    data = {"target": "[remote_addr]"}
    res = requests.put(url + f"/{domain_id}/records/{record_id}", headers=headers, data=json.dumps(data))
    res.raise_for_status()

    logging.debug(f"Response from linode: {res.json()}")


if "__main__" in __name__:
    update(sys.argv[1])
