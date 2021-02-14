class LogicalAgent():

    def __init__(self,KB):
        self.KB = KB

    # TODO
    def bottom_up(self):
        ''' Implements the botton up proof strategy and returns all the logical consequence odf the KB

        Returns:
            A list with all the logical consequences of KB
        '''
        pass

    # TODO
    def top_down(self,query):
        '''Implements the top down proof strategy. Given a query (the atom that it wants to prove) 
        it returns True if the query is a consequence of the knowledge base. 
        
        Args:
            querry: The atom that should be proved

        Returns: 
            True if the query is a logical consequence of KB, False otherwise

        '''
        
        pass
    
    # TODO
    def explain(self,g):
        '''Implements the process of abductions. It tries to explain the atoms  in the list g using
         the assumable in KB.

        Args:
            g: A set of atoms that should be explained
        
        Returns:
            A list of explanation for the atoms in g
        '''
        pass