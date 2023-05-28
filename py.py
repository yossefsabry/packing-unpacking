mytuple = ('js', 'python', 'css')
myskills = {
    'Go':'90%' ,
    'java scsript': '20%',
    'php' : '70%',
    'html' : '90%'
}

def hello(name, *skills ,**myskillsWithPrograss):

    print(f'hello {name}\n skills without prograss')

    for skill in skills:

        print(f'- {skill} -')

    print('skills with prograss')

    for skillvalue ,skillkay in myskillsWithPrograss.items():

        print(f'- {skillvalue} => {skillkay} -')



hello('yossef', *mytuple,**myskills)
