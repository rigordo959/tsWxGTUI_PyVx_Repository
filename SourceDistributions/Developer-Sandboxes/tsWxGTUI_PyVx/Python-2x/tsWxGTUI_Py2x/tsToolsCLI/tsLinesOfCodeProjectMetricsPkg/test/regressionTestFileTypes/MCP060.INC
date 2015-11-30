*
*     Measurement & Control Unit Configuration Data Base <860912.1030>
*
*****$list off
*
      common /mcu_dbase/ mcu_dbasei( mcui_count ),
     &                   mcu_dbaser( mcur_count ),
*
     &                   scan_log, provox_simulate, simulate_time,
*                        ***** mcu inputs from data base
     &                   mw_feedback, slc_feedback, flow_control,
     &                   rated_rpm, regulation, rated_to_vwo,
     &                   rated_stm_tmp, rated_rht_tmp,
     &                   control_type, reheat_type, admiss_type,
     &                   sv1_svb_limit, sv2_svb_limit, cv_wo_limit,
*                        ***** mcu outputs to data base
     &                   numb_sv_mtrs, rated_stm_psi, rated_rht_psi,
     &                   rated_mw_load, fa_pa_knob_angle,
     &                   ss_stroke_t, ls_stroke_t, ll_stroke_t,
     &                   svb1_flow_cap, svb1_stroke_t, svb1_hsm,
     &                   svb1_svbo, svb1_ht, svb1_lt, svb1_svbc,
     &                   svb2_flow_cap, svb2_stroke_t, svb2_hsm,
     &                   svb2_svbo, svb2_ht, svb2_lt, svb2_svbc,
     &                   cv_vo, cv_ht, cv_lt, cv_vc,
     &                   cv_stroke_t, turbine_flow
*
*     data base entry type identification
*
      integer            mcu_dbasei
      real               mcu_dbaser
*
      logical            scan_log, provox_simulate
      logical            mw_feedback, slc_feedback, flow_control
*
      real               simulate_time
      real               rated_rpm, regulation, rated_to_vwo
      real               rated_mw_load, fa_pa_knob_angle
      real               rated_stm_tmp, rated_rht_tmp
      real               sv1_svb_limit, sv2_svb_limit, cv_wo_limit
*
      integer            numb_sv_mtrs
      real               rated_stm_psi, rated_rht_psi
      real               ss_stroke_t, ls_stroke_t, ll_stroke_t
      real               svb1_flow_cap, svb1_stroke_t, svb1_hsm
      real               svb1_svbo, svb1_ht, svb1_lt, svb1_svbc
      real               svb2_flow_cap, svb2_stroke_t, svb2_hsm
      real               svb2_svbo, svb2_ht, svb2_lt, svb2_svbc
      real               cv_vo, cv_ht, cv_lt, cv_vc
      real               cv_stroke_t, turbine_flow
*
      integer control_type
*
          integer mhc_type               ! Schdy MHC
              parameter ( mhc_type = 1 )
*
          integer ehc1_type              ! Schdy EHC Mark 1
              parameter ( ehc1_type = 2 )
*
          integer ehc2_type              ! Schdy EHC Mark 2
              parameter ( ehc2_type = 3 )
*
          integer ehc3_type              ! Lynn EHC Mark 3
              parameter ( ehc3_type = 4 )
*
          integer rsm_type               ! Schdy RSM with Fisher CHIP
              parameter ( rsm_type  = 5 )
*
      integer reheat_type
*
          integer  non_reheat
              parameter ( non_reheat     = 1 )
*
          integer single_reheat
              parameter ( single_reheat  = 2 )
*
          integer double_reheat
              parameter ( double_reheat  = 3 )
*
      integer admiss_type
*
          integer sv_startup            ! fa/pa with startup on svbpv
              parameter ( sv_startup    =  1 )
*
          integer cv_startup            ! pa only with startup on ll
              parameter ( cv_startup    =  2 )
*
          integer ams_startup           ! fa/pa with startup on cv
              parameter ( ams_startup   =  3 )
*
*     PROVOX System Simulation Data Base
      common /provox_dbase/ provox_cycle,
     &                      provox_speed,
     &                      provox_temp,
     &                      provox_cle_pb
*
      real               provox_cycle
      real               provox_speed
      real               provox_temp
      integer            provox_cle_pb
*
*****$list on
*
