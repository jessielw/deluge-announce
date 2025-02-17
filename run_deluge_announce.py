from deluge_announce import Announcer


if __name__ == "__main__":
    announcer = Announcer(cron_schedule="*/5 * * * *")
    announcer.run_forever()
