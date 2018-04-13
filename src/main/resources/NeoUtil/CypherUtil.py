# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 16:58:18 2017

@author: Kristian Gausel
"""
#https://github.com/bruth/cypher
from cypher import Node, Collection, PropertyList, Map

def CCollection(col, identifier=None):
    """Returns a cypher statement representing a collection"""
    return str(Collection(col, identifier))
    
def CMap(col, identifier=None):
    """Returns a cypher statement representing a map"""
    return str(Map(col, identifier))

def CNode(properties=None, labels=None, identifier=None):
    """Returns a cypher statement representing a node"""
    if isinstance(labels, str):
        labels = [labels]
    return str(Node(props=properties, labels=labels, identifier=identifier))

def CProps(properties=None, identifier=None):
    """Returns a cypher statement representing a property list"""
    return str(PropertyList(props=properties, identifier=identifier))

class CypherBuilder(object):
    """Cypher query builder"""

    def __init__(self):
        self.result = []
        self.auto_include_spaces = True

    def _addSpace(self, inclspace=None):
        if not self.result: return
        if inclspace or (inclspace is None and self.auto_include_spaces):
            self.result.append(" ")

    def add(self, string, inclspace=None):
        if string is None: return self
        self._addSpace(inclspace)
        self.result.append(string)
        return self

    def Node(self, properties=None, labels=None, identifier=None, inclspace=None):
        self._addSpace(inclspace)
        self.result.append(CNode(properties, labels, identifier))
        return self

    def Collection(self, collection, identifier=None, inclspace=None):
        self._addSpace(inclspace)
        if isinstance(collection, list):
            self.result.append(CCollection(collection, identifier))
        elif isinstance(collection, dict):
            self.result.append(CMap(collection, identifier))
        else:
            raise NotImplementedError("Unrecognized collection type")
        return self

    def PropertyList(self, properties=None, identifier=None, inclspace=None):
        self._addSpace(inclspace)
        self.result.append(CProps(properties, identifier))
        return self

    def AS(self, extra=None, inclspace=None):
        self._addSpace(inclspace)
        self.result.append("AS")
        self.add(extra)
        return self

    def MATCH(self, extra=None, inclspace=None):
        self._addSpace(inclspace)
        self.result.append("MATCH")
        self.add(extra)
        return self

    def CREATE(self, extra=None, inclspace=None):
        self._addSpace(inclspace)
        self.result.append("CREATE")
        self.add(extra)
        return self

    def MERGE(self, extra=None, inclspace=None):
        self._addSpace(inclspace)
        self.result.append("MERGE")
        self.add(extra)
        return self

    def RETURN(self, extra=None, inclspace=None):
        self._addSpace(inclspace)
        self.result.append("RETURN")
        self.add(extra)
        return self

    def UNWIND(self, extra=None, inclspace=None):
        self._addSpace(inclspace)
        self.result.append("UNWIND")
        self.add(extra)
        return self

    def WITH(self, extra=None, inclspace=None):
        self._addSpace(inclspace)
        self.result.append("WITH")
        self.add(extra)
        return self

    def SET(self, extra=None, inclspace=None):
        self._addSpace(inclspace)
        self.result.append("SET")
        self.add(extra)
        return self

    def DELETE(self, extra=None, inclspace=None):
        self._addSpace(inclspace)
        self.result.append("DELETE")
        self.add(extra)
        return self
        
    def AND(self, extra=None, inclspace=None):
        self._addSpace(inclspace)
        self.result.append("AND")
        self.add(extra)
        return self
        
    def OR(self, extra=None, inclspace=None):
        self._addSpace(inclspace)
        self.result.append("OR")
        self.add(extra)
        return self

    def build(self):
        return "".join(self.result)
