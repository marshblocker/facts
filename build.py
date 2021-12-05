# NOTE: Before running this program in the Command Prompt, make sure that
#       the Command Prompt is 'Run as Administrator'.

from os import system, path
from src import main


def setup(): # Sets the PYTHONSTARTUP to the absolute path of /src/main.py.
	main_path = path.realpath(main.__file__)
	
	fail = system(f'setx PYTHONSTARTUP "{main_path}" /M >nul 2>&1')

	if fail:
		print(f'Failed to set PYTHONSTARTUP to {main_path}')
	else:
		print(f'Successfully set PYTHONSTARTUP to {main_path}')


if __name__ == '__main__':
	setup()

