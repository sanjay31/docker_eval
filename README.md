# docker_eval
Grab data from API  using Python
This docker containerization is intended for a python application which grabs data from MacAdress vendor lookup url (https://macaddress.io).

This python application takes two input paramaters from the command line:
One is ApiKey of the MaCadress lookup url (https://macaddress.io) and the second parameter is any device macAddress in 
right macaddress format, which is six groups of two hexadecimal digits separated by hyphens or colons.

To obtain ApiKey any individual who will be testing this containerized application has to sign up that above mentioned url and get his/her ApiKey.

In Unix machine or any VM to run this docker container, one has to install docker engine with proper command line install commands.

Here is this repository, Dockerfile is created and the python application file (mac_addr_lookup.py) has been added.

After installing docker in the unix machine, one has to create docker image from the Dockerfile and run docker container.

