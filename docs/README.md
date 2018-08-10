# OpenRVDAS
© David Pablo Cohn - david.cohn@gmail.com  
DRAFT 2018-08-09

The Open Research Vessel Data Acquisition System (OpenRVDAS) is a software framework used for building custom data acquisition systems (DAS). OpenRVDAS target audiences are oceanographic research vessel operators and operators of other science-related platforms that have the need to record streaming data. OpenRVDAS is capable of reading data records from serial ports and network-aware sensors, optionally modifying those data records and streaming either the result to one or more destinations, including logfiles, network ports, databases, etc.

OpenRVDAS is designed to be modular and extensible, relying on simple composition of Readers, Transforms and Writers to achieve the needed datalogging functionality.

The project code repository is at [https://github.com/davidpablocohn/openrvdas](https://github.com/davidpablocohn/openrvdas).

Please see the [OpenRVDAS Introduction to Loggers](intro_to_loggers.md) to get started.

Other relevant documents are:

* Running OpenRVDAS Loggers - how to use the core utility scripts
* [Configuration Files](configuration_files.md) - how to define configuration files to simplify running loggers with listen.py
* [OpenRVDAS Components](components.md) - what components exist and what they do
* NMEA Parsing - how to work with the included NMEA parser 
* [Simulating Serial Input](simulating_serial_input.md) - using the simulate_serial.py script to create virtual serial ports for development and testing
* OpenRVDAS User Interface - an introduction to the web-based GUI

A short link for the folder containing these documents is http://tinyurl.com/openrvdas-docs.

*DISCLAIMER*: THIS CODE IS EXPERIMENTAL AND STILL IN THE EARLY STAGES OF DEVELOPMENT. IT SHOULD UNDER NO CIRCUMSTANCES BE RELIED ON, ESPECIALLY NOT IN ANY APPLICATION WHERE ITS FAILURE COULD RESULT IN INJURY, LOSS OF LIFE, PROPERTY, SANITY OR CREDIBILITY AMONG YOUR PEERS WHO WILL TELL YOU THAT YOU REALLY SHOULD HAVE KNOWN BETTER.