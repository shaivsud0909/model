# building application as a package itself

from setuptools import setup, find_packages

hypen_e_dot = '-e .' #if we call the requirements.txt file this will create an error so we will remove it
def get_requirements(file_path:str)->list[str]:
    """this function will return the list of requirements"""
    requirements = []
    with open('requirments.txt') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n"," ") for req in requirements]
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
    return requirements

setup(
    name="ml_app", 
    version="0.0.1",
    author="Shaiv",
    author_email="shaivsood@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")       
)  