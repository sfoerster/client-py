#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Coding) on 2016-02-24.
#  2016, SMART Health IT.


import element

class Coding(element.Element):
    """ A reference to a code defined by a terminology system.
    """
    
    resource_name = "Coding"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Symbol in syntax defined by the system.
        Type `str`. """
        
        self.display = None
        """ Representation defined by the system.
        Type `str`. """
        
        self.system = None
        """ Identity of the terminology system.
        Type `str`. """
        
        self.userSelected = None
        """ If this coding was chosen directly by the user.
        Type `bool`. """
        
        self.version = None
        """ Version of the system - if relevant.
        Type `str`. """
        
        super(Coding, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Coding, self).elementProperties()
        js.extend([
            ("code", "code", str, False),
            ("display", "display", str, False),
            ("system", "system", str, False),
            ("userSelected", "userSelected", bool, False),
            ("version", "version", str, False),
        ])
        return js


