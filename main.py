import random

class Encryptor(object):
  def __init__(self):
    self.key = []
    self.username = []
    self.password = []
    
  def __generate_key(self, i) -> None:
    self.key.append([*range(256)])
    possible_values = [*range(256)]
    
    for j, character in enumerate(self.key[i]):
      new_value = possible_values[random.randint(0, len(possible_values) - 1)]
      possible_values.remove(new_value)
      self.key[i][j] = new_value
      
  def __generate_pass(self, password:str) -> None:
    current_key = self.key[len(self.key) - 1]
    password_list = []
    
    for character in password:
      character = ord(character)
      password_list.append(current_key[character])
    self.password.append(password_list)
    
  def __convert(self, password:str, key:list) -> list:
    converted_pass = []
    for character in password:
      character = ord(character)
      converted_pass.append(key[character])
    return converted_pass
    
      
  def add_account(self, username:str, password:str) -> None:
    self.__generate_key(len(self.key))
    self.username.append(username)
    self.__generate_pass(password)
    
  def validate(self, username:str, password:str) -> bool:
    try:
      index = self.username.index(username)
    except ValueError:
      return False
      
    actual_pass = self.password[index]
    password = self.__convert(password, self.key[index])
    
    if password == actual_pass:
      return True
    else:
     return False
      
encrypt = Encryptor()

encrypt.add_account("Pirategirl9000", "violet_syntax74#")
encrypt.add_account("TheRealBryanCorkle", "qwerty")

username = "Pirategirl9000"
password = "violet_syntax74#"
valid = encrypt.validate(username, password)
print(valid)

username = "TheRealBryanCorkle"
password = "qwerty"
valid = encrypt.validate(username, password)
print(valid)
