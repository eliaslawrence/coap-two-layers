#!/usr/bin/env python

from coapthon.resources.resource import Resource
from coapthon.server.coap import CoAP
import sys

# Temperature Threshold resource
class Threshold_T(Resource):
  def __init__(self,name="Threshold",coap_server=None):
    super(Threshold_T,self).__init__(name,coap_server,visible=True,observable=True,allow_children=True)
    self.payload = ""
    self.resource_type = "rt1"
    self.content_type = "application/json"
    self.interface_type = "if1"

  def set_server(self, server):
    self.server = server

  # Return payload
  def render_GET(self,request):    
    return self

  # Set payload
  def render_POST(self, request):
    self.server.t_lim = float(request.payload)
    res = self.init_resource(request, Threshold_T())
    return res

# Pressure Threshold resource
class Threshold_P(Resource):
  def __init__(self,name="Threshold",coap_server=None):
    super(Threshold_P,self).__init__(name,coap_server,visible=True,observable=True,allow_children=True)
    self.payload = ""
    self.resource_type = "rt1"
    self.content_type = "application/json"
    self.interface_type = "if1"

  def set_server(self, server):
    self.server = server

  # Return payload
  def render_GET(self,request):    
    return self

  # Set payload
  def render_POST(self, request):
    self.server.p_lim = float(request.payload)
    res = self.init_resource(request, Threshold_P())
    return res