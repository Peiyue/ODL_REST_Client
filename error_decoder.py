""" @Arthor: Jin Jing 
    @Email: jji@kth.se
    This function shows the error type in the command line """

def error_decoder(code):
        if code==200:
                result='Operation successful'
        elif code==201:
                result='New flow added'
        elif code==404:
                result='ContainerName or node not found'
        else:
                result='unknown error code'+str(code)
        return result
