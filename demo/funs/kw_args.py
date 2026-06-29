def show(**kwargs):
    for k, v in kwargs.items():
        print(k, ' -', v)


def show2(x, y, **kwargs):
    pass


show(x=10, y=20)
show(name='Python', ver=3.14)

show2(10, 20, meteric = 'inches')
show2(10, 20, meteric = 'cm')

