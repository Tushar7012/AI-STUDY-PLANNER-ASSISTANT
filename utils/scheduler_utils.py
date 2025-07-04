import schedule, threading, time

_scheduler_thread = None

def start_scheduler():
    global _scheduler_thread
    if _scheduler_thread and _scheduler_thread.is_alive():
        return
    def run_continuously():
        while True:
            schedule.run_pending()
            time.sleep(1)
    _scheduler_thread = threading.Thread(target=run_continuously, daemon=True)
    _scheduler_thread.start()

def schedule_job(cron_time: str, func, *args, **kwargs):
    schedule.every().day.at(cron_time).do(func, *args, **kwargs)

def clear_jobs():
    schedule.clear()
