/* Billing Utilities */

#include <stdio.h>
#include "clock.h"

time_string start_time;
date_string start_date;
time_string end_time;
date_string end_date;
float billing_time;

float
timer_seconds(time_string *timer) {

  int hours;   /* 0..23 */
  int minutes; /* 0..59 */
  int seconds; /* 0..59 */
  float result;

  hours   = 10 * ((int)(timer->hour[0]) - (int)('0')) +
    ((int)(timer->hour[1]) - (int)('0'));

  minutes = 10 * ((int)(timer->minute[0]) - (int)('0')) +
    ((int)(timer->minute[1]) - (int)('0'));

  seconds = 10 * ((int)(timer->second[0]) - (int)('0')) +
    ((int)(timer->second[1]) - (int)('0'));

  result = ((float)(seconds)) +
    ((float)(60.0) * ((float)(minutes))) +
    ((float)(3600.0) * ((float)(hours)));
#if (0)
  printf("timer_seconds: hours=%d; minutes=%d; seconds=%d; result=%f\n",
	 hours, minutes, seconds, result);
#endif
  return (result);

} /* timer_seconds */

float
timer_days(date_string *timer) {

  /* This function enables the determination of elapsed
   * time despite midnight and month clock transitions. */

  int month;          /* 1..12 */
  int day;            /* 1..31 */
  int year;           /* 1900..1999 */
  int days_per_month; /* 28..31 */
  int month_number;   /* 1..12 */
  int day_number;     /* 0..366 */
  int year_number;    /* 1900..1999 */
  float accumulated_days;
  float result;

  month   = 10 * ((int)(timer->month[0]) - (int)('0')) +
    ((int)(timer->month[1]) - (int)('0'));

  day     = 10 * ((int)(timer->day[0]) - (int)('0')) +
    ((int)(timer->day[1]) - (int)('0'));

  year    = 10 * ((int)(timer->year[0]) - (int)('0')) +
    ((int)(timer->year[1]) - (int)('0')) + 1900;

  day_number = 0;
  for (month_number = 1; month_number <= (month - 1); month_number++) {
    if (month_number == 2) days_per_month = 28;
    else if (month_number == 4) days_per_month = 30;
    else if (month_number == 6) days_per_month = 30;
    else if (month_number == 9) days_per_month = 30;
    else if (month_number == 11) days_per_month = 30;
    else days_per_month = 31;
  }
  day_number = day_number + days_per_month;
  accumulated_days = (float)(day + day_number);
  for (year_number = 1900; year_number <= (year - 1); year_number++){
    if ((year % 4) == 0)
      accumulated_days = accumulated_days + (float)(366.0);
    else
      accumulated_days = accumulated_days + (float)(365.0);
  }
  result = accumulated_days;
#if (0)
  printf("timer_days: month=%d; day=%d; year=%d; result=%f\n",
	 month, day, year, result);
#endif
  return (result);
} /* timer_days */

void
start_billing() {
  get_time(&start_time);
  get_date(&start_date);
#if (0)
  printf("start_time=%s\n",&start_time);
  printf("start_date=%s\n",&start_date);
#endif
} /* start_billing */

void
stop_billing() {
  get_time(&end_time);
  get_date(&end_date);
#if (0)
  printf("end_time=%s\n",&end_time);
  printf("end_date=%s\n",&end_date);
#endif
} /* stop_billing */

void
report_billing() {

  const float seconds_per_day = (float)(86400.0);

  int hours;   /* 0..23 */
  int minutes; /* 0..59 */
  int seconds; /* 0..59 */
  float elapsed_time;
  float billing_seconds;
  float billing_days;

  billing_seconds = timer_seconds(&end_time)
    - timer_seconds(&start_time);

  billing_days = timer_days(&end_date)
    - timer_days(&start_date);

  if (billing_seconds >= 0.0) {
    billing_time = (seconds_per_day * billing_days)
      + billing_seconds;
  }
  else {
    billing_time = (seconds_per_day * (billing_days - (float)(1.0)))
      + billing_seconds;
  }

  elapsed_time = billing_time;
  hours = (int)(elapsed_time / (float)(3600.0));
  elapsed_time = elapsed_time - (((float)(hours)) * (float)(3600.0));
  minutes = (int)(elapsed_time / 60.0);
  elapsed_time = elapsed_time - (((float)(minutes)) * (float)(60.0));
  seconds = (int)(elapsed_time);
  printf("Elapsed Time = %2.2d:%2.2d:%2.2d\n",
	 hours, minutes, seconds);
} /* report_billing */

#if (0)
int main() {

  int number;

  printf("Billing Test.\n");
  start_billing();

  printf("Enter a number:");
  scanf("%d", &number);

  stop_billing();
  report_billing();
  return (0);

} /* main */
#endif
