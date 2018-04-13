# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 16:58:18 2017

@author: Kristian Gausel
"""
import re
IP_REGEX = re.compile(r"^\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3}$")

def filter_dict(keys, dic):
    """Create a dict containing only the keys defined in keys from another dict"""
    return dict(filter(lambda (key, val): key in keys, dic.items()))

def is_ip_address(inp):
    return bool(IP_REGEX.match(inp))

class UniqueList(object):

    def __init__(self, *args, **kwargs):
        self.ulist = list(*args, **kwargs)
        self.uset = set(*args, **kwargs)
        self.list_append_lambda = None
        self.set_append_lambda = None

        self.skipped = 0

    def append(self, item):

        if self.set_append_lambda is None:
            if item in self.uset:
                self.skipped += 1
                return
        else:
            if self.set_append_lambda(item) in self.uset:
                self.skipped += 1
                return

        if self.set_append_lambda is None:
            self.uset.add(item)
        else:
            self.uset.add(self.set_append_lambda(item))

        if self.list_append_lambda is None:
            self.ulist.append(item)
        else:
            self.ulist.append(self.list_append_lambda(item))

    def clear_list(self, *args, **kwargs):
        """Clears the unique list, but keeps the set controlling appending
        This means that items added earlier can not be added again"""
        self.ulist = list(*args, **kwargs)

    def __iter__(self):
        for item in self.ulist:
            yield item

    def __contains__(self, item):
        return item in self.uset

    def __len__(self):
        return len(self.ulist)

    def __getitem__(self, k):
        return self.ulist[k]
