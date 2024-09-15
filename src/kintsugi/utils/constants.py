# This regex is used to extract Kintusgi section from parsed docstring,
# which is enclosed between "@--" and "--@" tags. Multiline sections are supported.
DOCSTRING_SECTION_REGEXP=r'@--(.*?)--@'

# This regex is used to extract references from Kintsugi section.
# These are basically links to other entities in the codebase,
# in the form of module, class or function names prefixed by "#>" marker.
REFERENCE_REGEXP=r'#>(\w+)'
