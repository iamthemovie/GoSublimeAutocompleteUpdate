GoSublimeAutocompleteUpdate
===========================

An add on to the GoSublime package, when installed it updates the autocomplete for external source files you may be working on in your path.

Sublime Text 3 only.

Note on the below:

GOPATH - This is the GOPATH for your project. No trailing slashes.
ROOT - The root is where your main binary you're building is compiled from.
GOBIN - Bin directory containing go binary


An example structure is

YourProject 
  - src
    - MainProject
    	- Main.go
    - ExternalLibrary
    	- ThingYouWantAutocompleteUpdating.go


Install
=======

1. Download the python script
2. Copy it into the Packages directory, Sublime Text -> Preferences -> Browse Packages -> GoSublime
3. Setup a Project with the following in:

	{
		"env": {
	    	"GOPATH": "/Users/YOURUSER/Documents/Projects/YourProject",
	    	"ROOT" : "src/MainProject",
	    	"GOBIN": "/usr/local/go/bin"
	    },
		"folders":
		[
			...sublimey stuff
		],
	}

4. Setup new key binding Sublime Text -> Preferences -> Keybindings - Users

	[
		{ "keys": ["super+s"], "command": "save_and_go_install" },
	]
