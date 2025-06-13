#!/usr/bin/env python3

def acronyms(s):
    res = []
    for word in s.split(" "):
        w = word.strip().replace('(','').replace(')','').replace('[','').replace(']','').replace(".", '').replace(',', '')
        if len(w) >= 2 and  w.isalnum() and w.isupper():
            res.append(w)
    return res
    # return [w for w in s.split(' ') if len(w) >= 2 and  w.isalnum() and w.isupper()]

def main():
    print(acronyms("For the (IBM Corp.) PO  Box 41 purposes of the EU General Data EU GDPR 'IBM', 'IBM', 'EEA', 'EEA', 'IBM', 'PO', 'PO6', '3AU' Protection Regulation (GDPR), the controller of your personal information is International Business Machines Corporation (IBM Corp.), 1 New Orchard Road, Armonk, New York, United States, unless indicated otherwise. Where IBM Corp. or a subsidiary it controls (not established in the European Economic Area (EEA)) is required to appoint a legal representative in the EEA, the representative for all such cases is IBM United Kingdom Limited, PO Box 41, North Harbour, Portsmouth, Hampshire, United Kingdom PO6 3AU."))


if __name__ == "__main__":
    main()


# from string import punctuation
 
# def acronyms(s):
#     L = [x.strip(punctuation) for x in s.split() ]
#     return [ x for x in L if x.isupper() and len(x) >= 2 ]