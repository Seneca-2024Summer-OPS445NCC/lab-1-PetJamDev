#!/usr/bin/env python3




def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
    f = open('data.txt', 'a')
    f.write(file_name)
    file_name = f.write(str(string_of_lines) + '\n')
    f.close()



if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
   # print(read_file_string(file1))
   # write_file_list(file2, list1)
   # print(read_file_string(file2))
   # copy_file_add_line_numbers(file2, file3)
   # print(read_file_string(file3))

