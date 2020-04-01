title:: A Vim setup for beginners
description:: From a beginner's perspective the bad thing about vim is it's configurability. There are a lot of options, and it can be overwhelming.

# A vim setup for beginners

The great thing about vim (aside from modal editing) is it's configurability.

From a beginner's perspective the bad thing about vim is it's configurability. There are a lot of options, and it can be overwhelming.

If someone were to ask me how to get started here's the advice I'd give them:

### Tips:
* Remap Caps Lock to Escape. On Mac this is trivial (Keyboard > Modifier Keys). You're on your own for Linux or Windows.
* Don't copy a massive vimrc file you found on the internet. It's better to build up your own vimrc file over time, because you'll understand the settings. Here's a good [starting point](([source](https://web.stanford.edu/class/cs107/resources/sample_vimrc), along with the next two bullet points below.
    * Map your leader key to comma: `let mapleader=","`
    * Quickly navigate to your previous file: `nnoremap <leader><leader>  <c-^>`.
* Type :vimtutor and work through the tutorial. That will show you the basics.
* Make a list of the common commands you use in your current editor.
* Translate those commands to vim commands
* ???
* [Profit](https://www.youtube.com/watch?v=tO5sxLapAts)

###Plugins

Plugin manager: [vim-pathogen](https://github.com/tpope/vim-pathogen)

Project wide search: [ag.vim](https://github.com/rking/ag.vim) / [ack.vim](https://github.com/mileszs/ack.vim)

_The reason I include two options is because ag.vim is "deprecated" and links to ack.vim as an alternative. However, I use ag.vim and haven't had any issues._

Fuzzy file finder: [command-T](https://github.com/wincent/command-t)

Comment multiple lines at once: [vim-commentary](https://github.com/tpope/vim-commentary)

Directory browser: [vinegar.vim](https://github.com/tpope/vim-vinegar)

_Vim has a directory browser called "netrw". Vim vinegar cleans it up a bit._

Testing: [vim.test](https://github.com/janko/vim-test)

_This plugin gives you some commands to run your tests using keybindings. YMMV, but I've found that it works with very little configuration needed._

Snippets: [ultisnips](https://github.com/SirVer/ultisnips)

That's it!

With this setup and a couple months of practice you'll soon be able to explain to all your programming friends why you're better than them.
