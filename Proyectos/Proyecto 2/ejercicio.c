/*
 * EIE 434 - Programacion 2
 * Proyecto N2 - Simulacion de Auto-Home de un Brazo Robotico en C
 *
 * El programa simula el proceso de auto-home de un brazo robotico
 * compuesto por 4 eslabones. Al iniciar genera una posicion aleatoria
 * (X, Y) en el rango 0-360 para cada eslabon y luego simula el avance
 * de cada posicion hasta llegar al origen (0, 0).
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

#define POS_MAX 360   /* Valor maximo permitido para X e Y */
#define PASO    1.0f   /* Decremento fijo por iteracion del auto-home */

/* Parte 1 - Estructura que representa un eslabon del brazo robotico */
typedef struct {
    int   id;   /* Identificador del eslabon */
    float x;    /* Posicion en el eje X */
    float y;    /* Posicion en el eje Y */
} Eslabon;

/*
 * Parte 2 - Genera la posicion inicial aleatoria de un eslabon.
 * Retorna dos valores (X e Y) a traves de punteros, ambos en el
 * rango 0 a 360.
 */
void generar_posicion(float *x, float *y) {
    *x = (float)(rand() % (POS_MAX + 1));   /* 0 a 360 */
    *y = (float)(rand() % (POS_MAX + 1));   /* 0 a 360 */
}

/*
 * Parte 3 - Simula el avance de un eslabon hacia su auto-home.
 * Recibe el eslabon por puntero y modifica sus posiciones, restando
 * un paso fijo en cada iteracion hasta que X e Y llegan a 0.
 * Retorna true cuando ambas posiciones son 0.
 */
bool auto_home(Eslabon *e) {
    while (e->x > 0.0f || e->y > 0.0f) {
        if (e->x > 0.0f) {
            e->x -= PASO;
            if (e->x < 0.0f) {
                e->x = 0.0f;   /* No pasarse del origen */
            }
        }
        if (e->y > 0.0f) {
            e->y -= PASO;
            if (e->y < 0.0f) {
                e->y = 0.0f;   /* No pasarse del origen */
            }
        }
        /* Traza del avance paso a paso */
        printf("  Eslabon %d avanzando -> X = %.1f, Y = %.1f\n",
               e->id, e->x, e->y);
    }
    return (e->x == 0.0f && e->y == 0.0f);
}

/* Parte 4 - Funcion principal */
int main(void) {
    /* Semilla aleatoria, una sola vez */
    srand((unsigned int)time(NULL));

    /* Definicion obligatoria de los 4 eslabones */
    Eslabon id1 = { 1, 0.0f, 0.0f };
    Eslabon id2 = { 2, 0.0f, 0.0f };
    Eslabon id3 = { 3, 0.0f, 0.0f };
    Eslabon id4 = { 4, 0.0f, 0.0f };

    /* Generacion de la posicion inicial aleatoria de cada eslabon */
    generar_posicion(&id1.x, &id1.y);
    generar_posicion(&id2.x, &id2.y);
    generar_posicion(&id3.x, &id3.y);
    generar_posicion(&id4.x, &id4.y);

    printf("Posiciones iniciales generadas:\n");
    printf("  Eslabon %d -> X = %.1f, Y = %.1f\n", id1.id, id1.x, id1.y);
    printf("  Eslabon %d -> X = %.1f, Y = %.1f\n", id2.id, id2.x, id2.y);
    printf("  Eslabon %d -> X = %.1f, Y = %.1f\n", id3.id, id3.x, id3.y);
    printf("  Eslabon %d -> X = %.1f, Y = %.1f\n", id4.id, id4.x, id4.y);
    printf("\nIniciando proceso de auto-home...\n\n");

    /* Proceso de auto-home de cada eslabon */
    bool fin1 = auto_home(&id1);
    if (fin1) {
        printf("Eslabon %d terminado\n", id1.id);
    }

    bool fin2 = auto_home(&id2);
    if (fin2) {
        printf("Eslabon %d terminado\n", id2.id);
    }

    bool fin3 = auto_home(&id3);
    if (fin3) {
        printf("Eslabon %d terminado\n", id3.id);
    }

    bool fin4 = auto_home(&id4);
    if (fin4) {
        printf("Eslabon %d terminado\n", id4.id);
    }

    /* Mensaje de termino cuando los 4 eslabones retornaron true */
    if (fin1 && fin2 && fin3 && fin4) {
        printf("Todos los eslabones realizaron auto-home correctamente.\n");
    }

    return 0;
}
