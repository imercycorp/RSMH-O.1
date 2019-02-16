class List:

    def select(self, nexus_list, nb_servo):
        self.nexus_list = nexus_list
        self.nb_servo = nb_servo 
        return self.nexus_list[self.nb_servo]
