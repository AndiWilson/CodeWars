#write a function that takes an array of words and smashes them together into a sentence and returns the sentence. 
def smash(words):
    return " ".join(words) if len(words) >= 1 else ""
    #this is using the join function which joins all items into a string. the if condition ensures there are no spaces at the beginning or end




# Sample Tests: 
#  import codewars_test as test
# from solution import smash

# @test.describe("smash")
# def _():
#     @test.it("Should return empty string for empty array.")
#     def _():
#         test.assert_equals(smash([]), "")
        
#     @test.it("One word example should return the word.")
#     def _():
#         test.assert_equals(smash(["hello"]), "hello")
        
#     @test.it("Multiple words should be separated by spaces.")
#     def _():
#         test.assert_equals(smash(["hello", "world"]), "hello world")
#         test.assert_equals(smash(["hello", "amazing", "world"]), "hello amazing world")
#         test.assert_equals(smash(["this", "is", "a", "really", "long", "sentence"]), "this is a really long sentence")