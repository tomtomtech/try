
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