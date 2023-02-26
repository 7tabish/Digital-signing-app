import os
import fpdf
imagePath=os.path.exists(os.path.join(os.getcwd(),'image.png'))
from datetime import datetime

current_date = str(datetime.today().strftime('%Y-%m-%d'))


def create_employe_declaration_form(checkedJobOption,checkedLoan,fullname):
    pdf = fpdf.FPDF(format='letter')  # pdf format
    pdf.add_font('DejaVu-bold', '', 'DejaVuSans-Bold.ttf', uni=True)
    pdf.set_font('DejaVu-bold', '', 12)
    pdf.add_page()  # create new page
    pdf.set_left_margin(15.0)
    pdf.set_right_margin(15.0)
    header_english="""
    We are required by law to obtain your tax information before we can pay you. The following questions must be completed to avoid any delay in your payments.
    """
    pdf.multi_cell(190,6,header_english,0,align='L')
    pdf.add_font('DejaVu-regular', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu-regular','', 12)
    header_other="""Απαιτείται από το νόμο να λάβουμε τα φορολογικά σας στοιχεία για να μπορέσουμε να σας πληρώσουμε. Οι ακόλουθες ερωτήσεις πρέπει να συμπληρωθούν για να αποφευχθεί οποιαδήποτε καθυστέρηση στις πληρωμές σας
    Ni se solicită prin lege să obținem informațiile fiscale înainte de a vă putea plăti. Următoarele întrebări trebuie completate pentru a evita orice întârziere la plăți"""
    pdf.multi_cell(190,6,header_other,0,align='L')


    pdf.ln(15)
    pdf.add_font('DejaVu-bold', '', 'DejaVuSans-Bold.ttf', uni=True)
    pdf.set_font('DejaVu-bold','', 12)
    pdf.cell(100, 6, "Full Name: {}".format(fullname),ln=1, align="L")
    pdf.add_font('DejaVu-regular', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu-regular','', 12)
    pdf.cell(200, 6, txt="Ονοματεπώνυμο / Numele complet:", ln=1, align="L")

    #text for 3 radio options

    pdf.add_font('DejaVu-bold', '', 'DejaVuSans-Bold.ttf', uni=True)
    pdf.set_font('DejaVu-bold','', 12)
    pdf.cell(200, 6, txt="Tick one of the following three statements:", ln=1, align="L")
    pdf.add_font('DejaVu-regular', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu-regular','', 10)
    pdf.cell(200, 6, txt="Επιλέξτε μία από τις ακόλουθες τρεις δηλώσεις / Bifați una dintre următoarele trei afirmații", ln=1, align="L")

    pdf.ln(10)
    option1_eng="""This is my first job since last 6 April and I have not been receiving taxable Jobseeker’s Allowance, Employment and Support Allowance, taxable Incapacity Benefit,State or Occupational Pension."""
    option1_other1="""Αυτή είναι η πρώτη μου δουλειά από τις 6 Απριλίου και δεν έχω λάβει φορολογητέο Επίδομα Εύρεσης Εργασίας, Επίδομα Απασχόλησης και Υποστήριξης, φορολογητέα Παροχή Ανικανότητας, Κρατική ή Επαγγελματική Σύνταξη."""
    option1_other2="""Acesta este primul meu loc de muncă incepand cu data de 6 aprilie anului trecut și nu primesc indemnizație impozabilă, indemnizațiede angajare și ajutor, solicitare de incapacitate, pensie de stat sau de muncă."""

    option2_eng="""This is now my only job but since last 6 April I have had another job, or received taxable Jobseeker’s Allowance, Employment and Support Allowance, taxable incapacity Benefit. I do not receive a state or Occupational Pension."""
    option2_other1="""Αυτή είναι τώρα η μόνη δουλειά μου, αλλά από τις 6 Απριλίου έχω εργαστεί και σε άλλη δουλειά ή έχω λάβει φορολογητέο Επίδομα Εύρεσης Εργασίας, Επίδομα Απασχόλησης και Υποστήριξης, φορολογητέα Παροχή Ανικανότητας. Δεν λαμβάνω κρατική ή επαγγελματική σύνταξη."""
    option2_other2="""Acesta este acum singurul meu loc de muncă, dar începând cu data de 6 aprilie a anului trecut, am mai avut un alt loc de muncă sau am primit Indemnizația, angajarea și sprijinul impozabilului solicitantului, Indemnizația de incapacitate impozabilă. Nu primesc o pensie de stat sau de muncă."""


    option3_eng="""As well as my new job, I have another job or receive a State or Occupational Pension."""
    option3_other1="""Εκτός από τη νέα μου δουλειά, έχω κι άλλη δουλειά ή λαμβάνω κρατική ή επαγγελματική σύνταξη."""
    option3_other2="""Inafara de noul meu loc de muncă, mai am un alt loc de muncă sau primesc o pensie de stat sau de muncă."""

    pdf.add_font('DejaVu-bold', '', 'DejaVuSans-Bold.ttf', uni=True)
    pdf.set_font('DejaVu-bold','', 12)
    if checkedJobOption==1:
        pdf.multi_cell(190, 6, "{} {}".format("CHECKED", option1_eng), 0, align='L')
    else:
        pdf.multi_cell(190,6,"{} {}".format("",option1_eng),0,align='L')

    pdf.add_font('DejaVu-regular', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu-regular','', 10)
    pdf.multi_cell(190,6,option1_other1,0,align='L')
    pdf.multi_cell(190,6,option1_other2,0,align='L')

    pdf.ln(5)
    pdf.add_font('DejaVu-bold', '', 'DejaVuSans-Bold.ttf', uni=True)
    pdf.set_font('DejaVu-bold','', 12)
    if checkedJobOption==2:
        pdf.multi_cell(190,6,"{} {}".format("CHECKED",option2_eng),0,align='L')
    else:
        pdf.multi_cell(190, 6, "{} {}".format("", option2_eng), 0, align='L')
    pdf.add_font('DejaVu-regular', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu-regular','', 10)
    pdf.multi_cell(190,6,option2_other1,0,align='L')
    pdf.multi_cell(190,6,option2_other2,0,align='L')

    pdf.ln(5)
    pdf.add_font('DejaVu-bold', '', 'DejaVuSans-Bold.ttf', uni=True)
    pdf.set_font('DejaVu-bold','', 12)
    if checkedJobOption==3:
        pdf.multi_cell(190, 6, "{} {}".format("CHECKED", option3_eng), 0, align='L')
    else:
        pdf.multi_cell(190,6,"{} {}".format("",option3_eng),0,align='L')
    pdf.add_font('DejaVu-regular', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu-regular','', 10)
    pdf.multi_cell(190,6,option3_other1,0,align='L')
    pdf.multi_cell(190,6,option3_other2,0,align='L')

    pdf.ln(15)
    pdf.add_font('DejaVu-bold', '', 'DejaVuSans-Bold.ttf', uni=True)
    pdf.set_font('DejaVu-bold','', 12)
    pdf.multi_cell(190,6,"Student loan:",0,align='L')
    pdf.add_font('DejaVu-regular', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu-regular','', 12)
    pdf.multi_cell(190,6,"Φοιτητικό δάνειο / Împrumut de student",0,align='L')

    pdf.ln(6)
    pdf.cell(190,6,"{} {}".format("(checked)","Plan 1 Σχέδιο 1 / Planul 1"))
    pdf.ln(10)
    pdf.cell(190,6,"{} {}".format("","Plan 2 Σχέδιο 2 / Planul 2"))
    pdf.ln(10)

    p45_eng="""Please supply your P45 to us by emailing it to . If you can’t do it now, please make a note of this for later. If you do not supply your P45, we are required to apply an ‘emergency tax’ code, which may mean you pay more tax than you need to. If there’s any reason why you can’t supply this, please notify us by emailing ."""
    p45_other1="""Παρακαλώ δώστε το P45 σας σε εμάς μέσω email στο Εάν δεν μπορείτε να το κάνετε τώρα, σημειώστε το για αργότερα. Εάν δεν παρέχετε το P45 σας, πρέπει να εφαρμόσουμε έναν κωδικό «φόρου έκτακτης ανάγκης», ο οποίος μπορεί να σημαίνει ότι πληρώνετε περισσότερο φόρο από ό, τι χρειάζεστε. Εάν υπάρχει κάποιος λόγος για τον οποίο δεν μπορείτε να το παρέχετε, ενημερώστε μας μέσω email στο """
    p45_other2="""Vă rugăm să ne furnizați P45-ul dvs. prin e-mail la  Dacă nu o puteți face acum, vă rugăm să notați acest lucru pentru mai târziu. Dacă nu furnizați P45, trebuie să aplicăm un cod „impozit de urgență”, ceea ce poate însemna că plătiți mai mult impozit decât trebuie. Dacă există vreun motiv pentru care nu puteți furniza acest lucru, vă rugăm să ne anunțați prin e-mail"""



    pdf.add_font('DejaVu-bold', '', 'DejaVuSans-Bold.ttf', uni=True)
    pdf.set_font('DejaVu-bold','', 12)
    pdf.cell(190,6,"P45")
    pdf.ln(15)

    pdf.add_font('DejaVu-regular', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu-regular','', 14)
    pdf.multi_cell(190,6,p45_eng,0,align='L')
    pdf.ln(5)
    pdf.add_font('DejaVu-regular', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu-regular','', 12)
    pdf.multi_cell(190,6,p45_other1,0,align='L')
    pdf.ln(5)
    pdf.add_font('DejaVu-regular', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu-regular','', 10)
    pdf.multi_cell(190,6,p45_other2,0,align='L')
    pdf.ln(20)



    # pdf.set_xy(50.0,200.0)
    pdf.image("image.png",w=30,h=30)
    pdf.cell(190,6,txt='Signed',ln=1,align="L")
    pdf.ln(15)


    pdf.cell(190,6,txt=current_date,ln=1,align="L")
    pdf.cell(190,6,txt='Date / Ημερομηνία / Data:',ln=1,align="L")
    filename="employeDeclration "+current_date+"-"+fullname+".pdf"
    pdf.output(filename,"F")



def create_workingHrs_form(fullname):
    pdf = fpdf.FPDF(format='letter')  # pdf format
    pdf.add_page()  # create new page
    pdf.set_left_margin(15.0)
    pdf.set_right_margin(15.0)
    pdf.add_font('DejaVu-regular', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu-regular','', 12)
    pdf.cell(190,5,"T: 0203 030 4508",ln=1,align="R")
    pdf.cell(190,5, "E: info@goinggreek.co.uk", ln=1, align="R")
    pdf.cell(190,5, "W: www.GoingGreek.co.uk", ln=1, align="R")
    pdf.ln(10)
    pdf.add_font('DejaVu-bold', '', 'DejaVuSans-Bold.ttf', uni=True)
    pdf.set_font('DejaVu-bold','', 14)
    pdf.cell(190,5,"INDIVIDUAL OPT-OUT AGREEMENT",ln=1,align="C")

    pdf.add_font('DejaVu-regular', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu-regular', '', 10)
    pdf.cell(190,5,"ΑΤΟΜΙΚΗ ΣΥΜΦΩΝΙΑ ΕΞΑΙΡΕΣΗΣ / ACORD DE A RENUNTA LA ANUMITE PREVEDERI",ln=1,align="C")
    pdf.ln(10)
    pdf.add_font('DejaVu-bold', '', 'DejaVuSans-Bold.ttf', uni=True)
    pdf.set_font('DejaVu-bold','', 12)
    pdf.multi_cell(190, 5, "An agreement to opt out of regulation 4(1) of The Working Time Regulations 1998 – maximum weekly working time.", 0, align="L")

    pdf.add_font('DejaVu-regular', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu-regular', '', 10)
    pdf.multi_cell(190,5,"""Συμφωνία για εξαίρεση από τον κανονισμό 4 (1) των Κανονισμών Χρόνου Εργασίας 1998 - μέγιστος εβδομαδιαίος χρόνος
εργασίας.
Un acord pentru a renunța la regulamentul 4 (1) din Regulamentul privind timpul de lucru din 1998 - timp de lucru maxim
săptămânal.
    """,0,align="L")

    pdf.add_font('DejaVu-regular', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu-regular', '', 14)
    pdf.multi_cell(190,5,"""I, {} (Το όνομα σου / Numele dumneavoastră)
    \nagree with GG Recreation LTD T/A Going Greek
    \nof WeWork, 2 Minster Court, London, EC3R 7BB""".format(fullname),0,align="L")
    filename = "workingHours " + str(current_date) + "-" + fullname + ".pdf"
    pdf.ln(5)
    pdf.multi_cell(190,5,"""(“the employer”) that the limit in regulation 4(1) of The Working Time Regulations 1998
shall not apply to me and that my average working time may therefore exceed 48 hours
for each seven-day period (as defined by and calculated in accordance with The Working
Time Regulations 1998).""",0,align="L")

    pdf.set_font('DejaVu-regular', '', 10)
    pdf.multi_cell(190,5,"""(«εργοδότης») ότι το όριο του κανονισμού 4 (1) των Κανονισμών Χρόνου Εργασίας 1998 δεν θα ισχύει για μένα και ότι  μέσος χρόνος εργασίας μου μπορεί κατά συνέπεια να υπερβαίνει τις 48 ώρες για κάθε επταήμερη περίοδο (όπως ορίζεται και υπολογίζεται σύμφωνα με τους Κανονισμούς Χρόνου Εργασίας 1998).
(„Angajatorul”) că limita prevăzută în regula 4 (1) din Regulamentul privind timpul de lucru din 1998 nu se aplică și că, prin urmare, media timpului meu de lucru poate depăși 48 de ore pentru fiecare perioadă de șapte zile (așa cum este definit de și calculat în în conformitate cu Regulamentul timpului 1009)""",0,align="L")


    pdf.ln(10)
    pdf.set_font('DejaVu-regular', '', 14)
    pdf.multi_cell(190,6,"""The agreement shall apply from your start date (as stated on your offer letter) until further notice.""",0,align="L")

    pdf.set_font('DejaVu-regular', '', 10)
    pdf.multi_cell(190, 6,
                   """Η συμφωνία θα ισχύει από την ημερομηνία έναρξης (όπως αναφέρεται στην επιστολή προσφοράς εργασίας σας) μέχρι νεωτέρας.
Acordul se aplică de la data de începere (după cum se menționează în scrisoarea de ofertă) până la o notificare ulterioară.""",0, align="L")

    pdf.add_page()
    pdf.set_font('DejaVu-regular', '', 14)
    pdf.multi_cell(190, 6,
                   """I agree that I will comply with any and all policies of the employer, from time to time in force, which relates to its maintenance of records of my hours of work.""",0, align="L")

    pdf.set_font('DejaVu-regular', '', 10)
    pdf.multi_cell(190, 6,
                   """Συμφωνώ ότι θα συμμορφωθώ με όλες τις πολιτικές του εργοδότη που ισχύουν από καιρό σε καιρό, οι οποίες σχετίζονται με τη διατήρηση του αρχείου των ωρών εργασίας μου.
Sunt de acord că voi respecta oricare și toate politicile angajatorului, în vigoare, care se referă la păstrarea registrelor de la orele mele de muncă.""",0, align="L")

    pdf.ln(10)
    pdf.set_font('DejaVu-regular', '', 14)
    pdf.multi_cell(190, 6,
                   """This agreement can be terminated by me giving three months’ notice in writing to the employer.""",0, align="L")

    pdf.set_font('DejaVu-regular', '', 10)
    pdf.multi_cell(190, 6,
                   """Αυτή η συμφωνία μπορεί να τερματιστεί από εμένα, με γραπτή προειδοποίηση τριών μηνών στον εργοδότη.Acest acord poate fi reziliat de mine, dând un aviz de trei luni în scris angajatorului.""",0, align="L")

    pdf.ln(10)
    pdf.image("image.png",w=30,h=30)
    pdf.cell(150,6,"Signed / Υπογραφή (Εργαζόμενου) / Semnat",0,align="L")
    pdf.ln(15)
    pdf.set_font('DejaVu-regular', '', 12)
    pdf.cell(150,6,current_date,ln=1,align="L")
    pdf.set_font('DejaVu-regular', '', 10)
    pdf.cell(150,6,"Dated / Ημερομηνία / Datat")
    pdf.output(filename, "F")
