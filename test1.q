//This file was generated from UPPAAL 4.0.2 (rev. 2491), August 2006

/*

*/

E<> End_S.Lock && 
job_count[3] == 11 && // force all UHF
job_count[0] == job_count[1] && // balance l band jobs
job_count[0] > 4 && job_count[1] > 4 && job_count[2] > 4 // enforce no. of jobs