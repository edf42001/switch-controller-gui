//*******************************************************************************
//  RePlay Switch Controller - ver. 1.1
//
//  Description
//
//  There are several types of toys that are difficult to adapt for use with a
//  single pushbutton switch.  Toys that have reversible motors most often have
//  a mechanical double-pole, double throw type switch with a center off
//  position.  With toys that have multiple functions, the volunteer has to
//  decide which function to adapt.  Toys that have an electronic controller
//  chip often have carbon pill type pushbuttons that are susceptible to
//  electrostatic discharge.
//
//  So, the idea is the "RePlay Switch Controller" which uses a MSP430G2101
//  low-power microcontroller.  The user's pushbutton generates an interrupt
//  event that wakes up the device in a low-power mode, services the request
//  and shuts down on return from the interrupt program.  The low power mode
//  maintains the RAM memory to for the next pushbutton event.  There are
//  several options that are configured with a PC app when installed in a
//  particular toy.
//
//  Configuration Options
//
//  Switch_type:
//     The user's switch is usually a momentary contact but can be a toggle
//     switch.  In either case, the logic is edge-triggered.
//     1) Normally Open (N.O.) - triggered when the contact closes.
//     2) Normally Closed (N.C.) - triggered when the contact opens.
//  N.B. To conserve power the N.C. should be polled, turning on the pull-up
//       resistor only a little before (3 RC time constants) the switch is
//       sampled.  Also, when a N.O. pushbutton is held on, the switch is
//       polled. (not implemented until Ver. 1.1)
//
//  Modes of Operation:
//     1) One-shot: Every push turns on the next output in sequence for a short
//        pulse (O.S. pulse width).  The one-shot masks the switch bounce and
//        the microcontroller goes into sleep mode after the short pulse.  The
//        switch has to be released before the next push can to detected
//        (generate an interrupt).
//     2) Retriggerable one-shot: Every push turns on the next input in
//        sequence.  As long as the push button is held on, the one-shot
//        retriggers.  The one-shot masks the switch bounce and the
//        microcontroller goes into sleep mode when the one-shot times out.
//        In order to save the batteries, after a maximum on time (~1 minute),
//        the µC turns the output off and goes to sleep.  The switch has to be
//        released before the next push can to detected (generate an interrupt).
//     3) On-off: The push turns on the next output in sequence and keeps it on
//        until the switch is released and pushed again.  A one-shot masks the
//        switch bounce.  The µC can go into sleep mode during the off period.
//        In order to save the batteries, after 1 minute, the µC turns the
//        output off and goes to sleep.  The switch has to be released before
//        the next push can to detected (generate an interrupt).
//
//  One Shot Pulse Width:
//        The one shot pulse width can be configured in increments of ~100
//        milliseconds.
//
//  Maximum On Time:
//        To save the batteries, the maximum time an output can remain on can
//        be configured in increments of ~100 milliseconds.
//
//  Number of Outputs in the Rotation Sequence:
//        The number of output in the rotation sequence is configured from one
//        output to the maximum number of outputs.
//
//  Resistor Pull-up Time:
//        The time the resistor is pulled up before the closed switch state can
//        be tested.  Time in ~.1 milliseconds.
//
//  Switch Test Time:
//        The switch test time plus the resistor pull-up time is the time
//        between tests of a closed switch in increments of ~100 milliseconds.
//
//  State Machine
//        The microcontroller only runs to set up the next state.  Once the next
//        state is set up, the micro goes to sleep and waits for the next
//        interrupt from either the switch or the timer.
//     1) Reset - initialize stack, I/O, timer, turn on LED for "welcome"
//        flash, set timer interrupt for .1 sec, set state = Flash and sleep.
//     2) Timer Interrupt:
//          if Flash, LED off, set up switch interrupt and sleep.
//          if StartPulse, turn off LED, pulse counter--, max counter--
//             if pulse counter = 0 (pulse done) then
//                if Mode = OneShot, turn off output. Increment next output, set
//                   up switch interrupt and sleep.
//                if Mode = Retrigger, set up Timer interrupt, State = Retrigger
//                   and sleep.
//                if Mode = OnOff, set up Timer interrupt, State=OnState.
//             else set up Timer interrupt and sleep.
//          if Retrigger, pulse counter--, max counter--
//             if switch = off OR max. counter = 0, turn off output. Increment
//                next output, set up switch interrupt and sleep.
//             else set up Timer interrupt and sleep.
//          if OnState and max. counter = 0, then turn off output.
//             Increment next output, set up switch interrupt, clear OnState
//             and sleep.
//          if Pull-up, turn on pull-up resistor, set pull-up time, set State =
//             Switch Test and sleep.
//          if Switch Test,
//             Contact closed, set switch test time, set State =  Pull-up, and
//                sleep.
//             Contact Open and N.C., set max. counter, set pulse counter, set
//                Timer interrupt for  1 seconds and set State = StartPulse.
//      3) Switch Interrupt (Only with N.O. switch):
//          if Waiting for Release, turn off pull-up resistor, set switch time,
//             State = Pull-up.
//          if OnState, turn off output. Increment next output, set up switch
//             interrupt, clear OnState and sleep.
//          else set max. counter, set pulse counter, set Timer interrupt for
//             .1 seconds and set State = StartPulse.
//
//  Microcontroller Options:
//        Auxiliary clock (ACLK) sourc ed from the internal LF oscillator
//        MCLK = SMCLK = default DCO
//        Watchdog timer (WDT+) module is not used
//
//                 MSP430x2xx
//              -----------------
//          /|\|              XIN|- Output
//           | |                 |
//           --|RST          XOUT|- Output
//             |                 |
//             |             P1.0|-->LED
//
//   Low-power mode 3 (LPM3) waits for a Timer interrupt
//      – CPU is disabled
//      – MCLK and SMCLK are disabled
//      – DCO's dc generator is disabled
//      – ACLK remains active (clocking Timer A2)
//
//   Low-power mode 4 (LPM4) waits for a N.O. switch interrupt
//      – CPU is disabled
//      – ACLK is disabled
//      – MCLK and SMCLK are disabled
//      – DCO's dc generator is disabled
//      - Crystal oscillator is stopped
//      - RAM memory is retained
//
//
//   E. J. Rapp
//   RePlay for Kids
//   December 2010
//
//   Built with IAR Embedded Workbench Version: 3.40A
//*******************************************************************************
#include "msp430.h"
#include "in430.h"
#include "Modified Output functions.h"

extern void set_output (unsigned char);     // I/O functions
extern unsigned char clear_output (unsigned char);

#define       TRUE 1
#define       FALSE 0

// Global variables
unsigned char Output;                       // Current Output in sequence
unsigned char State;                        // State variable
#define       Flash 0                       // Welcome LED flash
#define       Start_pulse 1                 // First time period after switch
#define       Retrigger 2                   // Switch is still on
#define       OnState 3                     // Output On in On/Off mode
unsigned int  Max_counter;                  // Maximum ON time counter

int main( void )
{
  WDTCTL = WDTPW + WDTHOLD;                 // Stop watchdog timer
  BCSCTL1 |= DIVA_3;                        // ACLK/8
  BCSCTL3 |= LFXT1S_2;                      // ACLK = VLO
  IFG1 &= OFIFG;                            // Clear OSC fault flag
  P1DIR |= ~Switch_bit;                     // Switch is the only input
  P1REN |= Switch_bit;                      // Enable resistor for switch
// Note: PxOUT and PxIES are not cleared on power up reset.
  P1OUT = Switch_bit;                       // All outputs off, pull-up res.
  P1IES = Switch_bit;                       // Interrupt on negative transistion
  P2SEL &= 0x03f;                           // Enable I/O function on P2.6 & 7
  P2DIR |= 0x0c0;                           // Enable outputs
  P2OUT &= 0x03f;                           // Port 2 outputs off

  Output = 0;				    // start with first output
  TACCTL0 = CCIE;                           // CCR0 timer interrupt enabled
  TACCR0 = (int)(Second*Pulse_width-5)/10;  // one shot pulse time (rounded-1)
  TACTL = TASSEL_1 + MC_1;                  // start timer, continuous mode
  State = Flash;                            // State = Flash
  P2OUT |= LED_bit;			    // Welcome flash, LED on
  _BIS_SR(LPM3_bits + GIE);                 // Wait for timer interrupt
}

// Switch interrupt service routine
#pragma vector=PORT1_VECTOR
__interrupt void Port_1(void)
{
  P1IFG &= ~Switch_bit;                     // reset switch interrupt flag
  if (State == OnState)
  {
    Output = clear_output (Output);         // turn off output
    State = Start_pulse;                    // finshed with OnState, clear
    _BIS_SR_IRQ(LPM4_bits);                 // Wait for switch (VLO off)
  }
  else
  {
    set_output (Output);	            // turn on output
    P2OUT |= LED_bit;			    // LED on when switch pushed
    P1IE |= Switch_bit;                     // switch interrupt disabled
    Max_counter = Max_time/Pulse_width;     // Start Max. on timer
    State = Start_pulse;                    // First time period after switch
    _BIC_SR_IRQ(OSCOFF);                    // Wait for timer interrupt
  }
}

// Timer interrupt service routine
#pragma vector=TIMERA0_VECTOR
__interrupt void Timer_A (void)
{
  switch (State)
  {
    case Flash:
      P2OUT &= ~LED_bit;                    // LED off
      P1IE |= Switch_bit;                   // switch interrupt enabled
      P1IFG &= ~Switch_bit;                 // switch IFG cleared
      P1IFG &= ~Switch_bit;                 // reset switch interrupt flag
      _BIS_SR_IRQ(LPM4_bits);                 // Wait for switch (VLO off)
      break;
    case Start_pulse:
      P2OUT &= ~LED_bit;                    // LED off
      if (Mode == 0)                        // if One Shot mode
      {
        Output = clear_output (Output);     // turn output off, select next out
        _BIS_SR_IRQ(LPM4_bits);             // Wait for switch (VLO off)
      }
      else if (Mode == 1) State = Retrigger;// if Retrigger or On/off
      else State = OnState;
      break;
    case Retrigger:
      if (((P1IN & Switch_bit) == 0) && (Max_counter != 0))
      {                                     // if switch still on and
        Max_counter--;                      //   not over max on time
      }
      else
      {
        Output = clear_output (Output);     // turn output off, select next out
        _BIS_SR_IRQ(LPM4_bits);             // Wait for switch (VLO off)
      }
      break;
    case OnState:                           // On/off mode
      if (Max_counter != 0)
      {
        Max_counter--;                      // count down max on time
      }
      else
      {
        Output = clear_output (Output);     // turn output off, select next out
        State = Start_pulse;                // finished with OnState, clear
        _BIS_SR_IRQ(LPM4_bits);             // Wait for switch (VLO off)
      }
      break;
    default:
      break;
  }
}
