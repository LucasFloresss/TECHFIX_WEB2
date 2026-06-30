#!/usr/bin/env python
import os
import sys

# Define o script que executa comandos do Django a partir do terminal.
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Django não encontrado. Rode: pip install -r requirements.txt") from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
