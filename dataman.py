
class dataoperate():
      def __init__(self,data,url_now):
          self.data=data
          self.url_now=url_now
          
       
      def data_save(self):
          with open('data/'+self.url_now+'.txt','w') as file_object:
              
                  file_object.write(self.url_now+'\n'+self.data+'\nover')
      def url_save(self):
          with open('urllist.txt','a') as file_object:
              file_object.write(self.url_now+'\n')
      def url_list_read(self):
          url_total=[]
          with open('urllist.txt','r') as file_object:
              for line in file_object:
                  url_total.append(line.rstrip())
              print(url_total)
              return url_total
