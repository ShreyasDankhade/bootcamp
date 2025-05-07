def copy_file_line_by_line(src, dst):
    with open(src, 'r') as source, open(dst, 'w') as destination:
        for line in source:
            destination.write(line)

copy_file_line_by_line('source_file.txt', 'destination_file.txt')
