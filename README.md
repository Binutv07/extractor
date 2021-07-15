# Resume Extractor

Python script to extract basic details from a textual resume file.

## Dependencies

``` sudo apt install antiword && pip3 install textract ```

Textract uses antiword as backend to extract information from .doc file.



## Running

``python3 ./extractor.py resume_sample1.doc``

Pass the filename/path as the argument to the script.

Example output: 

```
resume_sample1.doc
Name : Test Name
Mobile : 9999999999
Email : testName@gmail.com

```

