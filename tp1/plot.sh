#!/bin/bash


# Crear si no existe el directorio "plot"
mkdir -p plot

# Generar las imagenes en el directorio plot
gnuplot plot.gpi
