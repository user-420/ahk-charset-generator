## Generates and autohotkey script that replaces what you type with characters from a charset.

###### This code is still WIP

This code is terrible, but it works, this is mainly just for me to use for myself.
\
\
\
\
\
\
\
... so if you're still reading i'm gonna assume you want to use it

You'll need **Python 3** and **AHK** (I'm on version 1.1, unsure if syntax changes in 2)

The basics of using it:
- Grab `generator.py` from the repo
- Run it (python3) and then pick your charset and the key to pause the script
- Run the .ahk file that gets generated (same dir as the generator)
- Congrats, now you can type in 𝔠𝔬𝔬𝔩 and 𝓌𝒶𝒸𝓀𝓎 unicode characters.

\
\
How the charsets are layed out:
- Charsets go in the "charsets" list
- Each charset is a list with strings for what you want to replace the normal characters
  - lowercase a-z
  - then uppercase A-Z
  - then either a list with 1-9 then 0, then their shifted versions (!@#, etc) OR the name of the charset
    (if you have the list of numbers and symbols then the name goes after it)
    
  example (this would just do normal characters):
  `["a",(...)"z", "A"(...)"Z", ["1",(...),"9","0", "!",(...),")", "charset_name_here"]`
\
\
\
features coming eventually:
  - [] dynamic listing of all the charsets (thats why the name is in there)
  - [] might move charsets to a file outside of the python script itself
  - [] redo how the charsets are layed out, the way its done now is very... bad
  - [] support for more characters, although I'm not sure there's many more that have counterparts in unicode that would match sets of letters/nums
  - [] something to have each letter use a random charset
