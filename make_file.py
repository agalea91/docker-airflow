import os
import datetime

if __name__ == '__main__':
    name = 'test_{}.file'.format(datetime.datetime.now())
    name = os.path.join(os.getenv('PROJECT_HOME', '/'), name)
    print('writing test file {}'.format(name))
    with open(name, 'w') as f:
        f.write('Test file')
