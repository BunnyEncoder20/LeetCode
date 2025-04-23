from logger import Logger
from logger_config import LoggerConfig
from log_level import LogLevel
from file_writer import FileWriter

class LoggingFramework_Demo:
    @staticmethod
    def run():
        logger = Logger.get_intance()
        
        # Logging with default config
        logger.info('This is an information message')
        logger.warning("This is a warning message")
        logger.error("This is an error message")

        # Changing the log level and writer
        config = LoggerConfig(LogLevel.DEBUG, FileAppender("app.log"))
        logger.set_config(config)
        
        # Logging with new config 
        logger.debug("This is a debug message")
        logger.info("This is a information message")

if __name__ == "__main__":
    LoggingFrameworkDemo.run()
