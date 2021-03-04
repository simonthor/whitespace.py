# whitespace.py
People who dislike Python often complain about the fact that whitespace matters in Python. 
I decided to double down on that and make a "programming language" (in reality, it's just an encoder) that **only** cares about whitespace.

## How it works
whitespace.py will count the number of consequentive white spaces and convert it into the corresponding unicode character. As an example, 97 whitespaces will become the letter `a`. Other characters will be interpreted as a break between two characters. For example,
```
                                                                        H                                                                                                         i
```
will become 
```
Hi
```
You can replace `H` and `i` in the example with any and as many non-whitespace characters as you like, and it will still return `Hi`.

## How to use it
Don't.

If you really want to, use 
```bash
python whitespace.py compile filename
```
but replace `filename` with your actual file name and it will produce a file called `filename.whitespace`, which has converted your file into whitespace syntax.
If you want to decompile a whitespace file, run 
```bash
python whitespace.py decompile filename
```
Run 
```bash
python whitespace.py -h
```
for more info.

## FAQ
No one has actually asked questions, but I have answered some here before people start complaining
### Isn't this just a bad version of [whitespace](https://en.wikipedia.org/wiki/Whitespace_(programming_language))?
Yes.
### What are the practical applications of this?
None. However, I learned about argparse and pathlib in the process, so it was a fun project for me at least!
