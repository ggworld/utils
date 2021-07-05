import glob
import zipfile 


prefix='/Users/geva/Documents/private/pictpl/out/'
for fn in glob.glob('/Users/geva/Documents/private/pictpl/*.zip'):
    with zipfile.ZipFile(fn) as myzip:
        for allf in myzip.namelist():
            with myzip.open(allf) as myfile:
                with open(prefix+allf,'wb') as outf:
                    outf.write(myfile.read())
