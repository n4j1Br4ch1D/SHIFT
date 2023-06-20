import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='shift-ip',  
     version='1.0.0',
     scripts=['shift'] ,
     author="Najib Rachid",
     description="SHIFT is a penetration testing tool designed to help you identify the IP addresses of shared hosting associated with a specific domain. It checks each IP address to determine if the domain is hosted on that IP.",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/n4j1Br4ch1D/SHIFT",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )