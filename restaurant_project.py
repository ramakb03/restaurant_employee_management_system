#program designs an Object-Oriented model
#for a restaurant employee management system
class Employee :
    #constructor
    def __init__(self, name, address, telephone, SSN, bank_account_numb) :
        self.name = name
        self.address = address
        self.telephone = telephone
        self.SSN = SSN
        self.bank_account_number = bank_account_numb
        
    #getter for name
    def get_name(self) :
        return "Employee's name is " + self.name
    #setter for name
    def set_name(self, name) :
        self.name = name
    #getter for address
    def get_address(self) :
        return self.name + "'s address is " + self.address
    #setter for address
    def set_address(self, address) :
        self.address = address
    #getter for phone number
    def get_telephone(self) :
        return self.name + "'s phone number is " + self.telephone
    #setter for phone number
    def set_telephone(self, telephone) :
        self.telephone = telephone
    #getter for SSN
    def get_SSN(self) :
        return self.name + "'s social security number is " +  self.SSN
    #setter for SSN
    def set_SSN(self,SSN) :
        self.SSN = SSN
    #getter for bank account number
    def get_bank_account_number(self) :
        return self.name + "'s bank account number is " + self.bank_account_number
    #setter for bank account number 
    def set_bank_account_number(self, bank_account_number) :
        self.bank_account_number = bank_account_number

#Cook class inherits from the Employee class
class Cook (Employee):
    #constructor
    def __init__(self, name, address, telephone, SSN,
                 bank_account_number, experience) :
        super().__init__(name, address, telephone, SSN,
                         bank_account_number)
        self.experience = experience
        
    #getter for experience
    def get_experience(self) :
        return self.name + " has " + self.experience + " years of experience" 
    #setter for experience
    def set_experience(self, experience) :
        self.experience = experience

#Sous_Chef class inherits from the cook class
class Sous_Chef(Cook) :
        #constructor
        def __init__(self, name, address, telephone, SSN,
                     bank_account_number, experience,
                     institution_attended,
                     specialty) :
            super().__init__(name, address, telephone, SSN,
                          bank_account_number, experience)
            self.institution_attended = institution_attended
            self.specialty = specialty
        
        #getter for institution attended
        def get_institution_attended (self) :
            return self.name + "'s institution attended : " + self.institution_attended
        #setter for institution attended :
        def set_institution_attended(self,institution_attended) :
            self.institution_attended = institution_attended
        #getter for specialty
        def get_specialty(self) :
            return self.name + "'s specialty: " + self.specialty
        #setter for specialty
        def set_specialty(self, specialty) :
            self.specialty = specialty

#Chef class inherits from the Sous_Chef class
class Chef(Sous_Chef) :
    #constructor
    def __init__(self, name, address, telephone, SSN,
                 bank_account_number, experience,
                 institution_attended, specialty,
                 num_awards, num_shows_featured):
        super().__init__(name, address, telephone, SSN,
                        bank_account_number, experience,
                       institution_attended, specialty)
        self.num_awards = num_awards
        self.num_shows_featured = num_shows_featured
    
    #getter for number of awards
    def get_num_awards(self) :
        return self.name + "'s number of awards: " + self.num_awards
    #setter for number of awards
    def set_num_awards(self, num_awards) :
        self.num_awards = num_awards
    #getter for number of shows featured
    def get_num_shows_featured(self) :
        return self.name + "'s number of shows featured = " + self.num_shows_featured
    #setter for number of shows featured
    def set_num_shows_featured(self, num_shows_featured) :
        self.num_shows_featured = num_shows_featured

#Server class inherits from the Employee class
class Server(Employee) :
    def __init__(self, name, address, telephone, SSN, bank_account_number,
                 experience, num_positive_feedbacks, num_complaints) :
        super().__init__(name, address, telephone, SSN, bank_account_number)
        self.experience = experience
        self.num_positive_feedbacks = num_positive_feedbacks
        self.num_complaints = num_complaints
        
    #getter for years of experience
    def get_experience(self) :
        return self.name + " has " + self.experience + " years of experience"
    #setter for years of experience
    def set_experience(self, experience) :
        self.experience = experience
    #getter for number of positive feedbacks
    def get_num_positive_feedbacks(self):
        return self.name + " has " + self.num_positive_feedbacks + " positive feedbacks"
    #setter for number of positive feedbacks
    def set_num_positive_feedbacks(self, num_positive_feedbacks):
        self.num_positive_feedbacks = num_positive_feedbacks
    #getter for number of complaints
    def get_num_complaints(self):
        return self.name + " has " + self.num_complaints + " complaints"
    #setter for number of complaints
    def set_num_complaints(self, num_complaints) :
        self.num_complaints = num_complaints

#Jnaitor class inherits from the Employee class
class Janitor(Employee) :
    #constructor
    def __init__(self, name, address, telephone, SSN, bank_account_number,
                 experience, maintenance_training) :
        super().__init__(name, address, telephone, SSN, bank_account_number)
        self.experience = experience
        self.maintenance_training = maintenance_training
    
    #getter for years of experience
    def get_experience(self) :
        return self.name + " has " + self.experience + " years of experience"
    #setter for years of experience
    def set_experience(self, experience):
        self.experience = experience
    #getter for maintenance training
    def get_maintenance_training(self) :
        return self.name + "'s maintenance training: " + self.maintenance_training
    #setter for maintenance training
    def set_maintenance_training(self, maintenance_training) :
        self.maintenance_training = maintenance_training

#Manager class inherits from the Employee class
class Manager(Employee) :
    #constructor
    def __init__(self, name, address, telephone, SSN, bank_account_number,
                experience, tertiary_degree, num_employees_managed) :
        super().__init__(name, address, telephone, SSN, bank_account_number)
        self.experience = experience
        self.tertiary_degree = tertiary_degree
        self.num_employees_managed = num_employees_managed
    
    #getter for years of experience
    def get_experience(self):
        return self.name + " has " + self.experience + " years of experience"
    #setter for experience(self, experience):
    def set_experience(self, experience) :
        self.experience = experience
    #getter for tertiary degree
    def get_tertiary_degree(self) :
        return self.name + "'s tertiary degree: " + self.tertiary_degree
    #setter for tertiary degree(self, tertiary_degree)
    def set_tertiary_degree(self, tertiary_degree) :
        self.tertiary_degree = tertiary_degree
    #getter for number of employees managed
    def get_num_employees_managed(self) :
        return self.name + " manages " + self.num_employees_managed + " employees"
    #setter for number of employees managed
    def set_num_employees_managed(self, num_employees_managed) :
        self.num_employees_managed = num_employees_managed

#instantiate an object of each class
        
e1 = Employee("Mike", "123 Bushwick ave", "929-382-8268", "111-11-1111", "A384920202")
print(e1.get_name())
print(e1.get_address())
print(e1.get_telephone())
print(e1.get_SSN())
print(e1.get_bank_account_number())
print()

#reset values
e1.set_name("Anne")
e1.set_address("299 Cane St")
e1.set_telephone("298-181-1892")
e1.set_SSN("781-27-0010")
e1.set_bank_account_number("K28918902")

print(e1.get_name())
print(e1.get_address())
print(e1.get_telephone())
print(e1.get_SSN())
print(e1.get_bank_account_number())
print()

e2 = Cook("Daniel", "902 Ocean St", "378-282-1222", "389-28-2822", "D3793791121", "2" )
print(e2.get_name())
print(e2.get_address())
print(e2.get_telephone())
print(e2.get_SSN())
print(e2.get_bank_account_number())
print(e2.get_experience())
print()

#reset values
e2.set_name("Tati")
e2.set_address("83 Besfurl Ave")
e2.set_telephone("482-1111-382")
e2.set_SSN("281-88-9999")
e2.set_bank_account_number("I28191839")
e2.set_experience("3")

print(e2.get_name())
print(e2.get_address())
print(e2.get_telephone())
print(e2.get_SSN())
print(e2.get_bank_account_number())
print(e2.get_experience())
print()

e3 = Sous_Chef("Eren", "843 Park Ave", "894-221-8588", "119-01-2829",
               "W8391290028", "5", "Melbury", "Lasagna")
print(e3.get_name())
print(e3.get_address())
print(e3.get_telephone())
print(e3.get_SSN())
print(e3.get_bank_account_number())
print(e3.get_experience())
print(e3.get_institution_attended())
print(e3.get_specialty())
print()

#reset values
e3.set_name("Lala")
e3.set_address("999 Flatbush Ave")
e3.set_telephone("811-9292-1900")
e3.set_SSN("111-22-3333")
e3.set_bank_account_number("D8398002")
e3.set_experience("6")
e3.set_institution_attended("BK College")
e3.set_specialty("Domoda")

print(e3.get_name())
print(e3.get_address())
print(e3.get_telephone())
print(e3.get_SSN())
print(e3.get_bank_account_number())
print(e3.get_experience())
print(e3.get_institution_attended())
print(e3.get_specialty())
print()

e4 = Chef("Fada", "269 Franklin St", "373-267-8710", "210-38-2818", "A783919101", "10",
          "Cook University", "Mafé", "5", "3")
print(e4.get_name())
print(e4.get_address())
print(e4.get_telephone())
print(e4.get_SSN())
print(e4.get_bank_account_number())
print(e4.get_experience())
print(e4.get_institution_attended())
print(e4.get_specialty())
print(e4.get_num_awards())
print(e4.get_num_shows_featured())
print()

#reset values
e4.set_name("Thierno")
e4.set_address("373 Tamba St")
e4.set_telephone("121-2729-9990")
e4.set_SSN("333-55-6666")
e4.set_bank_account_number("S7398291")
e4.set_experience("8")
e4.set_institution_attended("Colgate University")
e4.set_specialty("Mburu")
e4.set_num_awards("10")
e4.set_num_shows_featured("7")

print(e4.get_name())
print(e4.get_address())
print(e4.get_telephone())
print(e4.get_SSN())
print(e4.get_bank_account_number())
print(e4.get_experience())
print(e4.get_institution_attended())
print(e4.get_specialty())
print(e4.get_num_awards())
print(e4.get_num_shows_featured())
print()

e5 = Server("Sofia", "832  Ralph Ave", "839-311-1111", "489-11-0101",
            "J24783891", "0", "5", "2")
print(e5.get_name())
print(e5.get_address())
print(e5.get_telephone())
print(e5.get_SSN())
print(e5.get_bank_account_number())
print(e5.get_num_positive_feedbacks())
print(e5.get_num_complaints())
print()

#reset values
e5.set_name("Laity")
e5.set_address("3821 Matam Ave")
e5.set_telephone("726-9119-2782")
e5.set_SSN("181-99-3223")
e5.set_bank_account_number("P2819121")
e5.set_experience("2")
e5.set_num_positive_feedbacks("10")
e5.set_num_complaints("8")

print(e5.get_name())
print(e5.get_address())
print(e5.get_telephone())
print(e5.get_SSN())
print(e5.get_bank_account_number())
print(e5.get_num_positive_feedbacks())
print(e5.get_num_complaints())
print()

e6 = Janitor("Youma", "221 Dakar St", "777-929-0010", "111-11-9919",
             "Q38923802", "2", "NOT completed")
print(e6.get_name())
print(e6.get_address())
print(e6.get_telephone())
print(e6.get_SSN())
print(e6.get_bank_account_number())
print(e6.get_experience())
print(e6.get_maintenance_training())
print()

#reset values
e6.set_name("Kardiatou")
e6.set_address("1717 Thies")
e6.set_telephone("118-3721-8390")
e6.set_SSN("198-22-7821")
e6.set_bank_account_number("B638313")
e6.set_experience("3")
e6.set_maintenance_training("completed")

print(e6.get_name())
print(e6.get_address())
print(e6.get_telephone())
print(e6.get_SSN())
print(e6.get_bank_account_number())
print(e6.get_experience())
print(e6.get_maintenance_training())
print()


e7 = Manager("Rama", "181 Bedford Ave", "478-292-1121",
             "282-99-1000", "D84920101", "5", "SABS", "3")
print(e7.get_name())
print(e7.get_address())
print(e7.get_telephone())
print(e7.get_SSN())
print(e7.get_bank_account_number())
print(e7.get_experience())
print(e7.get_tertiary_degree())
print(e7.get_num_employees_managed())
print()

#reset values
e7.set_name("Toulaye")
e7.set_address("4872 Dakar St")
e7.set_telephone("347-819-1881")
e7.set_SSN("171-99-1112")
e7.set_bank_account_number("A830390")
e7.set_experience("6")
e7.set_tertiary_degree("OLP Management School")
e7.set_num_employees_managed("7")

print(e7.get_name())
print(e7.get_address())
print(e7.get_telephone())
print(e7.get_SSN())
print(e7.get_bank_account_number())
print(e7.get_experience())
print(e7.get_tertiary_degree())
print(e7.get_num_employees_managed())
print()