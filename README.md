# Covid27 - A Language made in Pandemic
The compiler language made for the course SER 502 Spring 2020 @ ASU.

## Dependencies
To run the language you need to install Python3. 

After installation of Python3 make sure you have pip3 setup for you.

Run command `pip install antlr4-python3-runtime`

## Sample Program
Following is a sample program in the language
```
#begin
List l = {1,2,3};
List s = {1,2,3};
l + s;
print(l);
#end
```

Save this program with extension `.covid27`.

To compile the run program:

`python main.py --c --i <filename>.covid27 --o <output_filename>.icovid27`

To run the compiled file

`python main.py --r --i <output_filename>.icovid27`

And you are done.

To see the options for main.py run: `python main.py -h`

# Demo Videos
* Part 1: [Theory and presentation](https://youtu.be/YmK4orYHVgw)
* Part 2: [Code go through](https://youtu.be/Qt0TUfm-s30)
* Part 3: [Demo](https://youtu.be/-OLRKiujK-0)

