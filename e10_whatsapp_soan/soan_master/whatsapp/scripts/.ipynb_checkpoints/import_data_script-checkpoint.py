# -*- coding: utf-8 -*-
# Without the above line, following error was occurring: 
# SyntaxError: Non-ASCII character '\xc2' in file at line 57.

import re
import pandas   as pd
import numpy    as np
import io
from collections     import Counter
from dateutil.parser import parse
import os

def import_data(file, path = ''):
    """ Import whatsapp data and transform it to a dataframe
    
    Parameters:
    -----------
    file : str
        Name of file including its extension.
    path : str, default ''
        Path to file without the file name. 
        Keep it empty if the file is in the 
        working directory.
        
    Returns:
    --------
    df : dataframe
        Dataframe of all messages
    
    """
    
    timestamp_str_1 = r'\d\d/\d\d/\d\d, \d\d:\d\d'
    timestamp_str_2 = r'\d\d/\d\d/\d\d\d\d, \d\d?:\d\d? [ap]m'
    timestamp_str_3 = r'\d\d/\d\d/\d\d, \d\d?:\d\d? [ap]m' # 05/10/22, 5:01 pm AND 05/10/22, 11:01 pm

    timestamp_pattern_1 = re.compile(timestamp_str_1)
    timestamp_pattern_2 = re.compile(timestamp_str_2)
    timestamp_pattern_3 = re.compile(timestamp_str_3)

    phn_num_pattern = re.compile(r'[+]\d+ \d{5} \d{5}')
    #with open(path + file, encoding = 'utf-8') as outfile: # Original # Error: encoding is not a valid argument.
    with io.open(os.path.join(path, file), encoding = 'utf-8') as outfile:

        raw_text = outfile.readlines()

        timestamps = []
        users = []
        messages = []

        for message in raw_text: 
            # print("message: " + message)

            x1 = re.findall("^" + timestamp_str_1, message)
            x2 = re.findall("^" + timestamp_str_2, message)
            x3 = re.findall("^" + timestamp_str_3, message)
            # print(x1)
            # print(x2)
            if (x1 or x2 or x3) and ":" not in message.split(" - ")[1]:
                # 31/01/19, 19:13 - Messages to this group are now secured with end-to-end encryption. Tap for more info.
                if "Messages to this group are now secured with end-to-end encryption. Tap for more info." in message.split(" - ")[1]:
                    continue

                elif "left" in message.split(" - ")[1]:
                    continue

                elif "joined using this group's invite link" in message.split(" - ")[1]:
                    continue

                elif "added" in message.split(" - ")[1]: # 03/01/20, 11:07 - Ashiq Kumar added +91 97817 26200
                    continue

                # 16/01/20, 16:57 - +91 87488 95634 changed to +91 96321 38761
                elif "changed to" in message.split(" - ")[1]: 
                    continue

                # 01/06/2019, 4:52 pm - You created group "Cousins...❤👏🏻😊🧡😜😜😘😇😝🐼🐼"
                elif "created group" in message.split(" - ")[1]: 
                    continue

                # You changed this group's icon
                elif "changed this group's icon" in message.split(" - ")[1]: 
                    continue

            if len(message) > 15 and (re.search(timestamp_pattern_1, message[0:15]) \
                                      or re.search(timestamp_pattern_2, message[0:20]) \
                                      or re.search(timestamp_pattern_3, message[0:20])):
                
                if re.search(timestamp_pattern_1, message[0:15]):
                    timestamps.append( message[0:15] )
                elif re.search(timestamp_pattern_2, message[0:20]):
                    timestamps.append( message[0:20] )
                else:
                    # timestamp_pattern_3
                    timestamps.append( message[0:18] )
                 
                
                users.append( message.split(' - ')[1].split(':')[0] )
                messages.append( ''.join( message.split(' - ')[1].split(':')[1:] ) )
            else:
                # print(x1)
                # print(x2)
                # print("Exception in message: " + message)
                messages[-1] = messages[-1] + "\n" + message
                continue

    # Convert dictionary to dataframe

    df = pd.DataFrame({'Timestamp': timestamps, 'Message_Raw': messages, 'User': users})

    df.reset_index(inplace=True)

    return df

if __name__ == "__main__":
    file_name_1 = "WhatsApp Chat with Cousins (201910-201912).txt"
    file_name_2 = "WhatsApp Chat with BITS Lounge (New).txt"

    df = import_data(file_name_2, r'D:\workspace\Jupyter\exp_45.2_whatsapp\files_1'.replace("\\", "/"))
    print(df.head())
