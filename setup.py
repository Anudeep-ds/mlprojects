from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT='-e .'
def get_requiremets(file_path:str)->List[str]:


    requiremets=[]
    with open(file_path) as file_obj: 
        requiremets=file_obj.readlines()
        requiremets=[req.replace(":\n","")for req in requiremets]
        
        if HYPEN_E_DOT in requiremets:
            requiremets.remove(HYPEN_E_DOT)

    return requiremets

    
setup(
name='mlproject',
version='0.0.1',
author='Anudeep',
author_email='anudeeptds@gmail.com',
packages=find_packages(),
install_requires=get_requiremets('requirements.txt')
)