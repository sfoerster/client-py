#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Attachment) on 2016-02-24.
#  2016, SMART Health IT.


import element

class Attachment(element.Element):
    """ Content in a format defined elsewhere.
    
    For referring to data content defined in other formats.
    """
    
    resource_name = "Attachment"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.contentType = None
        """ Mime type of the content, with charset etc..
        Type `str`. """
        
        self.creation = None
        """ Date attachment was first created.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.data = None
        """ Data inline, base64ed.
        Type `str`. """
        
        self.hash = None
        """ Hash of the data (sha-1, base64ed).
        Type `str`. """
        
        self.language = None
        """ Human language of the content (BCP-47).
        Type `str`. """
        
        self.size = None
        """ Number of bytes of content (if url provided).
        Type `int`. """
        
        self.title = None
        """ Label to display in place of the data.
        Type `str`. """
        
        self.url = None
        """ Uri where the data can be found.
        Type `str`. """
        
        super(Attachment, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Attachment, self).elementProperties()
        js.extend([
            ("contentType", "contentType", str, False),
            ("creation", "creation", fhirdate.FHIRDate, False),
            ("data", "data", str, False),
            ("hash", "hash", str, False),
            ("language", "language", str, False),
            ("size", "size", int, False),
            ("title", "title", str, False),
            ("url", "url", str, False),
        ])
        return js


from . import fhirdate
