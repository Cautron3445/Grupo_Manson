/*

* EIE 434 - Programacion 2
* Proyecto N°2 - Simulacion de Auto-Home de un Brazo Robotico en C
*
* El programa genera posiciones aleatorias para cuatro eslabones y simula el regreso de cada uno al origen (X = 0, Y = 0). 
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

#define POS_MAX 360
#define PASO 100.0f

/* Parte 1 - Estructura del eslabon. */
typedef struct {
int id;
float x;
float y;
} Eslabon;

/* Parte 2 - Generar posicion inicial. */
  void generar_posicion(float *x, float *y) {
  *x = (float)(rand() % (POS_MAX + 1));
  *y = (float)(rand() % (POS_MAX + 1));
  }

/* Parte 3 - Simular el avance hacia auto-home. */
  bool auto_home(Eslabon *eslabon) {
  while (eslabon->x > 0.0f || eslabon->y > 0.0f) {

  
   if (eslabon->x > 0.0f) {
       eslabon->x = eslabon->x - PASO;

       if (eslabon->x < 0.0f) {
           eslabon->x = 0.0f;
       }
   }

   if (eslabon->y > 0.0f) {
       eslabon->y = eslabon->y - PASO;

       if (eslabon->y < 0.0f) {
           eslabon->y = 0.0f;
       }
   }

   printf("Eslabon %d avanzando -> X = %.0f, Y = %.0f\n",
          eslabon->id, eslabon->x, eslabon->y);
  

  }

  return (eslabon->x == 0.0f && eslabon->y == 0.0f);
  }

/* Parte 4 - Funcion principal. */
int main(void) {
bool fin1, fin2, fin3, fin4;


srand((unsigned int)time(NULL));

Eslabon id1 = {1, 0.0f, 0.0f};
Eslabon id2 = {2, 0.0f, 0.0f};
Eslabon id3 = {3, 0.0f, 0.0f};
Eslabon id4 = {4, 0.0f, 0.0f};

generar_posicion(&id1.x, &id1.y);
generar_posicion(&id2.x, &id2.y);
generar_posicion(&id3.x, &id3.y);
generar_posicion(&id4.x, &id4.y);

printf("Posiciones iniciales generadas:\n");
printf("Eslabon %d -> X = %.0f, Y = %.0f\n", id1.id, id1.x, id1.y);
printf("Eslabon %d -> X = %.0f, Y = %.0f\n", id2.id, id2.x, id2.y);
printf("Eslabon %d -> X = %.0f, Y = %.0f\n", id3.id, id3.x, id3.y);
printf("Eslabon %d -> X = %.0f, Y = %.0f\n", id4.id, id4.x, id4.y);

printf("\nIniciando proceso de auto-home...\n\n");

fin1 = auto_home(&id1);
if (fin1) {
    printf("Eslabon 1 terminado\n\n");
}

fin2 = auto_home(&id2);
if (fin2) {
    printf("Eslabon 2 terminado\n\n");
}

fin3 = auto_home(&id3);
if (fin3) {
    printf("Eslabon 3 terminado\n\n");
}

fin4 = auto_home(&id4);
if (fin4) {
    printf("Eslabon 4 terminado\n\n");
}

if (fin1 && fin2 && fin3 && fin4) {
    printf("Todos los eslabones realizaron auto-home correctamente.\n");
}

return 0;


}
