# Simplify Apt scripts!

This is a simple program that simplifies the usage of apt declaratively, scripts are easier now!

## Usage

Import Apt class

```Python
 from apt import Apt
```

Create an object from Apt class

```Python
update = Apt(option="rup", assume_yes=False)
```

Call the exec() method

```Python
update.exec()
```

Easy! You just updated your repos.

### What if I want to install a package?

Create use this then

```Python
apt_in = Apt(option="in", assume_yes=False)
```

And now use

```Python
apt_in.change("gimp")
```

That installs gimp.

If you want to remove a package it's the same syntax as before but pass "rm" to option argument instead. 

### What if I don't want confirmation?

Just change the assume_yes argument to True, simple.

### Another possible options for option argument:

- `up` : Updates packages(`sudo apt upgrade`)
- `dup` : Updates every package(`sudo apt full-upgrade`)
- `li` : Lists every package(`sudo apt list`) _Probably someday I will extend this one_

Use exec() method for these ones. For `rm` and `in` use change(packages)
