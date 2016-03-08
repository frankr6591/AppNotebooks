## AppNotebooks

This is a simple repository for creating notebooks that explain how to use your app. 

The original intent is to collaborate development of app plugins.    The idea is to develop plugin's within notebooks, test them and once stable - move them into your app library. 

### Structure

$HOME/opt/AppNotebooks  - contains notebooks about myapp
/opt/myapp/site         - contains app (ie. git clone here)
/opt/myapp/store        - contains storage for all data

### Dummy myapp

A dummy app is contained in this github.   One should copy to /opt.

    > mkdir -p $HOME/opt
    > cd $HOME/opt
    > git clone https://github.com/frankr6591/AppNotebooks.git
    > cd AppNotebooks
    > sudo (cd opt ; tar cf - myapp | (cd /opt ; tar -xf - ))

###  jupyterhub

The app notebooks depend on jupyterhub being installed into your environment.   
Refer to information on jupytherhub configuration. 