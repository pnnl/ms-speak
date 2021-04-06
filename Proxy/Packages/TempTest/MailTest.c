#include <stdio.h>
#include <string.h>
#include <errno.h>

/*
int main() {
	char cmd[100];  // to hold the command.
	char to[] = "sample@example.com"; // email id of the recepient.
	char body[] = "SO rocks";    // email body.
	char tempFile[100];     // name of tempfile.
	char tempdir[80];
	
	//strcpy(tempFile,tempnam("/tmp","sendmail")); // generate temp file name.
	//char *mkdirectory = mkdtemp(strcpy(tempdir, "/tmp/sndmail"));
	//strcpy(tempFile,tempnam("/tmp","sendmail")); // generate temp file name.

	
    FILE* fp = tmpfile(); 
    if (fp == NULL) 
    { 
        puts("Unable to create temp file"); 
        return 0; 
    } 	
	
	//FILE *fp = fopen(tempFile,"w"); // open it for writing.
	fprintf(fp,"%s\n",body);        // write body to it.
	fclose(fp);             // close it.

	sprintf(cmd,"sendmail %s < %s",to,tempFile); // prepare command.
	system(cmd);     // execute it.

	return 0;
}

*/

int sendmail(const char *to, const char *from, 
			 const char *subject, const char *message)
{
    int retval = -1;
    FILE *mailpipe = popen("/usr/lib/sendmail -t", "w");
    if (mailpipe != NULL) {
        fprintf(mailpipe, "To: %s\n", to);
        fprintf(mailpipe, "From: %s\n", from);
        fprintf(mailpipe, "Subject: %s\n\n", subject);
        fwrite(message, 1, strlen(message), mailpipe);
        fwrite(".\n", 1, 2, mailpipe);
        pclose(mailpipe);
        retval = 0;
     }
     else {
         perror("Failed to invoke sendmail");
     }
     return retval;
}

// sudo apt-get install sendmail
// gcc MailTest.c -o MailTest
// add into icap
int main(int argc, char** argv)
{
	const char *to, *from, *subject, *message;

	to = "cmiller267@hotmail.com";
	from = "primary_colors@gmail.com";
	subject = "-- PRIMARY COLORS --";
	message = "GOT ANY COLORS FOR ME TODAY?";
	
	//to = "loskind@gmail.com";
	//from = "loskind@gmail.com";
	//to = "primco1400@gmail.com";
	//from = "primary_colors@gmail.com";
	//subject = "-- PRIMARY COLORS --";
	//message = "GOT ANY COLORS FOR ME TODAY?";
	
	//from = "alexander.thompson67@gmail.com";
	//to = "james.in.richland@gmail.com";
	//from = "james.in.richland@gmail.com";
	//subject = "SEND YOURSELF MAIL MUCH?";
	//message = "HA HA HA HA ?";
	
	/*to = "carl.miller@pnnl.gov";
	from = "primary_colors@gmail.com";
	subject = "MUTLI-SPEAK ALERT";
	message = "TEST OF MAIL SERVICE";*/
	
	printf("\nSending Mail to '%s', from '%s'\n", to, from );
	sendmail( to, from, subject, message );
	
	return 0;
}
