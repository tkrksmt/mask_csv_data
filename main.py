import csv
import pandas as pd
import re

def get_csv_header(file_name):
    df = pd.read_csv(file_name , sep=',')
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

def replace_data(data):
    ret = list()
    for row in data:
        row['email'] = get_mask_email(row['email'])
        ret.append(row)
    return ret

def read_file(file_name):
    try:
        with open(file_name, 'r', encoding='UTF-8', errors='', newline='' ) as csv_file:
            #Read Dictionary data
            file_data = csv.DictReader(csv_file, delimiter=',', doublequote=True, lineterminator='\r\n', quotechar='"', skipinitialspace=True)
            data = replace_data(file_data)
            return data
    
    except FileNotFoundError:
        print('[ERROR]not exist csv data')
    return list()

def write_file(data , header , file_name):
    if len(data) <= 0:
        return
    
    with open(file_name, 'w', newline='') as f:
        # create same header
        w = csv.DictWriter(f, fieldnames = header)
        w.writeheader()
        for d in data:
            #print(d)
            w.writerow(d)

def main():
    #setting file Name
    file_name        = './data.csv'
    output_file_name = './data1.csv'

    data = read_file(file_name)
    header = get_csv_header(file_name)
    write_file(data ,header , output_file_name)
    
main()