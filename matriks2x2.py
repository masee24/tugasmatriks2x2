#A+B
from sunau import AUDIO_FILE_ENCODING_LINEAR_24


MatriksA = 1,3,6,9
MatriksB = 2,4,5,10

a21 = MatriksA[0] + MatriksB[0]
a22 = MatriksA[1] + MatriksB[1]
a23 = MatriksA[2] + MatriksB[2]
a24 = MatriksA[3] + MatriksB[3]

print("[",a21,a22,"] \n"  " )[" ,a23,a24, "]")