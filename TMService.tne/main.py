import subprocess

def supply(inputVal):
    if len(inputVal) > 1: raise ValueError('Too many arguments')
    functions = [
            {
                'name': 'Start Backup',
                'content': 'Run Time Machine backup with system preference',
                'innerItem': 'tmutil startbackup -a'
            },
            {
                'name': 'Stop Backup',
                'content': 'Interrupt and stop the running Time Machine backup',
                'innerItem': 'tmutil stopbackup'
            }
            ]
    if len(inputVal[0]) == 0:
        return functions

def serve(inputVal):
    innerCMD = inputVal['innerItem']
    subprocess.check_call(innerCMD, shell=True)
