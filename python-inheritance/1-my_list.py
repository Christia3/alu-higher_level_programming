class MyList(list):
    """A subclass of list that can print itself in sorted order."""
    
    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))

