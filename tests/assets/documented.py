import random


class DocumentedClass:
    """
        This is a test class
        @--
        #>AnotherDocumentedClass
        --@
    """
    def method(self) -> int:
        """
            @--
            #>AnotherDocumentedClass.another_method

            This method calls AnotherDocumentedClass.another_method
            and returns the result
            --@
        """
        return AnotherDocumentedClass.another_method()


class AnotherDocumentedClass:
    """
        This is a class on which DocumentedClass depends
    """
    @classmethod
    def another_method(cls) -> int:
        """
            This method returns a random number from 1 to 10
            @--
            #>random.randint
            --@
        """
        return random.randint(1, 10)
