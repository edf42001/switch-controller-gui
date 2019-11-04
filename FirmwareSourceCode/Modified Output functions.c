//*******************************************************************************
//   RePlay Switch Controller - I/O functions
//
//   E. J. Rapp
//   RePlay for Kids
//   November 2010
//
//   Built with IAR Embedded Workbench Version: 3.40A
//*******************************************************************************
#include "msp430.h"
#include "Modified Output functions.h"

// MSP430G2001 I/O assignments
const char Out_bit[8] = {0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x80};
const char Ports[8] = {1, 1, 1, 1, 1, 1, 1, 2};
// Configuration constants
const char config[16] = {
    0,                // 0=N.O. else N.C. switch
                      // N.C. not implemented in Ver. 1.0
    0,                // 0=One shot, 1=Retrigger, 2=On/Off
    2,                // Number of outputs in sequence
    1,                // Pulse width in milliseconds * 100
  100,                // Maximum time ON in milliseconds * 100
   20,                // Pull-up time (count * 85 usec.)
    5,                // Test N.C. switch time
    0,0,0,0,0,0,0,0,0
};

unsigned char clear_output (unsigned char Output)
{
  if (Ports[Output] == 1) P1OUT  &= ~Out_bit[Output];
  if (Ports[Output] == 2) P2OUT  &= ~Out_bit[Output];
  if (++Output >= Number_of_outputs) Output = 0;
  P1IE |= Switch_bit;                 // switch interrupt enabled
  P1IES |= Switch_bit;                // switch low going edge
  P1IFG &= ~Switch_bit;               // switch IFG cleared
  return Output;
}

void set_output (unsigned char Output)
{
  if (Ports[Output] == 1) P1OUT  |= Out_bit[Output];
  if (Ports[Output] == 2) P2OUT  |= Out_bit[Output];
}
