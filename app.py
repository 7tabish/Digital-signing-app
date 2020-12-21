from tkinter import *
import test
import reportGenerator
import tkinter.font as tkFont



fullName_=None
empfullName_=None
workHrsEmpFullName=None
employeDeclarationDetail=None
employeThanksWindow=None
completeAll=False
checkedJobOption=None
studentLoanOption=None
def open_DOB():
    if len(txt_fullname.get("1.0",'end-1c'))==0:
        lbl_emp_error['text']='Fullname cannot be empty.'
        return

    lbl_fullname.pack_forget()
    txt_fullname.pack_forget()
    btn_fullname_next.pack_forget()
    lbl_emp_error['text']=''

    lbl_DOB.pack()
    txt_DOB.pack()
    btn_DOB_next.pack(side=BOTTOM, pady=10, padx=10)

def open_gender():
    if len(txt_DOB.get("1.0",'end-1c'))==0:
        lbl_emp_error['text']='DOB cannot be empty.'
        return
    lbl_DOB.pack_forget()
    txt_DOB.pack_forget()
    btn_DOB_next.pack_forget()
    lbl_emp_error['text'] = ''

    lbl_gender.pack()
    txt_gender.pack()
    btn_gender_next.pack(side=BOTTOM, pady=10, padx=10)

def open_title():
    lbl_gender.pack_forget()
    txt_gender.pack_forget()
    btn_gender_next.pack_forget()

    lbl_title.pack()
    txt_title.pack()
    btn_title_next.pack(side=BOTTOM, pady=10, padx=10)

def open_mobile():
    if len(txt_title.get("1.0",'end-1c'))==0:
        lbl_emp_error['text']='Title cannot be empty.'
        return
    lbl_title.pack_forget()
    txt_title.pack_forget()
    btn_title_next.pack_forget()
    lbl_emp_error['text'] = ''

    lbl_mobile_no.pack()
    txt_mobile_no.pack()
    btn_mobile_next.pack(side=BOTTOM, pady=10, padx=10)

def open_telephone():
    lbl_mobile_no.pack_forget()
    txt_mobile_no.pack_forget()
    btn_mobile_next.pack_forget()

    lbl_telephone_no.pack()
    txt_telephone_no.pack()
    btn_telephone_next.pack(side=BOTTOM, pady=10, padx=10)

def open_email():
    if len(txt_telephone_no.get("1.0", 'end-1c')) == 0:
        lbl_emp_error['text'] = 'Telephone no cannot be empty.'
        return
    lbl_telephone_no.pack_forget()
    txt_telephone_no.pack_forget()
    btn_telephone_next.pack_forget()
    lbl_emp_error['text'] = ''

    lbl_email.pack()
    txt_email.pack()
    btn_email_next.pack(side=BOTTOM, pady=10, padx=10)

def open_passport():
    if len(txt_email.get("1.0", 'end-1c')) == 0:
        lbl_emp_error['text'] = 'Email  cannot be empty.'
        return
    lbl_email.pack_forget()
    txt_email.pack_forget()
    btn_email_next.pack_forget()
    lbl_emp_error['text'] = ''

    lbl_passport_no.pack()
    txt_passport_no.pack()
    btn_passport_next.pack(side=BOTTOM, pady=10, padx=10)

def open_NI():
    lbl_passport_no.pack_forget()
    txt_passport_no.pack_forget()
    btn_passport_next.pack_forget()

    lbl_NI_no.pack()
    txt_NI_no.pack()
    btn_NI_next.pack(side=BOTTOM, pady=10, padx=10)

def open_rightToWorkCode():
    lbl_NI_no.pack_forget()
    txt_NI_no.pack_forget()
    btn_NI_next.pack_forget()

    lbl_rightToWorkCode.pack()
    txt_rightToWorkCode.pack()
    btn_rightToWorkCode_next.pack(side=BOTTOM, pady=10, padx=10)

def open_adress():
    lbl_rightToWorkCode.pack_forget()
    txt_rightToWorkCode.pack_forget()
    btn_rightToWorkCode_next.pack_forget()

    lbl_adress.pack()
    txt_adress.pack()
    btn_adress_next.pack(side=BOTTOM, pady=10, padx=10)



def get_employe_detail():
    global fullName_,workHrsEmpFullName
    fullName_=txt_fullname.get("1.0", 'end-1c')
    workHrsEmpFullName=fullName_
    DOB=txt_DOB.get("1.0", 'end-1c')
    gender=txt_gender.get("1.0", 'end-1c')
    title=txt_title.get("1.0", 'end-1c')
    mobile_no=txt_mobile_no.get("1.0", 'end-1c')
    telephone_no=txt_telephone_no.get("1.0", 'end-1c')
    email=txt_email.get("1.0", 'end-1c')
    passport_no=txt_passport_no.get("1.0", 'end-1c')
    NI_no=txt_NI_no.get("1.0", 'end-1c')
    rightToWorkCode=txt_rightToWorkCode.get("1.0", 'end-1c')
    adress=txt_adress.get("1.0", 'end-1c')

    #emergency detail
    emergName=txt_emergencyName.get("1.0", 'end-1c')
    emergRelation=txt_emerRelation.get("1.0", 'end-1c')
    emergTel=txt_emergencyTel.get("1.0", 'end-1c')
    emergMob=txt_emergencyMob.get("1.0", 'end-1c')


    #bank detail
    bankName=txt_emergencyMob.get("1.0", 'end-1c')
    accountNo = txt_accountNo.get("1.0", 'end-1c')
    sortCode= txt_sortCode.get("1.0", 'end-1c')
    accountName = txt_accountName.get("1.0", 'end-1c')

    #write data to pdf

    test.create_pdf(fullName_,DOB,gender,title,telephone_no,mobile_no,email,passport_no,NI_no,rightToWorkCode,adress,emergName,emergRelation,emergTel,emergMob,bankName,accountNo,sortCode,accountName)


def emplopye_thanks_message():

    employeBankFormWindow.destroy()
    employeEmergencyFormWindow.destroy()
    employeStarterFormWindow.destroy()
    global employeThanksWindow
    employeThanksWindow=Tk()
    employeThanksWindow.title("Thanks")
    lucidaGrande = tkFont.Font(family="Lucida Grande", size=12)
    employeThanksWindow.resizable(0,0)
    empThankFrame=Frame(employeThanksWindow,bg='white')
    empThankFrame.pack()
    label=Label(empThankFrame,text="""
  Thank you. This information has been submitted successfully / Ευχαριστώ. Αυτές οι πληροφορίες έχουν υποβληθεί με επιτυχία / Mulțumesc. Această informație a fost trimisă cu succes.
    """,fg='black',bg='white',font=lucidaGrande)
    label.pack()
    btn_continue=Button(empThankFrame,text='Continue',bg='dodgerblue',fg='white',command=new_employe_declaration,font=lucidaGrande)
    btn_continue.pack()
    empThankFrame.mainloop()


def validate_bank_form():
    if len(txt_bankname.get("1.0", 'end-1c'))==0 or len(txt_accountNo.get("1.0", 'end-1c'))==0 or len(txt_sortCode.get("1.0", 'end-1c'))==0 or len(txt_accountName.get("1.0", 'end-1c'))==0:
        lbl_bank_error['text']='All fields are required.'
        return
    lbl_bank_error['text']=''
    get_employe_detail()
    employeBankFormWindow.withdraw()
    emplopye_thanks_message()

def open_bank_form():
    employeEmergencyFormWindow.withdraw()
    global employeBankFormWindow
    employeBankFormWindow=Tk()
    employeBankFormWindow.resizable(0,0)
    employeBankFormWindow.title("Bank details")
    lucidaGrande = tkFont.Font(family="Lucida Grande", size=12)
    employeBankFormFrame=Frame(employeBankFormWindow)
    employeBankFormFrame.pack()
    global lbl_bank_error
    lbl_bank_error=Label(employeBankFormFrame,text='',fg='red',font=lucidaGrande)
    lbl_bank_error.pack()

    lbl_title=Label(employeBankFormFrame,text='Bank Details \n Στοιχεία τράπεζας \n Detalii bancare ',font=lucidaGrande)
    lbl_title.pack()

    lbl_bankname = Label(employeBankFormFrame,text='Bank name \n  όνομα τράπεζας \n Numele băncii “REQUIRED',font=lucidaGrande)
    lbl_bankname.pack()
    global txt_bankname
    txt_bankname = Text(employeBankFormFrame, height=1, width=35,font=lucidaGrande)
    txt_bankname.pack()

    lbl_accountNo = Label(employeBankFormFrame, text='Account number \n  Αριθμός λογαριασμού \n Numar de cont “REQUIRED',font=lucidaGrande)
    lbl_accountNo.pack()
    global txt_accountNo
    txt_accountNo = Text(employeBankFormFrame, height=1, width=35,font=lucidaGrande)
    txt_accountNo.pack()


    lbl_sortCode = Label(employeBankFormFrame,text='Sort code \n Κωδικός είδους \n Cod de sortare “REQUIRED',font=lucidaGrande)
    lbl_sortCode.pack()
    global txt_sortCode
    txt_sortCode = Text(employeBankFormFrame, height=1, width=35,font=lucidaGrande)
    txt_sortCode.pack()

    lbl_accountName = Label(employeBankFormFrame, text='Account name \n Ονομα λογαριασμού \n Nume de cont “REQUIRED',font=lucidaGrande)
    lbl_accountName.pack()
    global txt_accountName
    txt_accountName = Text(employeBankFormFrame, height=1, width=35,font=lucidaGrande)
    txt_accountName.pack()


    btn_complete = Button(employeBankFormFrame, text='Complete', bg='dodgerblue', fg='white', height=2,width=9,command=validate_bank_form,font=lucidaGrande)
    btn_complete.pack(side=BOTTOM, pady=10, padx=10)
    employeBankFormWindow.geometry("920x450")
    employeBankFormWindow.mainloop()





def open_emergency_form():
    if len(txt_adress.get("1.0", 'end-1c')) == 0:
        lbl_emp_error['text'] = 'Adress  cannot be empty.'
        return
    lbl_emp_error['text'] = ''
    employeStarterFormWindow.withdraw()
    global employeEmergencyFormWindow
    employeEmergencyFormWindow=Tk()
    lucidaGrande = tkFont.Font(family="Lucida Grande", size=12)
    employeEmergencyFormWindow.title("Emergency contact detail")
    employeEmergencyFormWindow.resizable(0,0)
    employeEmergencyFormFrame=Frame(employeEmergencyFormWindow)
    employeEmergencyFormFrame.pack()
    lbl_title=Label(employeEmergencyFormFrame,text='Contact Information (in case of emergency) \n Στοιχεία επικοινωνίας (σε περίπτωση έκτακτης ανάγκης) \n Informații de contact (în caz de urgență) ',font=lucidaGrande)
    lbl_title.pack()

    lbl_emergencyName=Label(employeEmergencyFormFrame,text='Name of person to contact \n Όνομα ατόμου για επαφή \n Numele persoanei de contact ',font=lucidaGrande)
    lbl_emergencyName.pack()
    global txt_emergencyName
    txt_emergencyName=Text(employeEmergencyFormFrame,height=1,width=35,font=lucidaGrande)
    txt_emergencyName.pack()

    lbl_emerRelation=Label(employeEmergencyFormFrame,text='Relationship to you \n Σχέση με εσάς \n Relatia cu tine',font=lucidaGrande)
    lbl_emerRelation.pack()
    global txt_emerRelation
    txt_emerRelation=Text(employeEmergencyFormFrame,height=1,width=35,font=lucidaGrande)
    txt_emerRelation.pack()

    lbl_emergencyTel=Label(employeEmergencyFormFrame,text='Telephone \n Τηλέφωνο \n Telefon',font=lucidaGrande)
    lbl_emergencyTel.pack()
    global txt_emergencyTel
    txt_emergencyTel=Text(employeEmergencyFormFrame,height=1,width=35,font=lucidaGrande)
    txt_emergencyTel.pack()


    lbl_EmergencyMob=Label(employeEmergencyFormFrame,text='Mobile \n Κινητό \nMobil',font=lucidaGrande)
    lbl_EmergencyMob.pack()
    global txt_emergencyMob
    txt_emergencyMob=Text(employeEmergencyFormFrame,height=1,width=35,font=lucidaGrande)
    txt_emergencyMob.pack()

    btn_emerg_next = Button(employeEmergencyFormFrame, text='Next', bg='dodgerblue', fg='white', height=1,command=open_bank_form,font=lucidaGrande)
    btn_emerg_next.pack(side=BOTTOM, pady=10, padx=10)

    employeEmergencyFormWindow.geometry("920x450")
    employeEmergencyFormWindow.mainloop()


def new_employe_starter_form_window():
    #destroy the previous form
    employeStarterMainWindow.destroy()
    global employeStarterFormWindow
    employeStarterFormWindow = Tk()
    employeStarterFormWindow.title('New employee registration')
    employeStarterFormWindow.resizable(0,0)
    global employeStarterframe
    lucidaGrande = tkFont.Font(family="Lucida Grande", size=12)
    employeStarterframe=Frame(employeStarterFormWindow)
    employeStarterframe.pack()

    global lbl_emp_error
    lbl_emp_error=Label(employeStarterframe,text='',fg='red',font=lucidaGrande)
    lbl_emp_error.pack()
    global lbl_fullname
    lbl_fullname=Label(employeStarterframe,text='Please enter your full name \n Παρακαλώ εισάγετε το πλήρες όνομά σας \n Te rog sa introduci numele complet',font=lucidaGrande)
    lbl_fullname.pack()
    global txt_fullname
    txt_fullname=Text(employeStarterframe,height=1,width=35,font=lucidaGrande)
    txt_fullname.pack()
    global btn_fullname_next
    btn_fullname_next = Button(employeStarterframe, text='Next (DOB)', bg='dodgerblue', fg='white', height=1,command=open_DOB,font=lucidaGrande)
    btn_fullname_next.pack(side=BOTTOM, pady=10, padx=10)

    #defining widgets only from step 1 to step 12 but show only 1 at a time on screen

    #for date of birth
    global lbl_DOB
    lbl_DOB = Label(employeStarterframe, text='Please enter your date of birth \n Παρακαλώ εισάγετε την ημερομηνία γεννήσεως σας \n Vă rugăm să introduceți data dvs. de naștere “REQUIRED',font=lucidaGrande)
    global txt_DOB
    txt_DOB = Text(employeStarterframe, height=1,width=35,font=lucidaGrande)
    global btn_DOB_next
    btn_DOB_next = Button(employeStarterframe, text='Next (gender)', bg='dodgerblue', fg='white', height=1,command=open_gender,font=lucidaGrande)

    #for gender
    global lbl_gender
    lbl_gender = Label(employeStarterframe,text='Please enter your gender \n Εισαγάγετε το φύλο σας  \n Vă rugăm să introduceți genul',font=lucidaGrande)
    global txt_gender
    txt_gender=Text(employeStarterframe,height=1,width=35,font=lucidaGrande)

    global btn_gender_next
    btn_gender_next = Button(employeStarterframe, text='Next (Title)', bg='dodgerblue', fg='white', height=1,command=open_title,font=lucidaGrande)


    #for title (MR, MRS ..)
    global lbl_title
    lbl_title = Label(employeStarterframe, text='Please enter your title (Mr, Mrs, Miss, Ms, Other) \n Εισαγάγετε τον τίτλο σας (κ., Κυρία, δεσποινίς, κα, άλλο) \n Vă rugăm să introduceți titlul dvs. (dle, doamnă, domnișoară, doamnă, altele)',font=lucidaGrande)
    global txt_title
    txt_title = Text(employeStarterframe, height=1, width=35,font=lucidaGrande)
    global btn_title_next
    btn_title_next = Button(employeStarterframe, text='Next (Mobile no)', bg='dodgerblue', fg='white', height=1,command=open_mobile,font=lucidaGrande)

    #for mobile no
    global lbl_mobile_no
    lbl_mobile_no = Label(employeStarterframe, text='“Please enter your mobile telephone number \n Εισαγάγετε τον αριθμό του κινητού σας τηλεφώνου \n Vă rugăm să introduceți numărul dvs. de telefon mobil ',font=lucidaGrande)
    global txt_mobile_no
    txt_mobile_no = Text(employeStarterframe, height=1, width=35,font=lucidaGrande)
    global btn_mobile_next
    btn_mobile_next = Button(employeStarterframe, text='Next (Telephone)', bg='dodgerblue',font=lucidaGrande, fg='white', height=1,command=open_telephone)


    # for telephone
    global lbl_telephone_no
    lbl_telephone_no = Label(employeStarterframe, text='Please enter your telephone number \n Εισαγάγετε τον αριθμό τηλεφώνου σας \n Vă rugăm să introduceți numărul dvs. de telefon',font=lucidaGrande)
    global txt_telephone_no
    txt_telephone_no = Text(employeStarterframe, height=1, width=35,font=lucidaGrande)
    global btn_telephone_next
    btn_telephone_next = Button(employeStarterframe, text='Next (Email)', bg='dodgerblue', fg='white', height=1,command=open_email,font=lucidaGrande)

    #for email
    global lbl_email
    lbl_email = Label(employeStarterframe, text='Please enter your email address \n Παρακαλώ εισάγετε τη διεύθυνση ηλεκτρονικού ταχυδρομείου σας \n Vă rugăm să introduceți adresa dvs. de e-mail',font=lucidaGrande)
    global txt_email
    txt_email = Text(employeStarterframe, height=1, width=35,font=lucidaGrande)
    global btn_email_next
    btn_email_next = Button(employeStarterframe, text='Next (Passport no)', bg='dodgerblue', fg='white', height=1,command=open_passport,font=lucidaGrande)

    # for passort no
    global lbl_passport_no
    lbl_passport_no = Label(employeStarterframe, text='Please enter your passport number (if you do not have it with you, leave blank) \n Εισαγάγετε τον αριθμό διαβατηρίου σας (εάν δεν το έχετε μαζί σας, αφήστε κενό) \n Vă rugăm să introduceți numărul pașaportului (dacă nu îl aveți cu dvs., lăsați necompletat)',font=lucidaGrande)
    global txt_passport_no
    txt_passport_no = Text(employeStarterframe, height=1, width=35,font=lucidaGrande)
    global btn_passport_next
    btn_passport_next = Button(employeStarterframe, text='Next (NI no)', bg='dodgerblue', fg='white', height=1,command=open_NI,font=lucidaGrande)

    # for NI_no
    global lbl_NI_no
    lbl_NI_no = Label(employeStarterframe, text='Please enter your NI number (if you do not have it with you, leave blank) \n Εισαγάγετε τον αριθμό NI (εάν δεν τον έχετε μαζί σας, αφήστε κενό) \n Vă rugăm să introduceți numărul dvs. NI (dacă nu îl aveți cu dvs., lăsați necompletat)',font=lucidaGrande)

    global txt_NI_no
    txt_NI_no = Text(employeStarterframe, height=1, width=35,font=lucidaGrande)
    global btn_NI_next
    btn_NI_next = Button(employeStarterframe, text='Next (Right to work code)', bg='dodgerblue', fg='white', height=1,command=open_rightToWorkCode,font=lucidaGrande)

    # for rightToWorkCode
    global lbl_rightToWorkCode
    lbl_rightToWorkCode = Label(employeStarterframe, text='Please supply your right to work share code (ignore if you are an EU, EEA or Swiss citizen) \n Καταχωρίστε τον κωδικό μεριδίου εργασίας σας (αγνοήστε εάν είστε πολίτης της ΕΕ, του ΕΟΧ ή της Ελβετίας) \n Vă rugăm să vă furnizați codul de partajare a dreptului la muncă (ignorați dacă sunteți cetățean UE, SEE sau Elvețian)',font=lucidaGrande)
    global txt_rightToWorkCode
    txt_rightToWorkCode = Text(employeStarterframe, height=1, width=35,font=lucidaGrande)

    global btn_rightToWorkCode_next
    btn_rightToWorkCode_next = Button(employeStarterframe, text='Next (Adress)', bg='dodgerblue', fg='white', height=1,command=open_adress,font=lucidaGrande)

    # for adress
    global lbl_adress
    lbl_adress = Label(employeStarterframe, text='Please enter your address \n Εισαγάγετε τη διεύθυνσή σας \n Vă rugăm să introduceți adresa dvs.',font=lucidaGrande)
    global txt_adress
    txt_adress = Text(employeStarterframe, height=1, width=35,font=lucidaGrande)

    global btn_adress_next
    btn_adress_next = Button(employeStarterframe, text='Next', bg='dodgerblue', fg='white', height=1,command=open_emergency_form,font=lucidaGrande)

    employeStarterFormWindow.geometry("600x200")
    employeStarterFormWindow.mainloop()





def new_employe_starter_main_window():
    global completeAll
    completeAll=True
    welcomeWindow.withdraw()

    #create new windows for new_employe_starter_window
    global employeStarterMainWindow
    employeStarterMainWindow=Tk()
    employeStarterMainWindow.title('New employee registration')
    lucidaGrande = tkFont.Font(family="Lucida Grande", size=12)
    employeStarterMainWindow.resizable(0,0)
    frame=Frame(employeStarterMainWindow,bg='white')
    frame.pack()
    lbl_description=Label(frame,text='\nTo complete this, you’ll need: Your email address, your passport number, your national insurance number (if applicable) and your bank details. Ready to complete?'
                                     '\n\nΓια να το ολοκληρώσετε, θα χρειαστείτε: τη διεύθυνση email σας, τον αριθμό διαβατηρίου σας, τον εθνικό αριθμό ασφάλισης (εάν ισχύει) και τα στοιχεία της τράπεζάς σας.'
                                     '\nΈτοιμο να ολοκληρωθεί'
                                     '\n\nPentru a finaliza acest lucru, veți avea nevoie de: adresa dvs. de e-mail, numărul pașaportului, numărul dvs. național de asigurare (dacă este cazul) și datele bancare.'
                                     '\nGata de finalizare?',font=lucidaGrande,bg='white')
    lbl_description.pack()

    btn_continue=Button(frame,text='Cotinue',bg='dodgerblue',fg='white',height=2,width=10,command=new_employe_starter_form_window)
    btn_continue.pack(side=RIGHT,pady=10,padx=10)

    btn_quit = Button(frame, text='Quit', bg='grey', fg='white',height=2,width=10)
    btn_quit.pack(side=RIGHT, pady=10, padx=10)
    employeStarterMainWindow.mainloop()
def open_workingHrs_opt():
    newEmpThanksMessageWindow.destroy()
    working_hrs_main()

def new_employe_thanks_message():
    print('new empoye thankls')
    global newEmpThanksMessageWindow
    newEmpThanksMessageWindow=Tk()
    newEmpThanksMessageWindow.title("Thanks")
    lucidaGrande_bold = tkFont.Font(family="Lucida Grande", size=12,weight="bold")

    newEmpThanksMessageWindow.resizable(0,0)
    frame=Frame(newEmpThanksMessageWindow,bg="white")
    frame.pack()
    lbl_thanks_msg=Label(frame,text='Thank you. This information has been submitted successfully / Ευχαριστώ. Αυτές οι πληροφορίες έχουν υποβληθεί με επιτυχία / Mulțumesc. Această informație a fost trimisă cu succes',font=lucidaGrande_bold,bg="white").pack()

    if completeAll:
        btn_Continue=Button(frame,text='Continue',fg='white',bg='dodgerblue',command=open_workingHrs_opt,font=lucidaGrande_bold).pack()
    else:
        btn_Close = Button(frame, text='Close', fg='white', bg='grey', command=lambda :newEmpThanksMessageWindow.destroy(),font=lucidaGrande_bold).pack()
    newEmpThanksMessageWindow.mainloop()



import signing
def open_canvas():
    #dismiss the previous window open the canvas
    print('in canvas')
    selectedStudentPlan=None
    if studentLoanOption is not None:
        selectedStudentPlan=studentPlan.get()
        studentLoanOption.destroy()
    else:
        dialougeP45.destroy()
        employeDeclarationOption.destroy()
    signing.canvasSign()
    if fullName_ is None:
        reportGenerator.create_employe_declaration_form(checkedJobOption, selectedStudentPlan,empfullName_)
    else:
        reportGenerator.create_employe_declaration_form(checkedJobOption, selectedStudentPlan, fullName_)
    new_employe_thanks_message()




def open_p45_dialouge():
    global dialougeP45
    dialougeP45=Tk()
    lucidaGrande = tkFont.Font(family="Lucida Grande", size=12)
    dialougeP45.resizable(0,0)
    frame=Frame(dialougeP45)
    frame.pack()
    lbl_heading=Label(frame,
                      text='Please supply your P45 to us by emailing it to gpw@goinggreek.co.uk. If you can’t do it now, please make a note of this for later.\n If you do not supply your P45, we are required to apply an ‘emergency tax’ code, which may mean you pay more tax than you need to. If there’s any reason why you can’t supply this, please notify us by emailing gpw@goinggreek.co.uk.\n'
                           '\n Παρακαλώ δώστε το P45 σας σε εμάς μέσω email στο gpw@goinggreek.co.uk. Εάν δεν μπορείτε να το κάνετε τώρα, σημειώστε το για αργότερα. Εάν δεν παρέχετε το P45 σας, πρέπει να εφαρμόσουμε\n έναν κωδικό «φόρου έκτακτης ανάγκης», ο οποίος μπορεί να σημαίνει ότι πληρώνετε περισσότερο φόρο από ό, τι χρειάζεστε. Εάν υπάρχει κάποιος λόγος για τον οποίο δεν μπορείτε να το παρέχετε, ενημερώστε μας μέσω email στο gpw@goinggreek.co.uk. \n'
                           '\n Vă rugăm să ne furnizați P45-ul dvs. prin e-mail la gpw@goinggreek.co.uk. Dacă nu o puteți face acum, vă rugăm să notați acest lucru pentru mai târziu. Dacă nu furnizați P45, trebuie să aplicăm un cod „impozit de urgență”,\n ceea ce poate însemna că plătiți mai mult impozit decât trebuie. Dacă există vreun motiv pentru care nu puteți furniza acest lucru, vă rugăm să ne anunțați prin e-mail gpw@goinggreek.co.uk.”',font=lucidaGrande).pack()
    btn_continue=Button(frame,text='Continue',fg='white',bg='dodgerblue',command=open_canvas,font=lucidaGrande).pack()
    dialougeP45.mainloop()

def open_studentLoan_option():
    print('in loan option')
    global checkedJobOption
    checkedJobOption=int(question1.get())
    employeDeclarationOption.destroy()
    #if user select radio button 1 from open_employeDec_option then this will run
    global studentLoanOption
    studentLoanOption=Tk()
    lucidaGrande = tkFont.Font(family="Lucida Grande", size=12)
    studentLoanOption.resizable(0,0)
    frame1=Frame(studentLoanOption).pack()
    global studentPlan
    studentPlan = StringVar(frame1, "1")

    global rd_plan1,rd_plan2
    rd_plan1=Radiobutton(frame1,text='Plan 1 / Σχέδιο 1 / Planul 1',variable=studentPlan,value='1',font=lucidaGrande).pack()
    rd_plan2 = Radiobutton(frame1, text='Plan 2 / Σχέδιο 2 / Planul 2',variable=studentPlan,value='2',font=lucidaGrande).pack()
    btn_continue=Button(frame1,text='Continue',bg='dodgerblue',fg='white',command=open_canvas,font=lucidaGrande).pack()
    studentLoanOption.geometry("500x200")
    studentLoanOption.mainloop()



def validate_empDec_option():
    print("Selected job option is ",question1.get())
    if question1.get()=="2" or question1.get()=="3":
        # get the selected radio button if 2nd and 3rd are selected then show one static dialouge box and move to canvas else show student plan
        open_p45_dialouge()

    if question1.get()=="1":
        open_studentLoan_option()





def open_employeDec_option():
    if fullName_ is None:
        if len(txt_empFullName.get("1.0", 'end-1c'))==0:
            lbl_emp_error['text']='Fullname is required'
            return
        global empfullName_
        empfullName_=txt_empFullName.get("1.0", 'end-1c')
        print('name is ',empfullName_)

    if employeDeclarationDetail is not None:
        print('destroy employe declaration ')
        employeDeclarationDetail.destroy()

    global employeDeclarationOption
    employeDeclarationOption=Tk()
    lucidaGrande_bold = tkFont.Font(family="Lucida Grande", size=12,weight="bold")
    lucidaGrande = tkFont.Font(family="Lucida Grande", size=12)
    employeDeclarationOption.resizable(0,0)
    frame=Frame(employeDeclarationOption)
    frame.pack()
    lbl_heading=Label(frame,text='Tick one of the following three statements'
                                '\nΕπιλέξτε μία από τις ακόλουθες τρεις δηλώσεις.'
                                '\n Bifați una dintre următoarele trei afirmații',font=lucidaGrande_bold)
    lbl_heading.pack()

    #defingin radio buytton
    global question1
    question1 = StringVar(frame, "1")
    global rd_1,rd_2,rd_3
    rd_1=Radiobutton(frame,text='This is my first job since last 6 April and I have not been receiving taxable Jobseeker’s Allowance, Employment and Support Allowance, taxable Incapacity Benefit, State or Occupational Pension.'
                                '\n\nΑυτή είναι η πρώτη μου δουλειά από τις 6 Απριλίου και δεν έχω λάβει φορολογητέο Επίδομα Εύρεσης Εργασίας, Επίδομα Απασχόλησης και Υποστήριξης, φορολογητέα Παροχή Ανικανότητας, Κρατική ή Επαγγελματική Σύνταξη.'
                                '\n\nAcesta este primul meu loc de muncă incepand cu data de 6 aprilie  anului trecut și nu primesc indemnizație impozabilă, indemnizație de angajare și ajutor, solicitare de incapacitate, pensie de stat sau de muncă.',variable=question1, value="1",font=lucidaGrande).pack()

    rd_2=Radiobutton(frame,text='This is now my only job but since last 6 April I have had another job, or received taxable Jobseeker’s Allowance, Employment and Support Allowance, taxable incapacity Benefit.'
                                '\n I do not receive a state or Occupational Pension.'
                                '\nΑυτή είναι τώρα η μόνη δουλειά μου, αλλά από τις 6 Απριλίου έχω εργαστεί και σε άλλη δουλειά ή έχω λάβει φορολογητέο Επίδομα Εύρεσης Εργασίας, Επίδομα Απασχόλησης και Υποστήριξης, φορολογητέα Παροχή Ανικανότητας.'
                                '\n Δεν λαμβάνω κρατική ή επαγγελματική σύνταξη.'
                                '\nAcesta este acum singurul meu loc de muncă, dar începând cu data de 6 aprilie a anului trecut, am mai avut un alt loc de muncă sau am primit Indemnizația, angajarea și sprijinul impozabilului solicitantului, Indemnizația de incapacitate impozabilă. '
                                '\n Nu primesc o pensie de stat sau de muncă.',variable=question1,value="2",font=lucidaGrande).pack()

    rd_3=Radiobutton(frame,text='As well as my new job, I have another job or receive a State or Occupational Pension.'
                                '\n\nΕκτός από τη νέα μου δουλειά, έχω κι άλλη δουλειά ή λαμβάνω κρατική ή επαγγελματική σύνταξη.'
                                '\n\nInafara de noul meu loc de muncă, mai am un alt loc de muncă sau primesc o pensie de stat sau de muncă.',variable=question1,value="3",font=lucidaGrande).pack()
    btn_continue=Button(frame,text='Continue',width=7,height=1,bg='dodgerblue',fg='white',command=validate_empDec_option,font=lucidaGrande).pack()
    employeDeclarationOption.mainloop()


def employe_declaration_detail():
    newEmployeDeclarationWindow.destroy()
    if fullName_ is None:
        global employeDeclarationDetail
        employeDeclarationDetail=Tk()
        employeDeclarationDetail.title("New employe declaration")
        lucidaGrande = tkFont.Font(family="Lucida Grande", size=12)
        employeDeclarationDetail.resizable(0,0)
        empDeclFrame=Frame(employeDeclarationDetail)
        empDeclFrame.pack()
        global lbl_emp_error
        lbl_emp_error=Label(empDeclFrame,text='',fg='red',font=lucidaGrande)
        lbl_emp_error.pack()

        # if len(txt_fullname.get("1.0", 'end-1c'))==0:
        lbl_empFullname=Label(empDeclFrame,text='Enter fullname',font=lucidaGrande)
        lbl_empFullname.pack()
        global txt_empFullName
        txt_empFullName=Text(empDeclFrame,height=1, width=35,font=lucidaGrande)
        txt_empFullName.pack()
        btn_continue=Button(empDeclFrame,text='Continue',command=open_employeDec_option,font=lucidaGrande)
        btn_continue.pack()
        employeDeclarationDetail.geometry("500x200")
        employeDeclarationDetail.mainloop()
    else:
        open_employeDec_option()



def new_employe_declaration():
    if welcomeWindow is not None:
        welcomeWindow.destroy()
    if employeThanksWindow is not None:
        employeThanksWindow.destroy()


    global newEmployeDeclarationWindow
    newEmployeDeclarationWindow=Tk()
    lucidaGrande = tkFont.Font(family="Lucida Grande", size=12)
    newEmployeDeclarationWindow.title("New employe declaration")

    newEmployeDeclarationWindow.resizable(0,0)
    frame= Frame(newEmployeDeclarationWindow,bg='white')
    frame.pack()
    global lbl_empDeclaration
    lbl_empDeclaration=Label(frame,text='We are required by law to obtain your tax information before we can pay you. The following questions must be completed to avoid any delay in your payments.'
                                        '\n Απαιτείται από το νόμο να λάβουμε τα φορολογικά σας στοιχεία για να μπορέσουμε να σας πληρώσουμε. Οι ακόλουθες ερωτήσεις πρέπει να συμπληρωθούν για να αποφευχθεί οποιαδήποτε καθυστέρηση στις πληρωμές σας.'
                                        '\n Ni se solicită prin lege să obținem informațiile fiscale înainte de a vă putea plăti. Următoarele întrebări trebuie completate pentru a evita orice întârziere la plăți',font=lucidaGrande,bg='white')

    lbl_empDeclaration.pack()
    btn_continue=Button(frame,text='Continue',bg='dodgerblue',fg='white',width=8,height=4,font=lucidaGrande,command=employe_declaration_detail)
    btn_continue.pack()
    newEmployeDeclarationWindow.mainloop()

def open_notice_passport():
    workingHrsThanksWindow.destroy()
    notice_passport()

def signWorkingHrs():
    employeName=None
    if workHrsEmpFullName is None:
        employeName= txt_empFullName.get("1.0", 'end-1c')
    else:
        employeName=workHrsEmpFullName
    workingHrsDetail.destroy()
    signing.canvasSign()
    print('generate pdf for working hrs')
    reportGenerator.create_workingHrs_form(employeName)
    #show the thanks message
    global workingHrsThanksWindow
    workingHrsThanksWindow=Tk()
    lucidaGrande = tkFont.Font(family="Lucida Grande", size=12)
    workingHrsThanksWindow.resizable(0,0)
    workingHrsThanksWindow.title("Thanks")
    workingHrsThanksWindow.resizable(0,0)
    workingHrsThanksFrame=Frame(workingHrsThanksWindow).pack()
    lbl_msg=Label(workingHrsThanksFrame,text="Thank you. This information has been submitted successfully.",font=lucidaGrande).pack()
    btn_close=Button(workingHrsThanksFrame,text="Close",bg='grey',fg='white',command=open_notice_passport,font=lucidaGrande).pack()


def workingHrs_detail():
    workingHrsMain.destroy()
    global workingHrsDetail
    workingHrsDetail=Tk()
    workingHrsDetail.resizable(0,0)
    lucidaGrande = tkFont.Font(family="Lucida Grande", size=12)
    workingHrsDetail.title("Working hours opt out")
    workingHrsFrame=Frame(workingHrsDetail)
    workingHrsFrame.pack()
    print("work hours fullname is ",workHrsEmpFullName)
    if workHrsEmpFullName is None:
        print('in none')

        global lbl_emp_error
        lbl_emp_error=Label(workingHrsFrame,text='',fg='red',font=lucidaGrande)
        lbl_emp_error.pack()

        # if len(txt_fullname.get("1.0", 'end-1c'))==0:
        lbl_empFullname=Label(workingHrsFrame,text='Enter fullname',font=lucidaGrande)
        lbl_empFullname.pack()
        global txt_empFullName
        txt_empFullName=Text(workingHrsFrame,height=1, width=35,font=lucidaGrande)
        txt_empFullName.pack()
        btn_continue=Button(workingHrsFrame,text='Continue (dop signature)',fg='white',bg='dodgerblue',command=signWorkingHrs,font=lucidaGrande)
        btn_continue.pack()
        workingHrsDetail.geometry("500x200")
        workingHrsDetail.mainloop()
    else:
        lbl_sign_msg=Label(workingHrsFrame,text='Please continue to proceed to signature.',font=lucidaGrande).pack()
        btn_continue=Button(workingHrsFrame,text='Continue',fg='white',bg='dodgerblue',font=lucidaGrande,command=signWorkingHrs).pack()
        workingHrsDetail.mainloop()




#defining the working hours module
def working_hrs_main():
    global workingHrsMain
    workingHrsMain=Tk()
    lucidaGrande = tkFont.Font(family="Lucida Grande", size=12)
    workingHrsMain.resizable(0,0)
    workingHrsMain.title("Working hours opt out")
    frame=Frame(workingHrsMain).pack()
    lbl_heading=Label(frame,text="""
    We are required by law to ask you whether you would be happy to work more hours. The following document must be signed if you would 
    like more hours.It does not mean you have to work more hours, but it means you have the option in future.
     \n Απαιτείται από το νόμο να σας ρωτήσουμε εάν θα θέλατε να εργαστείτε περισσότερες ώρες. Το ακόλουθο έγγραφο πρέπει να υπογραφεί εάν 
     θέλετε περισσότερες ώρες.Δεν σημαίνει ότι πρέπει να εργάζεστε περισσότερες ώρες, αλλά σημαίνει ότι έχετε την επιλογή στο μέλλον
     \n Ni se solicită prin lege să vă întrebăm dacă vă veți bucura să lucrați mai multe ore. Următorul document trebuie semnat dacă 
     doriți mai multe ore. Nu înseamnă că trebuie să lucrați mai multe ore, ci înseamnă că aveți opțiunea pe viitor.""",font=lucidaGrande).pack()
    btn_continue=Button(frame,text='Continue',fg='white',bg='dodgerblue',command=workingHrs_detail,font=lucidaGrande).pack()
    workingHrsMain.mainloop()




def open_workingzHrs_from_main():
    welcomeWindow.destroy()
    working_hrs_main()

def notice_passport():
    passportWindow=Tk()
    passportWindow.resizable(0,0)
    passportFrame=Frame(passportWindow).pack()
    passportWindow.title("Notice re Passport")
    lucidaGrande = tkFont.Font(family="Lucida Grande", size=12)
    lbl_message=Label(passportFrame,text="""
    Please supply a copy of your passport to us by emailing it to gpw@goinggreek.co.uk. If you have already done this, you do not need to take any action. If you can’t do it now,
    please make a note of this for later. If there’s any reason why you can’t supply a copy of your passport, please notify us by emailing gpw@goinggreek.co.uk.
    \nΠαρακαλούμε δώστε μας αντίγραφο του διαβατηρίου σας μέσω email στο gpw@goinggreek.co.uk. Εάν το έχετε ήδη κάνει, δεν χρειάζεται να προβείτε σε καμία ενέργεια. Εάν δεν μπορείτε
    να το κάνετε τώρα, σημειώστε το για αργότερα. Εάν υπάρχει κάποιος λόγος για τον οποίο δεν μπορείτε να προσκομίσετε αντίγραφο του διαβατηρίου σας, ενημερώστε μας μέσω email στο gpw@goinggreek.co.uk.
    \nVă rugăm să ne furnizați o copie a pașaportului dvs., trimițându-l prin e-mail la gpw@goinggreek.co.uk. Dacă ați făcut deja acest lucru, nu este necesar să luați măsuri.
     Dacă nu o puteți face acum, vă rugăm să notați acest lucru pentru mai târziu. Dacă există vreun motiv pentru care nu puteți furniza o copie a pașaportului, vă rugăm să ne anunțați prin e-mail pe gpw@goinggreek.co.uk.
    """,font=lucidaGrande).pack()
    btn_close=Button(passportFrame,text="Close",bg='grey',fg='white',command=lambda:passportWindow.destroy(),font=lucidaGrande).pack()
    passportWindow.mainloop()


def mainWindow():
    global welcomeWindow
    welcomeWindow= Tk()
    lucidaGrande = tkFont.Font(family="Lucida Grande", size=12)
    welcomeWindow.resizable(0,0)
    frame = Frame(welcomeWindow,bg='white')
    frame.pack()
    welcomeWindow.title("Going Greek HR Documentation")


    lbl_description=Label(frame,text='''
    To ensure that you're paid on time, it is essential that we obtain information about you. We are required to do this by law. Click the ‘Complete All’ button below. Please respond in English.
    \nΓια να διασφαλίσουμε ότι πληρώνεστε εγκαίρως, είναι σημαντικό να λάβουμε πληροφορίες σχετικά με εσάς. Πρέπει να το κάνουμε από το νόμο. Κάντε κλικ στο κουμπί "Ολοκλήρωση όλων" παρακάτω. Όπου είναι δυνατόν, απαντήστε στα Αγγλικά.
    \nPentru a vă asigura că sunteți plătit la timp, este esențial să obținem informații despre dvs. Trebuie să facem acest lucru prin lege. Faceți clic pe butonul „Completați toate” de mai jos. Vă rugăm să răspundeți în engleză''',font=lucidaGrande,bg='white')
    lbl_description.pack()

    btn_complete=Button(frame,text='Complete all \n Ολοκληρώστε όλα \n Completează toate',bg='dodgerblue',fg='white',command=new_employe_starter_main_window)
    btn_complete.pack(side=RIGHT,pady=20,padx=20)

    btn_employee_declaration = Button(frame, text='Complete Employee Declaration Only \n Πλήρης δήλωση υπαλλήλου μόνο \n Completați numai declarația angajaților', bg='dodgerblue', fg='white',command=new_employe_declaration)
    btn_employee_declaration.pack(side=RIGHT, pady=10, padx=10)

    btn_working_hrs = Button(frame,
                                      text='Complete Working Hours Opt-Out Only \n Πλήρης εξαίρεση ωρών εργασίας \n Ore de lucru complete numai de renunțare ',
                                      bg='dodgerblue', fg='white',command=open_workingzHrs_from_main)
    btn_working_hrs.pack(side=RIGHT, pady=10, padx=10)


    welcomeWindow.mainloop()


mainWindow()
