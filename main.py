
file_a = "C://Users//Administrator//Desktop//log.txt"
new_log = ''
with open(file_a, 'r') as f:
    my_log = f.readlines()
for i in my_log:
    if "Request timed out." in i:
        new_log = new_log + f"{i}"

new_log_txt = "C://Users//Administrator//Desktop//new_log.txt"
with open (new_log_txt, 'w') as f:
    f.write(new_log)




if __name__ == '__main__':
    print('hi')

