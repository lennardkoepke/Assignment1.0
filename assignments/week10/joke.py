import pyjokes
import cowsay
import helper
helper.greet("Milk")
joke = pyjokes.get_joke(language="en")
cowsay.milk(joke)