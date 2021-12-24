import pandas as pd

#--------Import----------#
df_data = pd.read_table('Morse.txt', header=None)


#--------Data Prep----------#
df_data_clean = df_data.drop([3,4,5,6,7], axis=1)

for i in range (0,3):
    df_data_clean[i] = df_data_clean[i].str.strip()

df_data_clean = df_data_clean.rename(columns={0:'Letter', 1:'Morse', 2:'NATO'})


#--------Turn on translator-----#
translator_is_on = True


#--------Get Text Input---------#
while translator_is_on == True:
    input_text = input('What is the text you would like to translate?')
    if input_text == 'stop':
        translator_is_on = False
    else:
        text_to_translate = list(str(input_text).upper())


        #--------List comprehension to transform list-------#
        try:
            morse_list = [df_data_clean.loc[df_data_clean['Letter'] == letter].iloc[0, 1]+" " for letter in text_to_translate if letter != " "]
            # -------Print -----#
            print(''.join(morse_list))

        except IndexError:
            print('Please type Letters from A-Z')












