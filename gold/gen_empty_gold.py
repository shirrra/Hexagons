'''Generate Empty Gold

This script creates an initial .py file for parsing a drawing procedure.
The file will contain the drawing procedure instructions,
and everything else needed for running the file as a script.
The user can fill in the necessary code under the instructions.
When calling the .py file, it will plot the gold image,
and the image generated by the code added by the user.
It will also plot the difference between the two images.
'''

import os.path
import sys
sys.path.append('../src')
sys.path.append('../utils')

from reading_tasks import read_task

def main():

  # read the task from jsonl files
  task_index = int(input("Please provide the task index: "))
  task_dict = read_task(task_index)

  # use template to create file
  with open('../gold/template.txt', 'r') as file:
    template = file.read().split('\n')

  # create new file and write to it
  file_name = f'gold_{task_index:0>3}'
  file_path = '../gold/' + file_name + '.py'
  if os.path.exists(file_path):
    print(f'file {file_name} already exists')
  else:
    print(f'creating file {file_name}')
    with open(file_path, 'w+') as file_id:
      file_id.write('\n'.join(template[:7]))
      file_id.write(f'\ntask_index = {task_index}\n')
      file_id.write('\n'.join(template[8:13]))
      file_id.write(f"\n{task_dict['description']}\n\n")
      file_id.write(task_dict['instructions'])
      file_id.write('\n'.join(template[16:]))

if __name__ == "__main__":
  main()