#need add environment: export PATH=$PATH:/home/user/python_http
SHELL_FOLDER=$(dirname $(readlink -f "$0"))
cd $SHELL_FOLDER
python ReleasesApp.py
