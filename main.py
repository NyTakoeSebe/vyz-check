import codecs
import json
from colorama import init, Fore, Style

def read_file(filepath):
  with codecs.open(filepath, encoding='utf-8') as fin:
      return fin.readlines()

def read_config(filepath):
  with open(filepath, 'r') as f:
    cfg = json.load(f)
    faculties = cfg['faculties']
    w_t = cfg['with_tables']
  return [faculties, w_t]

faculties = read_config('config.json')[0]
with_tables = bool(read_config('config.json')[1])

def print_table(file):
   for i in file:
      print(i)

def get_all_amount_of_students(file):
  return len(file)

def get_all_amount_of_students_with_first_priority(arr):
  res = 0
  for student in arr:
    if int(student[1]) == 1:
      res +=1
  return res

def get_all_amount_of_students_with_second_priority(arr):
  res = 0
  for student in arr:
    if int(student[1]) == 2:
      res +=1
  return res

def get_all_amount_of_students_with_third_priority(arr):
  res = 0
  for student in arr:
    if int(student[1]) == 3:
      res +=1
  return res

def generate_my_data(file):
  res = []
  for i in range(len(file)):
    temp = file[i].replace('\n', '').replace('\r', '').replace('\t', ' ').split(' ')
    res.append([temp[2], temp[12]])
  return res

def get_only_first_priority(arr):
  res = []
  for i in range(len(arr)):
    item = arr[i]
    if (int(item[1]) == 1):
      res.append(item)
  return res

def get_first_and_second_priority(arr):
  res = []
  for i in range(len(arr)):
    item = arr[i]
    if (int(item[1]) == 1 or int(item[1]) == 2):
      res.append(item)
  return res

def get_first_and_second_and_third_priority(arr):
  res = []
  for i in range(len(arr)):
    item = arr[i]
    if (int(item[1]) == 1 or int(item[1]) == 2 or int(item[1]) == 3):
      res.append(item)
  return res

def print_data(filepath, amount):
  source_file = read_file(filepath)
  if with_tables:
    print("\nФайл, который вы загрузили:\n")
    print_table(source_file)

  data = generate_my_data(source_file)
  only_first = get_only_first_priority(data)
  first_and_second = get_first_and_second_priority(data)
  first_and_second_and_third = get_first_and_second_and_third_priority(data)
  all_students = get_all_amount_of_students(source_file)
  all_students_with_first_priority = str(get_all_amount_of_students_with_first_priority(data))
  all_students_with_second_priority = str(get_all_amount_of_students_with_second_priority(data))
  all_students_with_third_priority = str(get_all_amount_of_students_with_third_priority(data))

  print("\nВаше место среди всех студентов перед вами: " + str(all_students + 1) + "\n")
  print("Ваше место среди всех студентов перед вами c 1 приоритетом: " + str(len(only_first) + 1) + "\n")
  print("Ваше место среди всех студентов перед вами c 1 и 2 приоритетом: " + str(len(first_and_second) + 1) + "\n")
  print("Ваше место среди всех студентов перед вами c 1 и 2 и 3 приоритетом: " + str(len(first_and_second_and_third) + 1) + "\n")
  print("Всего студентов с 1 приоритетом: " + all_students_with_first_priority + " со 2 приоритетом: " + all_students_with_second_priority + " с третим приоритетом: " + all_students_with_third_priority)

  init(autoreset=True)

  if len(only_first) <= amount:
    print(Fore.GREEN + "\nВы проходите на бюджет среди  студентов с 1 приоритетом")
  else:
    print(Fore.RED + "\nВозможно вы не проходите на бюджет среди  студентов с 1 приоритетом")
  if len(first_and_second) <= amount:
    print(Fore.GREEN + "Вы проходите на бюджет среди  студентов с 1 и 2 приоритетом")
  else:
    print(Fore.RED + "Возможно вы не проходите на бюджет среди  студентов с 1 и 2 приоритетом")
  if len(first_and_second_and_third) <= amount:
    print(Fore.GREEN + "Вы проходите на бюджет среди  студентов с 1 и 2 и 3 приоритетом\n\n")
  else:
    print(Fore.RED + "Возможно вы не проходите на бюджет среди  студентов с 1 и 2 и 3 приоритетом\n\n")

for name, amount in faculties.items():
  filepath = name + '.txt'
  print("\n" + Style.BRIGHT + "Название напрвления: " + name + "\n")
  print(Style.RESET_ALL)
  print_data(filepath, int(amount))