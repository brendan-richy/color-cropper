def outputpath(input_image_path):
    print(input_image_path)
    # Split the input image by /
    splitList = input_image_path.split('/')
    print(splitList)

    # Image name is the last element of the splitList list
    imagename = splitList[-1]
    print(imagename)

    # Split imageName by .
    tmpList = imagename.split('.')
    imageNoExt = tmpList[0]
    print(imageNoExt)

    # Chop off the last element from splitList
    slicedList= splitList[:-1]
    print(slicedList)

    # Join all elements of splitList with /
    slicedList = '/'.join(slicedList)
    print(slicedList)

    # Add a folder to slicedList with /
    slicedList = slicedList + '/'
    print(slicedList)


    return slicedList + imageNoExt + "_modified.png"