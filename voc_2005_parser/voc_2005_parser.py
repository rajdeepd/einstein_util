import os

path = '/Users/rdua/work/metamind/datasets/VOC2005_1'
cal_tech = path + '/Annotations/Caltech_cars'
file = open('annotations.csv', 'w')


def main():
    cal_tech_list = os.listdir(cal_tech)
    max_no = 0

    for filename in cal_tech_list:

        full_filepath = cal_tech + '/' + filename
        with open(full_filepath) as fp:
            line = fp.readline()
            local_no = 0
            while line:
                line_ = line.strip()

                if line_.startswith('Bounding box for object'):
                    local_no += 1
                if local_no > max_no:
                    max_no = local_no

                line = fp.readline()
    print(max_no)
    s=''
    for x in range(0, int(max_no)):
        if x < (int(max_no)-1):
            s = s + '"box' + str(x) + '",'
        else:
            s = s + '"box' + str(x) + '"'

    first_line = '"image_file",' + s + '\n'
    print(first_line)
    file.write(first_line)

    for filename in cal_tech_list:
        full_filepath = cal_tech + '/' + filename
        imagename = filename.split(".")[0] + ".png"
        print(full_filepath)
        label = ''
        bounding_boxes = ''
        no_of_bounding_boxes = 0
        with open(full_filepath) as fp:
            line = fp.readline()
            while line:
                line_ = line.strip()

                if line_.startswith('Original label for object'):
                    label = line_.split(':')[1].strip()
                if line_.startswith('Bounding box for object'):
                    line_split = line_.split(":")
                    line_split_1 = line_split[1].strip()

                    x_y_min = line_split_1.split(") - (")[0].strip()[1:].split(',')
                    x_y_max = line_split_1.split(") - (")[1].strip()[0  :-1].split(',')
                    x_min = x_y_min[0]
                    if len(x_y_min) > 0:
                        y_min = x_y_min[1].strip()
                    else:
                        print('something is wrong' + line_)
                    x_max = x_y_max[0]
                    y_max = x_y_max[1]
                    height = int(y_max) - int(y_min)
                    width = int(x_max) - int(x_min)
                    if bounding_boxes == '':
                        bounding_boxes = '"{""label"": "' + label + '", ""y"": ' + y_min + ',  ""x"": ' + x_min + \
                            ', ""height"": ' + str(height) + ', ""width"": ' + str(width) + '}"'
                        no_of_bounding_boxes +=1
                    else:
                        bounding_boxes = bounding_boxes + ',' + '"{""label"": "' + label + '", ""y"": ' + y_min + ', ""x"": ' + x_min + \
                            ', ""height"": ' + str(height) + ', ""width"": ' + str(width) + '}"'
                        no_of_bounding_boxes += 1
                line = fp.readline()
        final =  '"' + imagename + '",' + bounding_boxes
        print(final)
        print(bounding_boxes)
        if final != ', \n' and bounding_boxes != '':
            if no_of_bounding_boxes < bounding_boxes:
                x = max_no - no_of_bounding_boxes
                final = final + ' ,' * x + '\n'
            else:
                final = final + '\n'
            print(final)
            file.write(final)

    file.close()


if __name__ == '__main__':
    main()