class Posting:
    def __init__(self, id, text, categories, description, descriptionPlain, lists, additional, additionalPlain,
                 hostedUrl, applyUrl, createdAt):
        self.id = id
        self.text = text
        self.categories = categories
        self.description = description
        self.descriptionPlain = descriptionPlain
        self.lists = lists
        self.additional = additional
        self.additionalPlain = additionalPlain
        self.hostedUrl = hostedUrl
        self.applyUrl = applyUrl

        self.createdAt = createdAt