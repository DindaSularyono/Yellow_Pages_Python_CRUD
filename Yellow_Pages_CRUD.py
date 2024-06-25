# UNIVERSAL FUNCTION
# A. Search business Index by code
def searchIndex (code):
    for business in yellowPages:
        if business ["Code"] == code.upper():
            return business
    return None  

# B. Search business Index by phone
def searchNumber (phone):
    for business in yellowPages:
        if business ["Phone"] == phone:
            return business
    return None

# C. Search business Index by website
def searchWebsite (website):
    for business in yellowPages:
        if business ["Website"] == website:
            return business
    return None

# D. Valid Business Code Function
def validNewCode():
    while True:
        inputCode = input("Enter the business code you want to create: ")
        if inputCode.isalpha() and len(inputCode)==4 :
            businessIndex= searchIndex(inputCode)
            if businessIndex:
                print (f"'{inputCode}' already exist. Please enter another code")
            else:
                return inputCode.upper()
        else:
            print ("Only a combination of four letters is allowed for the business code")

# E. Valid Business Phone Number Function
def validNewPhone ():
    while True:
        inputPhone = input("Enter the Phone number: ")
        if inputPhone.isdigit() and len(inputPhone)==10 and inputPhone.startswith("021") :
            businessIndex= searchNumber(inputPhone)
            if businessIndex:
                print (f"'{inputPhone}' is already associated with another business, Please enter a new number.")
            else:
                return inputPhone
        else:
            print("Phone number is invalid; it must be a 10-digit number starting with 021")

# F. Valid Business Website Function
def validNewWebsite():
    while True:
        inputCode = input("Enter the website: ")
        if inputCode.startswith(('http://', 'https://','www.')) and not inputCode.isspace():
            businessIndex= searchWebsite(inputCode)
            if businessIndex:
                print (f"'{inputCode}' already exist. Website can't be identical to other business")
            else:
                return inputCode
        else:
            print ("Invalid website url, please try again.")

# G. Valid Business Industry Function
def validNewIndustry():
    while True:        
        print("""
Industry list:
1. Technology\t5. Industrial\t\t9. Cyclical
2. Property\t6. Transportation\t10. Finance
3. Health\t7. Infrastructure\t11. Basic Industries
4. Energy\t8. Non-Cyclical
""")
        answer = input("Enter the Industry (1-11): ")
        if answer.isdigit() and int(answer)>=1 and int(answer)<=11:
            if answer == "1":
                return "Technology"            
            elif answer == "2":
                return "Property"            
            elif answer == "3":
                return "Health"            
            elif answer == "4":
                return "Energy"            
            elif answer == "5":
                return "Industrial"            
            elif answer == "6":
                return "Transportation"            
            elif answer == "7":
                return "Infrastructure"            
            elif answer == "8":
                return "Non-Cyclical"            
            elif answer == "9":
                return "Cyclical"            
            elif answer == "10":
                return "Finance"            
            elif answer == "11":
                return "Basic Industries"            
        else:
            print("Invalid answer. Please try again.\n")

# H. Valid Business Address Function
def validNewAddress():
    inputAddress = input("Enter the Address: ")
    while True:
        inputPostalCode = input("Specify the postal codes: ")
        if inputPostalCode.isdigit() and len(inputPostalCode) ==6:
            postalCode=inputPostalCode
            return inputAddress+" "+postalCode
        else:
            print("Invalid Postal Code, Please try again.")

# I. Print Business in detail
def printBusinessDetail (business):
    print(f"""
Code: {business['Code']}
Name: {business['Name']}
Phone: {business['Phone']}
Website: {business['Website']}
Industry: {business['Industry']}
Address: {business['Address']}
""")
    
###==============================================================================================================================================================
    
# MENU FUNCTION
# A. MAIN MENU
def mainMenu():
    while True:
        print("\n_________________________________________________________________\n\n           - Welcome to Yellow Pages Directory -\n")
        print("1. View Directory")
        print("2. Add a New Business")
        print("3. Update a Business")
        print("4. Delete a Business")
        print("0. Exit\n")

        answer = input("Enter your answer (0-4): ")
        if answer == "1":
            readMenu()
        elif answer == "2":
            createBusiness()
        elif answer == "3":
            updateBusiness()
        elif answer == "4":
            deleteMenu()
        elif answer == "0":
            exitMenu()
        else:
            print("!!! Invalid answer. Please try again !!!\n")

#==============================================================================================================================#

# B. READ MENU
def readMenu():
    while True:
        print("\n_________________________________________________________________\n\n           - View Directory -\n")
        print("1. Show All Directory")
        print("2. Search Specific Business")
        print("3. Back to Main Menu")
        print("0. Exit\n")
        
        answer = input("Enter your answer (0-3): ")
        if answer == "1":
            showAllDirectory()
        elif answer == "2":
            searchBusiness()
        elif answer == "3":
            mainMenu()
        elif answer == "0":
            exitMenu()
        else:
            print("!!! Invalid answer. Please try again !!!\n")

# B. 1. Show All Directory function
def showAllDirectory():
    if len(yellowPages)==0:
        print ("Yellow Page Directory is not available, try to entry data first.")
    else :
        print("\n_________________________________________________________________\n\n          - Show All Directory -\n")
        print(f" Index\t| Code \t| Phone\t\t| Website\t\t\t| Industry \t | Address\t\t\t\t\t|\n=================================================================================================================================")
        for business in range(len(yellowPages)):
            print(f"   {business}\t| {yellowPages[business]["Code"]}\t| {yellowPages[business]["Phone"]}\t| {yellowPages[business]["Website"]} \t\t| {yellowPages[business]["Industry"]} \t | {yellowPages[business]["Address"][:34]}...{yellowPages[business]["Address"][-6:]}\t|")

# B. 2. Search Specific Business
def searchBusiness():
    while True:
        print("\n_________________________________________________________________\n\n           - Search Specific Business-\n")
        inputCode = input("Enter the business code you want to search: ")
        businessIndex= searchIndex(inputCode)
        if businessIndex:
            print (f"\nThese are the business detail of '{inputCode.upper()}': ")
            printBusinessDetail(businessIndex)
            readMenu()
        else:
            print ("The Business you're looking for is not found, back to menu")
            readMenu()

#==============================================================================================================================#
   
# C. CREATE MENU
# C. 1. Create a new business
def createBusiness():
    print("\n_________________________________________________________________\n\n           - Add a New Business -\n")
    newBusiness={}
    newBusiness['Code'] = validNewCode().upper()
    newBusiness['Name'] = input("Enter the business name: ")
    newBusiness['Phone'] = validNewPhone()
    newBusiness['Website'] = validNewWebsite()
    newBusiness['Industry'] = validNewIndustry()
    newBusiness['Address'] = validNewAddress()
    yellowPages.append(newBusiness)
    print("The new business has been added successfully")
            
#==============================================================================================================================#

# # D. UPDATE MENU
# D. 1. Update a Business
def updateBusiness():
    print("\n_________________________________________________________________\n\n           - Update a Business -\n")
    while True:
        inputCode = input("Enter the business code you want to update: ")
        businessIndex= searchIndex(inputCode)
        if businessIndex:
            print (f"\n_________________________________________________________________\n\nThese are the business detail of '{inputCode.upper()}': ")
            printBusinessDetail(businessIndex)
            editBusinessMenu(businessIndex)
            mainMenu()
        else:
            print ("The Business you're looking for is not found, back to menu")
            mainMenu()

# D. 1. a. Update spesific business detail          
def editBusinessMenu(business):
    while True:        
        print("""
Which business details you want to edit?:
1. Business Code
2. Business Name
3. Business Phone Number
4. Business Website
5. Business Industry
6. Business Address
0. Cancel
""")
        # Update Business Code
        answer = input("Your answer (0-6): ")
        if answer == "1":
            updateCode=validNewCode()
            answer = input("Do you want to save the edit? (Y/N): ").strip().lower()
            if answer =="y":
                business["Code"] = updateCode
                print("Changes to your business code have been saved.")
                return  
            elif answer =="n":
                print ("Discard edit, return to main menu.\n\n_________________________________________________________________") 
                mainMenu ()
            else: 
                print("Invalid answer. Please try again\n")  

        # Update Business Name
        elif answer == "2":
            updateName=input("Enter the business name: ")
            answer = input("Do you want to save the edit? (Y/N): ").strip().lower()
            if answer =="y":
                business['Name'] = updateName
                print("Changes to your business name have been saved.")
                return
            elif answer =="n":
                print ("Discard edit, return to main menu.\n\n_________________________________________________________________") 
                mainMenu ()
            else: 
                print("Invalid answer. Please try again\n")

        # Update Business Phone Number
        elif answer == "3":
            updatePhone=validNewPhone()
            answer = input("Do you want to save the edit? (Y/N): ").strip().lower()
            if answer =="y":
                business['Phone'] = updatePhone
                print("Changes to your business phone number have been saved.")
                return   
            elif answer =="n":
                print ("Discard edit, return to main menu.\n\n_________________________________________________________________") 
                mainMenu ()
            else: 
                print("Invalid answer. Please try again\n")
        # Update Business Website
        elif answer == "4":
            updateWebsite= validNewWebsite()
            answer = input("Do you want to save the edit? (Y/N): ").strip().lower()
            if answer =="y":
                business['Website'] = updateWebsite
                print("Changes to your business website have been saved.") 
                return
            elif answer =="n":
                print ("Discard edit, return to main menu.\n\n_________________________________________________________________") 
                mainMenu ()
            else: 
                print("Invalid answer. Please try again\n")   

        # Update Business Industry
        elif answer == "5":
            updateIndustry=validNewIndustry()
            answer = input("Do you want to save the edit? (Y/N): ").strip().lower()
            if answer =="y":
                business['Industry'] = updateIndustry
                print("Changes to your business industry have been saved.")
                return
            elif answer =="n":
                print ("Discard edit, return to main menu.\n\n_________________________________________________________________") 
                mainMenu ()
            else: 
                print("Invalid answer. Please try again\n")  
        
        # Update Businesss Address
        elif answer == "6":
            updateAddress=validNewAddress()
            answer = input("Do you want to save the edit? (Y/N): ").strip().lower()
            if answer =="y":
                business['Address'] = updateAddress
                print("Changes to your business address have been saved.")
                return
            elif answer =="n":
                print ("Discard edit, return to main menu.\n\n_________________________________________________________________") 
                mainMenu ()
            else: 
                print("Invalid answer. Please try again\n")     
        
        elif answer == "0":
            print ("Canceling edit, back to main menu.")
            mainMenu()
        else:
            print("Invalid answer. Please try again.\n")

#==============================================================================================================================#

# E. DELETE MENU
def deleteMenu():
    while True:
        print("\n_________________________________________________________________\n\n           - Delete a Business -\n")
        print("1. Delete a Business")
        print("2. Back to Main Menu")
        print("0. Exit\n")
        
        answer = input("Enter your answer (0-2): ")
        if answer == "1":
            deleteBusiness()
        elif answer == "2":
            mainMenu()
        elif answer == "0":
            exitMenu()
        else:
            print("!!! Invalid answer. Please try again !!!\n") 

# E. 1. Delete Business Function
def deleteBusiness():
    while True:
        print("\n_________________________________________________________________\n\n           - Delete A Business-\n")
        inputCode = input("Enter the business code you want to delete: ")
        businessIndex= searchIndex(inputCode)
        if businessIndex:
            print (f"\n_________________________________________________________________\n\nPlease make sure you're going to delete the correct business!\nThese are the business detail of '{inputCode.upper()}': ")
            printBusinessDetail(businessIndex)
            answer = input(f"Type '{inputCode.upper()}' to continue delete business from Yellow Pages Directory:")
            if answer == inputCode.upper():
                yellowPages.remove (businessIndex)
                print (f"'{inputCode.upper()}' deleted successfully.")
                deleteMenu()
            else :
                print (f"Failed to delete '{inputCode.upper()}', back to menu.")
                deleteMenu()
        else:
            print ("The Business you're looking for is not found, back to menu")
            deleteMenu()

#==============================================================================================================================#

# F. EXIT MENU
def exitMenu():
    while True:
        answer = input("Are you sure want to exit the program? (Y/N): ").strip().lower()
        if answer =="y":
            print ("\n           -Thank you for using Yellow Pages, See you!-\n\n_________________________________________________________________") 
            exit ()
        elif answer =="n":
            print ("Canceling Exit, return to main menu.\n") 
            mainMenu ()
        else: 
            print("!!! Invalid answer. Please try again !!!\n")

###==========================================================================================================================###

# Database
yellowPages= [
    {
        "Code" : "BBCA",
        "Name" : "PT Bank Central Asia Tbk",
        "Phone" : "02123588000",
        "Website" : "www.bca.co.id",
        "Industry" : "Finance",
        "Address" : "Menara BCA, Grand Indonesia Jalan MH Thamrin No. 1 Jakarta 10310"
    },
    {
        "Code" : "BBRI",
        "Name" : "PT Bank Rakyat Indonesia (Persero) Tbk",
        "Phone" : "Finance",
        "Website" : "www.bri.co.id",
        "Industry" : "Banking",
        "Address" : "Gedung BRI I Lantai 20 Jl. Jenderal Sudirman Kav.44-46, Jakarta Pusat 10210"
    },
    {
        "Code" : "BBNI",
        "Name" : "PT Bank Negara Indonesia (Persero) Tbk",
        "Phone" : "Finance",
        "Website" : "www.bni.co.id",
        "Industry" : "Finance",
        "Address" : "Graha BNI Lantai 24 Jl. Jenderal Sudirman Kavling 1 Jakarta Pusat 10220"
    },
    {
        "Code" : "BRIS",
        "Name" : "PT Bank Syariah Indonesia Tbk",
        "Phone" : "02130405999",
        "Website" : "www.bankbsi.co.id",
        "Industry" : "Finance",
        "Address" : "Gedung The Tower, Jalan Gatot Subroto No.27, Kel. Karet Semanggi, Kec. Setiabudi, Jakarta Selatan 12930"
    },
    {
        "Code" : "ASII",
        "Name" : "Astra International Tbk",
        "Phone" : "02150843888",
        "Website" : "www.astra.co.id",
        "Industry" : "Industrials",
        "Address" : "Menara Astra Lt 58-63, Jl. Jendral Sudirman Kav 5-6, Jakarta 10220"
    },
    {
        "Code" : "TOTO",
        "Name" : "Surya Toto Indonesia Tbk",
        "Phone" : "02129298686",
        "Website" :"www.toto.co.id",
        "Industry" :"Industrials",
        "Address" : "Jl. Letjen S.Parman Kav 81, Kota Bambu Selatan, Pal Merah, Jakarta Barat, Jakarta 11420"
    },
    {
        "Code" : "AMFG",
        "Name" : "Asahimas Flat Glass Tbk",
        "Phone" : "0216904041",
        "Website" : "www.amfg.co.id",
        "Industry" : "Industrials",
        "Address" : "Jl. Ancol IX/5, Ancol Barat, Ancol-Pademangan Jakarta Utara-DKI Jakarta Raya 14430"
    },
    {
        "Code" : "HEXA",
        "Name" : "Hexindo Adiperkasa Tbk",
        "Phone" : "0214611688",
        "Website" : "www.hexindo.co.id",
        "Industry" : "Industrials",
        "Address" : "Jl. Pulo Kambing II Kav I & II/33, Jatinegara, Caking, Jakarta Timur, 13930"
    },
    {
        "Code" : "ADRO",
        "Name" : "Adaro Energy Indonesia Tbk",
        "Phone" : "02125533000",
        "Website" : "www.adaro.com",
        "Industry" : "Energy",
        "Address" : "Menara Karya 23rd Floor Jl. H.R. Rasuna Said, Block X-5, Kav. 1-2 Jakarta 12950"
    },
    {
        "Code" : "PGAS",
        "Name" : "PT Perusahaan Gas Negara Tbk",
        "Phone" : "0216334838",
        "Website" : "www.pgn.co.id",
        "Industry" : "Energy",
        "Address" : "Jl. KH. Zainul Arifin No. 20 Jakarta 11140"
    },
    {
        "Code" : "PTBA",
        "Name" : "Bukit Asam Tbk",
        "Phone" : "0215254014",
        "Website" : "www.ptba.co.id",
        "Industry" : "Energy",
        "Address" : "Menara Kadin Indonesia 15th Floor & 9th Floor Jl. HR Rasuna Said X-5, Kav 2& 3 Jakarta 12950"
    },
    {
        "Code" : "BUMI",
        "Name" : "Bumi Resources Tbk",
        "Phone" : "02157942080",
        "Website" :"www.bumires.com",
        "Industry" :"Energy",
        "Address" : "Bakrie Tower, Lt. 12 Complex Rasuna Epicentrum Jl. H.R. Rasuna Said Jakarta 12960"
    },
    {
        "Code" : "GOTO",
        "Name" : "PT GoTo Gojek Tokopedia Tbk",
        "Phone" : "0212910 1072",
        "Website" : "www.gotocompany.com",
        "Industry" : "Technology",
        "Address" : "Gedung Pasaraya Blok M, lantai 6-7 Jl. Iskandarsyah II No. 2, Jakarta 12160"
    },
    {
        "Code" : "BUKA",
        "Name" : "PT Bukalapak.com Tbk",
        "Phone" : "02150982008",
        "Website" : "www.bukalapak.com",
        "Industry" : "Technology",
        "Address" : "Metropolitan Tower, Lantai 22 Jalan Raden Adjeng Kartini, Kav. 14 Jakarta Selatan 12440"
    },
    {
        "Code" : "EMTK",
        "Name" : "Elang Mahkota Teknologi Tbk",
        "Phone" : "0217278 2066",
        "Website" : "www.emtek.co.id",
        "Industry" : "Technology",
        "Address" : "SCTV Tower, Lantai 18, Senayan City Jl. Asia Afrika Lot 19 Jakarta 10270"
    },
    {
        "Code" : "TFAS",
        "Name" : "PT Telefast Indonesia Tbk",
        "Phone" : "02129676236",
        "Website" : "www.telefast.co.id",
        "Industry" : "Technology",
        "Address" : "Mall Ambasador Lt. 5, No. 5 Jl. Prof. Dr. Satrio No. 65, Jakarta 12940"
    }
]

mainMenu() 