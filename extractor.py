import sys


def main(file_path):
    list_of_lines = []
    zana_cavas = ['Cavas, Forgotten Spirit:', 'Zana, Master Cartographer:']

    print('Creating lines.txt file.')
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if 'Cavas, Forgotten Spirit:' in line:  # first encounter with cavas  
                list_of_lines.append(line)             
                for line in f:  # look for zana or cavas memories
                    if any(x in line for x in zana_cavas):
                        list_of_lines.append(line)

    f = open('lines.txt', 'w', encoding='utf-8')
    for item in list_of_lines:
        f.write(item)
    input('Done! Press any key to continue...')

if __name__ == "__main__":
    txt = input(r"Copy path to your Client.txt file (e.g. C:\Program Files (x86)\Grinding Gear Games\Path of Exile\logs\Client.txt): ")
    main(txt)
