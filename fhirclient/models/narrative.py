#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Narrative) on 2016-02-24.
#  2016, SMART Health IT.


import element

class Narrative(element.Element):
    """ A human-readable formatted text, including images.
    """
    
    resource_name = "Narrative"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.div = None
        """ Limited xhtml content.
        Type `str`. """
        
        self.status = None
        """ generated | extensions | additional | empty.
        Type `str`. """
        
        super(Narrative, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Narrative, self).elementProperties()
        js.extend([
            ("div", "div", str, False),
            ("status", "status", str, False),
        ])
        return js


