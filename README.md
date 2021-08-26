# MrWorldwide
A tool to automatically generate language files for Minecraft by using a translation API.

## How to Use
Quite simple. Go to your terminal, and launch the program with a few arguments:
```bash
python MrWorldwide.py --sourceLang <source language> --targetLang <target language> --sourceFile <source file> --targetFile <target file>
```

For example, to take an English translation file and convert it to Russian:
```bash
python MrWorldwide.py --sourceLang en --targetLang ru --sourceFile en_us.json --targetFile ru_ru.json
```

### Notice
This isn't going to be 100% accurate and may have some quirks. The goal is to translate a bulk file. You'll probably have to go back and clean things up afterwards.

It also uses the [LibreTranslate](https://translate.argosopentech.com/) API. If something isn't working right (like language codes) go try it there.