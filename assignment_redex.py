# Assignment
post = "Loving the #sunny weather in #California. #travel #fun"

hashtags = re.findall(r'#\w+', post)
print(hashtags)

# Output
#['#sunny', '#California', '#travel', '#fun']