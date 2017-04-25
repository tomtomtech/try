
Git  scenario git tutoria szerint
https://try.github.io/levels/1/challenges/1

1
git init

1.1
	git status - állapot

2
git add file_name, vagy git add *.txt minden txt file hozzadasa

3. git commit -m "note to commit"

4.
show commits
$ git log

5.
Ez a sajat try repom
git remote add origin https://github.com/tomtomtech/try.git

Enneka remote reponak neve 'origin', mint ahogy a local nak 'master'
Ezzel lehet felnyomni a remotba a helyi master branch-t

5.1
remote repok lekerese
git remote -v
5.2
change remote origin repo
git remote set-url origin https://github.com/tomtomtech/try.git

6
felnyomni az online (az originbe)
$ git push -u origin master
	az 'u' az jelenti hoogy jjegyezze meg és később elég a 'git push' parancs

7.
ellenorzes
az ucso commit utani valtozasok
$ git diff HEAD

Meg stageleheto valtozasok
git diff --staged

Kiveszi a fajlt a add bol azaz mar nem kell rá a staged hasznalni, de lehet h kicsit félreértettem mert nem csinaltam végigaz elejétől.
git reset v. git reset path/file_name.ext

8.andHa vissza akarjuk kapni gy file utolso commitált állapotát. 
$ git checkout -- file_name.ext



9. Barnchelés
Akkor használjuk pl ha uj featoron v bugfixen dolgozunk. Gyakorlatilag egy copy a master branchrol
git baranch new_feature (group name a new_feature)