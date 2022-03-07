# py_url2domain

Outputs domains from URLs in a file, a string or a list of strings.

```
usage: url2domain [-h] [-o OUTPUT_NAME] [-a ALIASES] [-d MAX_DEPTH]
                  input_name

positional arguments:
  input_name            Input file name

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_NAME, --output_name OUTPUT_NAME
                        Output file name
  -a ALIASES, --aliases ALIASES
                        Domain aliases to replace (JSON format)
  -d MAX_DEPTH, --max-depth MAX_DEPTH
                        Maximum domain depth to consider (optional)
```

### Example

#### Get domains from URLs in a text file

```
python3 url2domain.py file_containing_urls.txt
```

#### Import and use as a library

```
from url2domain import url2domain

url2domain("www.address.com")
```
