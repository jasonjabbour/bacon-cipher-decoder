#Bacon's Cipher. A Message is Concealed in the presentation of text. 

class bacon_cipher:

    def __init__(self):
        self.bacon_codes_dict = {'aaaaa':'A', 'aaaab':'B', 'aaaba':'C',
                                'aaabb':'D', 'aabaa':'E', 'aabab':'F',
                                'aabba':'G', 'aabbb':'H', 'abaaa':'I',
                                'abaab':'J', 'ababa':'K', 'ababb':'L',
                                'abbaa':'M', 'abbab':'N', 'abbba':'O',
                                'abbbb':'P', 'baaaa':'Q', 'baaab':'R',
                                'baaba':'S', 'baabb':'T', 'babaa':'U',
                                'babab':'V', 'babba':'W', 'babbb':'X',
                                'bbaaa':'Y', 'bbaab':'Z',
        }

        self.decoded_message = ''


    def decode(self,message,upperCase='A'):
        """
            message: A decoded message as type string. Use upper and lower case letters to identify font type. 
            upperCase: Specify 'A' or 'B'. 
                        A uppercase letters as font type A and lowercase letters as font type B (Default). 
                        B lowercase letters as font type A and uppercase letters as font type B
        """

        try:
            #Verify input
            if type(message) != str:
                return 'Invalid message. Pass in a message as a string with upper and lowercase letters.'
            
            for character in message:
                if character.isdigit():
                    return 'Invalid message. Digits are not allowed. Please use only letters.'
            
            if upperCase not in ['A','a','B','b']:
                return 'Invalid upperCase parameter value. Please use "A" or "B" to specify which font type uppercase letters represent'
            
            #Default
            upperCase_letter = 'a'
            lowerCase_letter = 'b'
            self.decoded_message = ''

            #Determine what uppercase letters represent
            if upperCase in ['B','b']:
                upperCase_letter = 'b'
                lowerCase_letter = 'a'

            #Remove spaces
            message = message.replace(' ','')

            segment_pointer = 0
            jump = 5
            #leave out end of message if total does not equal 5
            while (segment_pointer + jump) <= len(message):
                message_segment = message[segment_pointer:segment_pointer+jump]
                converted_segment = ''

                for character in message_segment:
                    if character.isupper():
                        converted_segment+=upperCase_letter
                    else:
                        converted_segment+=lowerCase_letter

                #Save the found letter
                if converted_segment in self.bacon_codes_dict.keys():
                    self.decoded_message+=self.bacon_codes_dict[converted_segment]
                else:
                    return 'Invalid Message. The message is not encoded in bacon\'s cipher'

                segment_pointer+=jump

            return self.decoded_message
        except Exception as e:
            return e
