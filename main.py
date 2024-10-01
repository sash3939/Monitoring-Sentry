import sentry_sdk

sentry_sdk.init(
    dsn="https://68302aab4692bacd0ab143e0b725deda@o4508043825184768.ingest.de.sentry.io/4508048097738832",
    environment = "development",
    release="1.0",
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0
)

if __name__ == "__main__":
    division_by_zero = 1 / 0
