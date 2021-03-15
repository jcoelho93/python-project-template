import setuptools
from typing import List
from pip._internal.req import parse_requirements


def load_requirements(fname: str) -> List[str]:
    """Load contents of requirements.txt

    Args:
        fname (str): the file name

    Returns:
        List[str]: a list of requirements
    """
    reqs = parse_requirements(fname, session='test')
    # Handling multiple versions of parse_requirements
    try:
        requirements = [str(ir.req) for ir in reqs]
    except Exception:
        requirements = [str(ir.requirement) for ir in reqs]
    return requirements


setuptools.setup(
    packages=setuptools.find_packages(),
    install_requires=load_requirements('requirements.txt')
)
