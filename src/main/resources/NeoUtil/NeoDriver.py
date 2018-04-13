class NeoInternalDriver(object):
    def __init__(self, provider):
        self.db = provider.getGraphDatabaseService()
        self.logger = provider.getLogger()

    def query(self, q):
        try:
            tx = self.db.beginTx()
            result = self.db.execute(q)
            tx.success()
            tx.close()
            return result
        except Exception as e:
            self.logger.warn("NeoInternalDriver: Exception in query: " + q + " - " + str(e))
            tx.failure()
            tx.close()
