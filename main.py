#define _GNU_SOURCE

#include "MicroBit.h"
#include "NEPODefs.h"
#include <list>
#include <array>
#include <stdlib.h>
MicroBit _uBit;


ManagedString ___Komando;

int main()
{
    _uBit.init();
    ___Komando = ManagedString("");
    
    _uBit.radio.enable();
    _uBit.radio.setGroup(11);
    while ( true ) {
        ___Komando = ManagedString(_uBit.radio.datagram.recv());
        if ( ___Komando == ManagedString("A") ) {
            _uBit.soundmotor.motorOn(30);
        }
        if ( ___Komando == ManagedString("B") ) {
            _uBit.soundmotor.motorBreak();
        }
        _uBit.sleep(_ITERATION_SLEEP_TIMEOUT);
    }
    release_fiber();
}