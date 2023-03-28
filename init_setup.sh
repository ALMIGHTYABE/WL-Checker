echo [$(date)]: "START"
echo [$(date)]: "Creating conda env with python 3.8" # change py version as per your need
conda create --prefix ./env python=3.8 -y
echo [$(date)]: "activate env"
source activate ./env
echo [$(date)]: "intalling requirements"
pip install -r requirements.txt
echo [$(date)]: "END"
