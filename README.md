# file_search
A file searcher in python that is better than file exxplorer .More inside the readme file

#PLZ NOTE - this is my 1st project on Github so if there is anything wrong please let me know . Im not new to programming just new to GitHub . Thankyou :)\
          - this was built on a windows system hence may not work on mac and linux as there storage systems work differently

#How does this work?
1 = A list known as cache is built which in my case goes into my root file ie c:\\ and searches for all the files sub-dirs and all the files even inside of them
2 = all of them are stored inside the cache list
3 = Note : Its important to note how these files and dirs are stored . The complete path from the C:\\ is stored in the cache
4 = when someone wants to search some keyword , the keyword is converted into lowercase
5 = each element is compared to find which one matches

6 = Note : Program only searches the keywords starting from the last //
             The way windows stores complete paths is like C:\\Users\\user1\\Desktop\\solar
             In this example im assuming that solar is a directory and it has 3 file named 1.txt , 2.txt , 3.txt
             Hence we have 4 paths now : 
             C:\\Users\\user1\\Desktop\solar
             C:\\Users\\user1\\Desktop\\solar\\1.txt
             C:\\Users\\user1\\Desktop\\solar\\2.txt
             C:\\Users\\user1\\Desktop\\solar\\3.txt
             If my keyword is "solar" it will show all these 4 . So what i did was that the program sees the last '\\' and sees whats written at the end of each   
             string so now we only get 1 result that is C:\\Users\\user1\\Desktop\solar

7 = all the correct answers are printed
8 = we also use watchdog library . The watchdog library makes sure that if some change is made to the file system while the program is running . Those changes will be written into the cache so when you search u get the right results . 

I HOPE U LIKE IT
