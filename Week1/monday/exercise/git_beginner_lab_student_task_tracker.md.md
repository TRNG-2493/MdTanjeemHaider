# Part 1
```
mkdir student-task-tracker
cd student-task-tracker
git init
```
(after making readme file)
```
git status
```

# Part 2
(after creating tasks.txt with 3 sample tasks)
```
git status
git add README.md tasks.txt
git commit -m "Part 2 complete"
```
(after adding 4th task )
```
git status
git log
```

# Part 3
(after creating .gitignore and adding rules)
(after creating app.log and .env with dummy data)
```
git status
git add .gitignore
git commit -m "Add gitignore"
```

# Part 4
```
git remote add origin https://github.com/MdTanjeemHaider/test-repo.git
git push -u origin main
```
In a different folder:
```
git clone https://github.com/MdTanjeemHaider/test-repo.git
```
(After making changes to readme)
```
git add README.md
git commit -m "Add to readme"
git push
```

# Part 5
```
git fetch
git pull
git switch -c feature/add-priority
git add tasks.txt
git commit -m "add task priority"
git branch --set-upstream-to=origin/feature/add-priority
git push
```

# Part 6
On the repository: https://github.com/MdTanjeemHaider/test-repo

