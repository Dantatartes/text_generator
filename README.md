# text_generator
Simple text generator
## Usage examples
```Python
generator = TextGenerator() # initialize a model
generator.fit(file)
generator.generate(size=a) # generate sentence with 'a' words
generator.save_model() # saves model in csv format
