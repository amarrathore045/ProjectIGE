#This is the the file which is used to  run the server
#We will be providing the required documents along with this file
#Relavent Documentation is written along with the code
#For further documenrtation refer the attached documentation file

from website import create_app

app = create_app()

if __name__ == '__main__':
    #Everytime a change is made in any file, the server will 
    #automitacally re-run itself
    app.run(debug=True)