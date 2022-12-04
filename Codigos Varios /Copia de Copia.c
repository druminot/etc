#include <omp.h>
#include <stdio.h>
#include <stdlib.h>
int main()
{
    int n_procs;
    printf("Esto es OpenMP, version %d\n", _OPENMP);
    // Numero de procesadores
    n_procs = omp_get_num_procs();
	printf("Numero de procesadores: %d\n", n_procs);
// Creacion de hebras
    omp_set_num_threads(n_procs);
#pragma omp parallel
    printf("Soy la hebra %d de %d\n", omp_get_thread_num(), omp_get_num_threads());
return 0; }
