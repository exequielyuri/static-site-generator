# Static site generator
This program will generate web pages from markdown files in the contents directory. For example, if we have the following contents:
```
.
└── content
    ├── index.md
    └── majesty
        └── index.md
```

Running `./main.sh` will produce the following web pages:
```
.
└── public
    ├── images
    │   └── rivendell.png
    ├── index.css
    ├── index.html
    └── majesty
        └── index.html
```

Note that the default styling, or other assets like images can be found or added in the static directory.
```
.
└── static
    ├── images
    │   └── rivendell.png
    └── index.css
```

## Tests
There are also tests created to ensure correctness of functionality. To run the tests, do:
```bash
./test.sh
```
