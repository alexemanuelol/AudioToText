# AudioToText
Converts an audio file to a text file.

## Test result

This test is performed on 'The Hobbit' audio book read by *Rob Inglis*.

**The actual speech from the audio book:**

```
Chapter one. An unexpected party. In a hole in the ground there lived a hobbit. Not a nasty,
dirty, wet hole, filled with the ends of worms and an oozy smell, nor yet a dry, bare, sandy
hole with nothing in it to sit down on or to eat: it was a hobbit-hole, and that means comfort.
It had a perfectly round door like a porthole, painted green, with a shiny yellow brass knob in
the exact middle. The door opened on to a tube-shaped hall like a tunnel: a very comfortable
tunnel without smoke, with panelled walls, and floors tiled and carpeted, provided with polished
chairs, and lots and lots of pegs for hats and coats—the hobbit was fond of visitors. The tunnel
wound on and on, going fairly but not quite straight into the side of the hill —The Hill, as all
the people for many miles round called it—and many little round doors opened out of it, first on
one side and then on another. No going upstairs for the hobbit: bedrooms, bathrooms, cellars,
pantries (lots of these), wardrobes (he had whole rooms devoted to clothes), kitchens,
dining-rooms, all were on the same floor, and indeed on the same passage. The best rooms were all
on the left-hand side (going in), for these were the only ones to have windows, deep-set round
windows looking over his garden, and meadows beyond, sloping down to the river. This hobbit was
a very well-to-do hobbit, and his name was Baggins. The Bagginses had lived in the neighbourhood
of The Hill for time out of mind, and people considered them very respectable, not only because
most of them were rich, but also because they never had any adventures or did anything unexpected:
you could tell what a Baggins would say on any question without the bother of asking him. This is
a story of how a Baggins had an adventure, and found himself doing and saying things altogether
unexpected. He may have lost the neighbours’ respect, but he gained—well, you will see whether he
gained anything in the end. The mother of our particular hobbit—what is a hobbit? I suppose
hobbits need some description nowadays, since they have become rare and shy of the Big People,
as they call us. They are (or were) a little people, about half our height, and smaller than
the bearded Dwarves. Hobbits have no beards.
```

**The speech recognition from the script:**

```
Chapter one. An unexpected party. In a hole in the ground there lived a hobbit. Nothing nasty
dirty wet hole. Chilling with the ends of worms andaloussi smell. No yes it dry bad sandy hole
with nothing added to sit down on or to eat. It was a hobbit hole. And that means comfort. It
had a perfectly round door like a porthole. Painted green. With a shiny yellow brass knob in the
exact middle. The door opened onto a tube-shaped hole like a tunnel. A very comfortable tunnel
without smoke. With paneled walls and floors tiled and carpeted. Provided was published chairs.
Lots and lots of pegs for hats and coats. The hobbit was fun to visitors. The tunnel wound on and
on. Going fairly but not quite straight into the side of the hill. Zeze. As all the people from
many miles round coded. Anime need to surround the doors open. of it. First on one side and then
on another. No going upstairs for the hobbit. Bedrooms. Bathrooms. Sellers. Pantry lots of these.
Wardrobes. He had told rooms to go close. Kitchens. Dining rooms. Or on the same floor and indeed
on the same passage. The best rooms were all on the left hand side going in. For these were the
only ones to have windows. Deep set round windows looking over his garden and meadows beyond.
Sloping down to the river. This hobbit was a very well-to-do hobbit. And his name was baggins.
Lebakkens is it lived in the neighborhood of the hill for time out of mind. I'm people consider
them very respectable not only because most of them were very rich. But also because they never
had any adventures or did anything unexpected. You could tell what a baggins would say on any
question without the bother of asking him. This is a story of how a baggins had an adventure.
And found himself doing and saying things altogether unexpected. He may have lost the neighbors
respect. But he gained. Well you will see whether he gained anything in the end. The mother of our
particular hobbit. What is a hobbit. I suppose hobbits need some description nowadays. Since that
becoming a i don't try of the big people is they call us. They are. A little people. About hoffa
height. I'm smaller than the bearded dwarves. Puppies have no beards.
```


## Dependencies

Run the following command to install the dependencies:

    $ pip install -r requirements

## Usage

    usage: audio_to_text.py [-h] [-o OUTPUT] [-l LANGUAGE] input
    sample: (make sure you are in the src folder) py audio_to_text.py videoplayback.wav

    Converts an audio file to text.

    positional arguments:
        input                           The input audio file.

    optional arguments:
        -h, --help                      show this help message and exit
        -o OUTPUT, --output OUTPUT
                                        The output file for the text. Default 'outputText.txt'
        -l LANGUAGE, --language LANGUAGE
                                        See 'https://cloud.google.com/speech-to-text/docs/languages'
                                        for all possible language codes, Default is en-GB.


