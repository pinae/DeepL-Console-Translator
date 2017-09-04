# DeepL-Console-Translator
Use the [DeepL translator](https://deepl.com/translate) on the console.

## Installaltion

Checkout the repository:

```
git clone https://github.com/pinae/DeepL-Console-Translator.git
cd DeepL-Console-Translator/
```

Set up a virtual environment:

```
pyvenv env
source env/bin/activate
pip install wheel
pip install --upgrade pip
pip install requests
```

## Usage

Run the script:

```
python translate.py -l DE "This is just an example."
```

The parameter `-l` specifies the language to translate into. If omitted it uses english. After that follows the text.

