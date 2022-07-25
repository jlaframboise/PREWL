import prewl, json

#-----------------------------------------#

# Optionally use a config.json
#prewl.configure("config.json")

# Dynamically detect if the argument is json or a file with json
prewl.configure({
    'backend': {'service': 'gpt2'},
    'newline-delimited': True, # Should a new line indicate the end of the completion
    'classes': ['positive', 'negative', 'neutral'], # defaults to None
    'max-length': 100, # output response upper length limit
    'gpu': True, # True or the GPU number you would like to use. False or -1 indicates CPU
})

#-----------------------------------------#

PROMPTS = """
[
    {
        "text": "I really don't like this movie.",
        "sentiment": "negative"
    },

    {
        "text": "This flick was sick!",
        "sentiment": "positive"
    },

    {
        "text": "It was ok. I've seen better, though.",
        "sentiment": "neutral"
    }
]
"""

examples = json.loads(PROMPTS)

PATTERN = """
Text: {text}
Sentiment: {sentiment}
"""

# Prompts objects
prompts = prewl.load_prompts(PATTERN, examples, 'sentiment')


#-----------------------------------------#

# Creates a function that when called will
#  (1) prompt the server
#  (2) fetch the response
#  (3) returns the parsed result
model = prewl.train(prompts) # Model object

new_input = "This movie was off the hook!"
resp = model.infer(new_input)

print("\n New input: ", new_input)
print("Prediction: ", resp)
print()

