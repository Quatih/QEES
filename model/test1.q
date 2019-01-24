//This file was generated from UPPAAL 4.0.2 (rev. 2491), August 2006

/*

*/
// first check for the end of simulation, then check for all UHF jobs executed, then the balance of L band jobs and X band jobs
E<> End_S.Lock && job_count[3] == 11 && job_count[0] == job_count[1] && job_count[2] == (job_count[0] + job_count[1])