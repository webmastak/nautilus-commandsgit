# Nautilus script - commands Git

Nautilus script, command set for Git


## Dependencies

  * git
  * zenity
  * nautilus

## Install

* `git clone git: //github.com/webmastak/nautilus-commandsgit`
* `cd nautilus-commandsgit`
* `cp ~/nautilus-commandsgit/local/share/icons/git.png ~/.local/share/icons/git.png`

### Nautilus script

* `cp ~/nautilus-commandsgit/local/share/nautilus/scripts/CommandsGit ~/.local/share/nautilus/scripts/CommandsGit`
* `enjoy`

### Nautilus python extension 
Adds Commands Git to the Nautilus context menu

* `cp ~/nautilus-commandsgit/local/share/nautilus-python/extensions/nautilus-commandsgit.py ~/.local/share/nautilus-python/extensions/nautilus-commandsgit.py`
* `cp ~/nautilus-commandsgit/local/bin/commands-git ~/.local/bin/commands-git`
* `enjoy`


## Usage

In config file: `~/.gitconfig` specify your token
```html
[user]
	name = name
	email = email@example.com
	username = username
	token = token
```

## Contributing

* Fork it (<https://github.com/webmastak/nautilus-commandsgit/fork>)
* Create your feature branch (`git checkout -b my-new-feature`)
* Commit your changes (`git commit -am 'Add some feature'`)
* Push to the branch (`git push origin my-new-feature`)
* Create a new Pull Request


## Contributors

- [webmastak](https://github.com/webmastak) - creator and maintainer

