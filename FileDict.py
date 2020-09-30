import os

class FileDict(dict):
  """
  File based dict sub-class
  filepath [str]: path to the core file of the dict
  """
  def __init__(self,filepath,**kwargs):
      """Constructor method"""
      self.filepath = filepath
      if os.path.exists(f"{self.filepath}.txt"):
          self.a = open(f'{self.filepath}.txt', 'r+')
      else: 
          self.a = open(f'{self.filepath}.txt', 'w+')
      self.b = self.a.read()
      self.c = self.b.split()
      self.d = []
      for i in self.c:
          self.d.append(list(i.split(":")))
      self.dicio = dict(self.d)
      self.a.close()
      
        
  def __setitem__(self, key, value):
      """Creates a new item in the dict"""
      self.a = open(f'{self.filepath}.txt', 'r+')
      self.dicio[f"{key}"] = value
      conteudo = self.a.readlines()
      conteudo.append(f"{key}:{value}\n")
      self.a = open(f'{self.filepath}.txt', 'w+')
      self.a.writelines(conteudo)
      self.a.close()
      
  def pop(self,key):
      """Removes an item by the key"""
      self.a = open(f'{self.filepath}.txt', 'r+')
      content = self.a.readlines()
      value = self.dicio.get(f'{key}')
      self.dicio.pop(f"{key}")
      content.remove(f"{key}:{value}\n")
      self.a = open(f'{self.filepath}.txt', 'w+')
      self.a.writelines(content)
      self.a.close()
     

  def __del__(self):
      """Delete the dict and the file"""
      os.remove(f'{self.filepath}.txt')
      del self.dicio

