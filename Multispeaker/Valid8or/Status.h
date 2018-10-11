/*------------------------------------------------------------*
 |                  OFFICIAL USE ONLY                         |
 | May be exempt from public release under the Freedom of     |
 | Information Act (5 U.S.C 552), exemption number and        |
 | category:                                                  |
 |                                                            |
 | Exemptions 3, 5, 7                                         |
 |                                                            |
 | Department of Energy review required before public release |
 |                                                            |
 | Name / Org:  Wayne Meitzler / D7P25                        |
 | Date:        March 2018                                    |
 |                                                            |
 | Guidance (if applicable) Client Correspondence             |
 *------------------------------------------------------------*/

//----------------------------------------------------------------------------------------------------------------------------------
// Copyright (c) 2013-2018, Pacific Northwest National Laboratory
// This software is subject to copyright protection under the laws of the United States and other countries
// All rights in this computer software are reserved by Pacific Northwest National Laboratory (PNNL)
// Operated by Battelle for the U.S. Department of Energy
//----------------------------------------------------------------------------------------------------------------------------------

#ifndef STATUS_H
#define STATUS_H

enum class Status {
	Ready,      // Operation is ready to run
	Running,    // Operation is running
	Successful, // Operation exited normally (EXIT_SUCCESS for subprocesses)
	Failed,     // Operation did not exit normally (anything other than EXIT_SUCCESS for subprocesses)
	Crashed,    // Operation failed to start or crashed (exited with CrashExit for subprocesses)
	Canceled,   // Operation was canceled by the user
};

#endif // STATUS_H
