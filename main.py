from pybtex.database import parse_file
bib_data = parse_file('../RAW_WgroupQuantum.bib')

def output(f, str, n):
    f.write('{0: <8}'.format(''));
    f.write(str);
    if (n==-1):
        n = 13 - len(str);
    for i in range(n):
        f.write(' ');
    f.write('\t');
    f.write('={');

A = {};
for key, entry in bib_data.entries.items():
    #print(entry.persons['author'])
    if not ('year' in entry.fields):
        entry.fields['year'] = '0000';
    A[(entry.type, entry.fields['year'], key)] = entry;

B = sorted(A, key=lambda k: (k[0], -int(k[1])));
f = open("../WgroupQuantum.bib", "w")

f.write('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n%This bib file is created for the use of quantum information science references in the WGroup.\n%Thanks for pybtex: https://pybtex.org/\n%The format code is provided by Tianyi Peng in 2018: https://github.com/TianyiPeng/BibTex_Format\n%\n\n')

type_last = "";
for (type, year, key) in B:
    entry = bib_data.entries[key];

    if entry.type != type_last:
        f.write('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n');
        f.writelines(('%\n% ',entry.type,'\n%\n\n'));
        type_last = entry.type;

    f.writelines(('@',entry.type,'{',key,',\n'));
    #Author
    if 'author' in entry.persons:
        output(f, 'author', 6);
        count=0;
        for person in entry.persons['author']:
            count = count + 1;
            if (count != 1):
                f.write(' and ');
            f.writelines((str(person)));
        f.writelines('},\n');

    if 'title' in entry.fields:
        output(f,'title',10);
        f.write(entry.fields['title']);
        f.write('},\n');

    if 'journal' in entry.fields:
        output(f,'journal',6);
        f.write(entry.fields['journal']);
        f.write('},\n');

    if 'booktitle' in entry.fields:
        output(f,'booktitle',2);
        f.write(entry.fields['booktitle']);
        f.write('},\n');

    if 'volume' in entry.fields:
        output(f,'volume',5);
        f.write(entry.fields['volume']);
        f.write('},\n');

    if 'number' in entry.fields:
        output(f,'number',4);
        f.write(entry.fields['number']);
        f.write('},\n');
    
    if 'issue' in entry.fields:
        output(f, 'number', 4);
        f.write(entry.fields['issue']);
        f.write('},\n');
    
    if 'pages' in entry.fields:
        output(f,'pages',7);
        f.write(entry.fields['pages']);
        f.write('},\n');
    
    if 'numpages' in entry.fields:
        output(f,'numpages',0);
        f.write(entry.fields['numpages']);
        f.write('},\n');
    
    if 'month' in entry.fields:
        output(f,'month',7);
        f.write(entry.fields['month']);
        f.write('},\n');
    
    if 'year' in entry.fields:
        if not (year == '0000'):
            output(f,'year',10);
            f.write(entry.fields['year']);
            f.write('},\n');

    if 'note' in entry.fields:
        output(f,'note',10);
        f.write(entry.fields['note']);
        f.write('},\n');

    for field in entry.fields:
        F = field.lower();
        if (F != 'author' and F != 'title'
            and F != 'journal' and F != 'booktitle'
            and F != 'volume' and F != 'number'
            and F != 'issue' and F != 'pages'
            and F != 'numpages' and F != 'month'
            and F != 'year' and F != 'note'
            and F != 'keywords'):

            output(f,F,-1);
            f.write(entry.fields[field]);
            f.write('},\n');

    f.write('}\n\n');
