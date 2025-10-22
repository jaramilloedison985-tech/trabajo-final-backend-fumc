# ⚙️ Configuración de Terminal: CMD vs PowerShell

## 🎯 Por Qué Usamos CMD

Este proyecto está configurado para usar **Command Prompt (CMD)** en lugar de PowerShell por razones de compatibilidad con los equipos de los estudiantes.

---

## 🔍 Problema Identificado

En los equipos de los estudiantes:
- ❌ El entorno virtual NO se activa con `Activate.ps1` (PowerShell)
- ✅ El entorno virtual SÍ se activa con `activate.bat` (CMD)
- ❌ PowerShell puede tener restricciones de seguridad (`Set-ExecutionPolicy`)
- ✅ CMD funciona sin configuración adicional

---

## ✅ Solución Implementada

### 1. Configuración de Terminal Predeterminada

**Archivo**: `.vscode/settings.json`

```json
{
  "terminal.integrated.defaultProfile.windows": "Command Prompt",
  "terminal.integrated.profiles.windows": {
    "Command Prompt": {
      "path": ["${env:windir}\\System32\\cmd.exe"],
      "icon": "terminal-cmd"
    },
    "PowerShell": {
      "source": "PowerShell",
      "icon": "terminal-powershell"
    }
  },
  "python.terminal.activateEnvironment": true,
  "python.terminal.activateEnvInCurrentTerminal": true
}
```

**Resultado**:
- VS Code abre CMD por defecto cuando abres una nueva terminal
- La extensión de Python usa `activate.bat` automáticamente
- PowerShell sigue disponible como opción alternativa

### 2. Configuración de Tareas

**Archivo**: `.vscode/tasks.json`

Todas las tareas usan CMD explícitamente:

```json
{
  "label": "Instalar Dependencias",
  "type": "shell",
  "command": "venv\\Scripts\\activate.bat && python -m pip install --upgrade pip --quiet && pip install -r requirements.txt --quiet",
  "options": {
    "shell": {
      "executable": "cmd.exe",
      "args": ["/d", "/c"]
    }
  }
}
```

**Cambios clave**:
- ✅ `activate.bat` en lugar de `Activate.ps1`
- ✅ Shell explícito: `cmd.exe` con argumentos `/d /c`
- ✅ Comandos nativos de CMD en tarea "Limpiar Cache"

### 3. Documentación Actualizada

**Archivos modificados**:
- `README.md` - Comandos CMD como principal, PowerShell como alternativa
- `INICIO_RAPIDO.md` - Todo actualizado a CMD
- `apidog_collections/README.md` - Instrucciones con CMD
- `CAMBIOS_REALIZADOS.md` - Documentado el cambio

---

## 📝 Diferencias de Comandos

### Activar Entorno Virtual

**CMD (Recomendado)**:
```cmd
venv\Scripts\activate.bat
```

**PowerShell**:
```powershell
.\venv\Scripts\Activate.ps1
```

### Copiar Archivos

**CMD**:
```cmd
copy .env.example .env
```

**PowerShell**:
```powershell
Copy-Item .env.example .env
```

### Listar Archivos

**CMD**:
```cmd
dir
```

**PowerShell**:
```powershell
Get-ChildItem
# o también: dir (alias)
```

### Limpiar Cache Python

**CMD**:
```cmd
for /d /r . %d in (__pycache__) do @if exist "%d" rd /s /q "%d"
del /s /q *.pyc 2>nul
```

**PowerShell**:
```powershell
Get-ChildItem -Path . -Include __pycache__ -Recurse -Directory | Remove-Item -Recurse -Force
Get-ChildItem -Path . -Filter *.pyc -Recurse | Remove-Item -Force
```

---

## 🎓 Para Estudiantes

### ¿Qué Terminal Estoy Usando?

**Command Prompt (CMD)**:
```
C:\Users\TuNombre\proyecto>
```

**PowerShell**:
```
PS C:\Users\TuNombre\proyecto>
```
(Nota el `PS` al inicio)

### ¿Necesito Configurar Algo?

**NO**. Si usas este proyecto:
- ✅ VS Code ya está configurado para usar CMD
- ✅ Presionar F5 usa CMD automáticamente
- ✅ No necesitas ejecutar `Set-ExecutionPolicy`
- ✅ No necesitas cambiar nada

### ¿Puedo Usar PowerShell de Todos Modos?

**SÍ**. PowerShell sigue disponible:
1. En VS Code: Click en la flecha junto a "+" en la terminal
2. Selecciona "PowerShell"
3. Activa el entorno: `.\venv\Scripts\Activate.ps1`

**PERO**: En los equipos de los estudiantes, CMD es más confiable.

---

## 🔧 Troubleshooting

### Error: "activate.bat no encontrado"

**Problema**: No has creado el entorno virtual.

**Solución**:
```cmd
python -m venv venv
```

### Error: "python no reconocido"

**Problema**: Python no está en el PATH.

**Solución**: Reinstala Python y marca "Add Python to PATH"

### La Terminal Sigue Abriendo PowerShell

**Solución**:
1. `Ctrl+Shift+P`
2. "Terminal: Select Default Profile"
3. Selecciona "Command Prompt"

---

## 📚 Referencias

- **Documentación Python venv**: https://docs.python.org/3/library/venv.html
- **VS Code Terminal**: https://code.visualstudio.com/docs/terminal/basics
- **CMD vs PowerShell**: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands

---

**Fecha**: 2025-10-22  
**Motivo**: Compatibilidad con equipos de estudiantes FUMC
