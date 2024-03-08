from pathlib import Path

path = Path('./aaa/aa.txt')
path = Path('./Ch10/aa.txt')

with open(path, 'w') as file:
    file.write('aaa\n')
    file.write('aa\n')
    file.write('I love programming.')
    
try:
    if path.exist():
        with open(path) as file:    
            for line in file:
                print(line)

except Exception as e :
    print(e)
    pass
