import json
import sys
from pprint import pprint

class Resume():
    '''
    Provide an interface for interacting with a resume json file.
    '''

    def getJsonData(self, jsonFile):
        '''
        Load the data from local json.

        Arguments:
            jsonFile, a persistent local json file.

        Returns:
            A dictionary object containing the data from jsonFile.
        '''
        with open(jsonFile) as data_file:
            data = json.load(data_file)

        # print(isinstance(data, dict))
        return data

    def introduction(self):
        '''
        Introduce the resume holder and get the name of the user that is interacting with the cli.

        Returns:
            A string that the user inputs into the cli.
        '''
        resume_data = Resume.getJsonData(self, "resume.json")
        resume_basics = resume_data.get("basics")
        name = resume_basics["name"]
        user_name = input("{} {}{}".format("Hi, I'm", name, ". What's your name?\n"))
        print("{} {}{}".format("It's nice to meet you,", user_name, ".\n"))
        return user_name

    def listResumeCatagories(self, userName):
        '''
        '''
        resume_data = Resume.getJsonData(self, "resume.json")
        catagory_names = list(resume_data.keys())
        catagory_numbers = []
        print("Here's a list of my resume catagories.")
        for count, catagory in enumerate(catagory_names, 1):
            catagory_numbers.append(str(count))
            print(count, catagory)
        user_selection = input("Pick a number and I'll tell you a little bit more about me.\nTo exit type 'e'.\n")
        if user_selection == "e":
            print("{} {}{}".format("It was nice chatting with you today,", userName, "!\n"))
            sys.exit()
        if user_selection in catagory_numbers:
            print(user_selection, "is a valid number.")
        else:
            print('not cool. . . ')


if __name__ == '__main__':
    my_resume = Resume()
    cli_user = my_resume.introduction()
    my_resume.listResumeCatagories(cli_user)