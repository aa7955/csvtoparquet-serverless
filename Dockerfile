FROM ibmfunctions/action-python-v3

RUN pip install csvtoparquetlib

ADD serverless/listobjects.py /action/listobjects.py

RUN echo '#!/bin/bash\n\
python /action/listobjects.py "$1"' > /action/exec

RUN chmod +x /action/exec 

CMD ["/bin/bash", "-c", "cd actionProxy && python -u actionproxy.py"]
