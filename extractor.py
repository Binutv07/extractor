import textract 
import re 
import sys

PHONE_REG = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')
EMAIL_REG = re.compile(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')
NAME_REG = re.compile(r'Name[\s]*[:-][\s]*([a-zA-Z ]+)')
# ADDR_REG = re.compile(r'Address[\s]*[:-][\s]*([a-zA-Z ]+)')

def doc_extract(path):
    text = textract.process(path)
    if text:
        return text.decode("utf-8").replace('\t', ' ')
    return None

def extract_phone_number(resume_text):
    phone = re.findall(PHONE_REG, resume_text)
    if phone:
        number = ''.join(phone[0])
        if resume_text.find(number) >= 0 and len(number) < 16:
            return number
    return None

# Assume name is either in format 'Name: ' or occur as the first line.
def extract_name(txt):
    names = re.findall(NAME_REG, txt)
    if (len(names) > 0):
       return format_name(names[0])
    return format_name(get_first_line(txt))

# Assume first line has the candidate name
def get_first_line(text):
    texts = text.split('\n')
    for line in texts:
        if (len(line.strip()) > 0):
            return line.strip()

# Make name into Correct format
def format_name(name):
    names = name.split(' ')
    final_list = []
    for name in names:
        name = name[0].upper() + name[1:].lower()
        final_list.append(name)
    return ' '.join(final_list)

# Simply use the email regex to get the email
def extract_emails(resume_text):
    return re.findall(EMAIL_REG, resume_text)

# def extract_address(resume_text) :
#     return re.findall(ADDR_REG, resume_text)

if __name__ == '__main__':
    if (not len(sys.argv) > 1):
        print("No file name provided.")
        exit()

    for file in sys.argv[1:]:
        print(file)
        text = doc_extract(file)
        
        name = extract_name(text)
        print("Name : " + name)

        phone_number = extract_phone_number(text)
        print("Mobile : " + phone_number)

        emails = extract_emails(text)
        if emails:
            print("Email : " + emails[0])

        # address = extract_address(text)
        # if address:
        #     print("Address : " + address[0])

        print()
