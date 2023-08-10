import os
file=open("credentials.txt","r")
os.environ['FINSAGE_PASS'] = file.read() 