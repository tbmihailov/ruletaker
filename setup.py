from setuptools import find_packages, setup

if __name__ == '__main__':
    packages=find_packages()    
    setup(name='ruletaker',
        version='0.1',
        description="RuleTaker from `Transformers are Soft Reasoners over Language` paper https://arxiv.org/abs/2002.05867. "
                    "This is not an official setup. The goal of this setup is to be reusable.",
        author="AllenAI",
        packages=packages,
        install_requires=[
                "Cython==0.29.24",
                "nltk>=3.6.5",
                "numpy>=1.21.4",
                "problog==2.1.0.42",
                "pytest>=6.1.2",
                "tqdm>=4.51.0",
        ],
        python_requires=">=3.6",
    )