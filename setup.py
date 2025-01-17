from setuptools import setup

setup(
    name='tictactoe',
    author='Joan A. Pinol  (japinol)',
    version='0.0.5',
    license='MIT',
    description="Tic Tac Toe",
    long_description="Tic Tac Toe",
    url='https://github.com/japinol7/tictactoe',
    packages=['tictactoe'],
    python_requires='>=3.13',
    install_requires=['pygame-ce'],
    entry_points={
        'console_scripts': [
            'tictactoe=tictactoe.__main__:main',
            ],
    },
)
