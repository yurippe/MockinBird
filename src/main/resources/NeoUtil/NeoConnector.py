# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 09:58:18 2017

@author: Kristian Gausel
"""
import base64
import sys

try:
    import requests
except ImportError:
    pass

def generate_auth_header(username, password):
    """Create a basic authentication header value"""
    return "Basic " + base64.b64encode(username + ":" + password)

def chunks(lst, chunk_size):
    """Yield successive n-sized chunks from lst."""
    #Specifics for python 2 vs python 3
    if sys.version_info[0] == 2:
        range = xrange
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]

def get_connector(settings, connector="NeoRestConnector"):
    """Gets a Connector instance which connects using values found in settings.
    The connector type is defined in the argument connector
    Current legal values:
        * NeoRestConnector
    """
    if connector.lower() == "neorestconnector":
        return NeoRestConnector(settings)
    else:
        raise ValueError("No such connector exists")


class Connector(object):
    """Connector Interface"""

    def __init__(self, settings):
        self.settings = settings

    def query(self, query):
        """Query the database for something
        The query argument type is implementation specific
        The return type is implementation specific
        """
        raise NotImplementedError

    def bulk_update(self, queries):
        """Perfoms many queries / updates on the database
        The queries argument type is implementation specific
        The return type is implementation specific
        """
        raise NotImplementedError
