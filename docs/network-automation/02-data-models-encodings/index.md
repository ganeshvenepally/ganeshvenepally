# Data Models and Encodings

Data models and encodings are important concepts in networking that are used to represent and manage the configuration and state of network devices and services.

A data model is a structured representation of the data that a network device or service uses to configure and operate. This can include information such as network topology, device configurations, and performance metrics. Data models are typically defined using formal languages such as YANG, which is used to model network configurations and state data for various protocols such as IP, MPLS, and LACP.

An encoding is a method used to represent the data defined by a data model in a format that can be transmitted and processed by network devices and management systems. There are several encoding formats that are commonly used in networking, including XML, JSON. Each encoding format has its own strengths and weaknesses, and the choice of encoding format will depend on the specific requirements of the network and the devices and systems that will be using the data.

In Networking, data models are used to define the structure of the data, while encodings are used to represent the data in a format that can be transmitted over the network. For example, a YANG model can be used to define the structure of the data for a particular protocol such as BGP, and then that data can be encoded in JSON format to be transmitted over the network and processed by the devices and systems that are using the BGP protocol.

One of the main benefits of using data models and encodings in networking is that they allow for a more consistent and efficient management of network devices and services. Data models provide a standard way to represent the data, which allows for better interoperability between devices and systems.

## **YANG**

YANG (Yet Another Next Generation) is a data modeling language used to model the configuration and state data for various network protocols such as IP, MPLS, and LACP. It is used by several networking vendors, such as Cisco and Juniper, to define the data models for their devices and services. For example, a YANG data model can be used to define the structure of the data for a particular protocol such as BGP, and then that data can be encoded in JSON format to be transmitted over the network and processed by the devices and systems that are using the BGP protocol.

## **XML**

XML (Extensible Markup Language) is a markup language that is commonly used in networking to represent and manage the configuration and state of network devices and services. Here are some examples of how XML is used in networking.

Network Management Protocols: XML is used to represent data in several network management protocols such as SNMP (Simple Network Management Protocol) and NETCONF (Network Configuration). These protocols use XML to represent the data in a structured and easily readable format, which allows network management systems to easily extract and process the data.

Here is the sample CLI output of Junos `BGP Config` can be encoded with XML:

=== "CLI output"

    ```juniper
    protocols {
    bgp {
        group G1 {
            type external;
            peer-as 64501;
            neighbor 10.0.0.1;
        }
        group G2 {
            type external;
            peer-as 64502;
            neighbor 10.0.10.1;
        }
    }
    }
    ```

=== "XML output"

    ```xml
    <?xml version="1.0" encoding="UTF-8" ?>
    <configuration>
    <protocols>
        <bgp>
        <group>
            <name>G1</name>
            <type>external</type>
            <peer-as>64501</peer-as>
            <neighbor>
            <name>10.0.0.1</name>
            </neighbor>
        </group>
        <group>
            <name>G2</name>
            <type>external</type>
            <peer-as>64502</peer-as>
            <neighbor>
            <name>10.0.10.1</name>
            </neighbor>
        </group>
        </bgp>
    </protocols>
    </configuration>
    ```

## **JSON**

JSON: JavaScript Object Notation (JSON) is a lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate. JSON is widely used in networking because it is easy to understand, it is easy to parse, and it is easy to generate. JSON can be used as an encoding format for data models defined in YANG, as it is easy to read and write. JSON can also be used to represent the data in RESTful APIs, which are widely used in networking to manage devices and services.

Here is the sample data from previous sections encoded in JSON:

```json
{
  "configuration": {
    "protocols": {
      "bgp": {
        "group": [
          {
            "name": "G1",
            "type": "external",
            "peer-as": "64501",
            "neighbor": [
              {
                "name": "10.0.0.1"
              }
            ]
          },
          {
            "name": "G2",
            "type": "external",
            "peer-as": "64502",
            "neighbor": [
              {
                "name": "10.0.10.1"
              }
            ]
          }
        ]
      }
    }
  }
}
```

## **YAML**

YAML: YAML Ain't Markup Language (YAML) is a data serialization format that is often used in networking for configuration management. YAML is often preferred over JSON and XML because it is more human-readable and less verbose. YAML is widely used for configuration management, for example Ansible, a widely popular automation tool, uses YAML to define the configuration of devices.

Here is the sample data from previous sections encoded in YAML:

```yaml
---
configuration:
  protocols:
    bgp:
      group:
      - name: G1
        type: external
        peer-as: '64501'
        neighbor:
        - name: 10.0.0.1
      - name: G2
        type: external
        peer-as: '64502'
        neighbor:
        - name: 10.0.10.1
```


## **Summary**

Here is a summary table that compares the key properties of XML, JSON, and YAML:


|Property|XML|JSON|YAML|
|:----|:----|:----|:----|
|Structure|Hierarchical, nested tree structure|Key-value pairs|Indentation-based, human-readable|
|Readability|Verbose, not as human-readable as JSON or YAML|Easy to read and write|Easy to read and write|
|Parsing|Requires specialized parsing libraries|Can be parsed with a wide range of libraries|Can be parsed with a wide range of libraries|
|Platform Independence|Platform-independent|Platform-independent|Platform-independent|
|Verbosity|Verbose|Less verbose than XML|Less verbose than XML|
|Popularity|Commonly used in networking, but less popular than JSON|Widely used in web and mobile apps, becoming more popular in networking|Commonly used in configuration management and automation|