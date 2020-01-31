'''
Hacker Rank challenge
in
Practice>Tutorials>30 Days of CodeDay> 8: Dictionaries and Maps
'''
def main():
    NEntries = int(input()) #expected input: number of entries
    PhoneBook = {}
    for _ in range(NEntries): #make the phone book
        Entry = input() #expected input: 'name PhoneNumber'
        Entry = Entry.split()
        PhoneBook[Entry[0]] = Entry[1]
    # accept queries for phone numbers
    QueryInput = input() 
    while(QueryInput != ''):
        try:
            print(QueryInput + '=' + PhoneBook[QueryInput]) #print name and phone number
        except:
            print('Not found')
        try: #try-except to manage the EOFError when the input comes from the HackerRank system
            QueryInput = input()
        except EOFError:
            break
        
if __name__ == '__main__':
    main()