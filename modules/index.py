# Python PIP  -- PIP is a package manager for Python packages, or modules if you like.
# A package contains all the files you need for a module.
# PIP install camelcase
import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))