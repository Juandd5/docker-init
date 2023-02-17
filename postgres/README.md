# Postgres

`restart`: define la politica a aplicar cuanto muere un contenedor.

```yaml
- always: Siempre reinicia.
- unless-stopped: Siempre se reinicia a menos de que el contenedor sea detenido o removido.
```

`volumes`: Puede ser un volumen nombrado o un bind mount

```yaml
- postgres14-6:/var/lib/postgresql/data
- /postgres14-6:/var/lib/postgresql/data
```

    En el primer caso, el volumen es administrado por docker y se almacena en: 
    En el segundo caso es una carpeta creada por ti en la ruta elegida.