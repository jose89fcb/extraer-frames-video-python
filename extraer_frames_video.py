from itertools import count
import cv2

capture = cv2.VideoCapture('NOMBRE DE TU VÍDEO.mp4') #Escribe el nombre de tu vídeo .mp4
cont = 1
path = 'frames/' #Crea una carpeta llamada frames


while (capture.isOpened()):
    ret, frame = capture.read()
    if (ret == True):
        cv2.imwrite(path + 'imagen_%04d.png' % cont, frame)    
        print('imagen_%04d.png' % cont)
        cont += 1
        if (cv2.waitKey(1) == ord('s')):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()


