s -with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name = 'pydbloader',
      version = '0.0.2',
      description = 'A python database loader for various relational databases',
      url = 'https://github.com/Remillardj/pyDBLoader',
      author = 'Jaryd Remillard',
      license = 'Apache',
      install_requires = [ requirements ],
)
