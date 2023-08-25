
- GitLab BackUp & Restore

https://docs.gitlab.com/ee/administration/backup_restore/

1. GitLab BackUp


```sh
sudo gitlab-ctl registry-garbage-collect -m

sudo gitlab-backup create BACKUP=dump-20230824

gzip dump-20230824_gitlab_backup.tar

# memory usage
ps -o pid,user,%mem,command ax | sort -b -k3 -r
```

2. GitLab Restore

https://docs.gitlab.com/ee/administration/backup_restore/restore_gitlab.html

```sh
# Stop the processes that are connected to the database
docker exec -it <name of container> gitlab-ctl stop puma
docker exec -it <name of container> gitlab-ctl stop sidekiq

# Verify that the processes are all down before continuing
docker exec -it <name of container> gitlab-ctl status

# Run the restore. NOTE: "_gitlab_backup.tar" is omitted from the name
docker exec -it <name of container> gitlab-backup restore BACKUP=dump-20230824_gitlab_backup

# Restart the GitLab container docker restart <name of container>

# Check GitLab
docker exec -it <name of container> gitlab-rake gitlab:check SANITIZE=true
```
