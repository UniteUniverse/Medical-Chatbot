from setuptools import find_packages, setup

setup(
    name="Medical Chatbot",
    version="1.0.0",
    author='Pratyush Kumar Jha',
    packages=find_packages(),
    include_package_data=True,
    install_requires=["ctransformers", "sentence_transformers", "transformers", "langchain", "flask", "pinecone-client", "langchain-pinecone", "pypdf", "langchain-community"],
)