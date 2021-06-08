// C program to Open a File, Write in it, And Close the File
# include <stdio.h>
# include <string.h>

int main()
{
  
    // Declare the file pointer
    FILE *filePointer ;
      
    // Get the data to be written in file
    char dataToBeWritten[50] 
        = "This is content for OSS lab 1 submitted by Keshav";
  
    // Open the file using fopen()
    // in write mode using "w" attribute
    filePointer = fopen("file1.txt", "w") ;
      
    // Check if this filePointer is null
    // which maybe if the file does not exist
    if ( filePointer == NULL )
    {
        printf( "file failed to open." ) ;
    }
    else
    {
          
        printf("The file is now opened.\n") ;
          
        // Write the dataToBeWritten into the file
        if ( strlen (  dataToBeWritten  ) > 0 )
        {
              
            // writing in the file using fputs()
            fputs(dataToBeWritten, filePointer) ;   
            fputs("\n", filePointer) ;
        }
          
        // Closing the file using fclose()
        fclose(filePointer) ;
          
        printf("Data successfully written in file\n");
        printf("The file is now closed.") ;
    }
    return 0;        
}