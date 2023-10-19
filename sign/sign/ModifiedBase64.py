from ast import Str
from json.tool import main


class ModifiedBase64:
    def __init__(self) -> None:
        pass
        self.emptyBytes = bytearray().zfill(128)
        self.staticArray = ('K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/')
        self.initEmptyBytes()
    def initEmptyBytes(self):
        i=0
        ii=0
        while True:
            l=len( self.emptyBytes)
            if ii<l-1:
                self.emptyBytes[ii]=(-1+256)%256
                ii=ii+1
            else:
                break
        while True:
            carr=self.staticArray
            # print(type(carr))
            if i<len(carr)-1:
                aaa=self.staticArray[i]
                aaaByte=aaa.encode("utf8")
                # print(type(aaaByte))
                aaaInt=int.from_bytes(aaaByte, "big")
                self.emptyBytes[aaaInt]=i
                i=i+1
            else:
                return
    def decrypt(self,str:str):
        mybyteArray=bytearray()
        byte1=str.encode(encoding="utf-8")
        bArr=bytearray()
        for i in range(0,len(byte1)):
            iii=byte1[i]
            bArr.append(self.emptyBytes[iii])
        for i2 in  range(0,len(bArr)-1,4):
            i3=0
            bArr2=bytearray().zfill(3)
            for i4 in [0,1,2]:
                i5=i2+i4
                i6=i5+1
                if i6<=len(bArr)-1 and bArr[i6]<255:
                    r5=bArr[i5] 
                    r6=bArr[i6] 
                    a=(((r5& 255) << ((i4 * 2) + 2)) & 255)
                    b=((r6 & 255) >> (((2 - (i4 + 1)) * 2) + 2))
                    aa=a | b            
                    bArr2[i4]=aa    
                    i3=i3+1
            i7=0
            while i7<=i3-1:
                mybyteArray.append(bArr2[i7])
                i7=i7+1
        return mybyteArray
    
    def encrypt(self,bt:bytes):
        sb = ""
        print(bt)
        for i in range(0,len(bt),3):
            bArr2 = bytearray().zfill(4)
            b = 0;
            for i2 in range(0,3):
                i3 = i + i2;
                if i3 <= len(bt)-1:
                    bArr2[i2] = (b | ((bt[i3] & 255) >> ((i2 * 2) + 2)));
                    b = ((((bt[i3] & 255) << (((2 - i2) * 2) + 2)) & 255) >> 2);
                else:
                    bArr2[i2] = b;
                    b = 0x40;  
                
            bArr2[3] = b;
            for  i4  in range(0,4):
                right=(63+255)%255
                if (bArr2[i4] <= right):
                    sb=sb+self.staticArray[bArr2[i4]]
                else:
                    sb=sb+'=';
        return sb
    

def main():
    modifiedBase64= ModifiedBase64();
    
    strIn = "DJczEWU2DwPuDwDwYJOyDG==";
    print(strIn)
    uuidByte=modifiedBase64.decrypt(strIn)
    uuidStr=str(uuidByte,"utf8")
    print(uuidStr)
    ss=modifiedBase64.encrypt(uuidByte)
    print(ss)
  
        
if __name__ == '__main__':
    main()
    