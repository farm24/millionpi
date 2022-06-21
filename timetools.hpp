#include <iostream>
#include <time.h>
using namespace std;

void timesort(time_t y, time_t x) {
    float ts, tm, th, td, tw = 0;
    bool tsb, tmb, thb, tdb, twb = false;
    ts = (y - x); 
    tsb = true;
    if (ts >= 60) {
        while (ts >= 60) {
            ts = ts - 60;
            tm = tm + 1;   
        }
        tmb = true;
    }
    if (tm >= 60) {
        while (tm >= 60){
            tm = tm - 60;
            th = th + 1;
        }  
        thb = true;
    }
   if (th >= 24) {
        while (th >= 24){
            th = th - 24;
            td = td + 1;
        }  
        tdb = true;
    }
    if (td >= 7) {
        while (td >= 7){
            td = td - 7;
            tw = tw + 1;
        } 
        twb = true; 
    }
    if (tsb == true & tmb == false) {
        cout << "It took " << ts << " seconds to execute";
    }
    if (tsb == true & tmb == true & thb == false) {
        cout << "It took " << tm << " minutes and " << ts << " seconds to execute";
    }
    if (tsb == true & tmb == true & thb == true & tdb == false) {
        cout << "It took " << th << " hours, " << tm << " minutes, and " << ts << " seconds to execute";
    }
    if (tsb == true & tmb == true & thb == true & tdb == true & twb == false) {
        cout << "It took " << td << " days, " << th << " hours, " << tm << " minutes, and " << ts << " seconds to execute";
    }
    if (tsb == true & tmb == true & thb == true & tdb == true & twb == true) {
        cout << "It took " << tw << " weeks, " << td << " days, " << th << " hours, " << tm << " minutes, and " << ts << " seconds to execute";
    }
}