class Facility:

    def addFacility(self):
        with open('facilities.txt', "a") as file:
            self.Name = input("Enter Facility Name: ")
            file.write(self.Name + "\n")

    def displayFacilities(self):
        with open('facilities.txt', "r") as file:
            for line in file:
                print(line.strip())

    def writeListOffacilitiesToFile(self, facilities_list, file_name):
        with open(file_name, "w") as file:
            for facility in facilities_list:
                file.write("\n"+facility.Name + "\n")


print("Welcome to Alberta Hospital (AH) Managment system")
x=input("Select from the following options, or select 0 to stop: \n1 - 	Doctors\n2 - 	Facilities\n3 - 	Laboratories\n4 - 	Patients\n")
if x=='2':
    for i in range(1000):
        no=input("Facilities Menu:\n1 - Display Facilities list\n2 - Add Facility\n3 - Back to the Main Menu\n")
        if no=='1':
            Facility.displayFacilities(Facility)
            print("Back to the prevoius Menu")
        if no=='2':
            Facility.addFacility(Facility)
            print("Back to the prevoius Menu")
        if no=='3':
            print("Back to the prevoius Menu")
            quit()
else:
    quit()