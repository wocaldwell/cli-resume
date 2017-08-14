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
        user_name = input("Hi, I'm {}. What's your name?\n".format(name))
        print("It's nice to meet you, {}".format(user_name))
        return user_name

    def hal9000Response(self, userName):
        '''
        Print classic response from 2001: A Space Odyssey. Used when supplied input is not valid.
        '''
        print("I'm sorry {}, I'm afraid I can't do that.".format(userName))

    def displayCatagoryInformation(self, userSelection, userName):
        '''
        Display information from the resume json based on input from user.

        Arguments:
            userSelection(string), a 'number' that corresponds to a section of the resume.
        '''
        resume_data = Resume.getJsonData(self, "resume.json")
        resume_basics = resume_data.get("basics")
        while True:
            if userSelection == '1':
                print("Here's my basic information:")
                print("I'm a {} in {}, {}.".format(resume_basics["label"], resume_basics["location"]["city"], resume_basics["location"]["region"]))
                print(resume_basics["summary"])
                for profile in resume_basics["profiles"]:
                    print("I'm on {}, my username is {}. Go to {} to check it out!".format(profile['network'], profile['username'], profile['url']))
            if userSelection == '2':
                resume_work = resume_data.get("work")
                print("This is my work history:")
                for job in resume_work:
                    print(job["company"])
                    print(job["position"])
                    print(job["summary"])
                    if job["highlights"]:
                        for highlight in job["highlights"]:
                            print(highlight)
                            if len(job["highlights"]) > 1:
                                input("Press enter to continue reading.")
                    input("Press enter to see my next position.")

            userSelection = Resume.validateUserSelection(self, userName)






    # List that will store valid catagory selections from listResumeCatagories()
    catagory_numbers = []

    # List that will store catagory objects
    catagories = []

    def listResumeCatagories(self):
        '''
        Display the resume catagories and add them to the catagories lists.
        '''
        resume_data = Resume.getJsonData(self, "resume.json")
        catagory_names = list(resume_data.keys())
        print("Here's a list of my resume catagories.")
        for count, catagory in enumerate(catagory_names, 1):
            Resume.catagory_numbers.append(str(count))
            Resume.catagories.append({str(count): resume_data.get(catagory)})
            print(count, catagory)

    def validateUserSelection(self, userName):
        '''
        Ask for user input and repromt until user supplies a valid answer.

        Arguments:
            userName(string), the name input supplied by the cli user.

        Returns:
            The input from the cli user in response to asking then to pick a number from the catagories list.
        '''
        while True:
            user_selection = input("Pick a number from the list and I'll tell you a little bit more about myself.\nType 'e' to exit.\n")
            if user_selection not in Resume.catagory_numbers:
                if user_selection == "e":
                    print("It was nice chatting with you today, {}!\n".format(userName))
                    sys.exit()
                else:
                    Resume.hal9000Response(self, userName)
                    continue
            else:
                break
        return user_selection



if __name__ == '__main__':
    my_resume = Resume()
    cli_user = my_resume.introduction()
    my_resume.listResumeCatagories()
    user_selection = my_resume.validateUserSelection(cli_user)
    my_resume.displayCatagoryInformation(user_selection, cli_user)