tag = '<a href="http://www.python.org">Python web site</a>'
print  tag[9:30]
print tag[32:-4]
numbers = [1,2,3,4,5,6,7,8,9,10]
print numbers[3:6]
print numbers[0:1]

print(numbers[7:10])
print(numbers[-3:])
print(numbers[:3])
print(numbers[:])

#http://www.python.org
url = raw_input('Please enter the Url:')
domain = url[11:-4]
print("Domain name: " + domain)