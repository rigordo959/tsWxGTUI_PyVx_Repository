***********************************************************************
*                                                                     *
*                       Program MCP  <870518.1427>                    *
*                                                                     *
***********************************************************************
*
* Purpose:
* --------
*
*     Initiate and supervise the analog and digital signal input/output
*     involving the Measurement and Control Unit.
*
*     Provide utility functions to enable other application programs
*     to perform analog and digital signal output.
*
* Algorithm:
* ----------
*
*     The MCP Program initializes a local data base and portions of
*     a global data base from data retrieved from one or more disc-
*     based I/O configuration files.
*
*     During its initialization sequence, MCP verifies that the con-
*     figuration is consistent both internally and with the Measure-
*     ment and Control Unit's reported function card configuration.
*
*     After initialization, MCP scans the analog and digital input
*     in a time sequence chosen to gather prioritized data as
*     rapidly as practical without incurring excessive overhead.
*
*     Analog signals are then converted from voltage to appropriate
*     engineering units and subjected to high and low limit tests and
*     to delta limit tests, where appropriate, for signal validation.
*     Changes in signal validity are reported via the ALARM procedure.
*
*     Digital signals are derived from physical signals, when avail-
*     able, or from "transition-level" tests of analog signals.
*
* Symbol Definition:
* ------------------
*
*     Parameters:
*
*         There are no parameters passed to this program.
*
*     System Commons:
*
*         /iodata/        - Measurement & Control Unit Status.
*
*     Local Commons:
*
*         /airnd_state/   - Analog  Input  Configuration Information.
*         /aornd_state/   - Analog  Output Configuration Information.
*         /asop_state/    - ASCII String Output Configuration Information.
*         /diw_state/     - Digital Input  Configuration Information.
*         /dolw_state/    - Digital Output Configuration Information.
*         /mcu_dbase/     - Measurement & Control Software Configuration.
*         /mcu_io_config/ - Measurement & Control Hardware Configuration.
*         /tc_ref_calc/   - Thermocouple Reference Conversion Data.
*         /tc_failure/    - Thermocouple & TC Reference Fault Status.
*
* Error Handling:
* --------------
*
*     All invalidated operating system service requests, invalidated
*     FORTRAN I/O formats and detected configuration inconsistencies
*     are treated as non-recoverable. Control terminates via the
*     system error message output routine "ERROR".
*
*     All sensor limit test faults/fault recoveries are treated as
*     recoverable. Fault status changes are reported via the system
*     fault message output routine "ALARM".
*
* Externals Referenced:
* --------------------
*
*     Task Control Utilities
*
*         ALARM            - outputs fault messages
*         ERROR            - outputs error messages
*         DBASEI           - inputs/outputs integers from data base
*         DBASEL           - inputs/outputs logicals from data base
*         DBASER           - inputs/outputs reals    from data base
*         GETMSG           - decodes Inter-task messages
*         PUTMSG           - encodes Inter-task messages
*         SENDRQ           - transmits Inter-task messages
*         WAIT             - programmatic time delay
*         WAITRQ           - receives Inter-task messages
*         SYSTEM_IO_DEVICE - determines availability of I/O device
*
* Heading:
* --------
*
*     Author(s):          LG Jackson & RS Gordon
*     Creation Date:      December 3, 1984
*
*****$page
*
* Revision History:
* ----------------
*
*     Number   Date      Author & Change Description
*     -------  --------  ---------------------------
*         2.0  05/05/92  RS Gordon revised design for CHIP interface.
*
*****$page
*
* Resource Requirements:
* ---------------------
*
*     MCP Program uses Task Control Utility Services to communicate
*     with other program.
*
*     It operates in real time and must remain memory resident.
*
*
* External Architecture:
* ----------------------
*
*     +--------+     +--------+     +---------+     +---------+
*     | VMS    |     | MCP    |     | CHIP    |     | Fisher  |
*     | Op.    |---->|        |<===>| MCU I/O |<===>| PROVOX  |
*     | System |     | Task   |     | Library |     |         |
*     +--------+     +--------+     +---------+     +---------+
*
*****$page
*
* Internal Architecture:
* ---------------------
*
*                            ANALOG_SCAN
*                                 |
*      +-------------+--------+---+---+-------------+---------------+
*      |             |        |       |             |               |
*   LOCK_MCU  AIR_SIMULATE  <AIR>  UNLOCK_MCU  MCP_ERROR_REPORT  <ERROR>
*
*
*                            DIGITAL_SCAN
*                                |
*         +---------+--------+---+---------------+
*         |         |        |                   |
*     LOCK_MCU   <ERROR>  UNLOCK_MCU       MCP_ERROR_REPORT
*
*
*                            DOLW_DRIVER
*                              |
*      +-----------------------+-----------------+------------+
*      |                       |                 |            |
*   LOCK_MCU             UNLOCK_MCU    MCP_ERROR_REPORT  <ERROR>
*
*****$page
*
*                         FAULT_SIGNAL_OUT
*                                 |
*                         +-------+-------+
*                         |               |
*                      <DBASEL>        <ERROR>
*
*
*                         INSTALL_CONFIG
*                               |
*
*                        INSTALL_LIMITS
*                               |
*       +---------------+-------+--------+----------------+
*       |               |                |                |
* INSTALL_POLY    <GET_AI_NAME>     SCAN_ALARM         <ERROR>
*
*
*                         INSTALL_POLY
*                               |
*              +----------------+----------------+
*              |                |                |
*         CONFIG_ALARM     SCAN_ALARM         <ERROR>
*
*
*                           LOCK_MCU
*                               |
*                            <LURQ>
*
*
*                                MCP
*                                 |
*      +--------------+-----------+----------+---------+--------+
*      |              |           |          |         |        |
* SCAN_RESET  SCAN_SLEEP  UPDATE_SIMULATOR   |  SCAN_OUTPUT  <SIGNON>
*                                            |               <WAITRQ>
*                                            |               <PUTMSG>
*                                            |               <SENDRQ>
*                                            |               <SIGNOFF>
*                                            |
*      +-----------------+------------+------+----+-------------+
*      |                 |            |           |             |
* ANALOG_SCAN  SPEED_VALIDATE  TC_VALIDATE  CALIBRATAION  DIGITAL_SCAN
*
*
*
*                       MCP_ERROR_REPORT
*                               |
*                      +--------+-------+
*                      |                |
*                   <ALARM>          <ERROR>
*
*
*                        SPEED_VALIDATE
*                               |
*        +---------+---------+--+-------+--------+--------+------+-------+
*        |                   |
* SET_SHAFT_SPEED       NON_TC_RATE
*
*
*                          SCAN_ALARM
*                               |
*                            <ALARM>
*
*
*                         SCAN_OUTPUT
*                               |
*                 +-------------+-------------+
*                 |             |             |
*            <VPIO_AIRND>  <VPIO_DIW>  FAULT_SIGNAL_OUT
*
*
*                          SCAN_RESET
*                               |
*       +---------+-----+-------+------+-------+--------+--------+
*       |         |     |       |      |       |        |        |
* INSTALL_CONFIG  |  <RESET>    |   <FCID>     |  INSTALL_RANGE  |
*                 |             |              |                 |
*              LOCK_MCU  MCP_ERROR_REPORT  SCAN_ALARM            |
*                                                                |
*                 +---------------+-----------+------------------+
*                 |               |           |
*             UNLOCK_MCU  INSTALL_DRIVERS  <ERROR>
*
*
*                          SENSOR_ALARM
*                               |
*                    +----------+----------+
*                    |                     |
*               SCAN_ALARM              <ERROR>
*
*
*
*                       SET_SHAFT_SPEED
*                               |
*                         SENSOR_ALARM
*
*                        TC_CONSENSUS
*                               |
*                         TC_SIMULATE
*
*
*                          TC_CONVERT
*                               |
*                         POLY_CONVERT
*
*
*                         TC_VALIDATE
*                               |
*             +--------+--------+------+-------+-------+
*             |        |        |      |       |       |
*      TC_REF_CONVERT  |  TC_SIMULATE  |  OPEN_DETECT  |
*                      |               |               |
*                 TC_CONVERT     TC_CONSENSUS     SENSOR_ALARM
*
*
*                          UNLOCK_MCU
*                               |
*                            <LURQ>
