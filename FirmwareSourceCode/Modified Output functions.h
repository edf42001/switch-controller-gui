//*******************************************************************************
//   RePlay Switch Controller - Configuration ver. 1.1
//
//   Configuration Options
//
//   Switch_type:
//      The user's switch is usually a momentary contact but can be a toggle
//      switch.  In either case, the logic is edge-triggered.
//      1) Normally Open (N.O.) - triggered when the contact closes.
//      2) Normally Closed (N.C.) - triggered when the contact opens.
//
//   Modes of Operation:
//      1) One-shot: Every push turns on the next output in sequence for a short
//         pulse (~100 milliseconds).  The one-shot masks the switch bounce and
//         the microcontroller goes into sleep mode after the short pulse.  The
//         switch has to be released before the next push can to detected
//         (generate an interrupt).
//      2) Retriggerable one-shot: Every push turns on the next input in
//         sequence.  As long as the push button is held on, the one-shot
//         retriggers.  The one-shot masks the switch bounce and the
//         microcontroller goes into sleep mode when the one-shot times out.
//         In order to save the batteries, after a maximum on time (~1 minute),
//         the µC turns the output off and goes to sleep.  The switch has to be
//         released before the next push can be detected(generate an interrupt).
//      3) On-off: The push turns on the next output in sequence and keeps it on
//         until the switch is released and pushed again.  A one-shot masks the
//         switch bounce.  The µC can go into sleep mode during the off period.
//         In order to save the batteries, after 1 minute, the µC turns the
//         output off and goes to sleep.  The switch has to be released before
//         the next push can be detected(generate an interrupt).
//
//   Number of Outputs in the Rotation Sequence:
//         The number of output in the rotation sequence is configured from one
//         output to the maximum number of outputs (1 TO 8).
//
//   One Shot Pulse Width:
//         The one shot pulse width can be configured in increments of ~100
//         milliseconds.
//
//   Maximum On Time:
//         To save the batteries, the maximum time an output can remain on can
//         be configured in increments of ~100 milliseconds.
//
//  Resistor Pull-up Time:
//        The time the resistor is pulled up before the closed switch state can
//        be tested.  Time in ~.1 milliseconds.
//
//  Switch Test Time:
//        The switch test time plus the resistor pull-up time is the time
//        between tests of a closed switch in increments of ~100 milliseconds.  
//
//   E. J. Rapp
//   RePlay for Kids
//   December 2010
//
//   Built with IAR Embedded Workbench Version: 3.40A
//*******************************************************************************

// Configuration constants
extern const char config[16];

#define Mode                    config[1]
#define Number_of_outputs       config[2]
#define Pulse_width             config[3]
#define Max_time                config[4]


// The very low oscillator (VLO) in the MSP430 is approximately 12 kHz. If
// timing is important, this variable can be modified to correct for device
// variability.  (The LED on time can be measured with an oscilloscope to
// determine the actual clock frequency.)

#define       Second (int)12000/8           // ACLK = VLO frequency/8

// MSP430G2001 I/O assignments
#define       Switch_bit 0x01               // Switch input on Port 1
#define       LED_bit 0x040                 // LED on Port 2


