# UNIVERSAL FUNCTION
# A. Search business Index by code
def searchIndex (code):
    for business in yellowPages:
        if business ["Code"] == code.upper():
            return business
    return None  

# B. Print Business in detail
def printBusinessDetail (business):
    print(f"""
Code: {business['Code']}
Name: {business['Name']}
Phone: {business['Phone']}
Website: {business['Website']}
Industry: {business['Industry']}
Address: {business['Address']}
""")
    
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
            createMenu()
        elif answer == "3":
            updateMenu()
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
def createMenu():
    while True:
        print("\n_________________________________________________________________\n\n           - Add a New Business -\n")

#==============================================================================================================================#

# D. UPDATE MENU
def updateMenu():
    while True:
        print("\n_________________________________________________________________\n\n           - Update a Business -\n")
        answer= input("Enter the name of business you want to update: ")

#==============================================================================================================================#

# E. DELETE MENU
def deleteMenu():
    while True:
        print("\n_________________________________________________________________\n\n           - Delete a Business -\n")
        print("1. Delete a Business")
        print("2. Back to Main Menu")
        print("0. Exit\n")
        
        answer = input("Enter your answer (0-5): ")
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
            print ("Canceling Exit, return to main menu.\n\n_________________________________________________________________") 
            mainMenu ()
        else: 
            print("!!! Invalid answer. Please try again !!!\n")

###==========================================================================================================================###

# Dummy Database
yellowPages= [
    {
        "Code" : "BBCA",
        "Name" : "PT Bank Central Asia Tbk",
        "Phone" : "021-23588000",
        "Website" : "www.bca.co.id",
        "Industry" : "Banking",
        "Address" : "Menara BCA, Grand Indonesia Jalan MH Thamrin No. 1 Jakarta 10310"
    },
    {
        "Code" : "BBRI",
        "Name" : "PT Bank Rakyat Indonesia (Persero) Tbk",
        "Phone" : "021-5751966",
        "Website" : "www.bri.co.id",
        "Industry" : "Banking",
        "Address" : "Gedung BRI I Lantai 20 Jl. Jenderal Sudirman Kav.44-46, Jakarta Pusat 10210"
    },
    {
        "Code" : "BBNI",
        "Name" : "PT Bank Negara Indonesia (Persero) Tbk",
        "Phone" : "021-5728387",
        "Website" : "www.bni.co.id",
        "Industry" : "Banking",
        "Address" : "Graha BNI Lantai 24 Jl. Jenderal Sudirman Kavling 1 Jakarta Pusat 10220"
    },
    {
        "Code" : "BRIS",
        "Name" : "PT Bank Syariah Indonesia Tbk",
        "Phone" : "021-30405999",
        "Website" : "www.bankbsi.co.id",
        "Industry" : "Banking",
        "Address" : "Gedung The Tower, Jalan Gatot Subroto No.27, Kel. Karet Semanggi, Kec. Setiabudi, Jakarta Selatan 12930"
    },
    {
        "Code" : "ASII",
        "Name" : "Astra International Tbk",
        "Phone" : "021-50843888",
        "Website" : "www.astra.co.id",
        "Industry" : "Industrials",
        "Address" : "Menara Astra Lt 58-63, Jl. Jendral Sudirman Kav 5-6, Jakarta 10220"
    },
    {
        "Code" : "TOTO",
        "Name" : "Surya Toto Indonesia Tbk",
        "Phone" : "021-29298686",
        "Website" :"www.toto.co.id",
        "Industry" :"Industrials",
        "Address" : "Jl. Letjen S.Parman Kav 81, Kota Bambu Selatan, Pal Merah, Jakarta Barat, Jakarta 11420"
    },
    {
        "Code" : "AMFG",
        "Name" : "Asahimas Flat Glass Tbk",
        "Phone" : "021-6904041",
        "Website" : "www.amfg.co.id",
        "Industry" : "Industrials",
        "Address" : "Jl. Ancol IX/5, Ancol Barat, Ancol-Pademangan Jakarta Utara-DKI Jakarta Raya 14430"
    },
    {
        "Code" : "HEXA",
        "Name" : "Hexindo Adiperkasa Tbk",
        "Phone" : "021-4611688",
        "Website" : "www.hexindo.co.id",
        "Industry" : "Industrials",
        "Address" : "Jl. Pulo Kambing II Kav I & II/33, Jatinegara, Caking, Jakarta Timur, 13930"
    },
    {
        "Code" : "ADRO",
        "Name" : "Adaro Energy Indonesia Tbk",
        "Phone" : "021-25533000",
        "Website" : "www.adaro.com",
        "Industry" : "Energy",
        "Address" : "Menara Karya 23rd Floor Jl. H.R. Rasuna Said, Block X-5, Kav. 1-2 Jakarta 12950"
    },
    {
        "Code" : "PGAS",
        "Name" : "PT Perusahaan Gas Negara Tbk",
        "Phone" : "021-6334838",
        "Website" : "www.pgn.co.id",
        "Industry" : "Energy",
        "Address" : "Jl. KH. Zainul Arifin No. 20 Jakarta 11140"
    },
    {
        "Code" : "PTBA",
        "Name" : "Bukit Asam Tbk",
        "Phone" : "021-5254014",
        "Website" : "www.ptba.co.id",
        "Industry" : "Energy",
        "Address" : "Menara Kadin Indonesia 15th Floor & 9th Floor Jl. HR Rasuna Said X-5, Kav 2& 3 Jakarta 12950"
    },
    {
        "Code" : "BUMI",
        "Name" : "Bumi Resources Tbk",
        "Phone" : "021-57942080",
        "Website" :"www.bumires.com",
        "Industry" :"Energy",
        "Address" : "Bakrie Tower, Lt. 12 Complex Rasuna Epicentrum Jl. H.R. Rasuna Said Jakarta 12960"
    },
    {
        "Code" : "GOTO",
        "Name" : "PT GoTo Gojek Tokopedia Tbk",
        "Phone" : "021-2910 1072",
        "Website" : "www.gotocompany.com",
        "Industry" : "Technology",
        "Address" : "Gedung Pasaraya Blok M, lantai 6-7 Jl. Iskandarsyah II No. 2, Jakarta 12160"
    },
    {
        "Code" : "BUKA",
        "Name" : "PT Bukalapak.com Tbk",
        "Phone" : "021-50982008",
        "Website" : "www.bukalapak.com",
        "Industry" : "Technology",
        "Address" : "Metropolitan Tower, Lantai 22 Jalan Raden Adjeng Kartini, Kav. 14 Jakarta Selatan 12440"
    },
    {
        "Code" : "EMTK",
        "Name" : "Elang Mahkota Teknologi Tbk",
        "Phone" : "021-7278 2066",
        "Website" : "www.emtek.co.id",
        "Industry" : "Technology",
        "Address" : "SCTV Tower, Lantai 18, Senayan City Jl. Asia Afrika Lot 19 Jakarta 10270"
    },
    {
        "Code" : "TFAS",
        "Name" : "PT Telefast Indonesia Tbk",
        "Phone" : "021-29676236",
        "Website" : "www.telefast.co.id",
        "Industry" : "Technology",
        "Address" : "Mall Ambasador Lt. 5, No. 5 Jl. Prof. Dr. Satrio No. 65, Jakarta 12940"
    }
]

mainMenu() 