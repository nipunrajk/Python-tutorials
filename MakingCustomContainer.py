class TagCloud:
    def __init__(self):
        self.tags = {}

    # def __str__(self):
    #     return f'{self.tags}'
    
    # adding items to dictionary
    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    # count no of items 
    # we can't do this with typical dictionary because if we give count for item that does not
    # exist then dictionary will throw a error
    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    # assign no of items
    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    # get length of items
    def __len__(self):
        return len(self.tags)
    
    # implement iteration
    # returns an iterable object which gives one item at a time in forloop
    def __iter__(self):
        iter(self.tags)

cloud = TagCloud()

cloud.add('Dropbox')
cloud.add('dropbox')
cloud.add('Drive')
cloud.add('AWS')
print(cloud.tags)

print(cloud["dropbox"])
print(cloud["AWS"])

cloud['Drive'] = 3
print(cloud.tags)

print(len(cloud.tags))

for i in cloud.tags:
    print(i)
