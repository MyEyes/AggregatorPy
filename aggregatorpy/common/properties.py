from ..model.property import PropertyKind

# Common Path Properties

# Not matching because we probably want to identify files as similar or identical, even if they are in different locations
FilePathProperty = PropertyKind(None, "File Path", "A file system path of a file", is_matching=False)
"""Path of a file (not matching)"""

# Matching because we may want to identify that a function or other subject inside a file is at the exact same path
ContainingPathProperty = PropertyKind(None, "Containing Path", "A file system path as a parent of a subject", is_matching=True)
"""Path containing this subject (matching)"""

FileNameProperty = PropertyKind(None, "File Name", "Name of a file", is_matching=True)
"""Filename of a subject (matching)"""

DirNameProperty = PropertyKind(None, "Dir Name", "Name of a directory", is_matching=True)
"""Name of a directory subject (matching)"""

# Common Function Properties
FunctionNameProperty = PropertyKind(None, "Function Name", "The name of a function", is_matching=True)
"""Name of a function (matching)"""

FunctionSignatureProperty = PropertyKind(None, "Function Signature", "The full signature of a function", is_matching=True)
"""Full signature of a function (matching)"""

ReturnTypeProperty = PropertyKind(None, "Return Type", "The type returned by a function", is_matching=True)
"""Type returned by a function (matching)"""

ArgTypeProperty = PropertyKind(None, "Argument Type", "The type of an argument of a function", is_matching=True)
"""Type of a function argument (matching)

Prefix the type with its index if you care about the order."""

# Common generic properties
VersionProperty = PropertyKind(None, "Version", "A version number", is_matching=True)
"""Version of a subject (matching)"""

ContentHashProperty = PropertyKind(None, "Content Hash", "A hash of the contents of a subject", is_matching=True)
"""Generic hash of subject contents (matching)"""