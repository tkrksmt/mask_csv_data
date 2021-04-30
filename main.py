import csv
import pandas as pd
import re

Csv_file_name = './data.csv'
Output_file_name = './data1.csv'
Csv_Data = list()

def get_csv_header():
    df = pd.read_csv(Csv_file_name , sep=',')
    return df.head(0)


def get_mask_email(email):
    #print(email)

    email_split = re.split('[@.]', email)
    #print(email_split)
    #['username', 'domain_front', 'domain_back']
    
    username, domain_front, *domain_back_list = email_split
    username_masked = username[0] + 'x' * ( len(username) - 1 )
    domain_front_masked = 'x' * len(domain_front)
    domain_back = '.'.join(domain_back_list)
    email_masked = '{}@{}.{}'.format(username_masked, domain_front_masked, domain_back)
    #print(email_masked)
    return email_masked


def read_file():
    successFlag = False
    try:
        with open(Csv_file_name, 'r', encoding='UTF-8', errors='', newline='' ) as csv_file:
            #Read Dictionary data
            file_data = csv.DictReader(csv_file, delimiter=',', doublequote=True, lineterminator='\r\n', quotechar='"', skipinitialspace=True)
            for row in file_data:
                row['email'] = get_mask_email(row['email'])
                Csv_Data.append(row)
        successFlag = True
    
    except FileNotFoundError:
        print('[ERROR]not exist csv data')
    return successFlag

def write_file():
    with open(Output_file_name, 'w', newline='') as f:
        # create same header
        #header = 
        w = csv.DictWriter(f, fieldnames = get_csv_header())
        w.writeheader()
        for d in Csv_Data:
            #print(d)
            w.writerow(d)

def main():
    if read_file():
        write_file()
    
main()