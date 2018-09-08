import face_recognition
from PIL import Image

# image = face_recognition.load_image_file("friends.jpg")
# face_locations = face_recognition.face_locations(image)
#
# print(len(face_locations))


image = face_recognition.load_image_file("rooftop.jpg")
face_locations = face_recognition.face_locations(image)

print("Found Faces: ", len(face_locations))

for i,face_location in enumerate(face_locations,1):
    top, right, bottom, left = face_location
    print("#{} Face Located at Pixel Location Top: {}, Left:{}, Bottom:{}, Right:{}".format(i,top,right,bottom,left))

    face_image = image[top:bottom, left:right]#image is 2d array
    pil_image = Image.fromarray(face_image)
    pil_image.save("face-{}.jpg".format(i))

########## identifying person ############

toha_image = face_recognition.load_image_file("people/toha.jpg")
toha_encoding = face_recognition.face_encodings(toha_image)[0]
encodings=[]
for i in range(1,8):
    unknown_image = face_recognition.load_image_file("face-{}.jpg".format(i))
    unknown_encoding = face_recognition.face_encodings(unknown_image)
    encodings.append(unknown_encoding)
    print(face_recognition.compare_faces([toha_encoding],unknown_encoding[0]))
print(len(encodings))
#results = face_recognition.compare_faces([toha_encoding],unknown_encoding)
print(face_recognition.compare_faces([toha_encoding],encodings[1][0]))
print(results[0])

unknown_image = face_recognition.load_image_file("face-2.jpg")
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
print(face_recognition.compare_faces([toha_encoding],unknown_encoding))
