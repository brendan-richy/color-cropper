def outputpath(input_image_path):
    # Split the input image by /
    splitList = input_image_path.split('/')

    # Image name is the last element of the splitList list
    imagename = splitList[-1]

    # Split imageName by .
    tmpList = imagename.split('.')
    imageNoExt = tmpList[0]
    ext = '.' + tmpList[1]

    # Chop off the last element from splitList
    slicedList= splitList[:-1]

    # Join all elements of splitList with /
    slicedList = '/'.join(slicedList)

    # Add a folder to slicedList with /
    slicedList = slicedList + '/'
    
    return slicedList + imageNoExt + "_modified" + ext