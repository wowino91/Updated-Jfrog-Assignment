#!usr/bin/env pyhton3

import json
import requests 
from requests.structures import CaseInsensitiveDict


# TODO set token, username, and hearders as environment variables 
username = "favor"
BASE_URL = "https://favored1.jfrog.io"



artifactory_url = "https://favored1.jfrog.io/artifactory/api/"

headers = CaseInsensitiveDict()
#headers["X-JFrog-Art-Api"] = "AKCp8mZcenx5cU5mM1K5FphUHgutAN7wdfSdTUeQyBLU3eqUYJek3b3VNvzJu1xbkAiuifmms"


class repository:
    def create():
        url = artifactory_url + 'repositories/libs-release-local'
        resp = requests.put(url, headers=headers)
        print(resp.status_code)
        
    def update():
        print("will update repo")
        pass
    
# shows all the repositories in instance
    def show():
        url = artifactory_url + 'repositories'
        resp = requests.get(url, headers=headers) 
        pretty_text = resp.json()
        for repo in pretty_text:
            print(repo['key'])
            
class system:
    def ping():
        url = artifactory_url + 'system/ping'
        resp = requests.get(url, headers=headers)
        return (resp.status_code)
    
    def version():
        url = artifactory_url + 'system/version'         
        resp = requests.get(url, headers=headers) 
        pretty_text = resp.json()
        
        return pretty_text['version']
    
    def storageinfo():
        url = artifactory_url + 'storageinfo'
        resp = requests.get(url, headers=headers) 
        pretty_text = resp.json()
        
        return pretty_text

def main():
    
        #welcome()
        
        def welcome():
            print("Welcome to python artifactory manager")
            print("======================================")
            print('')
    
   
        #menu()
        
        def menu():
            print("menu")
            print("====")
            print("1. to ping the system type: ping")
            print("2. to get the system version type: version")
            print("3. to get storage infomation type: storageinfo ")
            print("4. to show the repositories type: rshow")
        
        user_input = ''
        while user_input != '\q':
            user_input = input('[admin user] #:  ')
            if user_input == "ping":           
                print(system.ping())
            elif user_input == "version":       
                print(system.version())
            elif user_input == 'storageinfo':
                print(storageinfo())
            elif user_input == "rshow":            
                repositories.show()
        
            elif user_input == "\q":
                pass
        else:
            print('Input invalid')
    
main()
