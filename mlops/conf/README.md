# ¿Para qué es esto?

Esta carpeta debe usarse para almacenar archivos de configuración utilizados por Kedro o por herramientas adicionales.

Este archivo puede usarse para proporcionar a los usuarios instrucciones sobre cómo reproducir la configuración local con sus propias credenciales. Puedes editar el archivo como prefieras, pero tal vez desees conservar la información a continuación y agregar tu propia sección en el apartado titulado **Instrucciones**.

## Configuración local

La carpeta `local` debe usarse para configuración que sea específica para cada usuario (por ejemplo, configuración del IDE) o protegida (como claves de seguridad).

> *Nota:* No subas ninguna configuración local al control de versiones.

## Configuración base

La carpeta `base` es para configuración compartida, como configuraciones no sensibles y relacionadas con el proyecto que pueden ser compartidas entre los miembros del equipo.

ADVERTENCIA: No coloques credenciales de acceso en la carpeta de configuración base.

## Más información
Puedes obtener más información sobre la configuración en la [documentación de la guía de usuario](https://docs.kedro.org/en/stable/configuration/configuration_basics.html).
