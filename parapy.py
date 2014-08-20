import sys
import jsonlib


_input = ''


def getInputArgumentNames():
  this_input = _getInputJson()
  return(this_input.keys())

def getInputArgumentByName(name):
  this_input = _getInputJson()
  return(this_input[name])

def getRawInput():
  return(_getInputJson())

def setOutput(code, message, output): 
  print("setOUtput")

def _getInputJson():
  global _input
  if len(_input) > 0:
    return(_input)
  this_input = sys.stdin.read()
  _input = jsonlib.read(this_input)
  return(_input)




