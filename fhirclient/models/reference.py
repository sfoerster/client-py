#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Reference) on 2016-02-24.
#  2016, SMART Health IT.


import element

class Reference(element.Element):
    """ A reference from one resource to another.
    """
    
    resource_name = "Reference"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.display = None
        """ Text alternative for the resource.
        Type `str`. """
        
        self.reference = None
        """ Relative, internal or absolute URL reference.
        Type `str`. """
        
        super(Reference, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Reference, self).elementProperties()
        js.extend([
            ("display", "display", str, False),
            ("reference", "reference", str, False),
        ])
        return js


