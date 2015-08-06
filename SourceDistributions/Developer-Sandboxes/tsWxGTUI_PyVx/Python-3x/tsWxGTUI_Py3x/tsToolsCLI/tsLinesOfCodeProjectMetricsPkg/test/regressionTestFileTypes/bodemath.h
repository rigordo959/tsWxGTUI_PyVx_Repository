/* Bode Math Utility Interface Declarations */

#if !defined (_BODEMATH_H)
#define _BODEMATH_H

#include "globals.h"
#include "fortmath.h"

typedef struct {
  real x;
  real y;
} complex;

typedef struct {
  real radius;
  real angle;
} polar;

real get_degrees(real radians);
real get_radians(real degrees);
complex get_complex(polar *argument);
polar get_polar(complex *argument);
polar get_polar_product(polar *arg1, polar *arg2);
polar get_polar_quotient(polar *arg1, polar *arg2);
polar get_polar_summation(polar *arg1, polar *arg2);
polar get_polar_difference(polar *arg1, polar *arg2);
polar standard_polar_form(polar *argument);

#endif /* !defined (_BODEMATH_H) */
