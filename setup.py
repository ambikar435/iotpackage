from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'CIENTRA IOT'
LONG_DESCRIPTION = 'A package that allows to do multiple functions to send data to to 5g network through the gateway .'

# Setting up
setup(
    name="iotpkg",
    version=VERSION,
    author="Ambika",
    author_email="<ambikar435@gmail.com.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['opencv-python', 'pyautogui', 'pyaudio', 'pillow', 'tkinter','configparser','sqlite3','threading','websocket','websockets','datetime','sounddevice','socket','string','time','json','datetime'],
    keywords=['python', 'payload','websockets', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Ubuntu"
    ]
)
