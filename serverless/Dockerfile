FROM ibmfunctions/action-python-v3

RUN pip install -U pip csvtoparquetlib pyarrow

ADD convertobjects.py /action/convertobjects.py

RUN echo '#!/bin/bash\n\
python /action/convertobjects.py "$1"' > /action/exec

RUN chmod +x /action/exec 

CMD ["/bin/bash", "-c", "cd actionProxy && python -u actionproxy.py"]
