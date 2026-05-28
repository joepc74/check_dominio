# Check Dominio

Un script simple en Python para verificar si un dominio está disponible y notificar por Telegram al usuario administrador.

## Requisitos

- Python 3.8+
- Dependencias listadas en `requirements.txt`

## Instalación

1. Clona o descarga el repositorio.
2. Navega al directorio del proyecto:

```bash
cd e:\codigo\check_dominio
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Configuración

Crea un archivo `.env` en el directorio raíz con estas variables:

```env
TELEGRAM_TOKEN=tu_token_de_bot_de_telegram
SUPER_USER=tu_chat_id_de_telegram
DOMAIN_LIST=dominio1.com,dominio2.net,dominio3.org
```

- `TELEGRAM_TOKEN`: token del bot de Telegram.
- `SUPER_USER`: chat ID del destinatario de la notificación.
- `DOMAIN_LIST`: lista de dominios separados por comas.

## Uso

Ejecuta el script:

```bash
python check.py
```

El script verifica cada dominio en `DOMAIN_LIST` y envía un mensaje por Telegram si el dominio está disponible.

## Notas

- La funcionalidad actual solo notifica cuando el dominio no está registrado.
- Puedes descomentar el bloque `else` en `check.py` para imprimir información adicional cuando el dominio está tomado.
