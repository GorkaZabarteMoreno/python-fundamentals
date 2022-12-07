def learn_scope():
    """
    Function with 3 wrappers inside to
    explain the scope of variables
    """

    def f1():
        """
        Define a local variable var
        It does affect the outer scope
        """
        var = 'Local variable inner to f function'

    def f2():
        """
        Define a non local variable var
        """
        nonlocal var
        var = 'Non local variable'

    def f3():
        """
        Define a global variable global_var
        """
        global var
        var = 'Global variable'

    var = 'Variable created in the main function'
    f1()
    print('After local assignment:', var)
    f2()
    print('After nonlocal assignment:', var)
    f3()
    print('After global assignment:', var)


learn_scope()  # It should print
print('In global scope:', var)
