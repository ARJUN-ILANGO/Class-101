import dropbox 

class TransferData:
    def init (self,acess_Token):
        self.acess_Token=acess_Token
    
    def upload_file(self,file_from,_file_to):
        """ Upload A file to DropBox using API V2
        """
        dbx=dropbox.DropBox(acess_Token)
        with open(self,file_from,'rb')as f:
            dbx.files_upload(f.read(),file_to)
    
    def main():
        acess_Token='sl.Ar0sJPAijXojXS3GF2JyR3o8wFy55AUlmquF-hoZLthohnVclOLQ6abZbtEQJ4ABDZ75diR88mVGDwNZuRIwT26tOKxjr2g_iefatYFhqsNln05QR9XXsiCX8-9pR2yPVa_G5Nc'
        transferData = TransferData(acess_Token)

        file_from='test.txt'
        file_to='/test_dropbox/test.txt'

        transferData.upload_file(file_from,file_to)
if __name__ == '__main__' :
    main()
