import face_recognition
import cv2
import sys, time
import os
reco=1

# This program processes frames from live video to detect faces and compares againts a list of known face encodings. 
# If the face is unrecognised, they are regarded as an intruder and an email is sent along with the frame attached by invoking a shell script.
# If the face is known, nothing is done.

# Get a reference to webcam #0 
print("[INFO] sampling frames from webcam...")
video_capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
  
# Load a sample picture and learn how to recognize it.
harry_image = face_recognition.load_image_file("known/harry_potter.jpg")
harry_face_encoding = face_recognition.face_encodings(harry_image)[0]


# Load a second sample picture and learn how to recognize it.
pichai_image = face_recognition.load_image_file("known/pichai.png")
pichai_face_encoding = face_recognition.face_encodings(pichai_image)[0]


# Load a third sample picture and learn how to recognize it.
selena_image = face_recognition.load_image_file("known/selena.png")
selena_face_encoding = face_recognition.face_encodings(selena_image)[0]

# Load a third sample picture and learn how to recognize it.
payal_image = face_recognition.load_image_file("known/Payal.jpeg")
payal_face_encoding = face_recognition.face_encodings(payal_image)[0]


# Create arrays of known face encodings and their names
known_face_encodings = [
    pichai_face_encoding,
    selena_face_encoding,
    harry_face_encoding,
    payal_face_encoding,
    
]
known_face_names = [
    "Sundar Pichai",
    "Selena Gomez",
    "Harry Potter",
    "Payal"
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True


while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()
    
    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []

        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, 0.55)
            distances = face_recognition.face_distance(known_face_encodings, face_encoding)
	    
            name = "Unknown"

            # If a match was found in known_face_encodings, use the one which had minimum face distance i.e. the closest match
            if True in matches:
                best_match_index = distances.argmin()
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), 5)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
       
    # Display the resulting image
    
    cv2.imshow('Camera', frame)
    out.write(frame)
    if 'Unknown' in face_names:
         # To prevent sending multiple emails when the face is in the frame for a long time       
	    if (time.time()-os.path.getctime(r'C:\Users\dell\Downloads\god/test.jpeg')) > 30:
             reco=0
             img = cv2.imwrite("test.jpeg",frame) 

    if (time.time()-os.path.getctime(r'C:\Users\dell\Downloads\god/test.jpeg')) > 30:
             
             img = cv2.imwrite("test.jpeg",frame) 
                    
        
    		

    if cv2.waitKey(1) & 0XFF==ord('q'):
        break
        
   

# Release handle to the webcam
video_capture.release()
out.release()
cv2.destroyAllWindows()




