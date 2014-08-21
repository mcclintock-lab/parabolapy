import sys, os
import jsonlib


_input = '';
_output = {};

def getInputArgumentNames():
  this_input = _getInputJson()
  return(this_input.keys())

def getInputArgumentAsObject(name):
  this_input = _getInputJson()
  return(this_input[name])

def getInputArgumentAsGeoJson(name):
  this_input = _getInputJson()
  return(jsonlib.write(this_input[name]))

def getInputAsObject():
  return(_getInputJson())

def getInputAsGeoJson():
  return(jsonlib.write(getInputAsObject()));

def setOutputByName(name, geojson): 
  global _output;
  _output[name] = jsonlib.read(geojson);

def sendOutput():
  global _output;
  outfile = os.fdopen(3, 'w');
  outfile.write(jsonlib.write(_output));
  outfile.close();

def _getInputJson():
  global _input
  if len(_input) > 0:
    return(_input)
  this_input = sys.stdin.read()
  _input = jsonlib.read(this_input)
  return(_input)

