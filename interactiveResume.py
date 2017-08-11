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

    def hal9000Response(self, userName):
        '''
        Print classic response from 2001: A Space Odyssey. Used when supplied input is not valid.
        '''
        print("{} {}{}".format("I'm sorry", userName, ", I'm afraid I can't do that."))

    def displayCatagoryInformation():
        '''
        '''
        pass

    # List that will store valid catagory selections from listResumeCatagories()
    catagory_numbers = []

    def listResumeCatagories(self):
        '''
        Display the resume catagories.

        Arguments:
            userName(string), the name input supplied by the cli user.

        Returns:
            The input from the cli user in response to asking then to pick a number from the catagories list.
        '''
        resume_data = Resume.getJsonData(self, "resume.json")
        catagory_names = list(resume_data.keys())
        print("Here's a list of my resume catagories.")
        for count, catagory in enumerate(catagory_names, 1):
            Resume.catagory_numbers.append(str(count))
            print(count, catagory)
        user_selection = input("Pick a number and I'll tell you a little bit more about myself.\nType 'e' to exit.\n")
        return user_selection

    def validateUserSelection(self, userSelection, userName):
        '''

        '''
        print('------------------\n', Resume.catagory_numbers)
        while True:
            user_selection = userSelection
            if user_selection not in Resume.catagory_numbers:
                Resume.hal9000Response(self, userName)
                user_selection = input("Please pick a number from the list.\n")
                continue
            elif user_selection == "e":
                print("{} {}{}".format("It was nice chatting with you today,", userName, "!\n"))
                sys.exit()
            else:
                print(user_selection, "is a valid number.")
                break
        return user_selection



if __name__ == '__main__':
    my_resume = Resume()
    cli_user = my_resume.introduction()
    catagory_selection = my_resume.listResumeCatagories()
    my_resume.validateUserSelection(catagory_selection, cli_user)