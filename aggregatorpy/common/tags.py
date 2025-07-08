from ..model.tag import Tag

# Status tags
openTag = Tag(None, "open", "open", "Not yet manually checked", color="lightblue")
"""Tag for not yet inspected results or subjects"""

confirmedTag = Tag(None, "confirmed", "confirmed", "True positive", color="darkgreen")
"""Tag for checked and confirmed results or subjects"""

rejectedTag = Tag(None, "rejected", "rejected", "False positive", color="darkred")
"""Tag for checked and rejected results or subjects"""

# Type tags
functionTag = Tag(None, "func", "function", "Is a function", color="purple")
"""Tag marking a function"""

fileTag = Tag(None, "file", "file", "Is a file", color="purple")
"""Tag marking a file"""

dirTag = Tag(None, "dir", "directory", "Is a directory", color="purple")
"""Tag marking a directory"""

rootTag = Tag(None, "root", "root", "Is root element of a subject tree", color="purple")
"""Tag marking root element of a tree"""