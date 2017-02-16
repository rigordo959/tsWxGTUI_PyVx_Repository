*
* Analog Input Point Identification <860625.1545>
*
$list off
*
*     ***** Validated/Dummy Analog Inputs
      integer main_stm_prs_pid         ! main steam pressure (PU)
                                       ! POSITION CONTROL = .not. flow_control
                                       ! if (POSITION CONTROL) then
                                       !   value = 1.0
                                       ! else if (main_stm_prs_in1 VALID) then
                                       !   value = main_stm_prs_in1
                                       ! else
                                       !   value = 1.0
                                       ! endif
          parameter ( main_stm_prs_pid =                    1 )
*
      integer rht_stm_prs_pid          ! reheat steam pressure (PU) (Spare)
                                       ! POSITION CONTROL = .not. flow_control
                                       ! if (POSITION CONTROL) then
                                       !   value = 1.0
                                       ! else if (rht_stm_prs_in1 VALID) then
                                       !   value = rht_stm_prs_in1
                                       ! else
                                       !   value = main_stm_prs_pid
                                       ! endif
          parameter ( rht_stm_prs_pid  = main_stm_prs_pid + 1 )
*
      integer chest_prs_pid            ! chest pressure (PU)
                                       ! if (chest_prs_in1 VALID) then
                                       !   value = chest_prs_in1
                                       ! else
                                       !   value = main_stm_prs_pid
                                       ! endif
          parameter ( chest_prs_pid    = rht_stm_prs_pid  + 1 )
*
$page
*
      integer power_load_pid           ! turbine/generator load (PU)
                                       ! if (power_load_in1 VALID) then
                                       !   value = generator_ld_pid
                                       ! else
                                       !   value = turbine_ld_pid
                                       ! endif
          parameter ( power_load_pid   = chest_prs_pid    + 1 )
*
      integer generator_ld_pid         ! generator load (PU)
                                       ! if (power_load_in1 VALID) then
                                       !   value = power_load_in1
                                       ! else
                                       !   value = turbine_ld_pid
                                       ! endif
          parameter ( generator_ld_pid = power_load_pid   + 1 )
*
      integer turbine_ld_pid           ! turbine load (PU)
                                       ! cv_stroke = cv_pos_in1
                                       !
                                       ! sv_stroke = ( svbpv_pos_in1 *
                                       !               svbpv1_size     ) +
                                       !             ( svbpv_pos_in2 *
                                       !               svbpv2_size     )
                                       !
                                       ! if ( sv_stroke .le. ( svbpv1_size +
                                       !      svbpv2_size ) ) then
                                       !
                                       !   turbine_flow = main_stm_prs_in1 *
                                       !                  min( cv_stroke,
                                       !                       sv_stroke )
                                       ! else
                                       !   turbine_flow = main_stm_prs_in1 *
                                       !                  cv_stroke
                                       ! endif
                                       !
                                       ! value = turbine_flow
          parameter ( turbine_ld_pid   = generator_ld_pid + 1 )
*
      integer load_lim_pos_pid         ! load limit pos (PU)
                                       ! if (ld_lim_pos_in1 VALID) then
                                       !   value = ld_lim_pos_in1
                                       ! else
                                       !   value = power_load_pid
                                       ! endif
          parameter ( load_lim_pos_pid = turbine_ld_pid  + 1 )
*
      integer load_set_pos_pid         ! load set position (PU)
                                       ! if (ld_set_pos_in1 VALID) then
                                       !   value = ld_set_pos_in1
                                       ! else
                                       !   value = power_load_pid
                                       ! endif
          parameter ( load_set_pos_pid = load_lim_pos_pid + 1 )
*
$page
*
      integer shaft_speed_pid          ! shaft speed (RPM)
                                       ! if (BREAKER CLOSED) then
                                       !   value = rated_rpm
                                       ! else if (shaft_speed_in1 VALID) then
                                       !   value = shaft_speed_in1
                                       ! else
                                       !   value = rated_rpm
                                       ! endif
          parameter ( shaft_speed_pid  = load_set_pos_pid + 1 )
*
      integer spd_set_pos_pid          ! speed set position (RPM)   (Lynn MK3)
                                       ! if (spd_set_pos_in1 VALID) then
                                       !   value = spd_set_pos_in1
                                       ! else
                                       !   value = shaft_speed_pid
                                       ! endif
          parameter ( spd_set_pos_pid  = shaft_speed_pid  + 1 )
*
$page
*
      integer svbpv_pos_pid            ! stop valve (max) position (PU)
                                       ! svb1_pos = svbpv_pos_in1
                                       ! svb2_pos = svbpv_pos_in2
                                       ! if (svb1_pos .le. svb1_llmit) then
                                       !   svb1_stroke = svb1_llmit
                                       ! else if (svb1_pos.ge.svb1_hlmit) then
                                       !   svb1_stroke = svb1_hlmit
                                       ! else
                                       !   svb1_stroke = svbpv_pos_in1
                                       ! endif
                                       ! svb1_stroke = amax1( svb1_stroke, 0 )
                                       ! if (svb2_pos .le. svb2_llmit) then
                                       !   svb2_stroke = svb2_llmit
                                       ! else if (svb2_pos.ge.svb2_hlmit) then
                                       !   svb2_stroke = svb2_hlmit
                                       ! else
                                       !   svb2_stroke = svbpv_pos_in2
                                       ! endif
                                       ! svb2_stroke = amax1( svb2_stroke, 0 )
                                       ! if (two SV positions) then
                                       !   flow1 = svb1_stroke*svb1_size
                                       !   flow2 = svb2_stroke*svb2_size
                                       !   value = (flow1+flow2)/
                                       !           (svb1_size+svb2_size)
                                       ! else if (one SV position) then
                                       !   value = svb1_stroke
                                       ! else
                                       !   value = 1.0e+38
                                       ! endif
          parameter ( svbpv_pos_pid    = spd_set_pos_pid  + 1 )
*
      integer cv_pos_pid               ! control valve position (PU)
                                       ! if (cv_pos_in1 VALID) then
                                       !   value = cv_pos_in1
                                       ! else if (below low_limit) then
                                       !   value = low_limit
                                       ! else
                                       !   value = high_limit
                                       ! endif
          parameter ( cv_pos_pid       = svbpv_pos_pid    + 1 )
*
$page
*
      integer main_stm_tmp_pid         ! main steam temperature (^F)
                                       ! if (both TC inputs VALID) then
                                       !   value = avg( main_stm_tmp_in1,
                                       !                main_stm_tmp_in2)
                                       ! else if (one TC input VALID) then
                                       !   value = one( main_stm_tmp_in1,
                                       !                main_stm_tmp_in2)
                                       ! else
                                       !   value = rated_ms_tmp
                                       ! endif
          parameter ( main_stm_tmp_pid = cv_pos_pid       + 1 )
*
      integer rht_stm_tmp_pid          ! reheat steam temperature (^F) (Spare)
                                       ! if (both TC inputs VALID) then
                                       !   value = avg( rht_stm_tmp_in1,
                                       !                rht_stm_tmp_in2)
                                       ! else if (one TC input VALID) then
                                       !   value = one( rht_stm_tmp_in1,
                                       !                rht_stm_tmp_in2)
                                       ! else
                                       !   value = rated_rs_tmp
                                       ! endif
          parameter ( rht_stm_tmp_pid  = main_stm_tmp_pid + 1 )
*
$page
*
      integer hp_shell_tmp_pid         ! hp inlet shell temp (^F)
                                       ! if (both TC inputs VALID) then
                                       !   value = avg( hp_shell_tmp_in1,
                                       !                hp_shell_tmp_in2)
                                       ! else if (one TC input VALID) then
                                       !   value = one( hp_shell_tmp_in1,
                                       !                hp_shell_tmp_in2)
                                       ! else
                                       !   value = main_stm_tmp
                                       ! endif
          parameter ( hp_shell_tmp_pid = rht_stm_tmp_pid  + 1 )
*
      integer rh_bowl_tmp_pid          ! rh inlet shell temp (^F)
                                       ! if (both TC inputs VALID) then
                                       !   value = avg( rh_bowl_tmp_in1,
                                       !                rh_bowl_tmp_in2)
                                       ! else if (one TC input VALID) then
                                       !   value = one( rh_bowl_tmp_in1,
                                       !                rh_bowl_tmp_in2)
                                       ! else
                                       !   value = rht_stm_tmp
                                       ! endif
          parameter ( rh_bowl_tmp_pid  = hp_shell_tmp_pid + 1 )
*
      integer xo_shell_tmp_pid         ! rh exhaust shell temp (^F)
                                       ! if (both TC inputs VALID) then
                                       !   value = avg( xo_shell_tmp_in1,
                                       !                xo_shell_tmp_in2)
                                       ! else if (one TC input VALID) then
                                       !   value = one( xo_shell_tmp_in1,
                                       !                xo_shell_tmp_in2)
                                       ! else
                                       !   value = rh_bowl_tmp
                                       ! endif
          parameter ( xo_shell_tmp_pid = rh_bowl_tmp_pid + 1 )
*
$page
*
      integer cv_inner_tmp_pid         ! cv inner metal temp (^F)
                                       ! if (both TC inputs VALID) then
                                       !   value = avg( cv_inner_tmp_in1,
                                       !                cv_inner_tmp_in2)
                                       ! else if (one TC input VALID) then
                                       !   value = one( cv_inner_tmp_in1,
                                       !                cv_inner_tmp_in2)
                                       ! else
                                       !   value = main_stm_tmp
                                       ! endif
          parameter ( cv_inner_tmp_pid = xo_shell_tmp_pid + 1 )
*
      integer cv_outer_tmp_pid         ! cv outer metal temp (^F)
                                       ! if (both TC inputs VALID) then
                                       !   value = avg( cv_outer_tmp_in1,
                                       !                cv_outer_tmp_in2)
                                       ! else if (one TC input VALID) then
                                       !   value = one( cv_outer_tmp_in1,
                                       !                cv_outer_tmp_in2)
                                       ! else
                                       !   value = cv_inner_tmp
                                       ! endif
          parameter ( cv_outer_tmp_pid = cv_inner_tmp_pid + 1 )
*
      integer tc_reference_pid         ! thermocouple ref temp (^F)
                                       ! if (tc_reference_in1 VALID) then
                                       !   value = tc_reference_in1
                                       ! else
                                       !   value = 80
                                       ! endif
          parameter ( tc_reference_pid = cv_outer_tmp_pid + 1 )
*
$page
*
*     ***** Measured Analog Inputs *****
      integer main_stm_prs_in1         ! main steam pressure (PU)
                                       ! value = poly(MEASUREMENT)/
                                       !         rated_ms_prs
          parameter ( main_stm_prs_in1 = tc_reference_pid + 1 )
*
      integer rht_stm_prs_in1          ! reheat steam pressure (PU) (Spare)
                                       ! value = poly(MEASUREMENT)/
                                       !         rated_rs_prs
          parameter ( rht_stm_prs_in1  = main_stm_prs_in1 + 1 )
*
      integer chest_prs_in1            ! chest pressure (PU)
                                       ! value = poly(MEASUREMENT)/
                                       !         rated_ms_prs
          parameter ( chest_prs_in1    = rht_stm_prs_in1  + 1 )
*
      integer power_load_in1           ! turbine/generator load (PU)
                                       ! value = poly(MEASUREMENT)/
                                       !         rated_load_mw
          parameter ( power_load_in1   = chest_prs_in1    + 1 )
*
      integer load_lim_pos_in1         ! load limit pos (PU)
                                       ! value = poly(MEASUREMENT)
          parameter ( load_lim_pos_in1 = power_load_in1  + 1 )
*
      integer load_set_pos_in1         ! load set position (PU)
                                       ! value = poly(MEASUREMENT)
          parameter ( load_set_pos_in1 = load_lim_pos_in1 + 1 )
*
$page
*
      integer shaft_speed_in1          ! shaft speed (RPM )
                                       ! value = poly(MEASUREMENT)
          parameter ( shaft_speed_in1  = load_set_pos_in1 + 1 )
*
      integer spd_set_pos_in1          ! speed set position (RPM)   (Lynn MK3)
                                       ! value = poly(MEASUREMENT)
          parameter ( spd_set_pos_in1  = shaft_speed_in1  + 1 )
*
      integer svbpv_pos_in1            ! stop valve #1 valve position (PU)
                                       ! value = poly(MEASUREMENT)
          parameter ( svbpv_pos_in1    = spd_set_pos_in1  + 1 )
*
      integer svbpv_pos_in2            ! stop valve #2 valve position (PU)
                                       ! value = poly(MEASUREMENT)
          parameter ( svbpv_pos_in2    = svbpv_pos_in1    + 1 )
*
      integer cv_pos_in1               ! control valve position (PU)
                                       ! value = poly(MEASUREMENT)
          parameter ( cv_pos_in1       = svbpv_pos_in2    + 1 )
*
$page
*
      integer main_stm_tmp_in1         ! main steam TC#1 temperature (^F)
                                       ! value = poly(MEASUREMENT)
          parameter ( main_stm_tmp_in1 = cv_pos_in1       + 1 )
*
      integer main_stm_tmp_in2         ! main steam TC#2 temperature (^F)
                                       ! value = poly(MEASUREMENT)
          parameter ( main_stm_tmp_in2 = main_stm_tmp_in1 + 1 )
*
      integer rht_stm_tmp_in1          ! reheat steam TC#1 temperature (^F)
                                       ! value = poly(MEASUREMENT)
          parameter ( rht_stm_tmp_in1  = main_stm_tmp_in2 + 1 )
*
      integer rht_stm_tmp_in2          ! reheat steam TC#2 temperature (^F)
                                       ! value = poly(MEASUREMENT)
          parameter ( rht_stm_tmp_in2  = rht_stm_tmp_in1  + 1 )
*
      integer hp_shell_tmp_in1         ! hp inlet TC#1 shell temp (^F)
                                       ! value = poly(MEASUREMENT)
          parameter ( hp_shell_tmp_in1 = rht_stm_tmp_in2  + 1 )
*
      integer hp_shell_tmp_in2         ! hp inlet TC#2 shell temp (^F)
                                       ! value = poly(MEASUREMENT)
          parameter ( hp_shell_tmp_in2 = hp_shell_tmp_in1 + 1 )
*
      integer rh_bowl_tmp_in1          ! rh inlet shell TC#1 temp (^F)
                                       ! value = poly(MEASUREMENT)
          parameter ( rh_bowl_tmp_in1  = hp_shell_tmp_in2 + 1 )
*
      integer rh_bowl_tmp_in2          ! rh inlet shell TC#2 temp (^F)
                                       ! value = poly(MEASUREMENT)
          parameter ( rh_bowl_tmp_in2  = rh_bowl_tmp_in1  + 1 )
*
      integer xo_shell_tmp_in1         ! rh exhaust shell TC#1 temp (^F)
                                       ! value = poly(MEASUREMENT)
          parameter ( xo_shell_tmp_in1 = rh_bowl_tmp_in2  + 1 )
*
      integer xo_shell_tmp_in2         ! rh exhaust shell TC#2 temp (^F)
                                       ! value = poly(MEASUREMENT)
          parameter ( xo_shell_tmp_in2 = xo_shell_tmp_in1 + 1 )
*
$page
*
      integer cv_inner_tmp_in1         ! cv inner metal TC#1 temp (^F)
                                       ! value = poly(MEASUREMENT)
          parameter ( cv_inner_tmp_in1 = xo_shell_tmp_in2 + 1 )
*
      integer cv_inner_tmp_in2         ! cv inner metal TC#2 temp (^F)
                                       ! value = poly(MEASUREMENT)
          parameter ( cv_inner_tmp_in2 = cv_inner_tmp_in1 + 1 )
*
      integer cv_outer_tmp_in1         ! cv outer metal TC#1 temp (^F)
                                       ! value = poly(MEASUREMENT)
          parameter ( cv_outer_tmp_in1 = cv_inner_tmp_in2 + 1 )
*
      integer cv_outer_tmp_in2         ! cv outer metal TC#2 temp (^F)
                                       ! value = poly(MEASUREMENT)
          parameter ( cv_outer_tmp_in2 = cv_outer_tmp_in1 + 1 )
*
      integer tc_reference_in1         ! thermocouple ref temp (^F)
                                       ! value = poly(MEASUREMENT)
          parameter ( tc_reference_in1 = cv_outer_tmp_in2 + 1 )
*
      integer airnd_count              ! number of analog inputs
          parameter ( airnd_count      = tc_reference_in1     )
*
$list on
*
