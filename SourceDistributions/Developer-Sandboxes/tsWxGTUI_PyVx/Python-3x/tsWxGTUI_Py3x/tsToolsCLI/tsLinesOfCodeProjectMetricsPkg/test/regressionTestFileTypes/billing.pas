{$linesize:132 $line+ $symtab-
 $title: 'Billing Utilities, (C) 1983 RS Gordon, d/b/a COMPUTER SOLUTIONS' }

{$include: 'banner.pif' }
{$include: 'clock.pif' }
{$include: 'billing.pif' }

{$subtitle: 'External Procedure Declarations' $page+ }
IMPLEMENTATION of billing ;

  USES clock ( get_time, get_date, time_string, date_string ) ;

{$subtitle: 'Start_Billing Procedure' $page+ }
PROCEDURE start_billing ;

  begin
    get_time( start_time ) ;
    get_date( start_date )
  end ;

{$subtitle: 'Timer_Seconds Function' $page+ }
FUNCTION timer_seconds ( VAR timer: time_string ): real ;

  VAR
    hours: 0..23 ;
    minutes: 0..59 ;
    seconds: 0..59 ;

  begin
    hours   := 10 * ( ord( timer[ 1 ] ) - ord( '0' ) ) +
                    ( ord( timer[ 2 ] ) - ord( '0' ) ) ;
    minutes := 10 * ( ord( timer[ 4 ] ) - ord( '0' ) ) +
                    ( ord( timer[ 5 ] ) - ord( '0' ) ) ;
    seconds := 10 * ( ord( timer[ 7 ] ) - ord( '0' ) ) +
                    ( ord( timer[ 8 ] ) - ord( '0' ) ) ;

    timer_seconds := float( seconds ) +
                     60.0 * float( minutes ) +
                     3600.0 * float( hours ) ;
  end ;

{$subtitle: 'Timer_Days Function' $page+ }
FUNCTION timer_days ( VAR timer: date_string ): real ;

  { This function enables the determination of elapsed
    time despite midnight and month clock transitions. }

  VAR
    month: 1..12 ;
    day: 1..31 ;
    year: 1980..1999 ;
    days_per_month: 28..31 ;
    month_number: 1..12 ;
    day_number: 0..366 ;
    year_number: 1980..1999 ;
    accumulated_days: real ;

  begin
    month   := 10 * ( ord( timer[ 1 ] ) - ord( '0' ) ) +
                    ( ord( timer[ 2 ] ) - ord( '0' ) ) ;
    day     := 10 * ( ord( timer[ 4 ] ) - ord( '0' ) ) +
                    ( ord( timer[ 5 ] ) - ord( '0' ) ) ;
    year    := 10 * ( ord( timer[ 7 ] ) - ord( '0' ) ) +
                    ( ord( timer[ 8 ] ) - ord( '0' ) ) + 1900 ;

    day_number := 0 ;
    for month_number := 1 to ( month - 1 )
      do begin
        if month_number = 2 then days_per_month := 28
        else if month_number = 4 then days_per_month := 30
        else if month_number = 6 then days_per_month := 30
        else if month_number = 9 then days_per_month := 30
        else if month_number = 11 then days_per_month := 30
        else days_per_month := 31 ;
        day_number := day_number + days_per_month
      end ;
    accumulated_days := float( day + day_number ) ;
    for year_number := 1980 to ( year - 1 )
      do begin
        if ( year mod 4 ) = 0 then
          accumulated_days := accumulated_days + 366.0
        else
          accumulated_days := accumulated_days + 365.0 ;
      end ;
    timer_days := accumulated_days ;
  end ;

{$subtitle: 'Stop_Billing Procedure' $page+ }
PROCEDURE stop_billing ;

  begin
    get_time( end_time ) ;
    get_date( end_date )
  end ;

{$subtitle: 'Report_Billing Procedure' $page+ }
PROCEDURE report_billing ;

  CONST
    seconds_per_day = 86400.0 ;

  VAR
    billing_seconds: real ;
    billing_days: real ;
    hours:   0..23 ;
    minutes: 0..59 ;
    seconds: 0..59 ;
    elapsed_time: real ;

  begin
    billing_seconds := timer_seconds( end_time ) - timer_seconds( start_time ) ;
    billing_days := timer_days( end_date ) - timer_days( start_date ) ;

    if billing_seconds >= 0.0 then
      billing_time := ( seconds_per_day * billing_days ) + billing_seconds
    else
      billing_time := ( seconds_per_day * ( billing_days - 1.0 ) ) + billing_seconds ;

    elapsed_time := billing_time ;
    hours := trunc( elapsed_time / 3600.0 ) ;
    elapsed_time := elapsed_time - ( float( hours ) * 3600.0 ) ;
    minutes := trunc( elapsed_time / 60.0 ) ;
    elapsed_time := elapsed_time - ( float( minutes ) * 60.0 ) ;
    seconds := trunc( elapsed_time ) ;
    writeln ( Output, 'Elapsed Time = ', hours:2, ':', minutes:2, ':', seconds:2 )
  end ;

begin
end.

