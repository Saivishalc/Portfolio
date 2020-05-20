from tkinter import *
global mainscreen, titleLabel, studentcaller, professorcaller, professorStateClick, professorGradeClick, professorSubjectEntry, professorEmailEntry, professorNameEntry, professorUniversityEntry, studentStateClick, studentGradeClick, studentSubjectEntry


def searchMenu():
    searchMenuScreen = Tk()
    searchMenuScreen.title("Research Programs")
    searchMenuScreen.configure(bg='medium spring green')

    if studentStateClick.get() == professorStateClick.get():
        if studentGradeClick.get() == professorGradeClick.get():
            if studentSubjectEntry.get() == professorSubjectEntry.get():
                header = Label(searchMenuScreen, text="Research Programs that best fit you: ")
                header.configure(bg='medium spring green', font='Courier')
                header.grid(row=0, column=0)
                professorStateDisplay = Label(searchMenuScreen, text=professorStateClick.get())
                professorStateDisplay.configure(bg='medium spring green')
                professorStateDisplay.grid()
                professorGradeDisplay = Label(searchMenuScreen, text=professorGradeClick.get())
                professorGradeDisplay.configure(bg='medium spring green')
                professorGradeDisplay.grid()
                professorSubjectDisplay = Label(searchMenuScreen, text=professorSubjectEntry.get())
                professorSubjectDisplay.configure(bg='medium spring green')
                professorSubjectDisplay.grid()
                professorNameDisplay = Label(searchMenuScreen, text=professorNameEntry.get())
                professorNameDisplay.configure(bg='medium spring green')
                professorNameDisplay.grid()
                professorUniversityDisplay = Label(searchMenuScreen, text=professorUniversityEntry.get())
                professorUniversityDisplay.configure(bg='medium spring green')
                professorUniversityDisplay.grid()
                professorEmailDisplay = Label(searchMenuScreen, text=professorEmailEntry.get())
                professorEmailDisplay.configure(bg='medium spring green')
                professorEmailDisplay.grid()

    if studentStateClick.get() != professorStateClick.get():
        if studentGradeClick.get() != professorGradeClick.get():
            if studentSubjectEntry.get() != professorSubjectEntry.get():
                header = Label(searchMenuScreen,
                               text="Sorry but there are currently no research openings that fits you")
                header.configure(bg='medium spring green', font='Courier')
                header.grid()
                professorStateDisplay = Label(searchMenuScreen, text=professorStateClick.get())
                professorStateDisplay.configure(bg='medium spring green')
                professorStateDisplay.grid()
                professorGradeDisplay = Label(searchMenuScreen, text=professorGradeClick.get())
                professorGradeDisplay.configure(bg='medium spring green')
                professorGradeDisplay.grid()
                professorSubjectDisplay = Label(searchMenuScreen, text=professorSubjectEntry.get())
                professorSubjectDisplay.configure(bg='medium spring green')
                professorSubjectDisplay.grid()
                professorNameDisplay = Label(searchMenuScreen, text=professorNameEntry.get())
                professorNameDisplay.configure(bg='medium spring green')
                professorNameDisplay.grid()
                professorUniversityDisplay = Label(searchMenuScreen, text=professorUniversityEntry.get())
                professorUniversityDisplay.configure(bg='medium spring green')
                professorUniversityDisplay.grid()
                professorEmailDisplay = Label(searchMenuScreen, text=professorEmailEntry.get())
                professorEmailDisplay.configure(bg='medium spring green')
                professorEmailDisplay.grid()

    if studentStateClick.get() == professorStateClick.get():
        if studentGradeClick.get() == professorGradeClick.get():
            if studentSubjectEntry.get() != professorSubjectEntry.get():
                header = Label(searchMenuScreen,
                               text="There are no research openings matching the subject you wanted, here are some research openings that are in your state and are looking for people in the same grade as you: ")
                header.configure(bg='medium spring green')
                header.grid()
                professorStateDisplay = Label(searchMenuScreen, text=professorStateClick.get())
                professorStateDisplay.configure(bg='medium spring green')
                professorStateDisplay.grid()
                professorGradeDisplay = Label(searchMenuScreen, text=professorGradeClick.get())
                professorGradeDisplay.configure(bg='medium spring green')
                professorGradeDisplay.grid()
                professorSubjectDisplay = Label(searchMenuScreen, text=professorSubjectEntry.get())
                professorSubjectDisplay.configure(bg='medium spring green')
                professorSubjectDisplay.grid()
                professorNameDisplay = Label(searchMenuScreen, text=professorNameEntry.get())
                professorNameDisplay.configure(bg='medium spring green')
                professorNameDisplay.grid()
                professorUniversityDisplay = Label(searchMenuScreen, text=professorUniversityEntry.get())
                professorUniversityDisplay.configure(bg='medium spring green')
                professorUniversityDisplay.grid()
                professorEmailDisplay = Label(searchMenuScreen, text=professorEmailEntry.get())
                professorEmailDisplay.configure(bg='medium spring green')
                professorEmailDisplay.grid()

    if studentStateClick.get() == professorStateClick.get():
        if studentGradeClick.get() != professorGradeClick.get():
            if studentSubjectEntry.get() != professorSubjectEntry.get():
                header = Label(searchMenuScreen,
                               text="There are no research openings matching your subject and your grade, here are the research programs available in your state: ")
                header.configure(bg='medium spring green')
                header.grid()
                professorStateDisplay = Label(searchMenuScreen, text=professorStateClick.get())
                professorStateDisplay.configure(bg='medium spring green')
                professorStateDisplay.grid()
                professorGradeDisplay = Label(searchMenuScreen, text=professorGradeClick.get())
                professorGradeDisplay.configure(bg='medium spring green')
                professorGradeDisplay.grid()
                professorSubjectDisplay = Label(searchMenuScreen, text=professorSubjectEntry.get())
                professorSubjectDisplay.configure(bg='medium spring green')
                professorSubjectDisplay.grid()
                professorNameDisplay = Label(searchMenuScreen, text=professorNameEntry.get())
                professorNameDisplay.configure(bg='medium spring green')
                professorNameDisplay.grid()
                professorUniversityDisplay = Label(searchMenuScreen, text=professorUniversityEntry.get())
                professorUniversityDisplay.configure(bg='medium spring green')
                professorUniversityDisplay.grid()
                professorEmailDisplay = Label(searchMenuScreen, text=professorEmailEntry.get())
                professorEmailDisplay.configure(bg='medium spring green')
                professorEmailDisplay.grid()

        if studentStateClick.get() != professorStateClick.get():
            if studentGradeClick.get() != professorGradeClick.get():
                if studentSubjectEntry.get() == professorSubjectEntry.get():
                    header = Label(searchMenuScreen,
                                   text="There are no research openings in your area thats available here are the stuff matching your subject")
                    header = Label(searchMenuScreen, text="Research Programs that best fit you: ")
                    header.configure(bg='medium spring green', font='Courier')
                    header.grid(row=0, column=0)
                    professorStateDisplay = Label(searchMenuScreen, text=professorStateClick.get())
                    professorStateDisplay.configure(bg='medium spring green')
                    professorStateDisplay.grid()
                    professorGradeDisplay = Label(searchMenuScreen, text=professorGradeClick.get())
                    professorGradeDisplay.configure(bg='medium spring green')
                    professorGradeDisplay.grid()
                    professorSubjectDisplay = Label(searchMenuScreen, text=professorSubjectEntry.get())
                    professorSubjectDisplay.configure(bg='medium spring green')
                    professorSubjectDisplay.grid()
                    professorNameDisplay = Label(searchMenuScreen, text=professorNameEntry.get())
                    professorNameDisplay.configure(bg='medium spring green')
                    professorNameDisplay.grid()
                    professorUniversityDisplay = Label(searchMenuScreen, text=professorUniversityEntry.get())
                    professorUniversityDisplay.configure(bg='medium spring green')
                    professorUniversityDisplay.grid()
                    professorEmailDisplay = Label(searchMenuScreen, text=professorEmailEntry.get())
                    professorEmailDisplay.configure(bg='medium spring green')
                    professorEmailDisplay.grid()

    if studentStateClick.get() != professorStateClick.get():
        if studentGradeClick.get() == professorGradeClick.get():
            if studentSubjectEntry.get() == professorSubjectEntry.get():
                header = Label(searchMenuScreen,
                               text="There are no research openings in your state, here are the research openings that did match your grade and subject")
                header.configure(bg='medium spring green')
                header.grid()
                professorStateDisplay = Label(searchMenuScreen, text=professorStateClick.get())
                professorStateDisplay.configure(bg='medium spring green')
                professorStateDisplay.grid()
                professorGradeDisplay = Label(searchMenuScreen, text=professorGradeClick.get())
                professorGradeDisplay.configure(bg='medium spring green')
                professorGradeDisplay.grid()
                professorSubjectDisplay = Label(searchMenuScreen, text=professorSubjectEntry.get())
                professorSubjectDisplay.configure(bg='medium spring green')
                professorSubjectDisplay.grid()
                professorNameDisplay = Label(searchMenuScreen, text=professorNameEntry.get())
                professorNameDisplay.configure(bg='medium spring green')
                professorNameDisplay.grid()
                professorUniversityDisplay = Label(searchMenuScreen, text=professorUniversityEntry.get())
                professorUniversityDisplay.configure(bg='medium spring green')
                professorUniversityDisplay.grid()
                professorEmailDisplay = Label(searchMenuScreen, text=professorEmailEntry.get())
                professorEmailDisplay.configure(bg='medium spring green')
                professorEmailDisplay.grid()

    if studentStateClick.get() == professorStateClick.get():
        if studentGradeClick.get() != professorGradeClick.get():
            if studentSubjectEntry.get() == professorSubjectEntry.get():
                header = Label(searchMenuScreen,
                               text="There are no research openings in your state that are matching your grade, here are the research openings that match your state and your subject but not your grade")
                header.configure(bg='medium spring green')
                header.grid()
                professorStateDisplay = Label(searchMenuScreen, text=professorStateClick.get())
                professorStateDisplay.configure(bg='medium spring green')
                professorStateDisplay.grid()
                professorGradeDisplay - Label(searchMenuScreen, text=professorGradeClick.get())
                professorGradeDisplay.configure(bg='medium spring green')
                professorGradeDisplay.grid()
                professorSubjectDisplay = Label(searchMenuScreen, text=professorSubjectEntry.get())
                professorSubjectDisplay.configure(bg='medium spring green')
                professorSubjectDisplay.grid()
                professorNameDisplay = Label(searchMenuScreen, text=professorNameEntry.get())
                professorNameDisplay.configure(bg='medium spring green')
                professorNameDisplay.grid()
                professorUniversityDisplay = Label(searchMenuScreen, text=professorUniversityEntry.get())
                professorUniversityDisplay.configure(bg='medium spring green')
                professorUniversityDisplay.grid()
                professorEmailDisplay = Label(searchMenuScreen, text=professorEmailEntry.get())
                professorEmailDisplay.configure(bg='medium spring green')
                professorEmailDisplay.grid()


def studentscreen():
  titleLabel.destroy()
  studentcaller.destroy()
  professorcaller.destroy()
  studentState = Label(mainscreen, text="Select the state you are looking to research at: ")
  studentState.configure(bg='cyan')
  studentState.grid(row=0, column=0)
  studentStateClick = StringVar()
  studentStateClick.set("Alabama")
  studentStateDropDown = OptionMenu(mainscreen, studentStateClick, "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Deleware", "Florida", "Georgia", "Hawaii", "Idaho", "Illnois", "Indiana", "Iowa", "Kansas", "Kentucky", "Lousiana", "Maine", "Maryland", "Massachussetts", "Michigan", "Minnesota", "Mississipi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennesee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconson", "Wyoming")
  studentStateDropDown.configure(bg='cyan')
  studentStateDropDown.grid(row=0, column=1)
  studentGrade = Label(mainscreen, text="Select the grade you are in: ")
  studentGrade.configure(bg='cyan')
  studentGrade.grid(row=1, column=0)
  studentGradeClick = StringVar()
  studentGradeClick.set("Grade 9")
  studentGradeDropDown = OptionMenu(mainscreen, studentGradeClick, "Grade 9", "Grade 10", "Grade 11", "Grade 12")
  studentGradeDropDown.configure(bg='cyan')
  studentGradeDropDown.grid(row=1, column=1)
  studentSubject = Label(mainscreen, text="Enter the subject you are looking to research in: ")
  studentSubject.configure(bg='cyan')
  studentSubject.grid(row=2, column=0)
  studentSubjectEntry = Entry(mainscreen)
  studentSubjectEntry.configure(bg='cyan')
  studentSubjectEntry.grid(row=2, column=1)
  searchButton = Button(mainscreen, text="Search for Research Programs", command=searchMenu)
  searchButton.configure(bg='cyan')
  searchButton.grid(row=3, column=1)


def publishOpening():
  professor_subject = professorSubjectEntry.get()
  professor_email = professorEmailEntry.get()
  professor_university = professorUniversityEntry.get()

  if len(professor_subject) == 0:
    errorLabel = Label(mainscreen, text="You did not enter the subject: ")
    errorLabel.grid(row=7, column=1)
  if len(professor_email) == 0: 
    errorLabel = Label(mainscreen, text="You did not enter your email: ")
    errorLabel.grid(row=7, column=1)
  if len(professor_university) == 0: 
    errorLabel = Label(mainscreen, text="You did not enter your university: ")
    errorLabel.grid(row=7, column=1)
  

  if len(professor_subject) == 0 and len(professor_email) == 0: 
    errorLabel = Label(mainscreen, text="You did not enter your subject and your email: ")
    errorLabel.grid(row=7, column=1)
  
  if len(professor_subject) == 0 and len(professor_university) == 0: 
    errorLabel = Label(mainscreen, text="You did not enter your subject and your university: ")
    errorLabel.grid(row=7, column=1)
  
  if len(professor_email) == 0 and len(professor_university) == 0: 
    errorLabel = Label(mainscreen, text="You did not enter your email and your university")
    errorLabel.grid(row=7, column=1)





def professorscreen():
    titleLabel.destroy()
    studentcaller.destroy()
    professorcaller.destroy()
    professorState = Label(mainscreen, text="Select the state you work in: ")
    professorState.configure(bg='cyan')
    professorState.grid(row=0, column=0)
    professorStateClick = StringVar()
    professorStateClick.set("Alabama")
    professorStateDropDown = OptionMenu(mainscreen, professorStateClick, "Alabama", "Alaska", "Arizona", "Arkansas",
                                        "California", "Colorado", "Connecticut", "Deleware", "Florida", "Georgia",
                                        "Hawaii", "Idaho", "Illnois", "Indiana", "Iowa", "Kansas", "Kentucky",
                                        "Lousiana", "Maine", "Maryland", "Massachussetts", "Michigan", "Minnesota",
                                        "Mississipi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
                                        "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota",
                                        "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
                                        "South Dakota", "Tennesee", "Texas", "Utah", "Vermont", "Virginia",
                                        "Washington", "West Virginia", "Wisconson", "Wyoming")
    professorStateDropDown.configure(bg='cyan')
    professorStateDropDown.grid(row=0, column=1)
    professorGrade = Label(mainscreen, text="Select the grade students should be in for this research program: ")
    professorGrade.configure(bg='cyan')
    professorGrade.grid(row=1, column=0)
    professorGradeClick = StringVar()
    professorGradeClick.set("Grade 9")
    professorGradeDropDown = OptionMenu(mainscreen, professorGradeClick, "Grade 9", "Grade 10", "Grade 11", "Grade 12",
                                        "Grades 9 - 10", "Grades 9 - 11,", "Grades 9 - 12", "Grades 10 - 11",
                                        "Grades 10-12", "Grades 11 - 12")
    professorGradeDropDown.configure(bg='cyan')
    professorGradeDropDown.grid(row=1, column=1)
    professorSubject = Label(mainscreen, text="Enter the subject this research program is covering: ")
    professorSubject.configure(bg='cyan')
    professorSubject.grid(row=2, column=0)
    professorSubjectEntry = Entry(mainscreen)
    professorSubjectEntry.configure(bg='cyan')
    professorSubjectEntry.grid(row=2, column=1)
    professorName = Label(mainscreen, text="Enter your full name: ")
    professorName.configure(bg='cyan')
    professorName.grid(row=3, column=0)
    professorNameEntry = Entry(mainscreen)
    professorNameEntry.configure(bg='cyan')
    professorNameEntry.grid(row=3, column=1)
    professorUniversity = Label(mainscreen, text="Enter the university you work for: ")
    professorUniversity.configure(bg='cyan')
    professorUniversity.grid(row=4, column=0)
    professorUniversityEntry = Entry(mainscreen)
    professorUniversityEntry.configure(bg='cyan')
    professorUniversityEntry.grid(row=4, column=1)
    professorEmail = Label(mainscreen, text="Enter your business email: ")
    professorEmail.configure(bg='cyan')
    professorEmail.grid(row=5, column=0)
    professorEmailEntry = Entry(mainscreen)
    professorEmailEntry.configure(bg='cyan')
    professorEmailEntry.grid(row=5, column=1)
    publishButton = Button(mainscreen, text="Publish Opening", command=publishOpening)
    publishButton.grid(row=6, column=1)


mainscreen = Tk()
mainscreen.title("Research-Matcher!")
mainscreen.configure(background='cyan')
professorStateClick = StringVar()
professorGradeClick = StringVar()
professorSubjectEntry = StringVar()
professorNameEntry = StringVar()
professorUniversityEntry = StringVar()
professorEmailEntry = StringVar()
studentStateClick = StringVar()
studentGradeClick = StringVar()
studentSubjectEntry = StringVar()
titleLabel = Label(mainscreen, text="Welcome!")
titleLabel.configure(background='cyan', font=('Courier', '50'))
titleLabel.grid(row=0, column=1)
studentcaller = Button(mainscreen, text="Student? Click Here!", command=studentscreen)
studentcaller.configure(background='cyan', font=('Courier'))
studentcaller.grid(row=1, column=1)
professorcaller = Button(mainscreen, text="Professor? Click Here!", command=professorscreen)
professorcaller.configure(background='cyan',font=('Courier'))
professorcaller.grid(row=2, column=1)
mainscreen.mainloop()


        








        
    






                




            
    
    
        
        

def studentscreen():
  titleLabel.destroy()
  studentcaller.destroy()
  professorcaller.destroy()
  studentState = Label(mainscreen, text="Select the state you are looking to research at: ")
  studentState.configure(bg='cyan')
  studentState.grid(row=0, column=0)
  studentStateClick = StringVar()
  studentStateClick.set("Alabama")
  studentStateDropDown = OptionMenu(mainscreen, studentStateClick, "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Deleware", "Florida", "Georgia", "Hawaii", "Idaho", "Illnois", "Indiana", "Iowa", "Kansas", "Kentucky", "Lousiana", "Maine", "Maryland", "Massachussetts", "Michigan", "Minnesota", "Mississipi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennesee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconson", "Wyoming")
  studentStateDropDown.configure(bg='cyan')
  studentStateDropDown.grid(row=0, column=1)
  studentGrade = Label(mainscreen, text="Select the grade you are in: ")
  studentGrade.configure(bg='cyan')
  studentGrade.grid(row=1, column=0)
  studentGradeClick = StringVar()
  studentGradeClick.set("Grade 9")
  studentGradeDropDown = OptionMenu(mainscreen, studentGradeClick, "Grade 9", "Grade 10", "Grade 11", "Grade 12")
  studentGradeDropDown.configure(bg='cyan')
  studentGradeDropDown.grid(row=1, column=1)
  studentSubject = Label(mainscreen, text="Enter the subject you are looking to research in: ")
  studentSubject.configure(bg='cyan')
  studentSubject.grid(row=2, column=0)
  studentSubjectEntry = Entry(mainscreen)
  studentSubjectEntry.configure(bg='cyan')
  studentSubjectEntry.grid(row=2, column=1)
  searchButton = Button(mainscreen, text="Search for Research Programs", command=searchMenu(studentStateClick, studentGradeClick, studentSubjectEntry, professorStateClick, professorGradeClick, professorSubjectEntry, professorNameEntry, professorUniversityEntry, professorEmailEntry))
  searchButton.configure(bg='cyan')
  searchButton.grid(row=3, column=1)
    



def publishOpening(): 
  published = Label(mainscreen, text="Research Program Published")
  published.configure(bg='cyan')
  published.grid(row=7, column=1)
    
    



def professorscreen():
  titleLabel.destroy()
  studentcaller.destroy()
  professorcaller.destroy()
  professorState = Label(mainscreen, text="Select the state you work in: ")
  professorState.configure(bg='cyan')
  professorState.grid(row=0, column=0)
  professorStateClick = StringVar()
  professorStateClick.set("Alabama")
  professorStateDropDown = OptionMenu(mainscreen, professorStateClick, "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Deleware", "Florida", "Georgia", "Hawaii", "Idaho", "Illnois", "Indiana", "Iowa", "Kansas", "Kentucky", "Lousiana", "Maine", "Maryland", "Massachussetts", "Michigan", "Minnesota", "Mississipi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennesee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconson", "Wyoming")
  professorStateDropDown.configure(bg='cyan')
  professorStateDropDown.grid(row=0, column=1)
  professorGrade = Label(mainscreen, text="Select the grade students should be in for this research program: ")
  professorGrade.configure(bg='cyan')
  professorGrade.grid(row=1, column=0)
  professorGradeClick = StringVar()
  professorGradeClick.set("Grade 9")
  professorGradeDropDown = OptionMenu(mainscreen, professorGradeClick, "Grade 9", "Grade 10", "Grade 11", "Grade 12", "Grades 9 - 10", "Grades 9 - 11,", "Grades 9 - 12", "Grades 10 - 11", "Grades 10-12", "Grades 11 - 12")
  professorGradeDropDown.configure(bg='cyan')
  professorGradeDropDown.grid(row=1, column=1)
  professorSubject = Label(mainscreen, text="Enter the subject this research program is covering: ")
  professorSubject.configure(bg='cyan')
  professorSubject.grid(row=2, column=0)
  professorSubjectEntry = Entry(mainscreen)
  professorSubjectEntry.configure(bg='cyan')
  professorSubjectEntry.grid(row=2, column=1)
  professorName = Label(mainscreen, text="Enter your full name: ")
  professorName.configure(bg='cyan')
  professorName.grid(row=3, column=0)
  professorNameEntry = Entry(mainscreen)
  professorNameEntry.configure(bg='cyan')
  professorNameEntry.grid(row=3, column=1)
  professorUniversity = Label(mainscreen, text="Enter the university you work for: ")
  professorUniversity.configure(bg='cyan')
  professorUniversity.grid(row=4, column=0)
  professorUniversityEntry = Entry(mainscreen)
  professorUniversityEntry.configure(bg='cyan')
  professorUniversityEntry.grid(row=4, column=1)
  professorEmail = Label(mainscreen, text="Enter your business email: ")
  professorEmail.configure(bg='cyan')
  professorEmail.grid(row=5, column=0)
  professorEmailEntry = Entry(mainscreen)
  professorEmailEntry.configure(bg='cyan')
  professorEmailEntry.grid(row=5, column=1)
  publishButton = Button(mainscreen, text="Publish Opening", command=publishOpening)
  publishButton.grid(row=6, column=1)
    
    
    
    
    








mainscreen = Tk()
mainscreen.title("Research-Matcher!")
mainscreen.configure(background='cyan')
titleLabel = Label(mainscreen, text="Welcome!")
titleLabel.configure(background='cyan', font=('Courier', '50'))
titleLabel.grid(row=0, column=1)
studentcaller = Button(mainscreen, text="Student? Click Here!", command=studentscreen)
studentcaller.configure(background='cyan', font=('Courier'))
studentcaller.grid(row=1, column=1)
professorcaller = Button(mainscreen, text="Professor? Click Here!", command=professorscreen)
professorcaller.configure(background='cyan',font=('Courier'))
professorcaller.grid(row=2, column=1)
mainscreen.mainloop()


