<p align="center">
 <h1 align="center"> AirBnB clone - The console </h1>
 <a href="" rel="noopener">
 <img src="https://github.com/bdbaraban/AirBnB_clone_v2/raw/master/assets/hbnb_logo.png">

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()

</div>

---

<p align="center"> This project aims to develop a command-line interpreter for managing objects in an AirBnB-like application. The interpreter facilitates the creation, storage, retrieval, updating, and deletion of various objects such as users, states, cities, and places.
    <br> 
</p>

## Table of Contents 📝

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)

## About <a name = "about"></a> 🧐

The purpose of this project is to develop a command-line interpreter tailored for managing objects within an AirBnB-like application. By creating this interpreter, users can efficiently create, store, retrieve, update, and delete various entities such as users, states, cities, and places, all from the convenience of their terminal. The project encompasses the implementation of a robust object-oriented structure, with a parent class (BaseModel) handling fundamental functionalities like initialization and serialization. Through a streamlined serialization flow, the interpreter seamlessly converts object instances to dictionaries, JSON strings, and ultimately to files, ensuring efficient storage and retrieval of application data.

![](https://github.com/VoiceOfDarkness/holbertonschool-AirBnB_clone/blob/main/assets/815046647d23428a14ca.png?raw=true)

This project serves as the foundation for the larger goal of building a fully functional AirBnB clone web application. By establishing a solid groundwork including object classes, serialization mechanisms, and storage engines, future phases of the project such as HTML/CSS templating, database integration, API development, and front-end implementation can be built upon with ease. Additionally, comprehensive unit tests are provided to validate the functionality of each component, ensuring the reliability and robustness of the application throughout its development lifecycle. Ultimately, this project aims to deliver a powerful yet user-friendly tool for managing AirBnB-like data, laying the groundwork for a seamless and immersive web experience for both hosts and guests.

## Getting Started <a name = "getting_started"></a> 🏁

1.Clone the repo

```
$ git clone https://github.com/VoiceOfDarkness/holbertonschool-AirBnB_clone.git

```

2.run console.py

```
$ ./console.py
```

## Requirements 📃

No requirements needed on this stage of project :)

## Running the tests <a name = "tests"></a> 🔧

Unittests for the HolbertonBnB project are defined in the tests folder. To run the entire test suite simultaneously, execute the following command:

```
$ python3 unittest -m discover tests
```

Alternatively, you can specify a single test file to run at a time:

```
$ python3 unittest -m tests/test_console.py
```

## Usage of console <a name="usage"></a> 💻

The console is a command line interpreter that permits management of the backend of HolbertonBnB. It can be used to handle and manipulate all classes utilized by the application (achieved by calls on the storage object defined above).

### Using the Console

The HolbertonBnB console can be run both interactively and non-interactively. To run the console in non-interactive mode, pipe any command(s) into an execution of the file console.py at the command line.

![](https://github.com/VoiceOfDarkness/holbertonschool-AirBnB_clone/blob/main/assets/help.gif?raw=true)

Alternatively, to use the HolbertonBnB console in interactive mode, run the file console.py by itself:

```
$ ./console.py
```

To quit the console, enter the command quit, or input an EOF signal (ctrl-D).

```
$ ./console.py
(hbnb) quit
$
```

```
$ ./console.py
(hbnb) EOF
$
```

### Console Commands

The HolbertonBnB console supports the following commands:

#### create

- Usage: `create <class>`
  Creates a new instance of a given class. The class' ID is printed and the instance is saved to the file `file.json`

![](https://github.com/VoiceOfDarkness/holbertonschool-AirBnB_clone/blob/main/assets/create.gif?raw=true)

#### show

- Usage: show `<class> <id>` or `<class>.show(<id>)`
  Prints the string representation of a class instance based on a given id.

![](https://github.com/VoiceOfDarkness/holbertonschool-AirBnB_clone/blob/main/assets/show.gif?raw=true)

#### destroy

- Usage: destroy `<class> <id>` or `<class>.destroy(<id>)`
  Deletes a class instance based on a given id.

![](https://github.com/VoiceOfDarkness/holbertonschool-AirBnB_clone/blob/main/assets/destory.gif?raw=true)

#### all

- Usage: all or all `<class>` or `<class>.all()`
  Prints the string representations of all instances of a given class. If no class name is provided, the command prints all instances of every class.

![](https://github.com/VoiceOfDarkness/holbertonschool-AirBnB_clone/blob/main/assets/all.gif?raw=true)

#### count

- Usage: count `<class>.count()`
  Retrieves the number of instances of a given class.

![](https://github.com/VoiceOfDarkness/holbertonschool-AirBnB_clone/blob/main/assets/count.gif?raw=true)

#### update

- Usage: update `<class> <id> <attribute name> "<attribute value>"` or `<class name>.update(<id>, <dictionary representation>)`
  Updates a class instance based on a given id with a given key/value attribute pair or dictionary of attribute pairs. If update is called with a single key/value attribute pair, only "simple" attributes can be updated (ie. not id, created_at, and updated_at).

![](https://github.com/VoiceOfDarkness/holbertonschool-AirBnB_clone/blob/main/assets/update.gif?raw=true)

## Authors <a name = "authors"></a> ✍️

- [@VoiceOfDarkness](https://github.com/VoiceOfDarkness) - Initial Work
- [@Somed-1](https://github.com/Somed-1) - Test Support & great Person

### Special Credits:

> You really don't need to know, but here's the link if you're curious:[link](https://www.youtube.com/watch?v=uwmeH6Rnj2E)
