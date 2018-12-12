# TNEExamples
TNE Script is a type of script supported by [Tonnerre](https://github.com/YaxinCheng/Tonnerre/). It provides extra functionalities to the Tonnerre app.

This repo holds some sample TNE Script, and you can take them as examples

## Introduction

A TNE Script is a simply packed Python or AppleScript (more will be supported...) script, with one extra json or maybe other resource files. 

It provides extra functionalities to Tonnerre, and it must be correctly installed by Tonnerre.

### General Hierarchy

```c
- Extension.tne
	- main.py // or main.scpt for AppleScript. or main.json for some other url tasks
	- description.json // describes the behaviour of this extension
	- icon.png // Optional, if you define your icon inside description.json
	- icon_dark.png // Optional, if do not have it, then icon.png will be used in both modes
```

#### Main.py

Inside the main.py, this is where you defines your extension. Two functions should be provided:

```python
# Supply is called when user typed in request in the searchbar of Tonnerre. The extension should give proper feedback based on the input. Threading and other GUI refreshing is handled by Tonnerre
#
# - inputVal: A list of strings given by user
# - returns: A dictionary represented options. 
#	Must include keys:
#		- name: displayed as the option name
#		- content: displayed as the content
#		- innerItem: the object that will be served
#	Optional keys:
#		- alterContent: the content displayed when cmd key is pressed
def supply(inputVal: List[str]) -> Dict[str, str]

# Serve is called when user clicked Enter on certain option. This function should react on what user has selected (e.g. if it is an URL, then open the URL in the browser)
# - inputVal: A dictionary represented option
# - returns: no return
def serve(inputVal: Dict[str, str])
```

For detailed examples, check: **ipservice.tne** and **TMService.tne**

#### Main.scpt

Inside the main.scpt, it is much easier. You can just put your script here. It is generated as an option when user type automatically in Tonnerre, and it is called .

For detailed examples, check: **LockService.tne** and **SafariPrivate.tne**

#### Main.json

Main.json is a special case, where you only put an URL template inside with some inputFormat regex (optional). Then Tonnerre will complete the URL based on user input, and open the url when user clicked **Enter**.

For detailed examples, check: **Flight.tne** and **UPS.tne**

### description.json

`description.json` represents the information for Tonnerre to display it as an option. The keys are listed below:

- name (string)
  - Mandatory. Displayed at the name label
- content (string)
  - Mandatory. Displayed at the content label. If you have %@ in your content, the user input will be filled in here. You can have multiple %@ in one content string
- keyword (string)
  - Mandatory. The keyword defines what the first word should be for user to trigger this option.
- argLowerBound (int)
  - Optional. It defines how many query requests are followed by the keyword to finally trigger the `supply` function
  - If not set, Tonnerre will consider it as **0**
- argUpperBound (int)
  - Optional. It defines how many query requests can be accepted by this option for the `supply` function. Once user enters more than the upper bound, this option will not be called
  - If not set, Tonnerre will consider it as **infinity** 
- icon (string)
  - Optional. It should be an URL string pointing to an icon file
  - If not set, Tonnerre will use `icon.png` in  the TNE Script instead
- icon_dark (string)
  - Optional. It should be an URL string pointing to an icon file
  - If not set, Tonnerre will use `icon_dark.png` in the TNE Script instead

## Create a TNE

Follow the steps:

1. Right click anywhere in Finder, and select `New Folder`
2. Put your `main`, `description.json`, `icon.png`, and something else inside
3. Rename the `UntitledFolder` as `SomeName.tne`

## Installation

**Automatic**: Double click to install. All TNE Script will be installed to `~/Library/Application\ Support/com.ycheng.Tonnerre/Services/`. 

**Manual**: Remove your TNE Script into the folder to complete the installation

## Uninstallation

**Automatic**: Open **SettingPanel** (Tonnerre, type in `Tonnerre`, then select `Tonnerre Settings`). In the **Provider Settings**, find the one you want to remove, and click on the remove button

**Manual**: Open `~/Library/Application\ Support/com.ycheng.Tonnerre/Services/`, remove the specific TNE Script file you want. 

## License

This project is licensed under the MIT Licence - see the [LICENSE.md](https://github.com/YaxinCheng/TNEExamples/blob/master/LICENSE)

