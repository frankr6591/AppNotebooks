'''
Config py_lib.app_config : link pynb environment to myapp
'''
import os, sys
APP_SITE = os.path.join('/opt/myapp/src')
APP_STORE = os.path.join('/opt/myapp/store')
os.environ['APP_SITE'] = APP_SITE
os.environ['APP_STORE'] = APP_STORE
# Link to APP_SITE
os.chdir(APP_SITE)
sys.path.append(APP_SITE)  
APP_UPLOAD = os.path.join(APP_STORE,'upload')