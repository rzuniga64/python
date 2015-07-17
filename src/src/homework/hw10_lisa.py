# Script to validate student survey appeals data, then create a
# .csv file as output that flags incorrect data.

import csv
import pyodbc
# import sybpydb <-- lesson09_module to access a sybase database

DtEffective = '06/30/2013'

def check_data(data):

    filename = DtEffective[0:2]+DtEffective[3:5]+DtEffective[8:10]+'.csv'
    
    newfile = open(filename,'w')

    count_appeals = 0

    # Connect to the database
##    cnxn = pypyodbc.connect('Driver = {Microsoft Access Driver (*. Mdb, *.accdb)}; DSN=MS Access Database; DBQ=C:\\Users\\meng.lisa\\Desktop\\DSS and Spamis Reports\\Student Survey Appeals\\appeals validation\\students.accdb')
    cnxn = pyodbc.connect('DSN=MS Access Database; DBQ=C:\\students.accdb')
    cursor = cnxn.cursor()

    for line in data:

        if 'Student ID,lname,fname,Weekly Earnings,Hourly Wage,Survey Month (6 or 12),Date Submitted' in line:
            pass
        else:
            count_appeals += 1
            appeal = line.strip()
            appeal = line.strip('\"')
            appeal = appeal.split(',')

            # Get ssn, stud_fname, stud_lname from database 'students', table 'student'

            cursor.execute('select ssn, stud_fname,stud_lname from student where stud_id = ?',[int(appeal[0])])
            student = cursor.fetchone()
##            if not student:
##                pass
##            else:
##                print(appeal[0],student[0],student[1],student[2],appeal[4],appeal[5])
            
            no_stud_id = appeal[0] # student id provided by the NO. = student[0]
            ssn = str(student[0])
            fname = student[1]
            lname = student[2]
            no_lname = appeal[1] # student last name provided by the NO
            no_fname = appeal[2] # student first name provided by the NO
            earn = appeal[3] # weekly earnings.
            wage = appeal[4] # hourly wage.
            pay_cd = appeal[5] # pay code.
            dt_submit = appeal[6] # date the appeal was requested.
            dt_effective = DtEffective # Appeal effective date.

            if DtEffective[0] == '0':
                dt_effective = DtEffective[1:]
            elif DtEffective[0] == '1':
                dt_effective = DtEffective
            else:
                pass

            ssn = ssn[0:-2]

            fname = fname.strip()
            lname = lname.strip()

            fname = fname.strip('\'\".')
            lname = lname.strip('\'\".')

            fname = fname.lower()
            lname = lname.lower()

            no_fname = no_fname.strip()
            no_lname = no_lname.strip()

            no_fname = no_fname.strip('\'\".')
            no_lname = no_lname.strip('\'\".')

            no_fname = no_fname.lower()
            no_lname = no_lname.lower()

            #print(ssn,lname,no_lname)

            if lname[0:2] == no_lname[0:2]:
                pass
            else:
                ssn = ssn+' CHECK '+no_fname.upper()+' '+no_lname.upper()

            if wage != '':
                wage = wage.strip('\'\"$')
                
            else:
                pass

            if earn !='':
                earn = earn.strip('\'\"$')
                
            else:
                pass

            if len(wage) < len(earn):
                pass
            elif wage == '' and earn == '':
                pass
            else:
                wage += ' CHECK WAGE'
                earn += ' CHECK EARN'
 
            if len(ssn) < 9:
                ssn += ' CHECK LEAD 0s'

            if pay_cd == '6':
                pay_cd = 'PGS2'
            elif pay_cd == '12':
                pay_cd = 'PGS3'
            else:
                pay_cd = ' CHECK PAY CODE'
                
            dt_submit = dt_submit.strip()
            
            if dt_submit[0] != dt_effective[0] or dt_submit[-5] != '/' or dt_submit[len(dt_submit)-1] != dt_effective[len(dt_effective)-1]:
                dt_submit += ' CHECK DATE'
                
            newfile.write(ssn + ',' + earn + ','+ wage + ',' + pay_cd + ',' + dt_submit + ',' + dt_effective + '\n')

    
    print(count_appeals,'student appeals have been submitted.')
    print('Check data in',filename,'and correct any flagged data before sending to DBA.')

    cnxn.close()
    newfile.close

def main():

    survey_data = open('survey_data_db.csv','r')

    check_data(survey_data)

    survey_data.close()

main()
