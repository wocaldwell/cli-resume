import json, sys, webbrowser
from pprint import pprint
from time import sleep

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
        greeting = "Hi, I'm {}. What's your name?".format(name)
        Resume.simulateTyping(self, greeting)
        user_name = input()
        response_to_user = "It's nice to meet you, {}!".format(user_name)
        Resume.simulateTyping(self, response_to_user)
        return user_name

    def simulateTyping(self, phrase):
        '''
        Make cli message appear character by charater as if they where being typed.

        Arguments:
            phrase(string), the message that will be rendered in the command line.
        '''
        for character in phrase:
            sleep(0.075)
            sys.stdout.write(character)
            sys.stdout.flush()
        print("\n")

    def hal9000Response(self, userName):
        '''
        Print classic response from 2001: A Space Odyssey. Used when supplied input is not valid.
        '''
        hal_9000_message = "I'm sorry {}, I'm afraid I can't do that.".format(userName)
        Resume.simulateTyping(self, hal_9000_message)

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
                # launch website
                webbrowser.open_new("https://www.williamocaldwell.com/")
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
            if userSelection == '3':
                resume_volunteer = resume_data.get("volunteer")
                volunteer_message = "I have recently done volunteer work for the following organizations:"
                Resume.simulateTyping(self, volunteer_message)
                for organization in resume_volunteer:
                    print(organization)
            if userSelection == '4':
                resume_education = resume_data.get("education")
                education_message = "Here's my education history."
                Resume.simulateTyping(self, education_message)
                for school in resume_education:
                    institution = school["institution"]
                    area = school["area"]
                    completion = school["studyType"]
                    school_message = "I attended {} where I studied {}.".format(institution, area)
                    degree_message = "I earned a {}.".format(completion)
                    print(school_message)
                    if completion != "N/A":
                        print(degree_message)
            if userSelection == '5':
                resume_awards = resume_data.get("awards")
                award_message = "Here are some of my recent awards."
                Resume.simulateTyping(self, award_message)
                for award in resume_awards:
                    print(award)
            if userSelection == '7':
                resume_skills = resume_data.get("skills")
                for skill in resume_skills:
                    skill_name = skill["name"]
                    skill_level = skill["level"]
                    skill_list = skill["keywords"]
                    skills_message = "The following are my {} skills.\n I am at the {} level in this skillset.\n Highlights of my {} assets are:".format(skill_name, skill_level, skill_name)
                    Resume.simulateTyping(self, skills_message)
                    for skill in skill_list:
                        print(skill)


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
        catagories_message = "Here's a list of my resume catagories."
        Resume.simulateTyping(self, catagories_message)
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
            selection_message = "Pick a number from the list to see specific details."
            Resume.simulateTyping(self, selection_message)
            user_selection = input("Type 'e' to exit.\n")
            if user_selection not in Resume.catagory_numbers:
                if user_selection == "e":
                    exit_message = "It was nice chatting with you today, {}!\n".format(userName)
                    Resume.simulateTyping(self, exit_message)
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